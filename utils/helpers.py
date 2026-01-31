from __future__ import annotations
from enum import Enum
from typing import Any, ClassVar, TypedDict, TYPE_CHECKING
import keyword

if TYPE_CHECKING:
    from lsp_schema import EveryType, BaseType, MapKeyType, Property


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


class SymbolNameTracker:
    symbols: ClassVar[dict[str, int]] = {
        # key: symbol name
        # value: symbol count
    }

    @classmethod
    def get_symbol_id(cls, symbol_name: str) -> int:
        count = SymbolNameTracker.symbols.get(symbol_name) or 1
        SymbolNameTracker.symbols[symbol_name] = count + 1
        return count

    @classmethod
    def clear(cls) -> None:
        SymbolNameTracker.symbols.clear()


def get_new_literal_structures() -> list[str]:
    return sorted(new_literal_structures)


def reset_new_literal_structures() -> None:
    new_literal_structures.clear()
    SymbolNameTracker.clear()


class StructureKind(Enum):
    Class = 1
    Function = 2


class FormatTypeContext(TypedDict):
    root_symbol_name: str


def format_type(typ: EveryType, context: FormatTypeContext, preferred_structure_kind: StructureKind) -> str:
    result = 'Any'
    if typ['kind'] == 'base':
        return format_base_types(typ)
    if typ['kind'] == 'reference':
        literal_symbol_name = typ['name']
        return f"'{literal_symbol_name}'"
    if typ['kind'] == 'array':
        literal_symbol_name = format_type(typ['element'], context, preferred_structure_kind)
        return f'List[{literal_symbol_name}]'
    if typ['kind'] == 'map':
        key = format_base_types(typ['key'])
        value = format_type(typ['value'], {'root_symbol_name': key}, preferred_structure_kind)
        return f'Dict[{key}, {value}]'
    if typ['kind'] == 'and':
        pass
    elif typ['kind'] == 'or':
        union = [format_type(item, context, preferred_structure_kind) for item in typ['items']]
        return f'Union[{", ".join(union)}]'
    elif typ['kind'] == 'tuple':
        union = [format_type(item, context, preferred_structure_kind) for item in typ['items']]
        return f'tuple[{", ".join(union)}]'
    elif typ['kind'] == 'literal':
        if not typ['value']['properties']:
            return 'Dict[str, LSPAny]'
        root_symbol_name = capitalize(context['root_symbol_name'])
        literal_symbol_name = f'__{root_symbol_name}_Type'
        symbol_id = SymbolNameTracker.get_symbol_id(literal_symbol_name)
        literal_symbol_name += f'_{symbol_id}'
        properties = get_formatted_properties(typ['value']['properties'], root_symbol_name, preferred_structure_kind)
        if preferred_structure_kind == StructureKind.Function:
            formatted_properties = format_dict_properties(properties)
            new_literal_structures.add(f"""
{literal_symbol_name} = TypedDict('{literal_symbol_name}', {{
{indentation}{formatted_properties}
}})
""")
        else:
            formatted_properties = format_class_properties(properties)
            new_literal_structures.add(f"""
class {literal_symbol_name}(TypedDict):
{indentation}{formatted_properties or 'pass'}
""")
        return f"'{literal_symbol_name}'"
    elif typ['kind'] == 'stringLiteral':
        return f"Literal['{typ['value']}']"
    elif typ['kind'] == 'integerLiteral' or typ['kind'] == 'booleanLiteral':
        return f'Literal[{typ["value"]}]'
    return result


def format_base_types(base_type: BaseType | MapKeyType) -> str:
    mapping: dict[str, str] = {
        'integer': 'int',
        'uinteger': 'Uint',
        'decimal': 'float',
        'string': 'str',
        'boolean': 'bool',
        'null': 'None'
    }
    name = base_type['name']

    return mapping.get(name, name)


class FormattedProperty(TypedDict):
    name: str
    value: Any
    documentation: str


def get_formatted_properties(
    properties: list[Property], root_symbol_name: str, preferred_structure_kind: StructureKind
) -> list[FormattedProperty]:
    result: list[FormattedProperty] = []
    for p in properties:
        key = p['name']
        value = format_type(p['type'], {'root_symbol_name': root_symbol_name + '_' + key}, preferred_structure_kind)
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
