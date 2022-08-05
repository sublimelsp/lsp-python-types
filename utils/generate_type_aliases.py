from typing import List
from lsp_schema import TypeAlias
from utils.helpers import format_comment, format_type

def generate_type_aliases(type_aliases: List[TypeAlias]) -> str:
	result = ""

	for type_alias in type_aliases:
		symbol_name = type_alias['name']
		documentation = format_comment(type_alias.get('documentation'))
		value = format_type(type_alias['type'], {
			'root_symbol_name': symbol_name
		})
		result += f"""
{symbol_name} = {value}
{documentation}
"""
	return result
