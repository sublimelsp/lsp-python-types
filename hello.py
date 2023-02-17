import asyncio
import json
import os
from typing import Any, Dict, List, Union, Optional
from lsp_requests import LspNotification, LspRequest, Response
from lsp_types import ErrorCodes

StringDict = Dict[str, Any]
PayloadLike = Union[List[StringDict], StringDict, None]
CONTENT_LENGTH = 'Content-Length: '
ENCODING = "utf-8"

class Error(Exception):

    def __init__(self, code: ErrorCodes, message: str) -> None:
        super().__init__(message)
        self.code = code

    def to_lsp(self) -> StringDict:
        return {"code": self.code, "message": super().__str__()}

    @classmethod
    def from_lsp(cls, d: StringDict) -> 'Error':
        return Error(d["code"], d["message"])

    def __str__(self) -> str:
        return f"{super().__str__()} ({self.code})"


def make_response(request_id: Any, params: PayloadLike) -> StringDict:
    return {"jsonrpc": "2.0", "id": request_id, "result": params}

def make_error_response(request_id: Any, err: Error) -> StringDict:
    return {"jsonrpc": "2.0", "id": request_id, "error": err.to_lsp()}

def make_notification(method: str, params: PayloadLike) -> StringDict:
    return {"jsonrpc": "2.0", "method": method, "params": params}

def make_request(method: str, request_id: Any, params: PayloadLike) -> StringDict:
    return {"jsonrpc": "2.0", "method": method, "id": request_id, "params": params}


class StopLoopException(Exception):
    pass

def create_message(payload: PayloadLike) :
    body = json.dumps(
        payload,
        check_circular=False,
        ensure_ascii=False,
        separators=(",", ":")).encode(ENCODING)
    return (
        f"Content-Length: {len(body)}\r\n".encode(ENCODING),
        "Content-Type: application/vscode-jsonrpc; charset=utf-8\r\n\r\n".encode(ENCODING),
        body
    )

class MessageType:
    error = 1
    warning = 2
    info = 3
    log = 4

class Request():
    global_id = 1
    def __init__(self) -> None:
        self.id = self.global_id
        self.global_id +=1
        self.cv = asyncio.Condition()
        self.result = None  # type: Optional[Response[PayloadLike]]
        self.error = None  # type: Optional[Error]

    async def on_result(self, params: PayloadLike) -> None:
        self.result = Response(params, self.id)
        async with self.cv:
            self.cv.notify()

    async def on_error(self, err: Error) -> None:
        self.error = err
        async with self.cv:
            self.cv.notify()


def content_length(line: bytes) -> Optional[int]:
    if line.startswith(b'Content-Length: '):
        _, value = line.split(b'Content-Length: ')
        value = value.strip()
        try:
            return int(value)
        except ValueError:
            raise ValueError("Invalid Content-Length header: {}".format(value))
    return None

