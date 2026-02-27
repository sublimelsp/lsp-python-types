from __future__ import annotations

from .lsp_types import *
from typing import Literal
from typing import TypedDict
from typing import Union
from typing_extensions import TypeAlias


class ImplementationRequest(TypedDict):
    method: Literal['textDocument/implementation']
    params: 'ImplementationParams'


class TypeDefinitionRequest(TypedDict):
    method: Literal['textDocument/typeDefinition']
    params: 'TypeDefinitionParams'


class WorkspaceFoldersRequest(TypedDict):
    method: Literal['workspace/workspaceFolders']
    params: None


class ConfigurationRequest(TypedDict):
    method: Literal['workspace/configuration']
    params: 'ConfigurationParams'


class DocumentColorRequest(TypedDict):
    method: Literal['textDocument/documentColor']
    params: 'DocumentColorParams'


class ColorPresentationRequest(TypedDict):
    method: Literal['textDocument/colorPresentation']
    params: 'ColorPresentationParams'


class FoldingRangeRequest(TypedDict):
    method: Literal['textDocument/foldingRange']
    params: 'FoldingRangeParams'


class FoldingRangeRefreshRequest(TypedDict):
    method: Literal['workspace/foldingRange/refresh']
    params: None


class DeclarationRequest(TypedDict):
    method: Literal['textDocument/declaration']
    params: 'DeclarationParams'


class SelectionRangeRequest(TypedDict):
    method: Literal['textDocument/selectionRange']
    params: 'SelectionRangeParams'


class WorkDoneProgressCreateRequest(TypedDict):
    method: Literal['window/workDoneProgress/create']
    params: 'WorkDoneProgressCreateParams'


class CallHierarchyPrepareRequest(TypedDict):
    method: Literal['textDocument/prepareCallHierarchy']
    params: 'CallHierarchyPrepareParams'


class CallHierarchyIncomingCallsRequest(TypedDict):
    method: Literal['callHierarchy/incomingCalls']
    params: 'CallHierarchyIncomingCallsParams'


class CallHierarchyOutgoingCallsRequest(TypedDict):
    method: Literal['callHierarchy/outgoingCalls']
    params: 'CallHierarchyOutgoingCallsParams'


class SemanticTokensRequest(TypedDict):
    method: Literal['textDocument/semanticTokens/full']
    params: 'SemanticTokensParams'


class SemanticTokensDeltaRequest(TypedDict):
    method: Literal['textDocument/semanticTokens/full/delta']
    params: 'SemanticTokensDeltaParams'


class SemanticTokensRangeRequest(TypedDict):
    method: Literal['textDocument/semanticTokens/range']
    params: 'SemanticTokensRangeParams'


class SemanticTokensRefreshRequest(TypedDict):
    method: Literal['workspace/semanticTokens/refresh']
    params: None


class ShowDocumentRequest(TypedDict):
    method: Literal['window/showDocument']
    params: 'ShowDocumentParams'


class LinkedEditingRangeRequest(TypedDict):
    method: Literal['textDocument/linkedEditingRange']
    params: 'LinkedEditingRangeParams'


class WillCreateFilesRequest(TypedDict):
    method: Literal['workspace/willCreateFiles']
    params: 'CreateFilesParams'


class WillRenameFilesRequest(TypedDict):
    method: Literal['workspace/willRenameFiles']
    params: 'RenameFilesParams'


class WillDeleteFilesRequest(TypedDict):
    method: Literal['workspace/willDeleteFiles']
    params: 'DeleteFilesParams'


class MonikerRequest(TypedDict):
    method: Literal['textDocument/moniker']
    params: 'MonikerParams'


class TypeHierarchyPrepareRequest(TypedDict):
    method: Literal['textDocument/prepareTypeHierarchy']
    params: 'TypeHierarchyPrepareParams'


class TypeHierarchySupertypesRequest(TypedDict):
    method: Literal['typeHierarchy/supertypes']
    params: 'TypeHierarchySupertypesParams'


class TypeHierarchySubtypesRequest(TypedDict):
    method: Literal['typeHierarchy/subtypes']
    params: 'TypeHierarchySubtypesParams'


class InlineValueRequest(TypedDict):
    method: Literal['textDocument/inlineValue']
    params: 'InlineValueParams'


