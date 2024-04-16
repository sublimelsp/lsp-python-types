from enum import Enum
from lsp_schema import Enumeration, EnumerationEntry
from typing import Dict, List, Literal
from utils.helpers import capitalize, format_comment, indentation
import keyword


class EnumKind(Enum):
    Number = 1
    String = 2


def format_enumeration_values(values: List[EnumerationEntry], kind: EnumKind) -> str:
    result: List[str] = []
    for v in values:
        key = capitalize(v['name'])
        if keyword.iskeyword(key):
            print(f'Conflict with {key} keyword, fallback to {key}_')
            key += "_"
        value = f"'{v['value']}'" if kind == EnumKind.String else v['value']
        documentation = format_comment(v.get('documentation'), indentation)
        if documentation:
            documentation = '\n' + documentation

        result.append(f"{key} = {value}{documentation}")

    return f"\n{indentation}".join(result)


def format_enumeration_literal_values(values: List[EnumerationEntry]) -> str:
    result: List[str] = []
    for v in values:
        value = f"'{v['value']}'"
        result.append(value)
    return f", ".join(result)


def generate_enumerations(enumerations: List[Enumeration], overrides: Dict[str, Literal['StrEnum', 'IntFlag']]) -> List[str]:

    def toString(enumeration: Enumeration) -> str:
        result = ''
        symbol_name = enumeration['name']
        documentation = format_comment(enumeration.get('documentation'), indentation)
        kind = EnumKind.String if enumeration['type']['name'] == 'string' else EnumKind.Number
        enum_class_override = overrides.get(symbol_name)
        enum_class = enum_class_override or ('Enum' if kind == EnumKind.String else 'IntEnum')
        values = format_enumeration_values(enumeration['values'], kind)
        result += f"class {symbol_name}({enum_class}):\n"
        if documentation:
            result += f"{documentation}\n"
        result += f'{indentation}' + values
        result += '\n'

        # add Literal types only for strings
        if kind == EnumKind.String:
            litearal_values = format_enumeration_literal_values(enumeration['values'])
            documentation = format_comment(enumeration.get('documentation'), '')
            result += f"\n\n{symbol_name}Literal = Literal[{litearal_values}]"
            if documentation:
                result += f"\n{documentation}\n"
        return result

    return [toString(enumeration) for enumeration in enumerations]
