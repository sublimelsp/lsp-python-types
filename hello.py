import asyncio
import os
from language_server import LanguageServer


async def main():
    server = LanguageServer('typescript-language-server --stdio')
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

    server.notify.did_open_text_document({
        'textDocument': {
            'version': 0,
            'languageId': 'javascript',
            'text': "let c = 1",
            'uri': 'file://' + os.path.abspath("hello.js")
        }
    })

    completions = await server.send.completion({
        "position": {"character": 0, "line": 0},
        "textDocument": {
            "uri": 'file://' + os.path.abspath("hello.js")
        }
    })

    if isinstance(completions, dict):
        item = completions['items'][0]
        resolved_item = await server.send.resolve_completion_item(item)
        print('resolved')
        print(resolved_item)

    await server.shutdown()

    server.stop()

asyncio.get_event_loop().run_until_complete(main())
