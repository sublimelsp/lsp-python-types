from typing import Any, List
from lsp_schema import Structure
from utils.helpers import FormattedProperty, format_comment, format_class_properties, format_dict_properties, get_formatted_properties, has_invalid_property_name

def generate_structures(structures: List[Structure]) -> str:
	result = ""

	for structure in structures:
		if has_invalid_property_name(structure['properties']):
			result += generate_function_type(structure, structures)
		else:
			result += generate_class_type(structure, structures)
	return result

def get_extends_properties(for_structure: Structure, structures: List[Structure]) -> List[FormattedProperty]:
	result: List[FormattedProperty] = []
	extends = for_structure.get('extends') or []
	for e in extends:
		if e['kind'] != 'reference':
			raise Exception("Cannot generate extends. Currently only supports kind: 'reference', but recieved:", e['kind'])
		extended_structure = next(structure for structure in structures if structure["name"] == e['name'])
		if extended_structure:
			properties = get_formatted_properties(extended_structure['properties'])
			result.extend(properties)
	return result


def generate_class_type(structure: Structure, structures: List[Structure]) -> str:
	result = ""
	symbol_name = structure['name']
	documentation = format_comment(structure.get('documentation'))
	properties = get_formatted_properties(structure['properties'])
	extended_properties = get_extends_properties(structure, structures)

	# add extended properties
	taken_property_names = [property['name'] for property in properties]
	for extended_property in extended_properties:
		if extended_property['name'] not in taken_property_names:
			properties.append(extended_property)

	formatted_properties = format_class_properties(properties)
	result += f"class {symbol_name}(TypedDict):\n"
	if documentation:
		result += f"\t{documentation}\n"
	result += f"\t{formatted_properties or 'pass'}\n\n"
	return result


def generate_function_type(structure: Structure, structures: List[Structure]) -> str:
	# TODO improvement
	# MyType = TypedDict('MyType', {}), doesn't support inheritance,
	# Add properties from structure['extends'] types in the properties list
	result = ""
	symbol_name = structure['name']
	documentation = format_comment(structure.get('documentation'))
	properties = get_formatted_properties(structure['properties'])
	formatted_properties = format_dict_properties(properties)

	extended_properties = get_extends_properties(structure, structures)

	# add extended properties
	taken_property_names = [property['name'] for property in properties]
	for extended_property in extended_properties:
		if extended_property['name'] not in taken_property_names:
			properties.append(extended_property)

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