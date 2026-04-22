from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any
from typing import Literal
from typing import TYPE_CHECKING
from typing import TypedDict
import keyword

if TYPE_CHECKING:
    from lsp_schema import BaseType
    from lsp_schema import Enumeration
    from lsp_schema import EnumerationType
    from lsp_schema import EveryType
    from lsp_schema import MapKeyType
    from lsp_schema import Property


indentation = '    '


def capitalize(text: str) -> str:
    return text[0].upper() + text[1:]


def format_comment(text: str | None, indent: str = '') -> str:
    if not text:
        return ''
    # Replace zero-width spaces.
    text = text.replace('\u200b', '')
    # Replace DIVISION SLASH that triggers RUF001.
    text = text.replace('\u2215', '/')
    is_multiline = '\n' in text
    contains_backslashes = '\\' in text
    raw = 'r' if contains_backslashes else ''
    if is_multiline:
        lines = text.splitlines(keepends=True)
        text = indent.join(lines)
        text = f'\n{indent}{text}\n{indent}'
    return f'{indent}{raw}"""{text}"""'


new_literal_structures: set[str] = set()


def get_new_literal_structures() -> list[str]:
    return sorted(new_literal_structures)


def reset_new_literal_structures() -> None:
    new_literal_structures.clear()


class StructureKind(Enum):
    Class = 1
    Function = 2


@dataclass
class GeneratorContext:
    alias_overrides: dict[str, str]
    enum_overrides: dict[str, Literal['StrEnum', 'IntFlag']]
    enumerations: dict[str, Enumeration]


def format_type(typ: EveryType, context: GeneratorContext) -> str:
    result = 'Any'
    if typ['kind'] == 'base':
        return format_base_types(typ)
    if typ['kind'] == 'reference':
        literal_symbol_name = typ['name']
        if (
            (enum := context.enumerations.get(literal_symbol_name))
            and enum.get('supportsCustomValues')
            and context.enum_overrides.get(literal_symbol_name) != 'IntFlag'
        ):
            return f'Union[{format_type(enum["type"], context)}, {literal_symbol_name}]'
        return f"'{literal_symbol_name}'"
    if typ['kind'] == 'array':
        literal_symbol_name = format_type(typ['element'], context)
        return f'List[{literal_symbol_name}]'
    if typ['kind'] == 'map':
        key = format_base_types(typ['key'])
        value = format_type(typ['value'], context)
        return f'Dict[{key}, {value}]'
    if typ['kind'] == 'and':
        pass
    elif typ['kind'] == 'or':
        union = [format_type(item, context) for item in typ['items']]
        return f'Union[{", ".join(union)}]'
    elif typ['kind'] == 'tuple':
        union = [format_type(item, context) for item in typ['items']]
        return f'list[{" | ".join(set(union))}]'
    elif typ['kind'] == 'literal':
        if not typ['value']['properties']:
            return 'Dict[str, LSPAny]'
        msg = 'Unsupported case, none of the cases in LSP schema need this currently!'
        raise Exception(msg)
    elif typ['kind'] == 'stringLiteral':
        return f"Literal['{typ['value']}']"
    elif typ['kind'] == 'integerLiteral' or typ['kind'] == 'booleanLiteral':
        return f'Literal[{typ["value"]}]'
    return result


def format_base_types(base_type: BaseType | MapKeyType | EnumerationType) -> str:
    mapping: dict[str, str] = {
        'integer': 'int',
        'uinteger': 'Uint',
        'decimal': 'float',
        'string': 'str',
        'boolean': 'bool',
        'null': 'None',
    }
    name = base_type['name']

    return mapping.get(name, name)


class FormattedProperty(TypedDict):
    name: str
    value: Any
    documentation: str


def get_formatted_properties(properties: list[Property], context: GeneratorContext) -> list[FormattedProperty]:
    result: list[FormattedProperty] = []
    for p in properties:
        key = p['name']
        value = format_type(p['type'], context)
        if p.get('optional'):
            value = f'NotRequired[{value}]'
        documentation = p.get('documentation') or ''
        result.append({'name': key, 'value': value, 'documentation': documentation})  # f"{key}: {value}{documentation}"

    return result  # "\n\t".join(result)


def has_invalid_property_name(properties: list[Property]) -> bool:
    return any(keyword.iskeyword(p['name']) for p in properties)


def format_class_properties(properties: list[FormattedProperty]) -> str:
    result: list[str] = []
    for p in properties:
        line = f'{p["name"]}: {p["value"]}'
        comment = format_comment(p['documentation'], indentation)
        if comment:
            line += f'\n{comment}'
        result.append(line)
    return f'\n{indentation}'.join(result)


def format_dict_properties(properties: list[FormattedProperty]) -> str:
    result: list[str] = []
    for p in properties:
        documentation = p.get('documentation')
        formatted_documentation = ''
        if documentation:
            formatted_documentation = documentation.replace('\n', f'\n{indentation}# ')
            formatted_documentation = f'# {formatted_documentation}\n{indentation}'
        result.append(f"{formatted_documentation}'{p['name']}': {p['value']},")
    return f'\n{indentation}'.join(result)
