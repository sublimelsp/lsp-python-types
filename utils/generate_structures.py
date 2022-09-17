from typing import List
from lsp_schema import Structure
from utils.helpers import FormattedProperty, format_comment, indentation, format_class_properties, format_dict_properties, get_formatted_properties, has_invalid_property_name


def generate_structures(structures: List[Structure]) -> List[str]:

    def toString(structure: Structure) -> str:
        if has_invalid_property_name(structure['properties']):
            return generate_function_type(structure, structures)
        return generate_class_type(structure, structures)

    return [toString(structure) for structure in structures]


def get_additional_properties(for_structure: Structure, structures: List[Structure]) -> List[FormattedProperty]:
    """Returns properties from extended and mixin types. """
    result: List[FormattedProperty] = []
    additional_structures = for_structure.get('extends') or []
    additional_structures.extend(for_structure.get('mixins') or [])
    for additional_structure in additional_structures:
        if additional_structure['kind'] != 'reference':
            raise Exception("Cannot generate extends. Currently only supports kind: 'reference', but received:", additional_structure['kind'])
        structure = next(structure for structure in structures if structure["name"] == additional_structure['name'])
        if structure:
            properties = get_formatted_properties(structure['properties'])
            result.extend(properties)
    return result


def generate_class_type(structure: Structure, structures: List[Structure]) -> str:
    result = ""
    symbol_name = structure['name']
    documentation = format_comment(structure.get('documentation'), indentation)
    properties = get_formatted_properties(structure['properties'])
    additional_properties = get_additional_properties(structure, structures)

    # add extended properties
    taken_property_names = [property['name'] for property in properties]
    for additional_property in additional_properties:
        if additional_property['name'] not in taken_property_names:
            properties.append(additional_property)

    formatted_properties = format_class_properties(properties)
    result += f"class {symbol_name}(TypedDict):\n"
    if documentation:
        result += f"{documentation}\n"
    result += f"{indentation}{formatted_properties or 'pass'}"
    return result


def generate_function_type(structure: Structure, structures: List[Structure]) -> str:
    result = ""
    symbol_name = structure['name']
    documentation = format_comment(structure.get('documentation'))
    properties = get_formatted_properties(structure['properties'])
    formatted_properties = format_dict_properties(properties)

    additional_properties = get_additional_properties(structure, structures)

    # add extended properties
    taken_property_names = [property['name'] for property in properties]
    for additional_property in additional_properties:
        if additional_property['name'] not in taken_property_names:
            properties.append(additional_property)

    result += f"{symbol_name} = TypedDict('{symbol_name}', "
    result += "{\n"
    result += f"{indentation}{formatted_properties}\n"
    result += "})"
    if documentation:
        result += f"\n{documentation}"

    return result