class InlineValueRefreshRequest(TypedDict):
    method: Literal['workspace/inlineValue/refresh']
    params: None


class InlayHintRequest(TypedDict):
    method: Literal['textDocument/inlayHint']
    params: 'InlayHintParams'


class InlayHintResolveRequest(TypedDict):
    method: Literal['inlayHint/resolve']
    params: 'InlayHint'


class InlayHintRefreshRequest(TypedDict):
    method: Literal['workspace/inlayHint/refresh']
    params: None


class DocumentDiagnosticRequest(TypedDict):
    method: Literal['textDocument/diagnostic']
    params: 'DocumentDiagnosticParams'


class WorkspaceDiagnosticRequest(TypedDict):
    method: Literal['workspace/diagnostic']
    params: 'WorkspaceDiagnosticParams'


class DiagnosticRefreshRequest(TypedDict):
    method: Literal['workspace/diagnostic/refresh']
    params: None


class InlineCompletionRequest(TypedDict):
    method: Literal['textDocument/inlineCompletion']
    params: 'InlineCompletionParams'


class TextDocumentContentRequest(TypedDict):
    method: Literal['workspace/textDocumentContent']
    params: 'TextDocumentContentParams'


class TextDocumentContentRefreshRequest(TypedDict):
    method: Literal['workspace/textDocumentContent/refresh']
    params: 'TextDocumentContentRefreshParams'


class RegistrationRequest(TypedDict):
    method: Literal['client/registerCapability']
    params: 'RegistrationParams'


class UnregistrationRequest(TypedDict):
    method: Literal['client/unregisterCapability']
    params: 'UnregistrationParams'


class InitializeRequest(TypedDict):
    method: Literal['initialize']
    params: 'InitializeParams'


class ShutdownRequest(TypedDict):
    method: Literal['shutdown']
    params: None


class ShowMessageRequest(TypedDict):
    method: Literal['window/showMessageRequest']
    params: 'ShowMessageRequestParams'


class WillSaveTextDocumentWaitUntilRequest(TypedDict):
    method: Literal['textDocument/willSaveWaitUntil']
    params: 'WillSaveTextDocumentParams'


class CompletionRequest(TypedDict):
    method: Literal['textDocument/completion']
    params: 'CompletionParams'


class CompletionResolveRequest(TypedDict):
    method: Literal['completionItem/resolve']
    params: 'CompletionItem'


class HoverRequest(TypedDict):
    method: Literal['textDocument/hover']
    params: 'HoverParams'


class SignatureHelpRequest(TypedDict):
    method: Literal['textDocument/signatureHelp']
    params: 'SignatureHelpParams'


class DefinitionRequest(TypedDict):
    method: Literal['textDocument/definition']
    params: 'DefinitionParams'


class ReferencesRequest(TypedDict):
    method: Literal['textDocument/references']
    params: 'ReferenceParams'


class DocumentHighlightRequest(TypedDict):
    method: Literal['textDocument/documentHighlight']
    params: 'DocumentHighlightParams'


class DocumentSymbolRequest(TypedDict):
    method: Literal['textDocument/documentSymbol']
    params: 'DocumentSymbolParams'


class CodeActionRequest(TypedDict):
    method: Literal['textDocument/codeAction']
    params: 'CodeActionParams'


class CodeActionResolveRequest(TypedDict):
    method: Literal['codeAction/resolve']
    params: 'CodeAction'


class WorkspaceSymbolRequest(TypedDict):
    method: Literal['workspace/symbol']
    params: 'WorkspaceSymbolParams'


class WorkspaceSymbolResolveRequest(TypedDict):
    method: Literal['workspaceSymbol/resolve']
    params: 'WorkspaceSymbol'


class CodeLensRequest(TypedDict):
    method: Literal['textDocument/codeLens']
    params: 'CodeLensParams'


class CodeLensResolveRequest(TypedDict):
    method: Literal['codeLens/resolve']
    params: 'CodeLens'


class CodeLensRefreshRequest(TypedDict):
    method: Literal['workspace/codeLens/refresh']
    params: None


class DocumentLinkRequest(TypedDict):
    method: Literal['textDocument/documentLink']
    params: 'DocumentLinkParams'


