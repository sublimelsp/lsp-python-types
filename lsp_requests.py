
# Code generated. DO NOT EDIT.
from lsp_request_context import RequestContext
import lsp_types
from typing import List, Union, Generic, TypeVar

T = TypeVar('T')
class Response(Generic[T]):
    def __init__(self, result: T, id: int, context: RequestContext) -> None:
        super().__init__()
        self.result = result
        self.id = id
        self.context = context


class LspRequest:
    def __init__(self, send_request):
        self.send_request = send_request

    async def implementation(self,  params: lsp_types.ImplementationParams) -> Response[Union['lsp_types.Definition', List['lsp_types.LocationLink'], None]]:
        return await self.send_request("textDocument/implementation", params)

    async def type_definition(self,  params: lsp_types.TypeDefinitionParams) -> Response[Union['lsp_types.Definition', List['lsp_types.LocationLink'], None]]:
        return await self.send_request("textDocument/typeDefinition", params)

    async def document_color(self,  params: lsp_types.DocumentColorParams) -> Response[List['lsp_types.ColorInformation']]:
        return await self.send_request("textDocument/documentColor", params)

    async def color_presentation(self,  params: lsp_types.ColorPresentationParams) -> Response[List['lsp_types.ColorPresentation']]:
        return await self.send_request("textDocument/colorPresentation", params)

    async def folding_range(self,  params: lsp_types.FoldingRangeParams) -> Response[Union[List['lsp_types.FoldingRange'], None]]:
        return await self.send_request("textDocument/foldingRange", params)

    async def declaration(self,  params: lsp_types.DeclarationParams) -> Response[Union['lsp_types.Declaration', List['lsp_types.LocationLink'], None]]:
        return await self.send_request("textDocument/declaration", params)

    async def selection_range(self,  params: lsp_types.SelectionRangeParams) -> Response[Union[List['lsp_types.SelectionRange'], None]]:
        return await self.send_request("textDocument/selectionRange", params)

    async def prepare_call_hierarchy(self,  params: lsp_types.CallHierarchyPrepareParams) -> Response[Union[List['lsp_types.CallHierarchyItem'], None]]:
        return await self.send_request("textDocument/prepareCallHierarchy", params)

    async def incoming_calls(self,  params: lsp_types.CallHierarchyIncomingCallsParams) -> Response[Union[List['lsp_types.CallHierarchyIncomingCall'], None]]:
        return await self.send_request("callHierarchy/incomingCalls", params)

    async def outgoing_calls(self,  params: lsp_types.CallHierarchyOutgoingCallsParams) -> Response[Union[List['lsp_types.CallHierarchyOutgoingCall'], None]]:
        return await self.send_request("callHierarchy/outgoingCalls", params)

    async def semantic_tokens_full(self,  params: lsp_types.SemanticTokensParams) -> Response[Union['lsp_types.SemanticTokens', None]]:
        return await self.send_request("textDocument/semanticTokens/full", params)

    async def semantic_tokens_delta(self,  params: lsp_types.SemanticTokensDeltaParams) -> Response[Union['lsp_types.SemanticTokens', 'lsp_types.SemanticTokensDelta', None]]:
        return await self.send_request("textDocument/semanticTokens/full/delta", params)

    async def semantic_tokens_range(self,  params: lsp_types.SemanticTokensRangeParams) -> Response[Union['lsp_types.SemanticTokens', None]]:
        return await self.send_request("textDocument/semanticTokens/range", params)

    async def linked_editing_range(self,  params: lsp_types.LinkedEditingRangeParams) -> Response[Union['lsp_types.LinkedEditingRanges', None]]:
        return await self.send_request("textDocument/linkedEditingRange", params)

    async def will_create_files(self,  params: lsp_types.CreateFilesParams) -> Response[Union['lsp_types.WorkspaceEdit', None]]:
        return await self.send_request("workspace/willCreateFiles", params)

    async def will_rename_files(self,  params: lsp_types.RenameFilesParams) -> Response[Union['lsp_types.WorkspaceEdit', None]]:
        return await self.send_request("workspace/willRenameFiles", params)

    async def will_delete_files(self,  params: lsp_types.DeleteFilesParams) -> Response[Union['lsp_types.WorkspaceEdit', None]]:
        return await self.send_request("workspace/willDeleteFiles", params)

    async def moniker(self,  params: lsp_types.MonikerParams) -> Response[Union[List['lsp_types.Moniker'], None]]:
        return await self.send_request("textDocument/moniker", params)

    async def prepare_type_hierarchy(self,  params: lsp_types.TypeHierarchyPrepareParams) -> Response[Union[List['lsp_types.TypeHierarchyItem'], None]]:
        return await self.send_request("textDocument/prepareTypeHierarchy", params)

    async def type_hierarchy_supertypes(self,  params: lsp_types.TypeHierarchySupertypesParams) -> Response[Union[List['lsp_types.TypeHierarchyItem'], None]]:
        return await self.send_request("typeHierarchy/supertypes", params)

    async def type_hierarchy_subtypes(self,  params: lsp_types.TypeHierarchySubtypesParams) -> Response[Union[List['lsp_types.TypeHierarchyItem'], None]]:
        return await self.send_request("typeHierarchy/subtypes", params)

    async def inline_value(self,  params: lsp_types.InlineValueParams) -> Response[Union[List['lsp_types.InlineValue'], None]]:
        return await self.send_request("textDocument/inlineValue", params)

    async def inlay_hint(self,  params: lsp_types.InlayHintParams) -> Response[Union[List['lsp_types.InlayHint'], None]]:
        return await self.send_request("textDocument/inlayHint", params)

    async def resolve_inlay_hint(self,  params: lsp_types.InlayHint) -> Response['lsp_types.InlayHint']:
        return await self.send_request("inlayHint/resolve", params)

    async def text_document_diagnostic(self,  params: lsp_types.DocumentDiagnosticParams) -> Response['lsp_types.DocumentDiagnosticReport']:
        return await self.send_request("textDocument/diagnostic", params)

    async def workspace_diagnostic(self,  params: lsp_types.WorkspaceDiagnosticParams) -> Response['lsp_types.WorkspaceDiagnosticReport']:
        return await self.send_request("workspace/diagnostic", params)

    async def initialize(self,  params: lsp_types.InitializeParams) -> Response['lsp_types.InitializeResult']:
        return await self.send_request("initialize", params)

    async def shutdown(self) -> Response[None]:
        return await self.send_request("shutdown")

    async def will_save_wait_until(self,  params: lsp_types.WillSaveTextDocumentParams) -> Response[Union[List['lsp_types.TextEdit'], None]]:
        return await self.send_request("textDocument/willSaveWaitUntil", params)

    async def completion(self,  params: lsp_types.CompletionParams) -> Response[Union[List['lsp_types.CompletionItem'], 'lsp_types.CompletionList', None]]:
        return await self.send_request("textDocument/completion", params)

    async def resolve_completion_item(self,  params: lsp_types.CompletionItem) -> Response['lsp_types.CompletionItem']:
        return await self.send_request("completionItem/resolve", params)

    async def hover(self,  params: lsp_types.HoverParams) -> Response[Union['lsp_types.Hover', None]]:
        return await self.send_request("textDocument/hover", params)

    async def signature_help(self,  params: lsp_types.SignatureHelpParams) -> Response[Union['lsp_types.SignatureHelp', None]]:
        return await self.send_request("textDocument/signatureHelp", params)

    async def definition(self,  params: lsp_types.DefinitionParams) -> Response[Union['lsp_types.Definition', List['lsp_types.LocationLink'], None]]:
        return await self.send_request("textDocument/definition", params)

    async def references(self,  params: lsp_types.ReferenceParams) -> Response[Union[List['lsp_types.Location'], None]]:
        return await self.send_request("textDocument/references", params)

    async def document_highlight(self,  params: lsp_types.DocumentHighlightParams) -> Response[Union[List['lsp_types.DocumentHighlight'], None]]:
        return await self.send_request("textDocument/documentHighlight", params)

    async def document_symbol(self,  params: lsp_types.DocumentSymbolParams) -> Response[Union[List['lsp_types.SymbolInformation'], List['lsp_types.DocumentSymbol'], None]]:
        return await self.send_request("textDocument/documentSymbol", params)

    async def code_action(self,  params: lsp_types.CodeActionParams) -> Response[Union[List[Union['lsp_types.Command', 'lsp_types.CodeAction']], None]]:
        return await self.send_request("textDocument/codeAction", params)

    async def resolve_code_action(self,  params: lsp_types.CodeAction) -> Response['lsp_types.CodeAction']:
        return await self.send_request("codeAction/resolve", params)

    async def workspace_symbol(self,  params: lsp_types.WorkspaceSymbolParams) -> Response[Union[List['lsp_types.SymbolInformation'], List['lsp_types.WorkspaceSymbol'], None]]:
        return await self.send_request("workspace/symbol", params)

    async def resolve_workspace_symbol(self,  params: lsp_types.WorkspaceSymbol) -> Response['lsp_types.WorkspaceSymbol']:
        return await self.send_request("workspaceSymbol/resolve", params)

    async def code_lens(self,  params: lsp_types.CodeLensParams) -> Response[Union[List['lsp_types.CodeLens'], None]]:
        return await self.send_request("textDocument/codeLens", params)

    async def resolve_code_lens(self,  params: lsp_types.CodeLens) -> Response['lsp_types.CodeLens']:
        return await self.send_request("codeLens/resolve", params)

    async def document_link(self,  params: lsp_types.DocumentLinkParams) -> Response[Union[List['lsp_types.DocumentLink'], None]]:
        return await self.send_request("textDocument/documentLink", params)

    async def resolve_document_link(self,  params: lsp_types.DocumentLink) -> Response['lsp_types.DocumentLink']:
        return await self.send_request("documentLink/resolve", params)

    async def formatting(self,  params: lsp_types.DocumentFormattingParams) -> Response[Union[List['lsp_types.TextEdit'], None]]:
        return await self.send_request("textDocument/formatting", params)

    async def range_formatting(self,  params: lsp_types.DocumentRangeFormattingParams) -> Response[Union[List['lsp_types.TextEdit'], None]]:
        return await self.send_request("textDocument/rangeFormatting", params)

    async def on_type_formatting(self,  params: lsp_types.DocumentOnTypeFormattingParams) -> Response[Union[List['lsp_types.TextEdit'], None]]:
        return await self.send_request("textDocument/onTypeFormatting", params)

    async def rename(self,  params: lsp_types.RenameParams) -> Response[Union['lsp_types.WorkspaceEdit', None]]:
        return await self.send_request("textDocument/rename", params)

    async def prepare_rename(self,  params: lsp_types.PrepareRenameParams) -> Response[Union['lsp_types.PrepareRenameResult', None]]:
        return await self.send_request("textDocument/prepareRename", params)

    async def execute_command(self,  params: lsp_types.ExecuteCommandParams) -> Response[Union['lsp_types.LSPAny', None]]:
        return await self.send_request("workspace/executeCommand", params)


