from __future__ import annotations
from utils.helpers import format_comment, format_type, StructureKind
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from lsp_schema import TypeAlias


def generate_type_aliases(
    type_aliases: list[TypeAlias], preferred_structure_kind: StructureKind = StructureKind.Class
) -> list[str]:
    def to_string(type_alias: TypeAlias) -> str:
        symbol_name = type_alias['name']
        documentation = format_comment(type_alias.get('documentation'))
        value = format_type(type_alias['type'], {'root_symbol_name': symbol_name}, preferred_structure_kind)
        result = f"""
{symbol_name} = {value}"""
        if documentation:
            result += f"""\n{documentation}"""
        return result

    return [to_string(type_alias) for type_alias in type_aliases]