class DocumentLinkResolveRequest(TypedDict):
    method: Literal['documentLink/resolve']
    params: 'DocumentLink'


class DocumentFormattingRequest(TypedDict):
    method: Literal['textDocument/formatting']
    params: 'DocumentFormattingParams'


class DocumentRangeFormattingRequest(TypedDict):
    method: Literal['textDocument/rangeFormatting']
    params: 'DocumentRangeFormattingParams'


class DocumentRangesFormattingRequest(TypedDict):
    method: Literal['textDocument/rangesFormatting']
    params: 'DocumentRangesFormattingParams'


class DocumentOnTypeFormattingRequest(TypedDict):
    method: Literal['textDocument/onTypeFormatting']
    params: 'DocumentOnTypeFormattingParams'


class RenameRequest(TypedDict):
    method: Literal['textDocument/rename']
    params: 'RenameParams'


class PrepareRenameRequest(TypedDict):
    method: Literal['textDocument/prepareRename']
    params: 'PrepareRenameParams'


class ExecuteCommandRequest(TypedDict):
    method: Literal['workspace/executeCommand']
    params: 'ExecuteCommandParams'


class ApplyWorkspaceEditRequest(TypedDict):
    method: Literal['workspace/applyEdit']
    params: 'ApplyWorkspaceEditParams'


ClientRequest: TypeAlias = Union[
    ImplementationRequest,
    TypeDefinitionRequest,
    DocumentColorRequest,
    ColorPresentationRequest,
    FoldingRangeRequest,
    DeclarationRequest,
    SelectionRangeRequest,
    CallHierarchyPrepareRequest,
    CallHierarchyIncomingCallsRequest,
    CallHierarchyOutgoingCallsRequest,
    SemanticTokensRequest,
    SemanticTokensDeltaRequest,
    SemanticTokensRangeRequest,
    LinkedEditingRangeRequest,
    WillCreateFilesRequest,
    WillRenameFilesRequest,
    WillDeleteFilesRequest,
    MonikerRequest,
    TypeHierarchyPrepareRequest,
    TypeHierarchySupertypesRequest,
    TypeHierarchySubtypesRequest,
    InlineValueRequest,
    InlayHintRequest,
    InlayHintResolveRequest,
    DocumentDiagnosticRequest,
    WorkspaceDiagnosticRequest,
    InlineCompletionRequest,
    TextDocumentContentRequest,
    InitializeRequest,
    ShutdownRequest,
    WillSaveTextDocumentWaitUntilRequest,
    CompletionRequest,
    CompletionResolveRequest,
    HoverRequest,
    SignatureHelpRequest,
    DefinitionRequest,
    ReferencesRequest,
    DocumentHighlightRequest,
    DocumentSymbolRequest,
    CodeActionRequest,
    CodeActionResolveRequest,
    WorkspaceSymbolRequest,
    WorkspaceSymbolResolveRequest,
    CodeLensRequest,
    CodeLensResolveRequest,
    DocumentLinkRequest,
    DocumentLinkResolveRequest,
    DocumentFormattingRequest,
    DocumentRangeFormattingRequest,
    DocumentRangesFormattingRequest,
    DocumentOnTypeFormattingRequest,
    RenameRequest,
    PrepareRenameRequest,
    ExecuteCommandRequest,
]


ServerRequest: TypeAlias = Union[
    WorkspaceFoldersRequest,
    ConfigurationRequest,
    FoldingRangeRefreshRequest,
    WorkDoneProgressCreateRequest,
    SemanticTokensRefreshRequest,
    ShowDocumentRequest,
    InlineValueRefreshRequest,
    InlayHintRefreshRequest,
    DiagnosticRefreshRequest,
    TextDocumentContentRefreshRequest,
    RegistrationRequest,
    UnregistrationRequest,
    ShowMessageRequest,
    CodeLensRefreshRequest,
    ApplyWorkspaceEditRequest,
]


class ImplementationResponse(TypedDict):
    method: Literal['textDocument/implementation']
    result: 'Definition' | list['DefinitionLink'] | None


class TypeDefinitionResponse(TypedDict):
    method: Literal['textDocument/typeDefinition']
    result: 'Definition' | list['DefinitionLink'] | None


