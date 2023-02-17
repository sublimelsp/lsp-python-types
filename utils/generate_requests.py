from typing import List
from lsp_schema import Request
from utils.helpers import format_comment, format_type, indentation, StructureKind
import re

method_to_symbol_name = {
    "textDocument/implementation": "implementation",
    "textDocument/typeDefinition": "type_definition",
    "textDocument/documentColor": "document_color",
    "textDocument/colorPresentation": "color_presentation",
    "textDocument/foldingRange": "folding_range",
    "textDocument/declaration": "declaration",
    "textDocument/selectionRange": "selection_range",
    "textDocument/prepareCallHierarchy": "prepare_call_hierarchy",
    "callHierarchy/incomingCalls": "incoming_calls",
    "callHierarchy/outgoingCalls": "outgoing_calls",
    "textDocument/semanticTokens/full": "semantic_tokens_full",
    "textDocument/semanticTokens/full/delta": "semantic_tokens_delta",
    "textDocument/semanticTokens/range": "semantic_tokens_range",
    "textDocument/linkedEditingRange": "linked_editing_range",
    "workspace/willCreateFiles": "will_create_files",
    "workspace/willRenameFiles": "will_rename_files",
    "workspace/willDeleteFiles": "will_delete_files",
    "textDocument/moniker": "moniker",
    "textDocument/prepareTypeHierarchy": "prepare_type_hierarchy",
    "typeHierarchy/supertypes": "type_hierarchy_supertypes",
    "typeHierarchy/subtypes": "type_hierarchy_subtypes",
    "textDocument/inlineValue": "inline_value",
    "textDocument/inlayHint": "inlay_hint",
    "inlayHint/resolve": "resolve_inlay_hint",
    "textDocument/diagnostic": "text_document_diagnostic",
    "workspace/diagnostic": "workspace_diagnostic",
    "initialize": "initialize",
    "shutdown": "shutdown",
    "textDocument/willSaveWaitUntil": "will_save_wait_until",
    "textDocument/completion": "completion",
    "completionItem/resolve": "resolve_completion_item",
    "textDocument/hover": "hover",
    "textDocument/signatureHelp": "signature_help",
    "textDocument/definition": "definition",
    "textDocument/references": "references",
    "textDocument/documentHighlight": "document_highlight",
    "textDocument/documentSymbol": "document_symbol",
    "textDocument/codeAction": "code_action",
    "codeAction/resolve": "resolve_code_action",
    "workspace/symbol": "workspace_symbol",
    "workspaceSymbol/resolve": "resolve_workspace_symbol",
    "textDocument/codeLens": "code_lens",
    "codeLens/resolve": "resolve_code_lens",
    "textDocument/documentLink": "document_link",
    "documentLink/resolve": "resolve_document_link",
    "textDocument/formatting": "formatting",
    "textDocument/rangeFormatting": "range_formatting",
    "textDocument/onTypeFormatting": "on_type_formatting",
    "textDocument/rename": "rename",
    "textDocument/prepareRename": "prepare_rename",
    "workspace/executeCommand": "execute_command"
}

def generate_requests(requests: List[Request]) -> List[str]:

    def toString(request: Request) -> str:
        return generate_request(request)

    return [toString(request) for request in requests if request['messageDirection'] in ['clientToServer', 'both']]


def generate_request(request: Request) -> str:
    result = ""
    method = request['method']
    symbol_name = method_to_symbol_name.get(method)
    if not symbol_name:
        raise Exception('Please define a symbol name for ', method)
    params = request.get('params', {})
    formatted_params = ""
    if params:
        if isinstance(params, list):
             raise Exception('You need to add code to handle when params is of type List[_Type]')

        # ... I implemented the case when the params is a referenceS
        # "params": {
        #     "kind": "reference",
        #     "name": "ImplementationParams"
        # },
        params_type = params.get('name')
        if not params_type:
            raise Exception('I expected params to be of type _Type. But got: ' + str(params))
        formatted_params = f",  params: lsp_types.{params_type}"
    result_type = format_type(request['result'], {
        "root_symbol_name": ""
    }, StructureKind.Class)
    result_type = prefix_lsp_types(result_type)
    # fix  Expected class type but received "str"
    result_type = result_type.replace("DefinitionLink", "LocationLink")
    result_type = result_type.replace("DeclarationLink", "LocationLink")
    result += f"{indentation}async def {symbol_name}(self{formatted_params}) -> {result_type}:"
    documentation = format_comment(request.get('documentation'), indentation + indentation)
    if documentation:
        result += f'\n{documentation}'
    result += f"""\n{indentation}{indentation}return await self.send_request("{method}"{', params' if params else ''})\n"""
    return result


def prefix_lsp_types(text: str) -> str:
    return re.sub(r"'(\w+)'", r"'lsp_types.\1'", text)