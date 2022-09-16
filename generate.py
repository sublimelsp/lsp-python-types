#!/usr/bin/env python3
import json

from lsp_schema import MetaModel
from utils.generate_enumerations import generate_enumerations
from utils.generate_requests import generate_requests
from utils.generate_structures import generate_structures
from utils.generate_type_aliases import generate_type_aliases
from utils.helpers import get_new_literal_structures


def generate() -> None:
    with open('./lsprotocol/lsp.json') as file:
        lsp_json: MetaModel = json.load(file)
        specification_version = lsp_json.get('metaData')['version']

        content = "".join([
            "# Code generated. DO NOT EDIT.\n",
            f"# LSP v{specification_version}\n\n",
            "from typing_extensions import NotRequired\n",
            "from typing import Dict, List, Literal, TypedDict, Union, Tuple\n",
            "from enum import Enum\n\n\n",
            "URI = str\n",
            "DocumentUri = str\n",
            "Uint = int\n",
            "RegExp = str\n\n",
        ])

        content += generate_enumerations(lsp_json['enumerations'])
        content += generate_type_aliases(lsp_json['typeAliases'])
        content += generate_structures(lsp_json['structures'])
        content += generate_requests(lsp_json['requests'])

        content += get_new_literal_structures()

        lines = content.split('\n')
        lines = [line.rstrip() for line in lines]
        content = '\n'.join(lines)

        with open('./lsp_types.py', "w") as new_file:
            new_file.write(content)


generate()
