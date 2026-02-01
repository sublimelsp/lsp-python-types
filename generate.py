#!/usr/bin/env python3

from __future__ import annotations
from pathlib import Path
from typing import Literal, cast, TYPE_CHECKING
from utils.generate_enumerations import generate_enumerations
from utils.generate_structures import generate_structures
from utils.generate_type_aliases import generate_type_aliases
from utils.helpers import get_new_literal_structures, reset_new_literal_structures
import json

if TYPE_CHECKING:
    from lsp_schema import MetaModel


ENUM_OVERRIDES: dict[str, Literal['StrEnum', 'IntFlag']] = {
    'CodeActionKind': 'StrEnum',
    'DocumentDiagnosticReportKind': 'StrEnum',
    'FailureHandlingKind': 'StrEnum',
    'FileOperationPatternKind': 'StrEnum',
    'FoldingRangeKind': 'StrEnum',
    'LanguageKind': 'StrEnum',
    'MarkupKind': 'StrEnum',
    'MonikerKind': 'StrEnum',
    'PositionEncodingKind': 'StrEnum',
    'ResourceOperationKind': 'StrEnum',
    'SemanticTokenModifiers': 'StrEnum',
    'SemanticTokenTypes': 'StrEnum',
    'TokenFormat': 'StrEnum',
    'TraceValue': 'StrEnum',
    'UniquenessLevel': 'StrEnum',
    'WatchKind': 'IntFlag',
    'ApplyKind': 'IntFlag',
}

ALIAS_OVERRIDES: dict[str, str] = {
    'LSPArray': "Sequence['LSPAny']",
    'LSPObject': 'Mapping[str, Any]'
}


def generate(output: str) -> None:
    reset_new_literal_structures()

    schema = Path('./lsprotocol/lsp.json').read_text(encoding='utf-8')
    lsp_json = cast('MetaModel', json.loads(schema))
    specification_version = lsp_json.get('metaData')['version']

    content = '\n'.join(
        [
            '# ruff: noqa: E501, UP006, UP007',
            '# Code generated. DO NOT EDIT.',
            f'# LSP v{specification_version}\n',
            'from __future__ import annotations',
            'from enum import IntEnum, IntFlag, StrEnum',
            'from typing import Any, Dict, List, Literal, Mapping, Sequence, TypedDict, Union',
            'from typing_extensions import NotRequired\n\n',
            'URI = str',
            'DocumentUri = str',
            'Uint = int',
            'RegExp = str',
        ]
    )

    content += '\n\n\n'
    content += '\n\n\n'.join(generate_enumerations(lsp_json['enumerations'], ENUM_OVERRIDES))
    content += '\n\n'
    content += '\n'.join(generate_type_aliases(lsp_json['typeAliases'], ALIAS_OVERRIDES))
    content += '\n\n\n'
    content += '\n\n\n'.join(generate_structures(lsp_json['structures']))
    content += '\n\n'
    content += '\n'.join(get_new_literal_structures())

    # Remove trailing spaces.
    lines = content.split('\n')
    lines = [line.rstrip() for line in lines]
    content = '\n'.join(lines)

    Path(output).write_text(content)


generate(output='./generated/lsp_types.py')