class WorkspaceFoldersResponse(TypedDict):
    method: Literal['workspace/workspaceFolders']
    result: list['WorkspaceFolder'] | None


class ConfigurationResponse(TypedDict):
    method: Literal['workspace/configuration']
    result: list['LSPAny']


class DocumentColorResponse(TypedDict):
    method: Literal['textDocument/documentColor']
    result: list['ColorInformation']


class ColorPresentationResponse(TypedDict):
    method: Literal['textDocument/colorPresentation']
    result: list['ColorPresentation']


class FoldingRangeResponse(TypedDict):
    method: Literal['textDocument/foldingRange']
    result: list['FoldingRange'] | None


class FoldingRangeRefreshResponse(TypedDict):
    method: Literal['workspace/foldingRange/refresh']
    result: None


class DeclarationResponse(TypedDict):
    method: Literal['textDocument/declaration']
    result: 'Declaration' | list['DeclarationLink'] | None


class SelectionRangeResponse(TypedDict):
    method: Literal['textDocument/selectionRange']
    result: list['SelectionRange'] | None


class WorkDoneProgressCreateResponse(TypedDict):
    method: Literal['window/workDoneProgress/create']
    result: None


class CallHierarchyPrepareResponse(TypedDict):
    method: Literal['textDocument/prepareCallHierarchy']
    result: list['CallHierarchyItem'] | None


class CallHierarchyIncomingCallsResponse(TypedDict):
    method: Literal['callHierarchy/incomingCalls']
    result: list['CallHierarchyIncomingCall'] | None


class CallHierarchyOutgoingCallsResponse(TypedDict):
    method: Literal['callHierarchy/outgoingCalls']
    result: list['CallHierarchyOutgoingCall'] | None


class SemanticTokensResponse(TypedDict):
    method: Literal['textDocument/semanticTokens/full']
    result: 'SemanticTokens' | None


class SemanticTokensDeltaResponse(TypedDict):
    method: Literal['textDocument/semanticTokens/full/delta']
    result: 'SemanticTokens' | 'SemanticTokensDelta' | None


class SemanticTokensRangeResponse(TypedDict):
    method: Literal['textDocument/semanticTokens/range']
    result: 'SemanticTokens' | None


class SemanticTokensRefreshResponse(TypedDict):
    method: Literal['workspace/semanticTokens/refresh']
    result: None


class ShowDocumentResponse(TypedDict):
    method: Literal['window/showDocument']
    result: 'ShowDocumentResult'


class LinkedEditingRangeResponse(TypedDict):
    method: Literal['textDocument/linkedEditingRange']
    result: 'LinkedEditingRanges' | None


class WillCreateFilesResponse(TypedDict):
    method: Literal['workspace/willCreateFiles']
    result: 'WorkspaceEdit' | None


class WillRenameFilesResponse(TypedDict):
    method: Literal['workspace/willRenameFiles']
    result: 'WorkspaceEdit' | None


class WillDeleteFilesResponse(TypedDict):
    method: Literal['workspace/willDeleteFiles']
    result: 'WorkspaceEdit' | None


class MonikerResponse(TypedDict):
    method: Literal['textDocument/moniker']
    result: list['Moniker'] | None


class TypeHierarchyPrepareResponse(TypedDict):
    method: Literal['textDocument/prepareTypeHierarchy']
    result: list['TypeHierarchyItem'] | None


class TypeHierarchySupertypesResponse(TypedDict):
    method: Literal['typeHierarchy/supertypes']
    result: list['TypeHierarchyItem'] | None


class TypeHierarchySubtypesResponse(TypedDict):
    method: Literal['typeHierarchy/subtypes']
    result: list['TypeHierarchyItem'] | None


class InlineValueResponse(TypedDict):
    method: Literal['textDocument/inlineValue']
    result: list['InlineValue'] | None


class InlineValueRefreshResponse(TypedDict):
    method: Literal['workspace/inlineValue/refresh']
    result: None


class InlayHintResponse(TypedDict):
    method: Literal['textDocument/inlayHint']
    result: list['InlayHint'] | None


class InlayHintResolveResponse(TypedDict):
    method: Literal['inlayHint/resolve']
    result: 'InlayHint'


