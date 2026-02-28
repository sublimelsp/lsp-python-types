#!/usr/bin/env python3

from __future__ import annotations

from operator import itemgetter
from pathlib import Path
from typing import cast
from typing import Literal
from typing import TYPE_CHECKING
from utils.generate_enumerations import generate_enumerations
from utils.generate_notifications import generate_notifications
from utils.generate_requests_and_responses import generate_requests_and_responses
from utils.generate_structures import generate_structures
from utils.generate_type_aliases import generate_type_aliases
from utils.helpers import get_new_literal_structures
from utils.helpers import reset_new_literal_structures
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

ALIAS_OVERRIDES: dict[str, str] = {'LSPArray': "Sequence['LSPAny']", 'LSPObject': 'Mapping[str, Any]'}


def generate_protocol(output: str) -> None:
    reset_new_literal_structures()

    schema = Path('./lsprotocol/lsp.json').read_text(encoding='utf-8')
    lsp_json = cast('MetaModel', json.loads(schema))
    specification_version = lsp_json.get('metaData')['version']

    content = '\n'.join(
        [
            '# ruff: noqa: E501, UP006, UP007',
            '# Code generated. DO NOT EDIT.',
            f'# LSP v{specification_version}\n',
            'from __future__ import annotations\n',
            'from enum import IntEnum',
            'from enum import IntFlag',
            'from enum import StrEnum',
            'from typing import Any',
            'from typing import Dict',
            'from typing import List',
            'from typing import Literal',
            'from typing import Mapping',
            'from typing import Sequence',
            'from typing import TypedDict',
            'from typing import Union',
            'from typing_extensions import NotRequired',
            'from typing_extensions import TypeAlias\n',
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
    content += '\n'
    content += '\n'.join(get_new_literal_structures())

    # Remove trailing spaces.
    lines = content.split('\n')
    lines = [line.rstrip() for line in lines]
    content = '\n'.join(lines)

    Path(output).write_text(content, encoding='utf-8')


def generate_custom(output: str) -> None:
    reset_new_literal_structures()

    schema = Path('./lsprotocol/lsp.json').read_text(encoding='utf-8')
    lsp_json = cast('MetaModel', json.loads(schema))

    content = '\n'.join(  # noqa: FLY002
        [
            '# ruff: noqa: UP006, UP007',
            'from __future__ import annotations\n',
            'from .lsp_types import *',
            'from typing import List',
            'from typing import Literal',
            'from typing import TypedDict',
            'from typing import Union',
            'from typing_extensions import TypeAlias',
        ]
    )

    # Sort by method name to avoid unstable order.
    requests = sorted(lsp_json['requests'], key=itemgetter('typeName'))
    notifications = sorted(lsp_json['notifications'], key=itemgetter('typeName'))

    content += '\n\n\n'
    content += '\n\n\n'.join(generate_requests_and_responses(requests))
    content += '\n\n\n'
    content += '\n\n\n'.join(generate_notifications(notifications))
    content += '\n'

    # Remove trailing spaces.
    lines = content.split('\n')
    lines = [line.rstrip() for line in lines]
    content = '\n'.join(lines)

    Path(output).write_text(content, encoding='utf-8')


generate_protocol(output='./generated/lsp_types.py')
generate_custom(output='./generated/custom.py')