class LspNotification:
    def __init__(self, send_notification):
        self.send_notification = send_notification

    def did_change_workspace_folders(self,  params: lsp_types.DidChangeWorkspaceFoldersParams) -> None:
        return self.send_notification("workspace/didChangeWorkspaceFolders", params)

    def cancel_work_done_progress(self,  params: lsp_types.WorkDoneProgressCancelParams) -> None:
        return self.send_notification("window/workDoneProgress/cancel", params)

    def did_create_files(self,  params: lsp_types.CreateFilesParams) -> None:
        return self.send_notification("workspace/didCreateFiles", params)

    def did_rename_files(self,  params: lsp_types.RenameFilesParams) -> None:
        return self.send_notification("workspace/didRenameFiles", params)

    def did_delete_files(self,  params: lsp_types.DeleteFilesParams) -> None:
        return self.send_notification("workspace/didDeleteFiles", params)

    def did_open_notebook_document(self,  params: lsp_types.DidOpenNotebookDocumentParams) -> None:
        return self.send_notification("notebookDocument/didOpen", params)

    def did_change_notebook_document(self,  params: lsp_types.DidChangeNotebookDocumentParams) -> None:
        return self.send_notification("notebookDocument/didChange", params)

    def did_save_notebook_document(self,  params: lsp_types.DidSaveNotebookDocumentParams) -> None:
        return self.send_notification("notebookDocument/didSave", params)

    def did_close_notebook_document(self,  params: lsp_types.DidCloseNotebookDocumentParams) -> None:
        return self.send_notification("notebookDocument/didClose", params)

    def initialized(self,  params: lsp_types.InitializedParams) -> None:
        return self.send_notification("initialized", params)

    def exit(self) -> None:
        return self.send_notification("exit")

    def workspace_did_change_configuration(self,  params: lsp_types.DidChangeConfigurationParams) -> None:
        return self.send_notification("workspace/didChangeConfiguration", params)

    def did_open_text_document(self,  params: lsp_types.DidOpenTextDocumentParams) -> None:
        return self.send_notification("textDocument/didOpen", params)

    def did_change_text_document(self,  params: lsp_types.DidChangeTextDocumentParams) -> None:
        return self.send_notification("textDocument/didChange", params)

    def did_close_text_document(self,  params: lsp_types.DidCloseTextDocumentParams) -> None:
        return self.send_notification("textDocument/didClose", params)

    def did_save_text_document(self,  params: lsp_types.DidSaveTextDocumentParams) -> None:
        return self.send_notification("textDocument/didSave", params)

    def will_save_text_document(self,  params: lsp_types.WillSaveTextDocumentParams) -> None:
        return self.send_notification("textDocument/willSave", params)

    def did_change_watched_files(self,  params: lsp_types.DidChangeWatchedFilesParams) -> None:
        return self.send_notification("workspace/didChangeWatchedFiles", params)

    def set_trace(self,  params: lsp_types.SetTraceParams) -> None:
        return self.send_notification("$/setTrace", params)

    def cancel_request(self,  params: lsp_types.CancelParams) -> None:
        return self.send_notification("$/cancelRequest", params)

    def progress(self,  params: lsp_types.ProgressParams) -> None:
        return self.send_notification("$/progress", params)
