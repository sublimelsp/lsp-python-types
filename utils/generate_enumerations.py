from typing import List
from lsp_schema import Enumeration, EnumerationEntry
from utils.helpers import capitalize, format_comment, indentation


def format_enumeration_values(values: List[EnumerationEntry]) -> str:
    result: List[str] = []
    for v in values:
        key = capitalize(v['name'])
        if key == 'None':
            print('Conflict with None keyword, fallback to Null')
            key = 'Null'  # 'None' is a reserved keyword, use Null :)
        value = v['value']
        try:
            value = int(value)
        except ValueError:
            value = f"'{value}'"
        documentation = format_comment(v.get('documentation'), indentation)
        if documentation:
            documentation = '\n' + documentation

        result.append(f"{key} = {value}{documentation}")

    return f"\n{indentation}".join(result)


def generate_enumerations(enumerations: List[Enumeration]) -> List[str]:

    def toString(enumeration: Enumeration) -> str:
        result = ''
        symbol_name = enumeration['name']
        documentation = format_comment(enumeration.get('documentation'), indentation)
        values = format_enumeration_values(enumeration['values'])
        result += f"class {symbol_name}(Enum):\n"
        if documentation:
            result += f"{documentation}\n"
        result += f'{indentation}' + values
        return result

    return [toString(enumeration) for enumeration in enumerations]
