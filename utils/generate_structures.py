from typing import List
from lsp_schema import Structure
from utils.helpers import format_comment, format_properties

def generate_structures(structures: List[Structure]) -> str:
	result = ""

	# Sorting is here important!
	# First define types that do not extend anything.
	# to avoid errors like:
	# TextDocumentPositionParams" is not defined
	# And hope that types that extend other types
	# dont extend types that are not yet defined :)
	structures = sorted(structures, key=lambda s: len(s.get('extends') or []))

	for structure in structures:
		symbol_name = structure['name']
		documentation = format_comment(structure.get('documentation'))
		extends = get_extends_for_structure(structure)
		properties = format_properties(structure['properties'])
		result += f"class {symbol_name}({extends}):\n"
		if documentation:
			result += f"\t{documentation}\n"
		result += f"\t{properties or 'pass'}\n\n"
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