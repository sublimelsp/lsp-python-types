#!/usr/bin/env python3

from __future__ import annotations

from pathlib import Path
from urllib.request import urlopen

REPO_URL = 'https://raw.githubusercontent.com/microsoft/language-server-protocol'

with urlopen(f'{REPO_URL}/refs/heads/gh-pages/_specifications/lsp/3.18/metaModel/metaModel.schema.json') as url:
    Path('./lsprotocol/lsp.schema.json').write_text(url.read().decode('utf-8'))

with urlopen(f'{REPO_URL}/refs/heads/gh-pages/_specifications/lsp/3.18/metaModel/metaModel.json') as url:
    Path('./lsprotocol/lsp.json').write_text(url.read().decode('utf-8'))
