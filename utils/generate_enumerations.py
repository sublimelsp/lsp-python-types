from typing import List
from lsp_schema import Enumeration, EnumerationEntry
from utils.helpers import capitalize, format_comment


def format_enumeration_values(values: List[EnumerationEntry]) -> str:
	result = []
	for v in values:
		key = capitalize(v['name'])
		if key == 'None':
			print('Conflict with None keyword, fallback to Null')
			key = 'Null' # 'None' is a reserved keyword, use Null :)
		value = v['value']
		try:
			value = int(value)
		except ValueError:
			value = f"'{value}'"
		documentation = format_comment(v.get('documentation'), '\n\t')

		result.append(f"{key} = {value}{documentation}")

	return "\n\t".join(result)


def generate_enumerations(enumerations: List[Enumeration]) -> str:
	result = ""

	for enumeration in enumerations:
		symbol_name = enumeration['name']
		documentation = format_comment(enumeration.get('documentation'))
		values = format_enumeration_values(enumeration['values'])
		result += f"\nclass {symbol_name}(Enum):\n"
		if documentation:
			result += f"\t{documentation}\n"
		result += '\t' + values
		result += "\n"
	return result