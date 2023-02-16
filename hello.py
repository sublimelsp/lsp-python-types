import asyncio
import json
import os
from lsp_requests import LspNotification, LspRequest, Response


CONTENT_LENGTH = 'Content-Length: '
class Server():
    def __init__(self, cmd: str) -> None:
        self.process = None
        self.cmd = cmd
        self.request_id = 1
        self.request = LspRequest(self.send_request)
        self.notify = LspNotification(self.send_notification)
        self.on_request_callbacks = {}
        self.on_notification_callbacks = {}

    async def start(self):
        self.process = await asyncio.create_subprocess_shell(
            self.cmd,
            stdout=asyncio.subprocess.PIPE,
            stdin=asyncio.subprocess.PIPE,
        )

    def stop(self):
        if self.process:
            self.process.kill()

    def send_notification(self, method: str, params: dict):
        self.request_id = 1
        content = json.dumps({
            "jsonrpc": "2.0",
            "method": method,
            "params": params
        })
        header = CONTENT_LENGTH + str(len(content))
        msg = header + '\r\n\r\n' + content
        if not self.process or not self.process.stdin:
            return
        self.process.stdin.write(msg.encode('UTF-8'))

    async def send_request(self, method: str, params: dict):
        self.request_id = 1
        content = json.dumps({
            "jsonrpc": "2.0",
            "id": self.request_id,
            "method": method,
            "params": params
        })
        header = CONTENT_LENGTH + str(len(content))
        msg = header + '\r\n\r\n' + content
        if not self.process or not self.process.stdin:
            return
        self.process.stdin.write(msg.encode('UTF-8'))
        context = self.request_context()
        response = await self._wait_response(self.request_id, context)
        return response

    def on_request(self, method: str, cb):
        self.on_request_callbacks[method] = cb

    def request_context(self):
        return {
            "session_name": "eej"
        }

    def on_notification(self, method: str, cb):
        self.on_notification_callbacks[method] = cb

    async def _wait_response(self, id, context):
        while True:
            if not self.process:
                return
            header_data = await self.process.stdout.readline()
            header = header_data.decode('UTF-8').rstrip()
            if len(header) > len(CONTENT_LENGTH):
                content_size = int(header[len(CONTENT_LENGTH):])
                await self.process.stdout.readline()
                response_data = await self.process.stdout.read(content_size)
                response = response_data.decode('UTF-8').rstrip()

                response_obj = json.loads(response)
                method = response_obj.get("method")
                result = response_obj.get("result")
                error = response_obj.get("error")
                rpc_id = response_obj.get("id")
                params = response_obj.get("params")
                if rpc_id == id:
                    return Response(response_obj, rpc_id, context)
                if method:
                    # request from server
                    if rpc_id:
                        cb = self.on_request_callbacks.get(method)
                        if not cb:
                            print('method not implemented', method)
                            continue
                        r = await cb(params)
                        content = json.dumps({
                            "id": rpc_id,
                            "jsonrpc": "2.0",
                            "result": r
                        })
                        header = CONTENT_LENGTH + str(len(content))
                        msg = header + '\r\n\r\n' + content
                        if not self.process or not self.process.stdin:
                            continue
                        self.process.stdin.write(msg.encode('UTF-8'))
                        continue
                    # notification from server
                    cb = self.on_notification_callbacks.get(method)
                    if not cb:
                        print('notification not implemented', method)
                        continue
                    cb(params)


async def main():
    server = Server('node /home/predragnikolic/Documents/sandbox/typescript-language-server/lib/cli.mjs --stdio')
    await server.start()

    def on_log_message(x):
        print('handle log message', x)

    async def on_apply_edit(x):
        print('handle apply edits', x)

    server.on_notification('window/logMessage', on_log_message)
    server.on_request('workspace/applyEdit', on_apply_edit)

    r = await server.request.initialize(({
        'processId': os.getpid(),
        'rootUri': None,
        'capabilities': {}
    }))

    print('response', r.result)
    print('response', r.context)

    server.notify.did_open_text_document({
        'textDocument': {
            'version': 0,
            'languageId': 'javascript',
            'text': "let c = 1\nprocess.stdout.write('Hey' + c + process.argv.slice(2) +'\\n')\n",
            'uri': 'file:///home/predragnikolic/Documents/sandbox/lsp_types/hello.js'
        }
    })

asyncio.run(main())
