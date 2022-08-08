from typing import List
from lsp_schema import Structure
from utils.helpers import format_comment, format_class_properties, format_dict_properties, get_formatted_properties, has_invalid_property_name

def generate_structures(structures: List[Structure]) -> str:
	result = ""

	# Sorting is here important!
	# First define types that do not extend anything.
	# to avoid errors like:
	# TextDocumentPositionParams" is not defined
	# And hope that types that extend other types
	# don't extend types that are not yet defined :)
	structures = sorted(structures, key=lambda s: len(s.get('extends') or []))

	for structure in structures:
		if has_invalid_property_name(structure['properties']):
			result += generate_function_type(structure)
		else:
			result += generate_class_type(structure)
	return result

def get_extends_for_structure(structure: Structure) -> str:
	result = []
	extends = structure.get('extends') or []
	for e in extends:
		if e['kind'] != 'reference':
			raise Exception("Cannot generate extends. Currently only supports kind: 'reference', but recieved:", e['kind'])
		result.append(e['name'])
	result.append('TypedDict')
	return ", ".join(result)


def generate_class_type(structure: Structure) -> str:
	result = ""
	symbol_name = structure['name']
	documentation = format_comment(structure.get('documentation'))
	properties = get_formatted_properties(structure['properties'])
	formatted_properties = format_class_properties(properties)
	extends = get_extends_for_structure(structure)
	result += f"class {symbol_name}({extends}):\n"
	if documentation:
		result += f"\t{documentation}\n"
	result += f"\t{formatted_properties or 'pass'}\n\n"
	return result


def generate_function_type(structure: Structure) -> str:
	# TODO improvement
	# MyType = TypedDict('MyType', {}), doesn't support inheritance,
	# Add properties from structure['extends'] types in the properties list
	result = ""
	symbol_name = structure['name']
	documentation = format_comment(structure.get('documentation'))
	properties = get_formatted_properties(structure['properties'])
	formatted_properties = format_dict_properties(properties)
	# TODO improvement
	# MyType = TypedDict('MyType', {}), doesn't support inheritance,
	# Add properties from structure['extends'] types in the properties list
	result += f"{symbol_name} = TypedDict('{symbol_name}', "
	result += "{\n"
	result += f"\t{formatted_properties}\n"
	result += "})"
	if documentation:
		result += f"\n{documentation}"
	result += "\n\n"

	return result