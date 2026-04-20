from __future__ import annotations

from typing import TYPE_CHECKING
from utils.helpers import format_comment
from utils.helpers import format_type

if TYPE_CHECKING:
    from lsp_schema import Enumeration
    from lsp_schema import TypeAlias


def generate_type_aliases(
    type_aliases: list[TypeAlias], overrides: dict[str, str], enumerations: dict[str, Enumeration]
) -> list[str]:
    def to_string(type_alias: TypeAlias) -> str:
        symbol_name = type_alias['name']
        documentation = format_comment(type_alias.get('documentation'))
        if symbol_name in overrides:
            value = overrides[symbol_name]
        else:
            value = format_type(type_alias['type'], {'enumerations': enumerations})
        result = f"""
{symbol_name}: TypeAlias = {value}"""
        if documentation:
            result += f"""\n{documentation}"""
        return result

    return [to_string(type_alias) for type_alias in type_aliases]
