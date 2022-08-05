from typing import List
import unittest

from lsp_schema import Enumeration
from utils.generate_enumerations import generate_enumerations

class GenerateEnumerationsTests(unittest.TestCase):
	def test_generate_str_enumerations(self):
		json: List[Enumeration] = [{
			"name": "FoldingRangeKind",
			"type": {
				"kind": "base",
				"name": "string"
			},
			"values": [
				{
					"name": "Comment",
					"value": "comment",
				},
				{
					"name": "Imports",
					"value": "imports",
				},
				{
					"name": "Region",
					"value": "region",
				}
			],
		}]

		expected = """
class FoldingRangeKind(Enum):
	Comment = 'comment'
	Imports = 'imports'
	Region = 'region'
"""

		self.assertEqual(generate_enumerations(json), expected)


	def test_generate_int_enumerations(self):
		json: List[Enumeration] = [{
			"name": "SymbolTag",
			"type": {
				"kind": "base",
				"name": "uinteger"
			},
			"values": [
				{
					"name": "Deprecated",
					"value": 1,
					"documentation": "Render a symbol as obsolete, usually using a strike-out."
				}
			],
			"documentation": "Symbol tags are extra annotations that tweak the rendering of a symbol.\n\n@since 3.16",
			"since": "3.16"
		}]

		expected = """
class SymbolTag(Enum):
	\"\"\" Symbol tags are extra annotations that tweak the rendering of a symbol.
\t
	@since 3.16 \"\"\"
	Deprecated = 1
	\"\"\" Render a symbol as obsolete, usually using a strike-out. \"\"\"
"""

		self.assertEqual(generate_enumerations(json), expected)

	def test_generate_negative_int_enumerations(self):
		json: List[Enumeration] = [{
			"name": "ErrorCodes",
			"type": {
				"kind": "base",
				"name": "integer"
			},
			"values": [
				{
					"name": "ParseError",
					"value": -32700
				}
			]
		}]

		expected ="""
class ErrorCodes(Enum):
	ParseError = -32700
"""
		self.assertEqual(generate_enumerations(json), expected)

	def test_dont_use_keyword_for_enum_keys_because_they_are_not_allowed(self):
		json: List[Enumeration] = [{
			"name": "TextDocumentSyncKind",
			"type": {
				"kind": "base",
				"name": "uinteger"
			},
			"values": [
				{
					"name": "None",
					"value": 0
				}
			]
		}]

		expected ="""
class TextDocumentSyncKind(Enum):
	Null = 0
"""
		self.assertEqual(generate_enumerations(json), expected)