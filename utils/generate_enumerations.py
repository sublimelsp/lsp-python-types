from enum import Enum
from typing import List
from lsp_schema import Enumeration, EnumerationEntry
from utils.helpers import capitalize, format_comment, indentation


class EnumKind(Enum):
    Number = 1
    String = 2


def format_enumeration_values(values: List[EnumerationEntry], kind: Enum) -> str:
    result: List[str] = []
    for v in values:
        key = capitalize(v['name'])
        if key == 'None':
            print('Conflict with None keyword, fallback to Null')
            key = 'Null'  # 'None' is a reserved keyword, use Null :)
        value = f"'{v['value']}'" if kind == EnumKind.String else v['value']
        documentation = format_comment(v.get('documentation'), indentation)
        if documentation:
            documentation = '\n' + documentation

        result.append(f"{key} = {value}{documentation}")

    return f"\n{indentation}".join(result)


def generate_enumerations(enumerations: List[Enumeration], bitwise_enums: List[str]) -> List[str]:

    def toString(enumeration: Enumeration) -> str:
        result = ''
        symbol_name = enumeration['name']
        documentation = format_comment(enumeration.get('documentation'), indentation)
        kind = EnumKind.String if enumeration['type']['name'] == 'string' else EnumKind.Number
        if kind == EnumKind.String:
            enum_class = 'Enum'
        else:
            enum_class = 'IntFlag' if symbol_name in bitwise_enums else 'IntEnum'
        values = format_enumeration_values(enumeration['values'], kind)
        result += f"class {symbol_name}({enum_class}):\n"
        if documentation:
            result += f"{documentation}\n"
        result += f'{indentation}' + values
        return result

    return [toString(enumeration) for enumeration in enumerations]