class Server():
    def __init__(self, cmd: str) -> None:
        self.send = LspRequest(self.send_request)
        self.notify = LspNotification(self.send_notification)

        self.cmd = cmd
        self.process = None
        self._received_shutdown = False

        self._response_handlers: Dict[Any, Request] = {}
        self.on_request_handlers = {}
        self.on_notification_handlers = {}

    async def start(self):
        self.process = await asyncio.create_subprocess_shell(
            self.cmd,
            stdout=asyncio.subprocess.PIPE,
            stdin=asyncio.subprocess.PIPE,
        )
        asyncio.get_event_loop().create_task(self.run_forever())

    def stop(self):
        if self.process:
            self.process.kill()

    def _log(self, message: str) -> None:
        self.send_notification("window/logMessage",
                     {"type": MessageType.info, "message": message})

    async def run_forever(self) -> bool:
        try:
            while self.process and self.process.stdout and not self.process.stdout.at_eof():
                line = await self.process.stdout.readline()
                if not line:
                    continue
                try:
                    num_bytes = content_length(line)
                except ValueError:
                    continue
                if num_bytes is None:
                    continue
                while line and line.strip():
                    line = await self.process.stdout.readline()
                if not line:
                    continue
                body = await self.process.stdout.readexactly(num_bytes)
                asyncio.get_event_loop().create_task(self._handle_body(body))
        except(BrokenPipeError, ConnectionResetError, StopLoopException):
            pass
        return self._received_shutdown

    async def _handle_body(self, body: bytes) -> None:
        try:
            await self._receive_payload(json.loads(body))
        except IOError as ex:
            self._log(f"malformed {ENCODING}: {ex}")
        except UnicodeDecodeError as ex:
            self._log(f"malformed {ENCODING}: {ex}")
        except json.JSONDecodeError as ex:
            self._log(f"malformed JSON: {ex}")

    async def _receive_payload(self, payload: StringDict) -> None:
        try:
            if "method" in payload:
                if "id" in payload:
                    await self._request_handler(payload)
                else:
                    await self._notification_handler(payload)
            elif "id" in payload:
                await self._response_handler(payload)
            else:
                self._log(f"Unknown payload type: {payload}")
        except Exception as err:
            self._log(f"Error handling server payload: {err}")

    def send_notification(self, method: str, params: dict):
        self._send_payload_sync(
            make_notification(method, params))

    def send_response(self, request_id: Any, params: PayloadLike) -> None:
        asyncio.get_event_loop().create_task(self._send_payload(
            make_response(request_id, params)))

    def send_error_response(self, request_id: Any, err: Error) -> None:
        asyncio.get_event_loop().create_task(self._send_payload(
            make_error_response(request_id, err)))

    async def send_request(self, method: str, params: dict):
        request = Request()
        self._response_handlers[request.id] = request
        async with request.cv:
            await self._send_payload(make_request(method, request.id, params))
            await request.cv.wait()
        if isinstance(request.error, Error):
            raise request.error
        return request.result

    def _send_payload_sync(self, payload: StringDict) -> None:
        if not self.process or not self.process.stdin:
            return
        msg = create_message(payload)
        self.process.stdin.writelines(msg)

    async def _send_payload(self, payload: StringDict) -> None:
        if not self.process or not self.process.stdin:
            return
        msg = create_message(payload)
        self.process.stdin.writelines(msg)
        await self.process.stdin.drain()

    def on_request(self, method: str, cb):
        self.on_request_handlers[method] = cb

    def on_notification(self, method: str, cb):
        self.on_notification_handlers[method] = cb

    async def _response_handler(self, response: StringDict) -> None:
        request = self._response_handlers.pop(response["id"])
        if "result" in response and "error" not in response:
            await request.on_result(response["result"])
        elif "result" not in response and "error" in response:
            await request.on_error(Error.from_lsp(response["error"]))
        else:
            await request.on_error(Error(ErrorCodes.InvalidRequest, ''))

    async def _request_handler(self, response: StringDict) -> None:
        method = response.get("method", "")
        params = response.get("params")
        request_id = response.get("id")
        handler = self.on_request_handlers.get(method)
        if not handler:
            self.send_error_response(request_id, Error(
                    ErrorCodes.MethodNotFound, "method '{}' not handled on client.".format(method)))
            return
        try:
            self.send_response(request_id, await handler(params))
        except Error as ex:
            self.send_error_response(request_id, ex)
        except Exception as ex:
            self.send_error_response(request_id, Error(ErrorCodes.InternalError, str(ex)))

    async def _notification_handler(self, response: StringDict) -> None:
        method = response.get("method", "")
        params = response.get("params")
        handler = self.on_notification_handlers.get(method)
        if not handler:
            self._log(f"unhandled {method}")
            return
        try:
            await handler(params)
        except asyncio.CancelledError:
            return
        except Exception as ex:
            if not self._received_shutdown:
                self.send_notification("window/logMessage", {"type": MessageType.error, "message": str(ex)})


async def main():
    server = Server('typescript-language-server --stdio')
    await server.start()

    def on_log_message(x):
        print('handle log message', x)

    async def on_apply_edit(x):
        print('handle apply edits', x)

    server.on_notification('window/logMessage', on_log_message)
    server.on_request('workspace/applyEdit', on_apply_edit)

    response = await server.send.initialize(({
        'processId': os.getpid(),
        'rootUri': None,
        'capabilities': {}
    }))

    print('response', response.data)


    server.notify.did_open_text_document({
        'textDocument': {
            'version': 0,
            'languageId': 'javascript',
            'text': "let c = 1",
            'uri': 'file://' + os.path.abspath("hello.js")
        }
    })

    completion_response = await server.send.completion({
        "position": {"character": 0, "line": 0},
        "textDocument": {
            "uri": 'file://' + os.path.abspath("hello.js")
        },
    })

    print(completion_response.data)
    # TODO: make the server accessible from the response
    # await response.server.send.resolve_completion_item()

    await asyncio.sleep(10)

asyncio.run(main())