class InlayHintRefreshResponse(TypedDict):
    method: Literal['workspace/inlayHint/refresh']
    result: None


class DocumentDiagnosticResponse(TypedDict):
    method: Literal['textDocument/diagnostic']
    result: 'DocumentDiagnosticReport'


class WorkspaceDiagnosticResponse(TypedDict):
    method: Literal['workspace/diagnostic']
    result: 'WorkspaceDiagnosticReport'


class DiagnosticRefreshResponse(TypedDict):
    method: Literal['workspace/diagnostic/refresh']
    result: None


class InlineCompletionResponse(TypedDict):
    method: Literal['textDocument/inlineCompletion']
    result: 'InlineCompletionList' | list['InlineCompletionItem'] | None


class TextDocumentContentResponse(TypedDict):
    method: Literal['workspace/textDocumentContent']
    result: 'TextDocumentContentResult'


class TextDocumentContentRefreshResponse(TypedDict):
    method: Literal['workspace/textDocumentContent/refresh']
    result: None


class RegistrationResponse(TypedDict):
    method: Literal['client/registerCapability']
    result: None


class UnregistrationResponse(TypedDict):
    method: Literal['client/unregisterCapability']
    result: None


class InitializeResponse(TypedDict):
    method: Literal['initialize']
    result: 'InitializeResult'


class ShutdownResponse(TypedDict):
    method: Literal['shutdown']
    result: None


class ShowMessageResponse(TypedDict):
    method: Literal['window/showMessageRequest']
    result: 'MessageActionItem' | None


class WillSaveTextDocumentWaitUntilResponse(TypedDict):
    method: Literal['textDocument/willSaveWaitUntil']
    result: list['TextEdit'] | None


class CompletionResponse(TypedDict):
    method: Literal['textDocument/completion']
    result: list['CompletionItem'] | 'CompletionList' | None


class CompletionResolveResponse(TypedDict):
    method: Literal['completionItem/resolve']
    result: 'CompletionItem'


class HoverResponse(TypedDict):
    method: Literal['textDocument/hover']
    result: 'Hover' | None


class SignatureHelpResponse(TypedDict):
    method: Literal['textDocument/signatureHelp']
    result: 'SignatureHelp' | None


class DefinitionResponse(TypedDict):
    method: Literal['textDocument/definition']
    result: 'Definition' | list['DefinitionLink'] | None


class ReferencesResponse(TypedDict):
    method: Literal['textDocument/references']
    result: list['Location'] | None


class DocumentHighlightResponse(TypedDict):
    method: Literal['textDocument/documentHighlight']
    result: list['DocumentHighlight'] | None


class DocumentSymbolResponse(TypedDict):
    method: Literal['textDocument/documentSymbol']
    result: list['SymbolInformation'] | list['DocumentSymbol'] | None


class CodeActionResponse(TypedDict):
    method: Literal['textDocument/codeAction']
    result: list['Command' | 'CodeAction'] | None


class CodeActionResolveResponse(TypedDict):
    method: Literal['codeAction/resolve']
    result: 'CodeAction'


class WorkspaceSymbolResponse(TypedDict):
    method: Literal['workspace/symbol']
    result: list['SymbolInformation'] | list['WorkspaceSymbol'] | None


class WorkspaceSymbolResolveResponse(TypedDict):
    method: Literal['workspaceSymbol/resolve']
    result: 'WorkspaceSymbol'


class CodeLensResponse(TypedDict):
    method: Literal['textDocument/codeLens']
    result: list['CodeLens'] | None


class CodeLensResolveResponse(TypedDict):
    method: Literal['codeLens/resolve']
    result: 'CodeLens'


class CodeLensRefreshResponse(TypedDict):
    method: Literal['workspace/codeLens/refresh']
    result: None


class DocumentLinkResponse(TypedDict):
    method: Literal['textDocument/documentLink']
    result: list['DocumentLink'] | None


class DocumentLinkResolveResponse(TypedDict):
    method: Literal['documentLink/resolve']
    result: 'DocumentLink'


class DocumentFormattingResponse(TypedDict):
    method: Literal['textDocument/formatting']
    result: list['TextEdit'] | None


