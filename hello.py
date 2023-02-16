import asyncio
import json
import os
from lsp_requests import LspNotification, LspRequest
import threading


CONTENT_LENGTH = 'Content-Length: '
class Server():
    def __init__(self, cmd: str) -> None:
        self.process = None
        self.cmd = cmd
        self.request_id = 1
        self.request = LspRequest(self.send_request)
        self.notify = LspNotification(self.send_notification)

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

        response = await self._wait_response(self.request_id)
        return response

    async def _wait_response(self, id):
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
                    return response_obj


async def main():
    server = Server('node /home/predragnikolic/Documents/sandbox/typescript-language-server/lib/cli.mjs --stdio')
    await server.start()
    r = await server.request.initialize(({
        'processId': os.getpid(),
        'rootUri': None,
        'capabilities': {}
    }))

    r1 = await server.request.initialize(({
        'processId': os.getpid(),
        'rootUri': None,
        'capabilities': {}
    }))

    server.notify.did_open_text_document({
        'textDocument': {
            'version': 0,
            'languageId': 'javascript',
            'text': "let c = 1\nprocess.stdout.write('Hey' + c + process.argv.slice(2) +'\\n')\n",
            'uri': 'file:///home/predragnikolic/Documents/sandbox/lsp_types/hello.js'
        }
    })
    print('dsda', r)
    print('dsda', r1)

asyncio.run(main())
