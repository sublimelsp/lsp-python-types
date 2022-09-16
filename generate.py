#!/usr/bin/env python3
import json

from lsp_schema import MetaModel
from utils.generate_enumerations import generate_enumerations
# from utils.generate_requests import generate_requests
from utils.generate_structures import generate_structures
from utils.generate_type_aliases import generate_type_aliases
from utils.helpers import get_new_literal_structures


def generate() -> None:
    with open('./lsprotocol/lsp.json') as file:
        lsp_json: MetaModel = json.load(file)
        specification_version = lsp_json.get('metaData')['version']

        content = "\n".join([
            "# Code generated. DO NOT EDIT.",
            f"# LSP v{specification_version}\n",
            "from typing_extensions import NotRequired",
            "from typing import Dict, List, Literal, TypedDict, Union, Tuple",
            "from enum import Enum\n\n",
            "URI = str",
            "DocumentUri = str",
            "Uint = int",
            "RegExp = str",
            # generate_requests(lsp_json['requests'])
        ])

        content += '\n\n\n'
        content += '\n\n\n'.join(generate_enumerations(lsp_json['enumerations']))
        content += '\n\n'
        content += '\n'.join(generate_type_aliases(lsp_json['typeAliases']))
        content += '\n\n\n'
        content += '\n\n\n'.join(generate_structures(lsp_json['structures']))
        content += '\n\n'
        content += '\n'.join(get_new_literal_structures())

        # Remove trailing spaces.
        lines = content.split('\n')
        lines = [line.rstrip() for line in lines]
        content = '\n'.join(lines)

        with open('./lsp_types.py', "w") as new_file:
            new_file.write(content)


generate()