class DocumentRangeFormattingResponse(TypedDict):
    method: Literal['textDocument/rangeFormatting']
    result: list['TextEdit'] | None


class DocumentRangesFormattingResponse(TypedDict):
    method: Literal['textDocument/rangesFormatting']
    result: list['TextEdit'] | None


class DocumentOnTypeFormattingResponse(TypedDict):
    method: Literal['textDocument/onTypeFormatting']
    result: list['TextEdit'] | None


class RenameResponse(TypedDict):
    method: Literal['textDocument/rename']
    result: 'WorkspaceEdit' | None


class PrepareRenameResponse(TypedDict):
    method: Literal['textDocument/prepareRename']
    result: 'PrepareRenameResult' | None


class ExecuteCommandResponse(TypedDict):
    method: Literal['workspace/executeCommand']
    result: 'LSPAny' | None


class ApplyWorkspaceEditResponse(TypedDict):
    method: Literal['workspace/applyEdit']
    result: 'ApplyWorkspaceEditResult'


ServerResponse: TypeAlias = Union[
    ImplementationResponse,
    TypeDefinitionResponse,
    DocumentColorResponse,
    ColorPresentationResponse,
    FoldingRangeResponse,
    DeclarationResponse,
    SelectionRangeResponse,
    CallHierarchyPrepareResponse,
    CallHierarchyIncomingCallsResponse,
    CallHierarchyOutgoingCallsResponse,
    SemanticTokensResponse,
    SemanticTokensDeltaResponse,
    SemanticTokensRangeResponse,
    LinkedEditingRangeResponse,
    WillCreateFilesResponse,
    WillRenameFilesResponse,
    WillDeleteFilesResponse,
    MonikerResponse,
    TypeHierarchyPrepareResponse,
    TypeHierarchySupertypesResponse,
    TypeHierarchySubtypesResponse,
    InlineValueResponse,
    InlayHintResponse,
    InlayHintResolveResponse,
    DocumentDiagnosticResponse,
    WorkspaceDiagnosticResponse,
    InlineCompletionResponse,
    TextDocumentContentResponse,
    InitializeResponse,
    ShutdownResponse,
    WillSaveTextDocumentWaitUntilResponse,
    CompletionResponse,
    CompletionResolveResponse,
    HoverResponse,
    SignatureHelpResponse,
    DefinitionResponse,
    ReferencesResponse,
    DocumentHighlightResponse,
    DocumentSymbolResponse,
    CodeActionResponse,
    CodeActionResolveResponse,
    WorkspaceSymbolResponse,
    WorkspaceSymbolResolveResponse,
    CodeLensResponse,
    CodeLensResolveResponse,
    DocumentLinkResponse,
    DocumentLinkResolveResponse,
    DocumentFormattingResponse,
    DocumentRangeFormattingResponse,
    DocumentRangesFormattingResponse,
    DocumentOnTypeFormattingResponse,
    RenameResponse,
    PrepareRenameResponse,
    ExecuteCommandResponse,
]


ClientResponse: TypeAlias = Union[
    WorkspaceFoldersResponse,
    ConfigurationResponse,
    FoldingRangeRefreshResponse,
    WorkDoneProgressCreateResponse,
    SemanticTokensRefreshResponse,
    ShowDocumentResponse,
    InlineValueRefreshResponse,
    InlayHintRefreshResponse,
    DiagnosticRefreshResponse,
    TextDocumentContentRefreshResponse,
    RegistrationResponse,
    UnregistrationResponse,
    ShowMessageResponse,
    CodeLensRefreshResponse,
    ApplyWorkspaceEditResponse,
]


class DidChangeWorkspaceFoldersNotification(TypedDict):
    method: Literal['workspace/didChangeWorkspaceFolders']
    params: 'DidChangeWorkspaceFoldersParams'


class WorkDoneProgressCancelNotification(TypedDict):
    method: Literal['window/workDoneProgress/cancel']
    params: 'WorkDoneProgressCancelParams'


class DidCreateFilesNotification(TypedDict):
    method: Literal['workspace/didCreateFiles']
    params: 'CreateFilesParams'


class DidRenameFilesNotification(TypedDict):
    method: Literal['workspace/didRenameFiles']
    params: 'RenameFilesParams'


