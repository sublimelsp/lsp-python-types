#!/usr/bin/env python3

from pathlib import Path
from urllib.request import urlopen

REPO_URL = 'https://raw.githubusercontent.com/microsoft/vscode-languageserver-node'

with urlopen(f'{REPO_URL}/main/protocol/metaModel.schema.json') as url:
    Path('./lsprotocol/lsp.schema.json').write_text(url.read().decode('utf-8'))

with urlopen(f'{REPO_URL}/main/protocol/metaModel.json'):
    Path('./lsprotocol/lsp.json').write_text(url.read().decode('utf-8'))
