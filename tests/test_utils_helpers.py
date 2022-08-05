import unittest
from utils.helpers import format_comment, capitalize


class UtilsHelpersTests(unittest.TestCase):
    def test_format_comment_when_text_exist(self):
        result = format_comment("Some comment.")
        expected = """\"\"\" Some comment. \"\"\""""
        self.assertEqual(result, expected)

    def test_format_comment_when_text_not_exist(self):
        result = format_comment("")
        expected = ""
        self.assertEqual(result, expected)

    def test_uppercase_first_letter(self):
        result = capitalize("asIs")
        expected = "AsIs"
        self.assertEqual(result, expected)