class DidDeleteFilesNotification(TypedDict):
    method: Literal['workspace/didDeleteFiles']
    params: 'DeleteFilesParams'


class DidOpenNotebookDocumentNotification(TypedDict):
    method: Literal['notebookDocument/didOpen']
    params: 'DidOpenNotebookDocumentParams'


class DidChangeNotebookDocumentNotification(TypedDict):
    method: Literal['notebookDocument/didChange']
    params: 'DidChangeNotebookDocumentParams'


class DidSaveNotebookDocumentNotification(TypedDict):
    method: Literal['notebookDocument/didSave']
    params: 'DidSaveNotebookDocumentParams'


class DidCloseNotebookDocumentNotification(TypedDict):
    method: Literal['notebookDocument/didClose']
    params: 'DidCloseNotebookDocumentParams'


class InitializedNotification(TypedDict):
    method: Literal['initialized']
    params: 'InitializedParams'


class ExitNotification(TypedDict):
    method: Literal['exit']
    params: None


class DidChangeConfigurationNotification(TypedDict):
    method: Literal['workspace/didChangeConfiguration']
    params: 'DidChangeConfigurationParams'


class ShowMessageNotification(TypedDict):
    method: Literal['window/showMessage']
    params: 'ShowMessageParams'


class LogMessageNotification(TypedDict):
    method: Literal['window/logMessage']
    params: 'LogMessageParams'


class TelemetryEventNotification(TypedDict):
    method: Literal['telemetry/event']
    params: 'LSPAny'


class DidOpenTextDocumentNotification(TypedDict):
    method: Literal['textDocument/didOpen']
    params: 'DidOpenTextDocumentParams'


class DidChangeTextDocumentNotification(TypedDict):
    method: Literal['textDocument/didChange']
    params: 'DidChangeTextDocumentParams'


class DidCloseTextDocumentNotification(TypedDict):
    method: Literal['textDocument/didClose']
    params: 'DidCloseTextDocumentParams'


class DidSaveTextDocumentNotification(TypedDict):
    method: Literal['textDocument/didSave']
    params: 'DidSaveTextDocumentParams'


class WillSaveTextDocumentNotification(TypedDict):
    method: Literal['textDocument/willSave']
    params: 'WillSaveTextDocumentParams'


class DidChangeWatchedFilesNotification(TypedDict):
    method: Literal['workspace/didChangeWatchedFiles']
    params: 'DidChangeWatchedFilesParams'


class PublishDiagnosticsNotification(TypedDict):
    method: Literal['textDocument/publishDiagnostics']
    params: 'PublishDiagnosticsParams'


class SetTraceNotification(TypedDict):
    method: Literal['$/setTrace']
    params: 'SetTraceParams'


class LogTraceNotification(TypedDict):
    method: Literal['$/logTrace']
    params: 'LogTraceParams'


class CancelNotification(TypedDict):
    method: Literal['$/cancelRequest']
    params: 'CancelParams'


class ProgressNotification(TypedDict):
    method: Literal['$/progress']
    params: 'ProgressParams'


ClientNotification: TypeAlias = Union[
    DidChangeWorkspaceFoldersNotification,
    WorkDoneProgressCancelNotification,
    DidCreateFilesNotification,
    DidRenameFilesNotification,
    DidDeleteFilesNotification,
    DidOpenNotebookDocumentNotification,
    DidChangeNotebookDocumentNotification,
    DidSaveNotebookDocumentNotification,
    DidCloseNotebookDocumentNotification,
    InitializedNotification,
    ExitNotification,
    DidChangeConfigurationNotification,
    DidOpenTextDocumentNotification,
    DidChangeTextDocumentNotification,
    DidCloseTextDocumentNotification,
    DidSaveTextDocumentNotification,
    WillSaveTextDocumentNotification,
    DidChangeWatchedFilesNotification,
    SetTraceNotification,
    CancelNotification,
    ProgressNotification,
]


ServerNotification: TypeAlias = Union[
    ShowMessageNotification,
    LogMessageNotification,
    TelemetryEventNotification,
    PublishDiagnosticsNotification,
    LogTraceNotification,
    CancelNotification,
    ProgressNotification,
]
