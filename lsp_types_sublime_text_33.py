# Code generated. DO NOT EDIT.
# LSP v3.17.0

from typing_extensions import NotRequired
from typing import Dict, List, Literal, TypedDict, Union
from enum import IntEnum, IntFlag, StrEnum


URI = str
DocumentUri = str
Uint = int
RegExp = str


class SemanticTokenTypes(StrEnum):
    """ A set of predefined token types. This set is not fixed
    an clients can specify additional token types via the
    corresponding client capabilities.

    @since 3.16.0 """
    Namespace = 'namespace'
    Type = 'type'
    """ Represents a generic type. Acts as a fallback for types which can't be mapped to
    a specific type like class or enum. """
    Class = 'class'
    Enum = 'enum'
    Interface = 'interface'
    Struct = 'struct'
    TypeParameter = 'typeParameter'
    Parameter = 'parameter'
    Variable = 'variable'
    Property = 'property'
    EnumMember = 'enumMember'
    Event = 'event'
    Function = 'function'
    Method = 'method'
    Macro = 'macro'
    Keyword = 'keyword'
    Modifier = 'modifier'
    Comment = 'comment'
    String = 'string'
    Number = 'number'
    Regexp = 'regexp'
    Operator = 'operator'
    Decorator = 'decorator'
    """ @since 3.17.0 """
    Label = 'label'
    """ @since 3.18.0 """


class SemanticTokenModifiers(StrEnum):
    """ A set of predefined token modifiers. This set is not fixed
    an clients can specify additional token types via the
    corresponding client capabilities.

    @since 3.16.0 """
    Declaration = 'declaration'
    Definition = 'definition'
    Readonly = 'readonly'
    Static = 'static'
    Deprecated = 'deprecated'
    Abstract = 'abstract'
    Async = 'async'
    Modification = 'modification'
    Documentation = 'documentation'
    DefaultLibrary = 'defaultLibrary'


class DocumentDiagnosticReportKind(StrEnum):
    """ The document diagnostic report kinds.

    @since 3.17.0 """
    Full = 'full'
    """ A diagnostic report with a full
    set of problems. """
    Unchanged = 'unchanged'
    """ A report indicating that the last
    returned report is still accurate. """


class ErrorCodes(IntEnum):
    """ Predefined error codes. """
    ParseError = -32700
    InvalidRequest = -32600
    MethodNotFound = -32601
    InvalidParams = -32602
    InternalError = -32603
    ServerNotInitialized = -32002
    """ Error code indicating that a server received a notification or
    request before the server has received the `initialize` request. """
    UnknownErrorCode = -32001


class LSPErrorCodes(IntEnum):
    RequestFailed = -32803
    """ A request failed but it was syntactically correct, e.g the
    method name was known and the parameters were valid. The error
    message should contain human readable information about why
    the request failed.

    @since 3.17.0 """
    ServerCancelled = -32802
    """ The server cancelled the request. This error code should
    only be used for requests that explicitly support being
    server cancellable.

    @since 3.17.0 """
    ContentModified = -32801
    """ The server detected that the content of a document got
    modified outside normal conditions. A server should
    NOT send this error code if it detects a content change
    in it unprocessed messages. The result even computed
    on an older state might still be useful for the client.

    If a client decides that a result is not of any use anymore
    the client should cancel the request. """
    RequestCancelled = -32800
    """ The client has canceled a request and a server has detected
    the cancel. """


class FoldingRangeKind(StrEnum):
    """ A set of predefined range kinds. """
    Comment = 'comment'
    """ Folding range for a comment """
    Imports = 'imports'
    """ Folding range for an import or include """
    Region = 'region'
    """ Folding range for a region (e.g. `#region`) """


class SymbolKind(IntEnum):
    """ A symbol kind. """
    File = 1
    Module = 2
    Namespace = 3
    Package = 4
    Class = 5
    Method = 6
    Property = 7
    Field = 8
    Constructor = 9
    Enum = 10
    Interface = 11
    Function = 12
    Variable = 13
    Constant = 14
    String = 15
    Number = 16
    Boolean = 17
    Array = 18
    Object = 19
    Key = 20
    Null = 21
    EnumMember = 22
    Struct = 23
    Event = 24
    Operator = 25
    TypeParameter = 26


class SymbolTag(IntEnum):
    """ Symbol tags are extra annotations that tweak the rendering of a symbol.

    @since 3.16 """
    Deprecated = 1
    """ Render a symbol as obsolete, usually using a strike-out. """


class UniquenessLevel(StrEnum):
    """ Moniker uniqueness level to define scope of the moniker.

    @since 3.16.0 """
    Document = 'document'
    """ The moniker is only unique inside a document """
    Project = 'project'
    """ The moniker is unique inside a project for which a dump got created """
    Group = 'group'
    """ The moniker is unique inside the group to which a project belongs """
    Scheme = 'scheme'
    """ The moniker is unique inside the moniker scheme. """
    Global = 'global'
    """ The moniker is globally unique """


class MonikerKind(StrEnum):
    """ The moniker kind.

    @since 3.16.0 """
    Import = 'import'
    """ The moniker represent a symbol that is imported into a project """
    Export = 'export'
    """ The moniker represents a symbol that is exported from a project """
    Local = 'local'
    """ The moniker represents a symbol that is local to a project (e.g. a local
    variable of a function, a class not visible outside the project, ...) """


class InlayHintKind(IntEnum):
    """ Inlay hint kinds.

    @since 3.17.0 """
    Type = 1
    """ An inlay hint that for a type annotation. """
    Parameter = 2
    """ An inlay hint that is for a parameter. """


class MessageType(IntEnum):
    """ The message type """
    Error = 1
    """ An error message. """
    Warning = 2
    """ A warning message. """
    Info = 3
    """ An information message. """
    Log = 4
    """ A log message. """
    Debug = 5
    """ A debug message.

    @since 3.18.0
    @proposed """


class TextDocumentSyncKind(IntEnum):
    """ Defines how the host (editor) should sync
    document changes to the language server. """
    None_ = 0
    """ Documents should not be synced at all. """
    Full = 1
    """ Documents are synced by always sending the full content
    of the document. """
    Incremental = 2
    """ Documents are synced by sending the full content on open.
    After that only incremental updates to the document are
    send. """


class TextDocumentSaveReason(IntEnum):
    """ Represents reasons why a text document is saved. """
    Manual = 1
    """ Manually triggered, e.g. by the user pressing save, by starting debugging,
    or by an API call. """
    AfterDelay = 2
    """ Automatic after a delay. """
    FocusOut = 3
    """ When the editor lost focus. """


class CompletionItemKind(IntEnum):
    """ The kind of a completion entry. """
    Text = 1
    Method = 2
    Function = 3
    Constructor = 4
    Field = 5
    Variable = 6
    Class = 7
    Interface = 8
    Module = 9
    Property = 10
    Unit = 11
    Value = 12
    Enum = 13
    Keyword = 14
    Snippet = 15
    Color = 16
    File = 17
    Reference = 18
    Folder = 19
    EnumMember = 20
    Constant = 21
    Struct = 22
    Event = 23
    Operator = 24
    TypeParameter = 25


class CompletionItemTag(IntEnum):
    """ Completion item tags are extra annotations that tweak the rendering of a completion
    item.

    @since 3.15.0 """
    Deprecated = 1
    """ Render a completion as obsolete, usually using a strike-out. """


class InsertTextFormat(IntEnum):
    """ Defines whether the insert text in a completion item should be interpreted as
    plain text or a snippet. """
    PlainText = 1
    """ The primary text to be inserted is treated as a plain string. """
    Snippet = 2
    """ The primary text to be inserted is treated as a snippet.

    A snippet can define tab stops and placeholders with `$1`, `$2`
    and `${3:foo}`. `$0` defines the final tab stop, it defaults to
    the end of the snippet. Placeholders with equal identifiers are linked,
    that is typing in one will update others too.

    See also: https://microsoft.github.io/language-server-protocol/specifications/specification-current/#snippet_syntax """


class InsertTextMode(IntEnum):
    """ How whitespace and indentation is handled during completion
    item insertion.

    @since 3.16.0 """
    AsIs = 1
    """ The insertion or replace strings is taken as it is. If the
    value is multi line the lines below the cursor will be
    inserted using the indentation defined in the string value.
    The client will not apply any kind of adjustments to the
    string. """
    AdjustIndentation = 2
    """ The editor adjusts leading whitespace of new lines so that
    they match the indentation up to the cursor of the line for
    which the item is accepted.

    Consider a line like this: <2tabs><cursor><3tabs>foo. Accepting a
    multi line completion item is indented using 2 tabs and all
    following lines inserted will be indented using 2 tabs as well. """


class DocumentHighlightKind(IntEnum):
    """ A document highlight kind. """
    Text = 1
    """ A textual occurrence. """
    Read = 2
    """ Read-access of a symbol, like reading a variable. """
    Write = 3
    """ Write-access of a symbol, like writing to a variable. """


class CodeActionKind(StrEnum):
    """ A set of predefined code action kinds """
    Empty = ''
    """ Empty kind. """
    QuickFix = 'quickfix'
    """ Base kind for quickfix actions: 'quickfix' """
    Refactor = 'refactor'
    """ Base kind for refactoring actions: 'refactor' """
    RefactorExtract = 'refactor.extract'
    """ Base kind for refactoring extraction actions: 'refactor.extract'

    Example extract actions:

    - Extract method
    - Extract function
    - Extract variable
    - Extract interface from class
    - ... """
    RefactorInline = 'refactor.inline'
    """ Base kind for refactoring inline actions: 'refactor.inline'

    Example inline actions:

    - Inline function
    - Inline variable
    - Inline constant
    - ... """
    RefactorMove = 'refactor.move'
    """ Base kind for refactoring move actions: `refactor.move`

    Example move actions:

    - Move a function to a new file
    - Move a property between classes
    - Move method to base class
    - ...

    @since 3.18.0
    @proposed """
    RefactorRewrite = 'refactor.rewrite'
    """ Base kind for refactoring rewrite actions: 'refactor.rewrite'

    Example rewrite actions:

    - Convert JavaScript function to class
    - Add or remove parameter
    - Encapsulate field
    - Make method static
    - Move method to base class
    - ... """
    Source = 'source'
    """ Base kind for source actions: `source`

    Source code actions apply to the entire file. """
    SourceOrganizeImports = 'source.organizeImports'
    """ Base kind for an organize imports source action: `source.organizeImports` """
    SourceFixAll = 'source.fixAll'
    """ Base kind for auto-fix source actions: `source.fixAll`.

    Fix all actions automatically fix errors that have a clear fix that do not require user input.
    They should not suppress errors or perform unsafe fixes such as generating new types or classes.

    @since 3.15.0 """
    Notebook = 'notebook'
    """ Base kind for all code actions applying to the entire notebook's scope. CodeActionKinds using
    this should always begin with `notebook.`

    @since 3.18.0 """


class CodeActionTag(IntEnum):
    """ Code action tags are extra annotations that tweak the behavior of a code action.

    @since 3.18.0 - proposed """
    LLMGenerated = 1
    """ Marks the code action as LLM-generated. """


class TraceValue(StrEnum):
    Off = 'off'
    """ Turn tracing off. """
    Messages = 'messages'
    """ Trace messages only. """
    Verbose = 'verbose'
    """ Verbose message tracing. """


class MarkupKind(StrEnum):
    """ Describes the content type that a client supports in various
    result literals like `Hover`, `ParameterInfo` or `CompletionItem`.

    Please note that `MarkupKinds` must not start with a `$`. This kinds
    are reserved for internal usage. """
    PlainText = 'plaintext'
    """ Plain text is supported as a content format """
    Markdown = 'markdown'
    """ Markdown is supported as a content format """


class LanguageKind(StrEnum):
    """ Predefined Language kinds
    @since 3.18.0 """
    ABAP = 'abap'
    WindowsBat = 'bat'
    BibTeX = 'bibtex'
    Clojure = 'clojure'
    Coffeescript = 'coffeescript'
    C = 'c'
    CPP = 'cpp'
    CSharp = 'csharp'
    CSS = 'css'
    D = 'd'
    """ @since 3.18.0
    @proposed """
    Delphi = 'pascal'
    """ @since 3.18.0
    @proposed """
    Diff = 'diff'
    Dart = 'dart'
    Dockerfile = 'dockerfile'
    Elixir = 'elixir'
    Erlang = 'erlang'
    FSharp = 'fsharp'
    GitCommit = 'git-commit'
    GitRebase = 'rebase'
    Go = 'go'
    Groovy = 'groovy'
    Handlebars = 'handlebars'
    Haskell = 'haskell'
    HTML = 'html'
    Ini = 'ini'
    Java = 'java'
    JavaScript = 'javascript'
    JavaScriptReact = 'javascriptreact'
    JSON = 'json'
    LaTeX = 'latex'
    Less = 'less'
    Lua = 'lua'
    Makefile = 'makefile'
    Markdown = 'markdown'
    ObjectiveC = 'objective-c'
    ObjectiveCPP = 'objective-cpp'
    Pascal = 'pascal'
    """ @since 3.18.0
    @proposed """
    Perl = 'perl'
    Perl6 = 'perl6'
    PHP = 'php'
    Powershell = 'powershell'
    Pug = 'jade'
    Python = 'python'
    R = 'r'
    Razor = 'razor'
    Ruby = 'ruby'
    Rust = 'rust'
    SCSS = 'scss'
    SASS = 'sass'
    Scala = 'scala'
    ShaderLab = 'shaderlab'
    ShellScript = 'shellscript'
    SQL = 'sql'
    Swift = 'swift'
    TypeScript = 'typescript'
    TypeScriptReact = 'typescriptreact'
    TeX = 'tex'
    VisualBasic = 'vb'
    XML = 'xml'
    XSL = 'xsl'
    YAML = 'yaml'


class InlineCompletionTriggerKind(IntEnum):
    """ Describes how an {@link InlineCompletionItemProvider inline completion provider} was triggered.

    @since 3.18.0
    @proposed """
    Invoked = 1
    """ Completion was triggered explicitly by a user gesture. """
    Automatic = 2
    """ Completion was triggered automatically while editing. """


class PositionEncodingKind(StrEnum):
    """ A set of predefined position encoding kinds.

    @since 3.17.0 """
    UTF8 = 'utf-8'
    """ Character offsets count UTF-8 code units (e.g. bytes). """
    UTF16 = 'utf-16'
    """ Character offsets count UTF-16 code units.

    This is the default and must always be supported
    by servers """
    UTF32 = 'utf-32'
    """ Character offsets count UTF-32 code units.

    Implementation note: these are the same as Unicode codepoints,
    so this `PositionEncodingKind` may also be used for an
    encoding-agnostic representation of character offsets. """


class FileChangeType(IntEnum):
    """ The file event type """
    Created = 1
    """ The file got created. """
    Changed = 2
    """ The file got changed. """
    Deleted = 3
    """ The file got deleted. """


class WatchKind(IntFlag):
    Create = 1
    """ Interested in create events. """
    Change = 2
    """ Interested in change events """
    Delete = 4
    """ Interested in delete events """


class DiagnosticSeverity(IntEnum):
    """ The diagnostic's severity. """
    Error = 1
    """ Reports an error. """
    Warning = 2
    """ Reports a warning. """
    Information = 3
    """ Reports an information. """
    Hint = 4
    """ Reports a hint. """


class DiagnosticTag(IntEnum):
    """ The diagnostic tags.

    @since 3.15.0 """
    Unnecessary = 1
    """ Unused or unnecessary code.

    Clients are allowed to render diagnostics with this tag faded out instead of having
    an error squiggle. """
    Deprecated = 2
    """ Deprecated or obsolete code.

    Clients are allowed to rendered diagnostics with this tag strike through. """


class CompletionTriggerKind(IntEnum):
    """ How a completion was triggered """
    Invoked = 1
    """ Completion was triggered by typing an identifier (24x7 code
    complete), manual invocation (e.g Ctrl+Space) or via API. """
    TriggerCharacter = 2
    """ Completion was triggered by a trigger character specified by
    the `triggerCharacters` properties of the `CompletionRegistrationOptions`. """
    TriggerForIncompleteCompletions = 3
    """ Completion was re-triggered as current completion list is incomplete """


class ApplyKind(IntFlag):
    """ Defines how values from a set of defaults and an individual item will be
    merged.

    @since 3.18.0 """
    Replace = 1
    """ The value from the individual item (if provided and not `null`) will be
    used instead of the default. """
    Merge = 2
    """ The value from the item will be merged with the default.

    The specific rules for mergeing values are defined against each field
    that supports merging. """


class SignatureHelpTriggerKind(IntEnum):
    """ How a signature help was triggered.

    @since 3.15.0 """
    Invoked = 1
    """ Signature help was invoked manually by the user or by a command. """
    TriggerCharacter = 2
    """ Signature help was triggered by a trigger character. """
    ContentChange = 3
    """ Signature help was triggered by the cursor moving or by the document content changing. """


class CodeActionTriggerKind(IntEnum):
    """ The reason why code actions were requested.

    @since 3.17.0 """
    Invoked = 1
    """ Code actions were explicitly requested by the user or by an extension. """
    Automatic = 2
    """ Code actions were requested automatically.

    This typically happens when current selection in a file changes, but can
    also be triggered when file content changes. """


class FileOperationPatternKind(StrEnum):
    """ A pattern kind describing if a glob pattern matches a file a folder or
    both.

    @since 3.16.0 """
    File = 'file'
    """ The pattern matches a file only. """
    Folder = 'folder'
    """ The pattern matches a folder only. """


class NotebookCellKind(IntEnum):
    """ A notebook cell kind.

    @since 3.17.0 """
    Markup = 1
    """ A markup-cell is formatted source that is used for display. """
    Code = 2
    """ A code-cell is source code. """


class ResourceOperationKind(StrEnum):
    Create = 'create'
    """ Supports creating new files and folders. """
    Rename = 'rename'
    """ Supports renaming existing files and folders. """
    Delete = 'delete'
    """ Supports deleting existing files and folders. """


class FailureHandlingKind(StrEnum):
    Abort = 'abort'
    """ Applying the workspace change is simply aborted if one of the changes provided
    fails. All operations executed before the failing operation stay executed. """
    Transactional = 'transactional'
    """ All operations are executed transactional. That means they either all
    succeed or no changes at all are applied to the workspace. """
    TextOnlyTransactional = 'textOnlyTransactional'
    """ If the workspace edit contains only textual file changes they are executed transactional.
    If resource changes (create, rename or delete file) are part of the change the failure
    handling strategy is abort. """
    Undo = 'undo'
    """ The client tries to undo the operations already executed. But there is no
    guarantee that this is succeeding. """


class PrepareSupportDefaultBehavior(IntEnum):
    Identifier = 1
    """ The client's default behavior is to select the identifier
    according the to language's syntax rule. """


class TokenFormat(StrEnum):
    Relative = 'relative'


Definition = Union['Location', List['Location']]
""" The definition of a symbol represented as one or many {@link Location locations}.
For most programming languages there is only one location at which a symbol is
defined.

Servers should prefer returning `DefinitionLink` over `Definition` if supported
by the client. """

DefinitionLink = 'LocationLink'
""" Information about where a symbol is defined.

Provides additional metadata over normal {@link Location location} definitions, including the range of
the defining symbol """

LSPArray = List['LSPAny']
""" LSP arrays.
@since 3.17.0 """

LSPAny = Union['LSPObject', 'LSPArray', str, int, Uint, float, bool, None]
""" The LSP any type.
Please note that strictly speaking a property with the value `undefined`
can't be converted into JSON preserving the property name. However for
convenience it is allowed and assumed that all these properties are
optional as well.
@since 3.17.0 """

Declaration = Union['Location', List['Location']]
""" The declaration of a symbol representation as one or many {@link Location locations}. """

DeclarationLink = 'LocationLink'
""" Information about where a symbol is declared.

Provides additional metadata over normal {@link Location location} declarations, including the range of
the declaring symbol.

Servers should prefer returning `DeclarationLink` over `Declaration` if supported
by the client. """

InlineValue = Union['InlineValueText', 'InlineValueVariableLookup', 'InlineValueEvaluatableExpression']
""" Inline value information can be provided by different means:
- directly as a text value (class InlineValueText).
- as a name to use for a variable lookup (class InlineValueVariableLookup)
- as an evaluatable expression (class InlineValueEvaluatableExpression)
The InlineValue types combines all inline value types into one type.

@since 3.17.0 """

DocumentDiagnosticReport = Union['RelatedFullDocumentDiagnosticReport', 'RelatedUnchangedDocumentDiagnosticReport']
""" The result of a document diagnostic pull request. A report can
either be a full report containing all diagnostics for the
requested document or an unchanged report indicating that nothing
has changed in terms of diagnostics in comparison to the last
pull request.

@since 3.17.0 """

PrepareRenameResult = Union['Range', 'PrepareRenamePlaceholder', 'PrepareRenameDefaultBehavior']

DocumentSelector = List['DocumentFilter']
""" A document selector is the combination of one or many document filters.

@sample `let sel:DocumentSelector = [{ language: 'typescript' }, { language: 'json', pattern: '**∕tsconfig.json' }]`;

The use of a string as a document filter is deprecated @since 3.16.0. """

ProgressToken = Union[int, str]

ChangeAnnotationIdentifier = str
""" An identifier to refer to a change annotation stored with a workspace edit. """

WorkspaceDocumentDiagnosticReport = Union['WorkspaceFullDocumentDiagnosticReport', 'WorkspaceUnchangedDocumentDiagnosticReport']
""" A workspace diagnostic document report.

@since 3.17.0 """

TextDocumentContentChangeEvent = Union['TextDocumentContentChangePartial', 'TextDocumentContentChangeWholeDocument']
""" An event describing a change to a text document. If only a text is provided
it is considered to be the full content of the document. """

MarkedString = Union[str, 'MarkedStringWithLanguage']
""" MarkedString can be used to render human readable text. It is either a markdown string
or a code-block that provides a language and a code snippet. The language identifier
is semantically equal to the optional language identifier in fenced code blocks in GitHub
issues. See https://help.github.com/articles/creating-and-highlighting-code-blocks/#syntax-highlighting

The pair of a language and a value is an equivalent to markdown:
```${language}
${value}
```

Note that markdown strings will be sanitized - that means html will be escaped.
@deprecated use MarkupContent instead. """

DocumentFilter = Union['TextDocumentFilter', 'NotebookCellTextDocumentFilter']
""" A document filter describes a top level text document or
a notebook cell document.

@since 3.17.0 - support for NotebookCellTextDocumentFilter. """

LSPObject = Dict[str, 'LSPAny']
""" LSP object definition.
@since 3.17.0 """

GlobPattern = Union['Pattern', 'RelativePattern']
""" The glob pattern. Either a string pattern or a relative pattern.

@since 3.17.0 """

TextDocumentFilter = Union['TextDocumentFilterLanguage', 'TextDocumentFilterScheme', 'TextDocumentFilterPattern']
""" A document filter denotes a document by different properties like
the {@link TextDocument.languageId language}, the {@link Uri.scheme scheme} of
its resource, or a glob-pattern that is applied to the {@link TextDocument.fileName path}.

Glob patterns can have the following syntax:
- `*` to match one or more characters in a path segment
- `?` to match on one character in a path segment
- `**` to match any number of path segments, including none
- `{}` to group sub patterns into an OR expression. (e.g. `**​/*.{ts,js}` matches all TypeScript and JavaScript files)
- `[]` to declare a range of characters to match in a path segment (e.g., `example.[0-9]` to match on `example.0`, `example.1`, …)
- `[!...]` to negate a range of characters to match in a path segment (e.g., `example.[!0-9]` to match on `example.a`, `example.b`, but not `example.0`)

@sample A language filter that applies to typescript files on disk: `{ language: 'typescript', scheme: 'file' }`
@sample A language filter that applies to all package.json paths: `{ language: 'json', pattern: '**package.json' }`

@since 3.17.0 """

NotebookDocumentFilter = Union['NotebookDocumentFilterNotebookType', 'NotebookDocumentFilterScheme', 'NotebookDocumentFilterPattern']
""" A notebook document filter denotes a notebook document by
different properties. The properties will be match
against the notebook's URI (same as with documents)

@since 3.17.0 """

Pattern = str
""" The glob pattern to watch relative to the base path. Glob patterns can have the following syntax:
- `*` to match one or more characters in a path segment
- `?` to match on one character in a path segment
- `**` to match any number of path segments, including none
- `{}` to group conditions (e.g. `**​/*.{ts,js}` matches all TypeScript and JavaScript files)
- `[]` to declare a range of characters to match in a path segment (e.g., `example.[0-9]` to match on `example.0`, `example.1`, …)
- `[!...]` to negate a range of characters to match in a path segment (e.g., `example.[!0-9]` to match on `example.a`, `example.b`, but not `example.0`)

@since 3.17.0 """

RegularExpressionEngineKind = str


ImplementationParams = TypedDict('ImplementationParams', {
    # The text document.
    'textDocument': 'TextDocumentIdentifier',
    # The position inside the text document.
    'position': 'Position',
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
    # An optional token that a server can use to report partial results (e.g. streaming) to
    # the client.
    'partialResultToken': NotRequired['ProgressToken'],
})


Location = TypedDict('Location', {
    'uri': 'DocumentUri',
    'range': 'Range',
})
""" Represents a location inside a resource, such as a line
inside a text file. """


ImplementationRegistrationOptions = TypedDict('ImplementationRegistrationOptions', {
    # A document selector to identify the scope of the registration. If set to null
    # the document selector provided on the client side will be used.
    'documentSelector': Union['DocumentSelector', None],
    # The id used to register the request. The id can be used to deregister
    # the request again. See also Registration#id.
    'id': NotRequired[str],
})


TypeDefinitionParams = TypedDict('TypeDefinitionParams', {
    # The text document.
    'textDocument': 'TextDocumentIdentifier',
    # The position inside the text document.
    'position': 'Position',
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
    # An optional token that a server can use to report partial results (e.g. streaming) to
    # the client.
    'partialResultToken': NotRequired['ProgressToken'],
})


TypeDefinitionRegistrationOptions = TypedDict('TypeDefinitionRegistrationOptions', {
    # A document selector to identify the scope of the registration. If set to null
    # the document selector provided on the client side will be used.
    'documentSelector': Union['DocumentSelector', None],
    # The id used to register the request. The id can be used to deregister
    # the request again. See also Registration#id.
    'id': NotRequired[str],
})


WorkspaceFolder = TypedDict('WorkspaceFolder', {
    # The associated URI for this workspace folder.
    'uri': 'URI',
    # The name of the workspace folder. Used to refer to this
    # workspace folder in the user interface.
    'name': str,
})
""" A workspace folder inside a client. """


DidChangeWorkspaceFoldersParams = TypedDict('DidChangeWorkspaceFoldersParams', {
    # The actual workspace folder change event.
    'event': 'WorkspaceFoldersChangeEvent',
})
""" The parameters of a `workspace/didChangeWorkspaceFolders` notification. """


ConfigurationParams = TypedDict('ConfigurationParams', {
    'items': List['ConfigurationItem'],
})
""" The parameters of a configuration request. """


DocumentColorParams = TypedDict('DocumentColorParams', {
    # The text document.
    'textDocument': 'TextDocumentIdentifier',
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
    # An optional token that a server can use to report partial results (e.g. streaming) to
    # the client.
    'partialResultToken': NotRequired['ProgressToken'],
})
""" Parameters for a {@link DocumentColorRequest}. """


ColorInformation = TypedDict('ColorInformation', {
    # The range in the document where this color appears.
    'range': 'Range',
    # The actual color value for this color range.
    'color': 'Color',
})
""" Represents a color range from a document. """


DocumentColorRegistrationOptions = TypedDict('DocumentColorRegistrationOptions', {
    # A document selector to identify the scope of the registration. If set to null
    # the document selector provided on the client side will be used.
    'documentSelector': Union['DocumentSelector', None],
    # The id used to register the request. The id can be used to deregister
    # the request again. See also Registration#id.
    'id': NotRequired[str],
})


ColorPresentationParams = TypedDict('ColorPresentationParams', {
    # The text document.
    'textDocument': 'TextDocumentIdentifier',
    # The color to request presentations for.
    'color': 'Color',
    # The range where the color would be inserted. Serves as a context.
    'range': 'Range',
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
    # An optional token that a server can use to report partial results (e.g. streaming) to
    # the client.
    'partialResultToken': NotRequired['ProgressToken'],
})
""" Parameters for a {@link ColorPresentationRequest}. """


ColorPresentation = TypedDict('ColorPresentation', {
    # The label of this color presentation. It will be shown on the color
    # picker header. By default this is also the text that is inserted when selecting
    # this color presentation.
    'label': str,
    # An {@link TextEdit edit} which is applied to a document when selecting
    # this presentation for the color.  When `falsy` the {@link ColorPresentation.label label}
    # is used.
    'textEdit': NotRequired['TextEdit'],
    # An optional array of additional {@link TextEdit text edits} that are applied when
    # selecting this color presentation. Edits must not overlap with the main {@link ColorPresentation.textEdit edit} nor with themselves.
    'additionalTextEdits': NotRequired[List['TextEdit']],
})


WorkDoneProgressOptions = TypedDict('WorkDoneProgressOptions', {
    'workDoneProgress': NotRequired[bool],
})


TextDocumentRegistrationOptions = TypedDict('TextDocumentRegistrationOptions', {
    # A document selector to identify the scope of the registration. If set to null
    # the document selector provided on the client side will be used.
    'documentSelector': Union['DocumentSelector', None],
})
""" General text document registration options. """


FoldingRangeParams = TypedDict('FoldingRangeParams', {
    # The text document.
    'textDocument': 'TextDocumentIdentifier',
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
    # An optional token that a server can use to report partial results (e.g. streaming) to
    # the client.
    'partialResultToken': NotRequired['ProgressToken'],
})
""" Parameters for a {@link FoldingRangeRequest}. """


FoldingRange = TypedDict('FoldingRange', {
    # The zero-based start line of the range to fold. The folded area starts after the line's last character.
    # To be valid, the end must be zero or larger and smaller than the number of lines in the document.
    'startLine': Uint,
    # The zero-based character offset from where the folded range starts. If not defined, defaults to the length of the start line.
    'startCharacter': NotRequired[Uint],
    # The zero-based end line of the range to fold. The folded area ends with the line's last character.
    # To be valid, the end must be zero or larger and smaller than the number of lines in the document.
    'endLine': Uint,
    # The zero-based character offset before the folded range ends. If not defined, defaults to the length of the end line.
    'endCharacter': NotRequired[Uint],
    # Describes the kind of the folding range such as 'comment' or 'region'. The kind
    # is used to categorize folding ranges and used by commands like 'Fold all comments'.
    # See {@link FoldingRangeKind} for an enumeration of standardized kinds.
    'kind': NotRequired['FoldingRangeKind'],
    # The text that the client should show when the specified range is
    # collapsed. If not defined or not supported by the client, a default
    # will be chosen by the client.
    #
    # @since 3.17.0
    'collapsedText': NotRequired[str],
})
""" Represents a folding range. To be valid, start and end line must be bigger than zero and smaller
than the number of lines in the document. Clients are free to ignore invalid ranges. """


FoldingRangeRegistrationOptions = TypedDict('FoldingRangeRegistrationOptions', {
    # A document selector to identify the scope of the registration. If set to null
    # the document selector provided on the client side will be used.
    'documentSelector': Union['DocumentSelector', None],
    # The id used to register the request. The id can be used to deregister
    # the request again. See also Registration#id.
    'id': NotRequired[str],
})


DeclarationParams = TypedDict('DeclarationParams', {
    # The text document.
    'textDocument': 'TextDocumentIdentifier',
    # The position inside the text document.
    'position': 'Position',
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
    # An optional token that a server can use to report partial results (e.g. streaming) to
    # the client.
    'partialResultToken': NotRequired['ProgressToken'],
})


DeclarationRegistrationOptions = TypedDict('DeclarationRegistrationOptions', {
    # A document selector to identify the scope of the registration. If set to null
    # the document selector provided on the client side will be used.
    'documentSelector': Union['DocumentSelector', None],
    # The id used to register the request. The id can be used to deregister
    # the request again. See also Registration#id.
    'id': NotRequired[str],
})


SelectionRangeParams = TypedDict('SelectionRangeParams', {
    # The text document.
    'textDocument': 'TextDocumentIdentifier',
    # The positions inside the text document.
    'positions': List['Position'],
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
    # An optional token that a server can use to report partial results (e.g. streaming) to
    # the client.
    'partialResultToken': NotRequired['ProgressToken'],
})
""" A parameter literal used in selection range requests. """


SelectionRange = TypedDict('SelectionRange', {
    # The {@link Range range} of this selection range.
    'range': 'Range',
    # The parent selection range containing this range. Therefore `parent.range` must contain `this.range`.
    'parent': NotRequired['SelectionRange'],
})
""" A selection range represents a part of a selection hierarchy. A selection range
may have a parent selection range that contains it. """


SelectionRangeRegistrationOptions = TypedDict('SelectionRangeRegistrationOptions', {
    # A document selector to identify the scope of the registration. If set to null
    # the document selector provided on the client side will be used.
    'documentSelector': Union['DocumentSelector', None],
    # The id used to register the request. The id can be used to deregister
    # the request again. See also Registration#id.
    'id': NotRequired[str],
})


WorkDoneProgressCreateParams = TypedDict('WorkDoneProgressCreateParams', {
    # The token to be used to report progress.
    'token': 'ProgressToken',
})


WorkDoneProgressCancelParams = TypedDict('WorkDoneProgressCancelParams', {
    # The token to be used to report progress.
    'token': 'ProgressToken',
})


CallHierarchyPrepareParams = TypedDict('CallHierarchyPrepareParams', {
    # The text document.
    'textDocument': 'TextDocumentIdentifier',
    # The position inside the text document.
    'position': 'Position',
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
})
""" The parameter of a `textDocument/prepareCallHierarchy` request.

@since 3.16.0 """


CallHierarchyItem = TypedDict('CallHierarchyItem', {
    # The name of this item.
    'name': str,
    # The kind of this item.
    'kind': 'SymbolKind',
    # Tags for this item.
    'tags': NotRequired[List['SymbolTag']],
    # More detail for this item, e.g. the signature of a function.
    'detail': NotRequired[str],
    # The resource identifier of this item.
    'uri': 'DocumentUri',
    # The range enclosing this symbol not including leading/trailing whitespace but everything else, e.g. comments and code.
    'range': 'Range',
    # The range that should be selected and revealed when this symbol is being picked, e.g. the name of a function.
    # Must be contained by the {@link CallHierarchyItem.range `range`}.
    'selectionRange': 'Range',
    # A data entry field that is preserved between a call hierarchy prepare and
    # incoming calls or outgoing calls requests.
    'data': NotRequired['LSPAny'],
})
""" Represents programming constructs like functions or constructors in the context
of call hierarchy.

@since 3.16.0 """


CallHierarchyRegistrationOptions = TypedDict('CallHierarchyRegistrationOptions', {
    # A document selector to identify the scope of the registration. If set to null
    # the document selector provided on the client side will be used.
    'documentSelector': Union['DocumentSelector', None],
    # The id used to register the request. The id can be used to deregister
    # the request again. See also Registration#id.
    'id': NotRequired[str],
})
""" Call hierarchy options used during static or dynamic registration.

@since 3.16.0 """


CallHierarchyIncomingCallsParams = TypedDict('CallHierarchyIncomingCallsParams', {
    'item': 'CallHierarchyItem',
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
    # An optional token that a server can use to report partial results (e.g. streaming) to
    # the client.
    'partialResultToken': NotRequired['ProgressToken'],
})
""" The parameter of a `callHierarchy/incomingCalls` request.

@since 3.16.0 """


CallHierarchyIncomingCall = TypedDict('CallHierarchyIncomingCall', {
    # The item that makes the call.
    'from': 'CallHierarchyItem',
    # The ranges at which the calls appear. This is relative to the caller
    # denoted by {@link CallHierarchyIncomingCall.from `this.from`}.
    'fromRanges': List['Range'],
})
""" Represents an incoming call, e.g. a caller of a method or constructor.

@since 3.16.0 """


CallHierarchyOutgoingCallsParams = TypedDict('CallHierarchyOutgoingCallsParams', {
    'item': 'CallHierarchyItem',
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
    # An optional token that a server can use to report partial results (e.g. streaming) to
    # the client.
    'partialResultToken': NotRequired['ProgressToken'],
})
""" The parameter of a `callHierarchy/outgoingCalls` request.

@since 3.16.0 """


CallHierarchyOutgoingCall = TypedDict('CallHierarchyOutgoingCall', {
    # The item that is called.
    'to': 'CallHierarchyItem',
    # The range at which this item is called. This is the range relative to the caller, e.g the item
    # passed to {@link CallHierarchyItemProvider.provideCallHierarchyOutgoingCalls `provideCallHierarchyOutgoingCalls`}
    # and not {@link CallHierarchyOutgoingCall.to `this.to`}.
    'fromRanges': List['Range'],
})
""" Represents an outgoing call, e.g. calling a getter from a method or a method from a constructor etc.

@since 3.16.0 """


SemanticTokensParams = TypedDict('SemanticTokensParams', {
    # The text document.
    'textDocument': 'TextDocumentIdentifier',
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
    # An optional token that a server can use to report partial results (e.g. streaming) to
    # the client.
    'partialResultToken': NotRequired['ProgressToken'],
})
""" @since 3.16.0 """


SemanticTokens = TypedDict('SemanticTokens', {
    # An optional result id. If provided and clients support delta updating
    # the client will include the result id in the next semantic token request.
    # A server can then instead of computing all semantic tokens again simply
    # send a delta.
    'resultId': NotRequired[str],
    # The actual tokens.
    'data': List[Uint],
})
""" @since 3.16.0 """


SemanticTokensPartialResult = TypedDict('SemanticTokensPartialResult', {
    'data': List[Uint],
})
""" @since 3.16.0 """


SemanticTokensRegistrationOptions = TypedDict('SemanticTokensRegistrationOptions', {
    # A document selector to identify the scope of the registration. If set to null
    # the document selector provided on the client side will be used.
    'documentSelector': Union['DocumentSelector', None],
    # The legend used by the server
    'legend': 'SemanticTokensLegend',
    # Server supports providing semantic tokens for a specific range
    # of a document.
    'range': NotRequired[Union[bool, dict]],
    # Server supports providing semantic tokens for a full document.
    'full': NotRequired[Union[bool, 'SemanticTokensFullDelta']],
    # The id used to register the request. The id can be used to deregister
    # the request again. See also Registration#id.
    'id': NotRequired[str],
})
""" @since 3.16.0 """


SemanticTokensDeltaParams = TypedDict('SemanticTokensDeltaParams', {
    # The text document.
    'textDocument': 'TextDocumentIdentifier',
    # The result id of a previous response. The result Id can either point to a full response
    # or a delta response depending on what was received last.
    'previousResultId': str,
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
    # An optional token that a server can use to report partial results (e.g. streaming) to
    # the client.
    'partialResultToken': NotRequired['ProgressToken'],
})
""" @since 3.16.0 """


SemanticTokensDelta = TypedDict('SemanticTokensDelta', {
    'resultId': NotRequired[str],
    # The semantic token edits to transform a previous result into a new result.
    'edits': List['SemanticTokensEdit'],
})
""" @since 3.16.0 """


SemanticTokensDeltaPartialResult = TypedDict('SemanticTokensDeltaPartialResult', {
    'edits': List['SemanticTokensEdit'],
})
""" @since 3.16.0 """


SemanticTokensRangeParams = TypedDict('SemanticTokensRangeParams', {
    # The text document.
    'textDocument': 'TextDocumentIdentifier',
    # The range the semantic tokens are requested for.
    'range': 'Range',
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
    # An optional token that a server can use to report partial results (e.g. streaming) to
    # the client.
    'partialResultToken': NotRequired['ProgressToken'],
})
""" @since 3.16.0 """


ShowDocumentParams = TypedDict('ShowDocumentParams', {
    # The uri to show.
    'uri': 'URI',
    # Indicates to show the resource in an external program.
    # To show, for example, `https://code.visualstudio.com/`
    # in the default WEB browser set `external` to `true`.
    'external': NotRequired[bool],
    # An optional property to indicate whether the editor
    # showing the document should take focus or not.
    # Clients might ignore this property if an external
    # program is started.
    'takeFocus': NotRequired[bool],
    # An optional selection range if the document is a text
    # document. Clients might ignore the property if an
    # external program is started or the file is not a text
    # file.
    'selection': NotRequired['Range'],
})
""" Params to show a resource in the UI.

@since 3.16.0 """


ShowDocumentResult = TypedDict('ShowDocumentResult', {
    # A boolean indicating if the show was successful.
    'success': bool,
})
""" The result of a showDocument request.

@since 3.16.0 """


LinkedEditingRangeParams = TypedDict('LinkedEditingRangeParams', {
    # The text document.
    'textDocument': 'TextDocumentIdentifier',
    # The position inside the text document.
    'position': 'Position',
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
})


LinkedEditingRanges = TypedDict('LinkedEditingRanges', {
    # A list of ranges that can be edited together. The ranges must have
    # identical length and contain identical text content. The ranges cannot overlap.
    'ranges': List['Range'],
    # An optional word pattern (regular expression) that describes valid contents for
    # the given ranges. If no pattern is provided, the client configuration's word
    # pattern will be used.
    'wordPattern': NotRequired[str],
})
""" The result of a linked editing range request.

@since 3.16.0 """


LinkedEditingRangeRegistrationOptions = TypedDict('LinkedEditingRangeRegistrationOptions', {
    # A document selector to identify the scope of the registration. If set to null
    # the document selector provided on the client side will be used.
    'documentSelector': Union['DocumentSelector', None],
    # The id used to register the request. The id can be used to deregister
    # the request again. See also Registration#id.
    'id': NotRequired[str],
})


CreateFilesParams = TypedDict('CreateFilesParams', {
    # An array of all files/folders created in this operation.
    'files': List['FileCreate'],
})
""" The parameters sent in notifications/requests for user-initiated creation of
files.

@since 3.16.0 """


WorkspaceEdit = TypedDict('WorkspaceEdit', {
    # Holds changes to existing resources.
    'changes': NotRequired[Dict['DocumentUri', List['TextEdit']]],
    # Depending on the client capability `workspace.workspaceEdit.resourceOperations` document changes
    # are either an array of `TextDocumentEdit`s to express changes to n different text documents
    # where each text document edit addresses a specific version of a text document. Or it can contain
    # above `TextDocumentEdit`s mixed with create, rename and delete file / folder operations.
    #
    # Whether a client supports versioned document edits is expressed via
    # `workspace.workspaceEdit.documentChanges` client capability.
    #
    # If a client neither supports `documentChanges` nor `workspace.workspaceEdit.resourceOperations` then
    # only plain `TextEdit`s using the `changes` property are supported.
    'documentChanges': NotRequired[List[Union['TextDocumentEdit', 'CreateFile', 'RenameFile', 'DeleteFile']]],
    # A map of change annotations that can be referenced in `AnnotatedTextEdit`s or create, rename and
    # delete file / folder operations.
    #
    # Whether clients honor this property depends on the client capability `workspace.changeAnnotationSupport`.
    #
    # @since 3.16.0
    'changeAnnotations': NotRequired[Dict['ChangeAnnotationIdentifier', 'ChangeAnnotation']],
})
""" A workspace edit represents changes to many resources managed in the workspace. The edit
should either provide `changes` or `documentChanges`. If documentChanges are present
they are preferred over `changes` if the client can handle versioned document edits.

Since version 3.13.0 a workspace edit can contain resource operations as well. If resource
operations are present clients need to execute the operations in the order in which they
are provided. So a workspace edit for example can consist of the following two changes:
(1) a create file a.txt and (2) a text document edit which insert text into file a.txt.

An invalid sequence (e.g. (1) delete file a.txt and (2) insert text into file a.txt) will
cause failure of the operation. How the client recovers from the failure is described by
the client capability: `workspace.workspaceEdit.failureHandling` """


FileOperationRegistrationOptions = TypedDict('FileOperationRegistrationOptions', {
    # The actual filters.
    'filters': List['FileOperationFilter'],
})
""" The options to register for file operations.

@since 3.16.0 """


RenameFilesParams = TypedDict('RenameFilesParams', {
    # An array of all files/folders renamed in this operation. When a folder is renamed, only
    # the folder will be included, and not its children.
    'files': List['FileRename'],
})
""" The parameters sent in notifications/requests for user-initiated renames of
files.

@since 3.16.0 """


DeleteFilesParams = TypedDict('DeleteFilesParams', {
    # An array of all files/folders deleted in this operation.
    'files': List['FileDelete'],
})
""" The parameters sent in notifications/requests for user-initiated deletes of
files.

@since 3.16.0 """


MonikerParams = TypedDict('MonikerParams', {
    # The text document.
    'textDocument': 'TextDocumentIdentifier',
    # The position inside the text document.
    'position': 'Position',
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
    # An optional token that a server can use to report partial results (e.g. streaming) to
    # the client.
    'partialResultToken': NotRequired['ProgressToken'],
})


Moniker = TypedDict('Moniker', {
    # The scheme of the moniker. For example tsc or .Net
    'scheme': str,
    # The identifier of the moniker. The value is opaque in LSIF however
    # schema owners are allowed to define the structure if they want.
    'identifier': str,
    # The scope in which the moniker is unique
    'unique': 'UniquenessLevel',
    # The moniker kind if known.
    'kind': NotRequired['MonikerKind'],
})
""" Moniker definition to match LSIF 0.5 moniker definition.

@since 3.16.0 """


MonikerRegistrationOptions = TypedDict('MonikerRegistrationOptions', {
    # A document selector to identify the scope of the registration. If set to null
    # the document selector provided on the client side will be used.
    'documentSelector': Union['DocumentSelector', None],
})


TypeHierarchyPrepareParams = TypedDict('TypeHierarchyPrepareParams', {
    # The text document.
    'textDocument': 'TextDocumentIdentifier',
    # The position inside the text document.
    'position': 'Position',
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
})
""" The parameter of a `textDocument/prepareTypeHierarchy` request.

@since 3.17.0 """


TypeHierarchyItem = TypedDict('TypeHierarchyItem', {
    # The name of this item.
    'name': str,
    # The kind of this item.
    'kind': 'SymbolKind',
    # Tags for this item.
    'tags': NotRequired[List['SymbolTag']],
    # More detail for this item, e.g. the signature of a function.
    'detail': NotRequired[str],
    # The resource identifier of this item.
    'uri': 'DocumentUri',
    # The range enclosing this symbol not including leading/trailing whitespace
    # but everything else, e.g. comments and code.
    'range': 'Range',
    # The range that should be selected and revealed when this symbol is being
    # picked, e.g. the name of a function. Must be contained by the
    # {@link TypeHierarchyItem.range `range`}.
    'selectionRange': 'Range',
    # A data entry field that is preserved between a type hierarchy prepare and
    # supertypes or subtypes requests. It could also be used to identify the
    # type hierarchy in the server, helping improve the performance on
    # resolving supertypes and subtypes.
    'data': NotRequired['LSPAny'],
})
""" @since 3.17.0 """


TypeHierarchyRegistrationOptions = TypedDict('TypeHierarchyRegistrationOptions', {
    # A document selector to identify the scope of the registration. If set to null
    # the document selector provided on the client side will be used.
    'documentSelector': Union['DocumentSelector', None],
    # The id used to register the request. The id can be used to deregister
    # the request again. See also Registration#id.
    'id': NotRequired[str],
})
""" Type hierarchy options used during static or dynamic registration.

@since 3.17.0 """


TypeHierarchySupertypesParams = TypedDict('TypeHierarchySupertypesParams', {
    'item': 'TypeHierarchyItem',
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
    # An optional token that a server can use to report partial results (e.g. streaming) to
    # the client.
    'partialResultToken': NotRequired['ProgressToken'],
})
""" The parameter of a `typeHierarchy/supertypes` request.

@since 3.17.0 """


TypeHierarchySubtypesParams = TypedDict('TypeHierarchySubtypesParams', {
    'item': 'TypeHierarchyItem',
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
    # An optional token that a server can use to report partial results (e.g. streaming) to
    # the client.
    'partialResultToken': NotRequired['ProgressToken'],
})
""" The parameter of a `typeHierarchy/subtypes` request.

@since 3.17.0 """


InlineValueParams = TypedDict('InlineValueParams', {
    # The text document.
    'textDocument': 'TextDocumentIdentifier',
    # The document range for which inline values should be computed.
    'range': 'Range',
    # Additional information about the context in which inline values were
    # requested.
    'context': 'InlineValueContext',
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
})
""" A parameter literal used in inline value requests.

@since 3.17.0 """


InlineValueRegistrationOptions = TypedDict('InlineValueRegistrationOptions', {
    # A document selector to identify the scope of the registration. If set to null
    # the document selector provided on the client side will be used.
    'documentSelector': Union['DocumentSelector', None],
    # The id used to register the request. The id can be used to deregister
    # the request again. See also Registration#id.
    'id': NotRequired[str],
})
""" Inline value options used during static or dynamic registration.

@since 3.17.0 """


InlayHintParams = TypedDict('InlayHintParams', {
    # The text document.
    'textDocument': 'TextDocumentIdentifier',
    # The document range for which inlay hints should be computed.
    'range': 'Range',
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
})
""" A parameter literal used in inlay hint requests.

@since 3.17.0 """


InlayHint = TypedDict('InlayHint', {
    # The position of this hint.
    #
    # If multiple hints have the same position, they will be shown in the order
    # they appear in the response.
    'position': 'Position',
    # The label of this hint. A human readable string or an array of
    # InlayHintLabelPart label parts.
    #
    # *Note* that neither the string nor the label part can be empty.
    'label': Union[str, List['InlayHintLabelPart']],
    # The kind of this hint. Can be omitted in which case the client
    # should fall back to a reasonable default.
    'kind': NotRequired['InlayHintKind'],
    # Optional text edits that are performed when accepting this inlay hint.
    #
    # *Note* that edits are expected to change the document so that the inlay
    # hint (or its nearest variant) is now part of the document and the inlay
    # hint itself is now obsolete.
    'textEdits': NotRequired[List['TextEdit']],
    # The tooltip text when you hover over this item.
    'tooltip': NotRequired[Union[str, 'MarkupContent']],
    # Render padding before the hint.
    #
    # Note: Padding should use the editor's background color, not the
    # background color of the hint itself. That means padding can be used
    # to visually align/separate an inlay hint.
    'paddingLeft': NotRequired[bool],
    # Render padding after the hint.
    #
    # Note: Padding should use the editor's background color, not the
    # background color of the hint itself. That means padding can be used
    # to visually align/separate an inlay hint.
    'paddingRight': NotRequired[bool],
    # A data entry field that is preserved on an inlay hint between
    # a `textDocument/inlayHint` and a `inlayHint/resolve` request.
    'data': NotRequired['LSPAny'],
})
""" Inlay hint information.

@since 3.17.0 """


InlayHintRegistrationOptions = TypedDict('InlayHintRegistrationOptions', {
    # The server provides support to resolve additional
    # information for an inlay hint item.
    'resolveProvider': NotRequired[bool],
    # A document selector to identify the scope of the registration. If set to null
    # the document selector provided on the client side will be used.
    'documentSelector': Union['DocumentSelector', None],
    # The id used to register the request. The id can be used to deregister
    # the request again. See also Registration#id.
    'id': NotRequired[str],
})
""" Inlay hint options used during static or dynamic registration.

@since 3.17.0 """


DocumentDiagnosticParams = TypedDict('DocumentDiagnosticParams', {
    # The text document.
    'textDocument': 'TextDocumentIdentifier',
    # The additional identifier  provided during registration.
    'identifier': NotRequired[str],
    # The result id of a previous response if provided.
    'previousResultId': NotRequired[str],
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
    # An optional token that a server can use to report partial results (e.g. streaming) to
    # the client.
    'partialResultToken': NotRequired['ProgressToken'],
})
""" Parameters of the document diagnostic request.

@since 3.17.0 """


DocumentDiagnosticReportPartialResult = TypedDict('DocumentDiagnosticReportPartialResult', {
    'relatedDocuments': Dict['DocumentUri', Union['FullDocumentDiagnosticReport', 'UnchangedDocumentDiagnosticReport']],
})
""" A partial result for a document diagnostic report.

@since 3.17.0 """


DiagnosticServerCancellationData = TypedDict('DiagnosticServerCancellationData', {
    'retriggerRequest': bool,
})
""" Cancellation data returned from a diagnostic request.

@since 3.17.0 """


DiagnosticRegistrationOptions = TypedDict('DiagnosticRegistrationOptions', {
    # A document selector to identify the scope of the registration. If set to null
    # the document selector provided on the client side will be used.
    'documentSelector': Union['DocumentSelector', None],
    # An optional identifier under which the diagnostics are
    # managed by the client.
    'identifier': NotRequired[str],
    # Whether the language has inter file dependencies meaning that
    # editing code in one file can result in a different diagnostic
    # set in another file. Inter file dependencies are common for
    # most programming languages and typically uncommon for linters.
    'interFileDependencies': bool,
    # The server provides support for workspace diagnostics as well.
    'workspaceDiagnostics': bool,
    # The id used to register the request. The id can be used to deregister
    # the request again. See also Registration#id.
    'id': NotRequired[str],
})
""" Diagnostic registration options.

@since 3.17.0 """


WorkspaceDiagnosticParams = TypedDict('WorkspaceDiagnosticParams', {
    # The additional identifier provided during registration.
    'identifier': NotRequired[str],
    # The currently known diagnostic reports with their
    # previous result ids.
    'previousResultIds': List['PreviousResultId'],
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
    # An optional token that a server can use to report partial results (e.g. streaming) to
    # the client.
    'partialResultToken': NotRequired['ProgressToken'],
})
""" Parameters of the workspace diagnostic request.

@since 3.17.0 """


WorkspaceDiagnosticReport = TypedDict('WorkspaceDiagnosticReport', {
    'items': List['WorkspaceDocumentDiagnosticReport'],
})
""" A workspace diagnostic report.

@since 3.17.0 """


WorkspaceDiagnosticReportPartialResult = TypedDict('WorkspaceDiagnosticReportPartialResult', {
    'items': List['WorkspaceDocumentDiagnosticReport'],
})
""" A partial result for a workspace diagnostic report.

@since 3.17.0 """


DidOpenNotebookDocumentParams = TypedDict('DidOpenNotebookDocumentParams', {
    # The notebook document that got opened.
    'notebookDocument': 'NotebookDocument',
    # The text documents that represent the content
    # of a notebook cell.
    'cellTextDocuments': List['TextDocumentItem'],
})
""" The params sent in an open notebook document notification.

@since 3.17.0 """


NotebookDocumentSyncRegistrationOptions = TypedDict('NotebookDocumentSyncRegistrationOptions', {
    # The notebooks to be synced
    'notebookSelector': List[Union['NotebookDocumentFilterWithNotebook', 'NotebookDocumentFilterWithCells']],
    # Whether save notification should be forwarded to
    # the server. Will only be honored if mode === `notebook`.
    'save': NotRequired[bool],
    # The id used to register the request. The id can be used to deregister
    # the request again. See also Registration#id.
    'id': NotRequired[str],
})
""" Registration options specific to a notebook.

@since 3.17.0 """


DidChangeNotebookDocumentParams = TypedDict('DidChangeNotebookDocumentParams', {
    # The notebook document that did change. The version number points
    # to the version after all provided changes have been applied. If
    # only the text document content of a cell changes the notebook version
    # doesn't necessarily have to change.
    'notebookDocument': 'VersionedNotebookDocumentIdentifier',
    # The actual changes to the notebook document.
    #
    # The changes describe single state changes to the notebook document.
    # So if there are two changes c1 (at array index 0) and c2 (at array
    # index 1) for a notebook in state S then c1 moves the notebook from
    # S to S' and c2 from S' to S''. So c1 is computed on the state S and
    # c2 is computed on the state S'.
    #
    # To mirror the content of a notebook using change events use the following approach:
    # - start with the same initial content
    # - apply the 'notebookDocument/didChange' notifications in the order you receive them.
    # - apply the `NotebookChangeEvent`s in a single notification in the order
    #   you receive them.
    'change': 'NotebookDocumentChangeEvent',
})
""" The params sent in a change notebook document notification.

@since 3.17.0 """


DidSaveNotebookDocumentParams = TypedDict('DidSaveNotebookDocumentParams', {
    # The notebook document that got saved.
    'notebookDocument': 'NotebookDocumentIdentifier',
})
""" The params sent in a save notebook document notification.

@since 3.17.0 """


DidCloseNotebookDocumentParams = TypedDict('DidCloseNotebookDocumentParams', {
    # The notebook document that got closed.
    'notebookDocument': 'NotebookDocumentIdentifier',
    # The text documents that represent the content
    # of a notebook cell that got closed.
    'cellTextDocuments': List['TextDocumentIdentifier'],
})
""" The params sent in a close notebook document notification.

@since 3.17.0 """


InlineCompletionParams = TypedDict('InlineCompletionParams', {
    # Additional information about the context in which inline completions were
    # requested.
    'context': 'InlineCompletionContext',
    # The text document.
    'textDocument': 'TextDocumentIdentifier',
    # The position inside the text document.
    'position': 'Position',
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
})
""" A parameter literal used in inline completion requests.

@since 3.18.0
@proposed """


InlineCompletionList = TypedDict('InlineCompletionList', {
    # The inline completion items
    'items': List['InlineCompletionItem'],
})
""" Represents a collection of {@link InlineCompletionItem inline completion items} to be presented in the editor.

@since 3.18.0
@proposed """


InlineCompletionItem = TypedDict('InlineCompletionItem', {
    # The text to replace the range with. Must be set.
    'insertText': Union[str, 'StringValue'],
    # A text that is used to decide if this inline completion should be shown. When `falsy` the {@link InlineCompletionItem.insertText} is used.
    'filterText': NotRequired[str],
    # The range to replace. Must begin and end on the same line.
    'range': NotRequired['Range'],
    # An optional {@link Command} that is executed *after* inserting this completion.
    'command': NotRequired['Command'],
})
""" An inline completion item represents a text snippet that is proposed inline to complete text that is being typed.

@since 3.18.0
@proposed """


InlineCompletionRegistrationOptions = TypedDict('InlineCompletionRegistrationOptions', {
    # A document selector to identify the scope of the registration. If set to null
    # the document selector provided on the client side will be used.
    'documentSelector': Union['DocumentSelector', None],
    # The id used to register the request. The id can be used to deregister
    # the request again. See also Registration#id.
    'id': NotRequired[str],
})
""" Inline completion options used during static or dynamic registration.

@since 3.18.0
@proposed """


TextDocumentContentParams = TypedDict('TextDocumentContentParams', {
    # The uri of the text document.
    'uri': 'DocumentUri',
})
""" Parameters for the `workspace/textDocumentContent` request.

@since 3.18.0
@proposed """


TextDocumentContentResult = TypedDict('TextDocumentContentResult', {
    # The text content of the text document. Please note, that the content of
    # any subsequent open notifications for the text document might differ
    # from the returned content due to whitespace and line ending
    # normalizations done on the client
    'text': str,
})
""" Result of the `workspace/textDocumentContent` request.

@since 3.18.0
@proposed """


TextDocumentContentRegistrationOptions = TypedDict('TextDocumentContentRegistrationOptions', {
    # The schemes for which the server provides content.
    'schemes': List[str],
    # The id used to register the request. The id can be used to deregister
    # the request again. See also Registration#id.
    'id': NotRequired[str],
})
""" Text document content provider registration options.

@since 3.18.0
@proposed """


TextDocumentContentRefreshParams = TypedDict('TextDocumentContentRefreshParams', {
    # The uri of the text document to refresh.
    'uri': 'DocumentUri',
})
""" Parameters for the `workspace/textDocumentContent/refresh` request.

@since 3.18.0
@proposed """


RegistrationParams = TypedDict('RegistrationParams', {
    'registrations': List['Registration'],
})


UnregistrationParams = TypedDict('UnregistrationParams', {
    'unregisterations': List['Unregistration'],
})


InitializeParams = TypedDict('InitializeParams', {
    # The process Id of the parent process that started
    # the server.
    #
    # Is `null` if the process has not been started by another process.
    # If the parent process is not alive then the server should exit.
    'processId': Union[int, None],
    # Information about the client
    #
    # @since 3.15.0
    'clientInfo': NotRequired['ClientInfo'],
    # The locale the client is currently showing the user interface
    # in. This must not necessarily be the locale of the operating
    # system.
    #
    # Uses IETF language tags as the value's syntax
    # (See https://en.wikipedia.org/wiki/IETF_language_tag)
    #
    # @since 3.16.0
    'locale': NotRequired[str],
    # The rootPath of the workspace. Is null
    # if no folder is open.
    #
    # @deprecated in favour of rootUri.
    'rootPath': NotRequired[Union[str, None]],
    # The rootUri of the workspace. Is null if no
    # folder is open. If both `rootPath` and `rootUri` are set
    # `rootUri` wins.
    #
    # @deprecated in favour of workspaceFolders.
    'rootUri': Union['DocumentUri', None],
    # The capabilities provided by the client (editor or tool)
    'capabilities': 'ClientCapabilities',
    # User provided initialization options.
    'initializationOptions': NotRequired['LSPAny'],
    # The initial trace setting. If omitted trace is disabled ('off').
    'trace': NotRequired['TraceValue'],
    # The workspace folders configured in the client when the server starts.
    #
    # This property is only available if the client supports workspace folders.
    # It can be `null` if the client supports workspace folders but none are
    # configured.
    #
    # @since 3.6.0
    'workspaceFolders': NotRequired[Union[List['WorkspaceFolder'], None]],
})


InitializeResult = TypedDict('InitializeResult', {
    # The capabilities the language server provides.
    'capabilities': 'ServerCapabilities',
    # Information about the server.
    #
    # @since 3.15.0
    'serverInfo': NotRequired['ServerInfo'],
})
""" The result returned from an initialize request. """


InitializeError = TypedDict('InitializeError', {
    # Indicates whether the client execute the following retry logic:
    # (1) show the message provided by the ResponseError to the user
    # (2) user selects retry or cancel
    # (3) if user selected retry the initialize method is sent again.
    'retry': bool,
})
""" The data type of the ResponseError if the
initialize request fails. """


InitializedParams = TypedDict('InitializedParams', {

})


DidChangeConfigurationParams = TypedDict('DidChangeConfigurationParams', {
    # The actual changed settings
    'settings': 'LSPAny',
})
""" The parameters of a change configuration notification. """


DidChangeConfigurationRegistrationOptions = TypedDict('DidChangeConfigurationRegistrationOptions', {
    'section': NotRequired[Union[str, List[str]]],
})


ShowMessageParams = TypedDict('ShowMessageParams', {
    # The message type. See {@link MessageType}
    'type': 'MessageType',
    # The actual message.
    'message': str,
})
""" The parameters of a notification message. """


ShowMessageRequestParams = TypedDict('ShowMessageRequestParams', {
    # The message type. See {@link MessageType}
    'type': 'MessageType',
    # The actual message.
    'message': str,
    # The message action items to present.
    'actions': NotRequired[List['MessageActionItem']],
})


MessageActionItem = TypedDict('MessageActionItem', {
    # A short title like 'Retry', 'Open Log' etc.
    'title': str,
})


LogMessageParams = TypedDict('LogMessageParams', {
    # The message type. See {@link MessageType}
    'type': 'MessageType',
    # The actual message.
    'message': str,
})
""" The log message parameters. """


DidOpenTextDocumentParams = TypedDict('DidOpenTextDocumentParams', {
    # The document that was opened.
    'textDocument': 'TextDocumentItem',
})
""" The parameters sent in an open text document notification """


DidChangeTextDocumentParams = TypedDict('DidChangeTextDocumentParams', {
    # The document that did change. The version number points
    # to the version after all provided content changes have
    # been applied.
    'textDocument': 'VersionedTextDocumentIdentifier',
    # The actual content changes. The content changes describe single state changes
    # to the document. So if there are two content changes c1 (at array index 0) and
    # c2 (at array index 1) for a document in state S then c1 moves the document from
    # S to S' and c2 from S' to S''. So c1 is computed on the state S and c2 is computed
    # on the state S'.
    #
    # To mirror the content of a document using change events use the following approach:
    # - start with the same initial content
    # - apply the 'textDocument/didChange' notifications in the order you receive them.
    # - apply the `TextDocumentContentChangeEvent`s in a single notification in the order
    #   you receive them.
    'contentChanges': List['TextDocumentContentChangeEvent'],
})
""" The change text document notification's parameters. """


TextDocumentChangeRegistrationOptions = TypedDict('TextDocumentChangeRegistrationOptions', {
    # How documents are synced to the server.
    'syncKind': 'TextDocumentSyncKind',
    # A document selector to identify the scope of the registration. If set to null
    # the document selector provided on the client side will be used.
    'documentSelector': Union['DocumentSelector', None],
})
""" Describe options to be used when registered for text document change events. """


DidCloseTextDocumentParams = TypedDict('DidCloseTextDocumentParams', {
    # The document that was closed.
    'textDocument': 'TextDocumentIdentifier',
})
""" The parameters sent in a close text document notification """


DidSaveTextDocumentParams = TypedDict('DidSaveTextDocumentParams', {
    # The document that was saved.
    'textDocument': 'TextDocumentIdentifier',
    # Optional the content when saved. Depends on the includeText value
    # when the save notification was requested.
    'text': NotRequired[str],
})
""" The parameters sent in a save text document notification """


TextDocumentSaveRegistrationOptions = TypedDict('TextDocumentSaveRegistrationOptions', {
    # A document selector to identify the scope of the registration. If set to null
    # the document selector provided on the client side will be used.
    'documentSelector': Union['DocumentSelector', None],
    # The client is supposed to include the content on save.
    'includeText': NotRequired[bool],
})
""" Save registration options. """


WillSaveTextDocumentParams = TypedDict('WillSaveTextDocumentParams', {
    # The document that will be saved.
    'textDocument': 'TextDocumentIdentifier',
    # The 'TextDocumentSaveReason'.
    'reason': 'TextDocumentSaveReason',
})
""" The parameters sent in a will save text document notification. """


TextEdit = TypedDict('TextEdit', {
    # The range of the text document to be manipulated. To insert
    # text into a document create a range where start === end.
    'range': 'Range',
    # The string to be inserted. For delete operations use an
    # empty string.
    'newText': str,
})
""" A text edit applicable to a text document. """


DidChangeWatchedFilesParams = TypedDict('DidChangeWatchedFilesParams', {
    # The actual file events.
    'changes': List['FileEvent'],
})
""" The watched files change notification's parameters. """


DidChangeWatchedFilesRegistrationOptions = TypedDict('DidChangeWatchedFilesRegistrationOptions', {
    # The watchers to register.
    'watchers': List['FileSystemWatcher'],
})
""" Describe options to be used when registered for text document change events. """


PublishDiagnosticsParams = TypedDict('PublishDiagnosticsParams', {
    # The URI for which diagnostic information is reported.
    'uri': 'DocumentUri',
    # Optional the version number of the document the diagnostics are published for.
    #
    # @since 3.15.0
    'version': NotRequired[int],
    # An array of diagnostic information items.
    'diagnostics': List['Diagnostic'],
})
""" The publish diagnostic notification's parameters. """


CompletionParams = TypedDict('CompletionParams', {
    # The completion context. This is only available it the client specifies
    # to send this using the client capability `textDocument.completion.contextSupport === true`
    'context': NotRequired['CompletionContext'],
    # The text document.
    'textDocument': 'TextDocumentIdentifier',
    # The position inside the text document.
    'position': 'Position',
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
    # An optional token that a server can use to report partial results (e.g. streaming) to
    # the client.
    'partialResultToken': NotRequired['ProgressToken'],
})
""" Completion parameters """


CompletionItem = TypedDict('CompletionItem', {
    # The label of this completion item.
    #
    # The label property is also by default the text that
    # is inserted when selecting this completion.
    #
    # If label details are provided the label itself should
    # be an unqualified name of the completion item.
    'label': str,
    # Additional details for the label
    #
    # @since 3.17.0
    'labelDetails': NotRequired['CompletionItemLabelDetails'],
    # The kind of this completion item. Based of the kind
    # an icon is chosen by the editor.
    'kind': NotRequired['CompletionItemKind'],
    # Tags for this completion item.
    #
    # @since 3.15.0
    'tags': NotRequired[List['CompletionItemTag']],
    # A human-readable string with additional information
    # about this item, like type or symbol information.
    'detail': NotRequired[str],
    # A human-readable string that represents a doc-comment.
    'documentation': NotRequired[Union[str, 'MarkupContent']],
    # Indicates if this item is deprecated.
    # @deprecated Use `tags` instead.
    'deprecated': NotRequired[bool],
    # Select this item when showing.
    #
    # *Note* that only one completion item can be selected and that the
    # tool / client decides which item that is. The rule is that the *first*
    # item of those that match best is selected.
    'preselect': NotRequired[bool],
    # A string that should be used when comparing this item
    # with other items. When `falsy` the {@link CompletionItem.label label}
    # is used.
    'sortText': NotRequired[str],
    # A string that should be used when filtering a set of
    # completion items. When `falsy` the {@link CompletionItem.label label}
    # is used.
    'filterText': NotRequired[str],
    # A string that should be inserted into a document when selecting
    # this completion. When `falsy` the {@link CompletionItem.label label}
    # is used.
    #
    # The `insertText` is subject to interpretation by the client side.
    # Some tools might not take the string literally. For example
    # VS Code when code complete is requested in this example
    # `con<cursor position>` and a completion item with an `insertText` of
    # `console` is provided it will only insert `sole`. Therefore it is
    # recommended to use `textEdit` instead since it avoids additional client
    # side interpretation.
    'insertText': NotRequired[str],
    # The format of the insert text. The format applies to both the
    # `insertText` property and the `newText` property of a provided
    # `textEdit`. If omitted defaults to `InsertTextFormat.PlainText`.
    #
    # Please note that the insertTextFormat doesn't apply to
    # `additionalTextEdits`.
    'insertTextFormat': NotRequired['InsertTextFormat'],
    # How whitespace and indentation is handled during completion
    # item insertion. If not provided the clients default value depends on
    # the `textDocument.completion.insertTextMode` client capability.
    #
    # @since 3.16.0
    'insertTextMode': NotRequired['InsertTextMode'],
    # An {@link TextEdit edit} which is applied to a document when selecting
    # this completion. When an edit is provided the value of
    # {@link CompletionItem.insertText insertText} is ignored.
    #
    # Most editors support two different operations when accepting a completion
    # item. One is to insert a completion text and the other is to replace an
    # existing text with a completion text. Since this can usually not be
    # predetermined by a server it can report both ranges. Clients need to
    # signal support for `InsertReplaceEdits` via the
    # `textDocument.completion.insertReplaceSupport` client capability
    # property.
    #
    # *Note 1:* The text edit's range as well as both ranges from an insert
    # replace edit must be a [single line] and they must contain the position
    # at which completion has been requested.
    # *Note 2:* If an `InsertReplaceEdit` is returned the edit's insert range
    # must be a prefix of the edit's replace range, that means it must be
    # contained and starting at the same position.
    #
    # @since 3.16.0 additional type `InsertReplaceEdit`
    'textEdit': NotRequired[Union['TextEdit', 'InsertReplaceEdit']],
    # The edit text used if the completion item is part of a CompletionList and
    # CompletionList defines an item default for the text edit range.
    #
    # Clients will only honor this property if they opt into completion list
    # item defaults using the capability `completionList.itemDefaults`.
    #
    # If not provided and a list's default range is provided the label
    # property is used as a text.
    #
    # @since 3.17.0
    'textEditText': NotRequired[str],
    # An optional array of additional {@link TextEdit text edits} that are applied when
    # selecting this completion. Edits must not overlap (including the same insert position)
    # with the main {@link CompletionItem.textEdit edit} nor with themselves.
    #
    # Additional text edits should be used to change text unrelated to the current cursor position
    # (for example adding an import statement at the top of the file if the completion item will
    # insert an unqualified type).
    'additionalTextEdits': NotRequired[List['TextEdit']],
    # An optional set of characters that when pressed while this completion is active will accept it first and
    # then type that character. *Note* that all commit characters should have `length=1` and that superfluous
    # characters will be ignored.
    'commitCharacters': NotRequired[List[str]],
    # An optional {@link Command command} that is executed *after* inserting this completion. *Note* that
    # additional modifications to the current document should be described with the
    # {@link CompletionItem.additionalTextEdits additionalTextEdits}-property.
    'command': NotRequired['Command'],
    # A data entry field that is preserved on a completion item between a
    # {@link CompletionRequest} and a {@link CompletionResolveRequest}.
    'data': NotRequired['LSPAny'],
})
""" A completion item represents a text snippet that is
proposed to complete text that is being typed. """


CompletionList = TypedDict('CompletionList', {
    # This list it not complete. Further typing results in recomputing this list.
    #
    # Recomputed lists have all their items replaced (not appended) in the
    # incomplete completion sessions.
    'isIncomplete': bool,
    # In many cases the items of an actual completion result share the same
    # value for properties like `commitCharacters` or the range of a text
    # edit. A completion list can therefore define item defaults which will
    # be used if a completion item itself doesn't specify the value.
    #
    # If a completion list specifies a default value and a completion item
    # also specifies a corresponding value, the rules for combining these are
    # defined by `applyKinds` (if the client supports it), defaulting to
    # ApplyKind.Replace.
    #
    # Servers are only allowed to return default values if the client
    # signals support for this via the `completionList.itemDefaults`
    # capability.
    #
    # @since 3.17.0
    'itemDefaults': NotRequired['CompletionItemDefaults'],
    # Specifies how fields from a completion item should be combined with those
    # from `completionList.itemDefaults`.
    #
    # If unspecified, all fields will be treated as ApplyKind.Replace.
    #
    # If a field's value is ApplyKind.Replace, the value from a completion item
    # (if provided and not `null`) will always be used instead of the value
    # from `completionItem.itemDefaults`.
    #
    # If a field's value is ApplyKind.Merge, the values will be merged using
    # the rules defined against each field below.
    #
    # Servers are only allowed to return `applyKind` if the client
    # signals support for this via the `completionList.applyKindSupport`
    # capability.
    #
    # @since 3.18.0
    'applyKind': NotRequired['CompletionItemApplyKinds'],
    # The completion items.
    'items': List['CompletionItem'],
})
""" Represents a collection of {@link CompletionItem completion items} to be presented
in the editor. """


CompletionRegistrationOptions = TypedDict('CompletionRegistrationOptions', {
    # A document selector to identify the scope of the registration. If set to null
    # the document selector provided on the client side will be used.
    'documentSelector': Union['DocumentSelector', None],
    # Most tools trigger completion request automatically without explicitly requesting
    # it using a keyboard shortcut (e.g. Ctrl+Space). Typically they do so when the user
    # starts to type an identifier. For example if the user types `c` in a JavaScript file
    # code complete will automatically pop up present `console` besides others as a
    # completion item. Characters that make up identifiers don't need to be listed here.
    #
    # If code complete should automatically be trigger on characters not being valid inside
    # an identifier (for example `.` in JavaScript) list them in `triggerCharacters`.
    'triggerCharacters': NotRequired[List[str]],
    # The list of all possible characters that commit a completion. This field can be used
    # if clients don't support individual commit characters per completion item. See
    # `ClientCapabilities.textDocument.completion.completionItem.commitCharactersSupport`
    #
    # If a server provides both `allCommitCharacters` and commit characters on an individual
    # completion item the ones on the completion item win.
    #
    # @since 3.2.0
    'allCommitCharacters': NotRequired[List[str]],
    # The server provides support to resolve additional
    # information for a completion item.
    'resolveProvider': NotRequired[bool],
    # The server supports the following `CompletionItem` specific
    # capabilities.
    #
    # @since 3.17.0
    'completionItem': NotRequired['ServerCompletionItemOptions'],
})
""" Registration options for a {@link CompletionRequest}. """


HoverParams = TypedDict('HoverParams', {
    # The text document.
    'textDocument': 'TextDocumentIdentifier',
    # The position inside the text document.
    'position': 'Position',
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
})
""" Parameters for a {@link HoverRequest}. """


Hover = TypedDict('Hover', {
    # The hover's content
    'contents': Union['MarkupContent', 'MarkedString', List['MarkedString']],
    # An optional range inside the text document that is used to
    # visualize the hover, e.g. by changing the background color.
    'range': NotRequired['Range'],
})
""" The result of a hover request. """


HoverRegistrationOptions = TypedDict('HoverRegistrationOptions', {
    # A document selector to identify the scope of the registration. If set to null
    # the document selector provided on the client side will be used.
    'documentSelector': Union['DocumentSelector', None],
})
""" Registration options for a {@link HoverRequest}. """


SignatureHelpParams = TypedDict('SignatureHelpParams', {
    # The signature help context. This is only available if the client specifies
    # to send this using the client capability `textDocument.signatureHelp.contextSupport === true`
    #
    # @since 3.15.0
    'context': NotRequired['SignatureHelpContext'],
    # The text document.
    'textDocument': 'TextDocumentIdentifier',
    # The position inside the text document.
    'position': 'Position',
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
})
""" Parameters for a {@link SignatureHelpRequest}. """


SignatureHelp = TypedDict('SignatureHelp', {
    # One or more signatures.
    'signatures': List['SignatureInformation'],
    # The active signature. If omitted or the value lies outside the
    # range of `signatures` the value defaults to zero or is ignored if
    # the `SignatureHelp` has no signatures.
    #
    # Whenever possible implementors should make an active decision about
    # the active signature and shouldn't rely on a default value.
    #
    # In future version of the protocol this property might become
    # mandatory to better express this.
    'activeSignature': NotRequired[Uint],
    # The active parameter of the active signature.
    #
    # If `null`, no parameter of the signature is active (for example a named
    # argument that does not match any declared parameters). This is only valid
    # if the client specifies the client capability
    # `textDocument.signatureHelp.noActiveParameterSupport === true`
    #
    # If omitted or the value lies outside the range of
    # `signatures[activeSignature].parameters` defaults to 0 if the active
    # signature has parameters.
    #
    # If the active signature has no parameters it is ignored.
    #
    # In future version of the protocol this property might become
    # mandatory (but still nullable) to better express the active parameter if
    # the active signature does have any.
    'activeParameter': NotRequired[Union[Uint, None]],
})
""" Signature help represents the signature of something
callable. There can be multiple signature but only one
active and only one active parameter. """


SignatureHelpRegistrationOptions = TypedDict('SignatureHelpRegistrationOptions', {
    # A document selector to identify the scope of the registration. If set to null
    # the document selector provided on the client side will be used.
    'documentSelector': Union['DocumentSelector', None],
    # List of characters that trigger signature help automatically.
    'triggerCharacters': NotRequired[List[str]],
    # List of characters that re-trigger signature help.
    #
    # These trigger characters are only active when signature help is already showing. All trigger characters
    # are also counted as re-trigger characters.
    #
    # @since 3.15.0
    'retriggerCharacters': NotRequired[List[str]],
})
""" Registration options for a {@link SignatureHelpRequest}. """


DefinitionParams = TypedDict('DefinitionParams', {
    # The text document.
    'textDocument': 'TextDocumentIdentifier',
    # The position inside the text document.
    'position': 'Position',
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
    # An optional token that a server can use to report partial results (e.g. streaming) to
    # the client.
    'partialResultToken': NotRequired['ProgressToken'],
})
""" Parameters for a {@link DefinitionRequest}. """


DefinitionRegistrationOptions = TypedDict('DefinitionRegistrationOptions', {
    # A document selector to identify the scope of the registration. If set to null
    # the document selector provided on the client side will be used.
    'documentSelector': Union['DocumentSelector', None],
})
""" Registration options for a {@link DefinitionRequest}. """


ReferenceParams = TypedDict('ReferenceParams', {
    'context': 'ReferenceContext',
    # The text document.
    'textDocument': 'TextDocumentIdentifier',
    # The position inside the text document.
    'position': 'Position',
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
    # An optional token that a server can use to report partial results (e.g. streaming) to
    # the client.
    'partialResultToken': NotRequired['ProgressToken'],
})
""" Parameters for a {@link ReferencesRequest}. """


ReferenceRegistrationOptions = TypedDict('ReferenceRegistrationOptions', {
    # A document selector to identify the scope of the registration. If set to null
    # the document selector provided on the client side will be used.
    'documentSelector': Union['DocumentSelector', None],
})
""" Registration options for a {@link ReferencesRequest}. """


DocumentHighlightParams = TypedDict('DocumentHighlightParams', {
    # The text document.
    'textDocument': 'TextDocumentIdentifier',
    # The position inside the text document.
    'position': 'Position',
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
    # An optional token that a server can use to report partial results (e.g. streaming) to
    # the client.
    'partialResultToken': NotRequired['ProgressToken'],
})
""" Parameters for a {@link DocumentHighlightRequest}. """


DocumentHighlight = TypedDict('DocumentHighlight', {
    # The range this highlight applies to.
    'range': 'Range',
    # The highlight kind, default is {@link DocumentHighlightKind.Text text}.
    'kind': NotRequired['DocumentHighlightKind'],
})
""" A document highlight is a range inside a text document which deserves
special attention. Usually a document highlight is visualized by changing
the background color of its range. """


DocumentHighlightRegistrationOptions = TypedDict('DocumentHighlightRegistrationOptions', {
    # A document selector to identify the scope of the registration. If set to null
    # the document selector provided on the client side will be used.
    'documentSelector': Union['DocumentSelector', None],
})
""" Registration options for a {@link DocumentHighlightRequest}. """


DocumentSymbolParams = TypedDict('DocumentSymbolParams', {
    # The text document.
    'textDocument': 'TextDocumentIdentifier',
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
    # An optional token that a server can use to report partial results (e.g. streaming) to
    # the client.
    'partialResultToken': NotRequired['ProgressToken'],
})
""" Parameters for a {@link DocumentSymbolRequest}. """


SymbolInformation = TypedDict('SymbolInformation', {
    # Indicates if this symbol is deprecated.
    #
    # @deprecated Use tags instead
    'deprecated': NotRequired[bool],
    # The location of this symbol. The location's range is used by a tool
    # to reveal the location in the editor. If the symbol is selected in the
    # tool the range's start information is used to position the cursor. So
    # the range usually spans more than the actual symbol's name and does
    # normally include things like visibility modifiers.
    #
    # The range doesn't have to denote a node range in the sense of an abstract
    # syntax tree. It can therefore not be used to re-construct a hierarchy of
    # the symbols.
    'location': 'Location',
    # The name of this symbol.
    'name': str,
    # The kind of this symbol.
    'kind': 'SymbolKind',
    # Tags for this symbol.
    #
    # @since 3.16.0
    'tags': NotRequired[List['SymbolTag']],
    # The name of the symbol containing this symbol. This information is for
    # user interface purposes (e.g. to render a qualifier in the user interface
    # if necessary). It can't be used to re-infer a hierarchy for the document
    # symbols.
    'containerName': NotRequired[str],
})
""" Represents information about programming constructs like variables, classes,
interfaces etc. """


DocumentSymbol = TypedDict('DocumentSymbol', {
    # The name of this symbol. Will be displayed in the user interface and therefore must not be
    # an empty string or a string only consisting of white spaces.
    'name': str,
    # More detail for this symbol, e.g the signature of a function.
    'detail': NotRequired[str],
    # The kind of this symbol.
    'kind': 'SymbolKind',
    # Tags for this document symbol.
    #
    # @since 3.16.0
    'tags': NotRequired[List['SymbolTag']],
    # Indicates if this symbol is deprecated.
    #
    # @deprecated Use tags instead
    'deprecated': NotRequired[bool],
    # The range enclosing this symbol not including leading/trailing whitespace but everything else
    # like comments. This information is typically used to determine if the clients cursor is
    # inside the symbol to reveal in the symbol in the UI.
    'range': 'Range',
    # The range that should be selected and revealed when this symbol is being picked, e.g the name of a function.
    # Must be contained by the `range`.
    'selectionRange': 'Range',
    # Children of this symbol, e.g. properties of a class.
    'children': NotRequired[List['DocumentSymbol']],
})
""" Represents programming constructs like variables, classes, interfaces etc.
that appear in a document. Document symbols can be hierarchical and they
have two ranges: one that encloses its definition and one that points to
its most interesting range, e.g. the range of an identifier. """


DocumentSymbolRegistrationOptions = TypedDict('DocumentSymbolRegistrationOptions', {
    # A document selector to identify the scope of the registration. If set to null
    # the document selector provided on the client side will be used.
    'documentSelector': Union['DocumentSelector', None],
    # A human-readable string that is shown when multiple outlines trees
    # are shown for the same document.
    #
    # @since 3.16.0
    'label': NotRequired[str],
})
""" Registration options for a {@link DocumentSymbolRequest}. """


CodeActionParams = TypedDict('CodeActionParams', {
    # The document in which the command was invoked.
    'textDocument': 'TextDocumentIdentifier',
    # The range for which the command was invoked.
    'range': 'Range',
    # Context carrying additional information.
    'context': 'CodeActionContext',
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
    # An optional token that a server can use to report partial results (e.g. streaming) to
    # the client.
    'partialResultToken': NotRequired['ProgressToken'],
})
""" The parameters of a {@link CodeActionRequest}. """


Command = TypedDict('Command', {
    # Title of the command, like `save`.
    'title': str,
    # An optional tooltip.
    #
    # @since 3.18.0
    # @proposed
    'tooltip': NotRequired[str],
    # The identifier of the actual command handler.
    'command': str,
    # Arguments that the command handler should be
    # invoked with.
    'arguments': NotRequired[List['LSPAny']],
})
""" Represents a reference to a command. Provides a title which
will be used to represent a command in the UI and, optionally,
an array of arguments which will be passed to the command handler
function when invoked. """


CodeAction = TypedDict('CodeAction', {
    # A short, human-readable, title for this code action.
    'title': str,
    # The kind of the code action.
    #
    # Used to filter code actions.
    'kind': NotRequired['CodeActionKind'],
    # The diagnostics that this code action resolves.
    'diagnostics': NotRequired[List['Diagnostic']],
    # Marks this as a preferred action. Preferred actions are used by the `auto fix` command and can be targeted
    # by keybindings.
    #
    # A quick fix should be marked preferred if it properly addresses the underlying error.
    # A refactoring should be marked preferred if it is the most reasonable choice of actions to take.
    #
    # @since 3.15.0
    'isPreferred': NotRequired[bool],
    # Marks that the code action cannot currently be applied.
    #
    # Clients should follow the following guidelines regarding disabled code actions:
    #
    #   - Disabled code actions are not shown in automatic [lightbulbs](https://code.visualstudio.com/docs/editor/editingevolved#_code-action)
    #     code action menus.
    #
    #   - Disabled actions are shown as faded out in the code action menu when the user requests a more specific type
    #     of code action, such as refactorings.
    #
    #   - If the user has a [keybinding](https://code.visualstudio.com/docs/editor/refactoring#_keybindings-for-code-actions)
    #     that auto applies a code action and only disabled code actions are returned, the client should show the user an
    #     error message with `reason` in the editor.
    #
    # @since 3.16.0
    'disabled': NotRequired['CodeActionDisabled'],
    # The workspace edit this code action performs.
    'edit': NotRequired['WorkspaceEdit'],
    # A command this code action executes. If a code action
    # provides an edit and a command, first the edit is
    # executed and then the command.
    'command': NotRequired['Command'],
    # A data entry field that is preserved on a code action between
    # a `textDocument/codeAction` and a `codeAction/resolve` request.
    #
    # @since 3.16.0
    'data': NotRequired['LSPAny'],
    # Tags for this code action.
    #
    # @since 3.18.0 - proposed
    'tags': NotRequired[List['CodeActionTag']],
})
""" A code action represents a change that can be performed in code, e.g. to fix a problem or
to refactor code.

A CodeAction must set either `edit` and/or a `command`. If both are supplied, the `edit` is applied first, then the `command` is executed. """


CodeActionRegistrationOptions = TypedDict('CodeActionRegistrationOptions', {
    # A document selector to identify the scope of the registration. If set to null
    # the document selector provided on the client side will be used.
    'documentSelector': Union['DocumentSelector', None],
    # CodeActionKinds that this server may return.
    #
    # The list of kinds may be generic, such as `CodeActionKind.Refactor`, or the server
    # may list out every specific kind they provide.
    'codeActionKinds': NotRequired[List['CodeActionKind']],
    # Static documentation for a class of code actions.
    #
    # Documentation from the provider should be shown in the code actions menu if either:
    #
    # - Code actions of `kind` are requested by the editor. In this case, the editor will show the documentation that
    #   most closely matches the requested code action kind. For example, if a provider has documentation for
    #   both `Refactor` and `RefactorExtract`, when the user requests code actions for `RefactorExtract`,
    #   the editor will use the documentation for `RefactorExtract` instead of the documentation for `Refactor`.
    #
    # - Any code actions of `kind` are returned by the provider.
    #
    # At most one documentation entry should be shown per provider.
    #
    # @since 3.18.0
    # @proposed
    'documentation': NotRequired[List['CodeActionKindDocumentation']],
    # The server provides support to resolve additional
    # information for a code action.
    #
    # @since 3.16.0
    'resolveProvider': NotRequired[bool],
})
""" Registration options for a {@link CodeActionRequest}. """


WorkspaceSymbolParams = TypedDict('WorkspaceSymbolParams', {
    # A query string to filter symbols by. Clients may send an empty
    # string here to request all symbols.
    #
    # The `query`-parameter should be interpreted in a *relaxed way* as editors
    # will apply their own highlighting and scoring on the results. A good rule
    # of thumb is to match case-insensitive and to simply check that the
    # characters of *query* appear in their order in a candidate symbol.
    # Servers shouldn't use prefix, substring, or similar strict matching.
    'query': str,
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
    # An optional token that a server can use to report partial results (e.g. streaming) to
    # the client.
    'partialResultToken': NotRequired['ProgressToken'],
})
""" The parameters of a {@link WorkspaceSymbolRequest}. """


WorkspaceSymbol = TypedDict('WorkspaceSymbol', {
    # The location of the symbol. Whether a server is allowed to
    # return a location without a range depends on the client
    # capability `workspace.symbol.resolveSupport`.
    #
    # See SymbolInformation#location for more details.
    'location': Union['Location', 'LocationUriOnly'],
    # A data entry field that is preserved on a workspace symbol between a
    # workspace symbol request and a workspace symbol resolve request.
    'data': NotRequired['LSPAny'],
    # The name of this symbol.
    'name': str,
    # The kind of this symbol.
    'kind': 'SymbolKind',
    # Tags for this symbol.
    #
    # @since 3.16.0
    'tags': NotRequired[List['SymbolTag']],
    # The name of the symbol containing this symbol. This information is for
    # user interface purposes (e.g. to render a qualifier in the user interface
    # if necessary). It can't be used to re-infer a hierarchy for the document
    # symbols.
    'containerName': NotRequired[str],
})
""" A special workspace symbol that supports locations without a range.

See also SymbolInformation.

@since 3.17.0 """


WorkspaceSymbolRegistrationOptions = TypedDict('WorkspaceSymbolRegistrationOptions', {
    # The server provides support to resolve additional
    # information for a workspace symbol.
    #
    # @since 3.17.0
    'resolveProvider': NotRequired[bool],
})
""" Registration options for a {@link WorkspaceSymbolRequest}. """


CodeLensParams = TypedDict('CodeLensParams', {
    # The document to request code lens for.
    'textDocument': 'TextDocumentIdentifier',
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
    # An optional token that a server can use to report partial results (e.g. streaming) to
    # the client.
    'partialResultToken': NotRequired['ProgressToken'],
})
""" The parameters of a {@link CodeLensRequest}. """


CodeLens = TypedDict('CodeLens', {
    # The range in which this code lens is valid. Should only span a single line.
    'range': 'Range',
    # The command this code lens represents.
    'command': NotRequired['Command'],
    # A data entry field that is preserved on a code lens item between
    # a {@link CodeLensRequest} and a {@link CodeLensResolveRequest}
    'data': NotRequired['LSPAny'],
})
""" A code lens represents a {@link Command command} that should be shown along with
source text, like the number of references, a way to run tests, etc.

A code lens is _unresolved_ when no command is associated to it. For performance
reasons the creation of a code lens and resolving should be done in two stages. """


CodeLensRegistrationOptions = TypedDict('CodeLensRegistrationOptions', {
    # A document selector to identify the scope of the registration. If set to null
    # the document selector provided on the client side will be used.
    'documentSelector': Union['DocumentSelector', None],
    # Code lens has a resolve provider as well.
    'resolveProvider': NotRequired[bool],
})
""" Registration options for a {@link CodeLensRequest}. """


DocumentLinkParams = TypedDict('DocumentLinkParams', {
    # The document to provide document links for.
    'textDocument': 'TextDocumentIdentifier',
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
    # An optional token that a server can use to report partial results (e.g. streaming) to
    # the client.
    'partialResultToken': NotRequired['ProgressToken'],
})
""" The parameters of a {@link DocumentLinkRequest}. """


DocumentLink = TypedDict('DocumentLink', {
    # The range this link applies to.
    'range': 'Range',
    # The uri this link points to. If missing a resolve request is sent later.
    'target': NotRequired['URI'],
    # The tooltip text when you hover over this link.
    #
    # If a tooltip is provided, is will be displayed in a string that includes instructions on how to
    # trigger the link, such as `{0} (ctrl + click)`. The specific instructions vary depending on OS,
    # user settings, and localization.
    #
    # @since 3.15.0
    'tooltip': NotRequired[str],
    # A data entry field that is preserved on a document link between a
    # DocumentLinkRequest and a DocumentLinkResolveRequest.
    'data': NotRequired['LSPAny'],
})
""" A document link is a range in a text document that links to an internal or external resource, like another
text document or a web site. """


DocumentLinkRegistrationOptions = TypedDict('DocumentLinkRegistrationOptions', {
    # A document selector to identify the scope of the registration. If set to null
    # the document selector provided on the client side will be used.
    'documentSelector': Union['DocumentSelector', None],
    # Document links have a resolve provider as well.
    'resolveProvider': NotRequired[bool],
})
""" Registration options for a {@link DocumentLinkRequest}. """


DocumentFormattingParams = TypedDict('DocumentFormattingParams', {
    # The document to format.
    'textDocument': 'TextDocumentIdentifier',
    # The format options.
    'options': 'FormattingOptions',
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
})
""" The parameters of a {@link DocumentFormattingRequest}. """


DocumentFormattingRegistrationOptions = TypedDict('DocumentFormattingRegistrationOptions', {
    # A document selector to identify the scope of the registration. If set to null
    # the document selector provided on the client side will be used.
    'documentSelector': Union['DocumentSelector', None],
})
""" Registration options for a {@link DocumentFormattingRequest}. """


DocumentRangeFormattingParams = TypedDict('DocumentRangeFormattingParams', {
    # The document to format.
    'textDocument': 'TextDocumentIdentifier',
    # The range to format
    'range': 'Range',
    # The format options
    'options': 'FormattingOptions',
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
})
""" The parameters of a {@link DocumentRangeFormattingRequest}. """


DocumentRangeFormattingRegistrationOptions = TypedDict('DocumentRangeFormattingRegistrationOptions', {
    # A document selector to identify the scope of the registration. If set to null
    # the document selector provided on the client side will be used.
    'documentSelector': Union['DocumentSelector', None],
    # Whether the server supports formatting multiple ranges at once.
    #
    # @since 3.18.0
    # @proposed
    'rangesSupport': NotRequired[bool],
})
""" Registration options for a {@link DocumentRangeFormattingRequest}. """


DocumentRangesFormattingParams = TypedDict('DocumentRangesFormattingParams', {
    # The document to format.
    'textDocument': 'TextDocumentIdentifier',
    # The ranges to format
    'ranges': List['Range'],
    # The format options
    'options': 'FormattingOptions',
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
})
""" The parameters of a {@link DocumentRangesFormattingRequest}.

@since 3.18.0
@proposed """


DocumentOnTypeFormattingParams = TypedDict('DocumentOnTypeFormattingParams', {
    # The document to format.
    'textDocument': 'TextDocumentIdentifier',
    # The position around which the on type formatting should happen.
    # This is not necessarily the exact position where the character denoted
    # by the property `ch` got typed.
    'position': 'Position',
    # The character that has been typed that triggered the formatting
    # on type request. That is not necessarily the last character that
    # got inserted into the document since the client could auto insert
    # characters as well (e.g. like automatic brace completion).
    'ch': str,
    # The formatting options.
    'options': 'FormattingOptions',
})
""" The parameters of a {@link DocumentOnTypeFormattingRequest}. """


DocumentOnTypeFormattingRegistrationOptions = TypedDict('DocumentOnTypeFormattingRegistrationOptions', {
    # A document selector to identify the scope of the registration. If set to null
    # the document selector provided on the client side will be used.
    'documentSelector': Union['DocumentSelector', None],
    # A character on which formatting should be triggered, like `{`.
    'firstTriggerCharacter': str,
    # More trigger characters.
    'moreTriggerCharacter': NotRequired[List[str]],
})
""" Registration options for a {@link DocumentOnTypeFormattingRequest}. """


RenameParams = TypedDict('RenameParams', {
    # The document to rename.
    'textDocument': 'TextDocumentIdentifier',
    # The position at which this request was sent.
    'position': 'Position',
    # The new name of the symbol. If the given name is not valid the
    # request must return a {@link ResponseError} with an
    # appropriate message set.
    'newName': str,
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
})
""" The parameters of a {@link RenameRequest}. """


RenameRegistrationOptions = TypedDict('RenameRegistrationOptions', {
    # A document selector to identify the scope of the registration. If set to null
    # the document selector provided on the client side will be used.
    'documentSelector': Union['DocumentSelector', None],
    # Renames should be checked and tested before being executed.
    #
    # @since version 3.12.0
    'prepareProvider': NotRequired[bool],
})
""" Registration options for a {@link RenameRequest}. """


PrepareRenameParams = TypedDict('PrepareRenameParams', {
    # The text document.
    'textDocument': 'TextDocumentIdentifier',
    # The position inside the text document.
    'position': 'Position',
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
})


ExecuteCommandParams = TypedDict('ExecuteCommandParams', {
    # The identifier of the actual command handler.
    'command': str,
    # Arguments that the command should be invoked with.
    'arguments': NotRequired[List['LSPAny']],
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
})
""" The parameters of a {@link ExecuteCommandRequest}. """


ExecuteCommandRegistrationOptions = TypedDict('ExecuteCommandRegistrationOptions', {
    # The commands to be executed on the server
    'commands': List[str],
})
""" Registration options for a {@link ExecuteCommandRequest}. """


ApplyWorkspaceEditParams = TypedDict('ApplyWorkspaceEditParams', {
    # An optional label of the workspace edit. This label is
    # presented in the user interface for example on an undo
    # stack to undo the workspace edit.
    'label': NotRequired[str],
    # The edits to apply.
    'edit': 'WorkspaceEdit',
    # Additional data about the edit.
    #
    # @since 3.18.0
    # @proposed
    'metadata': NotRequired['WorkspaceEditMetadata'],
})
""" The parameters passed via an apply workspace edit request. """


ApplyWorkspaceEditResult = TypedDict('ApplyWorkspaceEditResult', {
    # Indicates whether the edit was applied or not.
    'applied': bool,
    # An optional textual description for why the edit was not applied.
    # This may be used by the server for diagnostic logging or to provide
    # a suitable error for a request that triggered the edit.
    'failureReason': NotRequired[str],
    # Depending on the client's failure handling strategy `failedChange` might
    # contain the index of the change that failed. This property is only available
    # if the client signals a `failureHandlingStrategy` in its client capabilities.
    'failedChange': NotRequired[Uint],
})
""" The result returned from the apply workspace edit request.

@since 3.17 renamed from ApplyWorkspaceEditResponse """


WorkDoneProgressBegin = TypedDict('WorkDoneProgressBegin', {
    'kind': Literal['begin'],
    # Mandatory title of the progress operation. Used to briefly inform about
    # the kind of operation being performed.
    #
    # Examples: "Indexing" or "Linking dependencies".
    'title': str,
    # Controls if a cancel button should show to allow the user to cancel the
    # long running operation. Clients that don't support cancellation are allowed
    # to ignore the setting.
    'cancellable': NotRequired[bool],
    # Optional, more detailed associated progress message. Contains
    # complementary information to the `title`.
    #
    # Examples: "3/25 files", "project/src/module2", "node_modules/some_dep".
    # If unset, the previous progress message (if any) is still valid.
    'message': NotRequired[str],
    # Optional progress percentage to display (value 100 is considered 100%).
    # If not provided infinite progress is assumed and clients are allowed
    # to ignore the `percentage` value in subsequent in report notifications.
    #
    # The value should be steadily rising. Clients are free to ignore values
    # that are not following this rule. The value range is [0, 100].
    'percentage': NotRequired[Uint],
})


WorkDoneProgressReport = TypedDict('WorkDoneProgressReport', {
    'kind': Literal['report'],
    # Controls enablement state of a cancel button.
    #
    # Clients that don't support cancellation or don't support controlling the button's
    # enablement state are allowed to ignore the property.
    'cancellable': NotRequired[bool],
    # Optional, more detailed associated progress message. Contains
    # complementary information to the `title`.
    #
    # Examples: "3/25 files", "project/src/module2", "node_modules/some_dep".
    # If unset, the previous progress message (if any) is still valid.
    'message': NotRequired[str],
    # Optional progress percentage to display (value 100 is considered 100%).
    # If not provided infinite progress is assumed and clients are allowed
    # to ignore the `percentage` value in subsequent in report notifications.
    #
    # The value should be steadily rising. Clients are free to ignore values
    # that are not following this rule. The value range is [0, 100]
    'percentage': NotRequired[Uint],
})


WorkDoneProgressEnd = TypedDict('WorkDoneProgressEnd', {
    'kind': Literal['end'],
    # Optional, a final message indicating to for example indicate the outcome
    # of the operation.
    'message': NotRequired[str],
})


SetTraceParams = TypedDict('SetTraceParams', {
    'value': 'TraceValue',
})


LogTraceParams = TypedDict('LogTraceParams', {
    'message': str,
    'verbose': NotRequired[str],
})


CancelParams = TypedDict('CancelParams', {
    # The request id to cancel.
    'id': Union[int, str],
})


ProgressParams = TypedDict('ProgressParams', {
    # The progress token provided by the client or server.
    'token': 'ProgressToken',
    # The progress data.
    'value': 'LSPAny',
})


TextDocumentPositionParams = TypedDict('TextDocumentPositionParams', {
    # The text document.
    'textDocument': 'TextDocumentIdentifier',
    # The position inside the text document.
    'position': 'Position',
})
""" A parameter literal used in requests to pass a text document and a position inside that
document. """


WorkDoneProgressParams = TypedDict('WorkDoneProgressParams', {
    # An optional token that a server can use to report work done progress.
    'workDoneToken': NotRequired['ProgressToken'],
})


PartialResultParams = TypedDict('PartialResultParams', {
    # An optional token that a server can use to report partial results (e.g. streaming) to
    # the client.
    'partialResultToken': NotRequired['ProgressToken'],
})


LocationLink = TypedDict('LocationLink', {
    # Span of the origin of this link.
    #
    # Used as the underlined span for mouse interaction. Defaults to the word range at
    # the definition position.
    'originSelectionRange': NotRequired['Range'],
    # The target resource identifier of this link.
    'targetUri': 'DocumentUri',
    # The full target range of this link. If the target for example is a symbol then target range is the
    # range enclosing this symbol not including leading/trailing whitespace but everything else
    # like comments. This information is typically used to highlight the range in the editor.
    'targetRange': 'Range',
    # The range that should be selected and revealed when this link is being followed, e.g the name of a function.
    # Must be contained by the `targetRange`. See also `DocumentSymbol#range`
    'targetSelectionRange': 'Range',
})
""" Represents the connection of two locations. Provides additional metadata over normal {@link Location locations},
including an origin range. """


Range = TypedDict('Range', {
    # The range's start position.
    'start': 'Position',
    # The range's end position.
    'end': 'Position',
})
""" A range in a text document expressed as (zero-based) start and end positions.

If you want to specify a range that contains a line including the line ending
character(s) then use an end position denoting the start of the next line.
For example:
```ts
{
    start: { line: 5, character: 23 }
    end : { line 6, character : 0 }
}
``` """


ImplementationOptions = TypedDict('ImplementationOptions', {
    'workDoneProgress': NotRequired[bool],
})


StaticRegistrationOptions = TypedDict('StaticRegistrationOptions', {
    # The id used to register the request. The id can be used to deregister
    # the request again. See also Registration#id.
    'id': NotRequired[str],
})
""" Static registration options to be returned in the initialize
request. """


TypeDefinitionOptions = TypedDict('TypeDefinitionOptions', {
    'workDoneProgress': NotRequired[bool],
})


WorkspaceFoldersChangeEvent = TypedDict('WorkspaceFoldersChangeEvent', {
    # The array of added workspace folders
    'added': List['WorkspaceFolder'],
    # The array of the removed workspace folders
    'removed': List['WorkspaceFolder'],
})
""" The workspace folder change event. """


ConfigurationItem = TypedDict('ConfigurationItem', {
    # The scope to get the configuration section for.
    'scopeUri': NotRequired['URI'],
    # The configuration section asked for.
    'section': NotRequired[str],
})


TextDocumentIdentifier = TypedDict('TextDocumentIdentifier', {
    # The text document's uri.
    'uri': 'DocumentUri',
})
""" A literal to identify a text document in the client. """


Color = TypedDict('Color', {
    # The red component of this color in the range [0-1].
    'red': float,
    # The green component of this color in the range [0-1].
    'green': float,
    # The blue component of this color in the range [0-1].
    'blue': float,
    # The alpha component of this color in the range [0-1].
    'alpha': float,
})
""" Represents a color in RGBA space. """


DocumentColorOptions = TypedDict('DocumentColorOptions', {
    'workDoneProgress': NotRequired[bool],
})


FoldingRangeOptions = TypedDict('FoldingRangeOptions', {
    'workDoneProgress': NotRequired[bool],
})


DeclarationOptions = TypedDict('DeclarationOptions', {
    'workDoneProgress': NotRequired[bool],
})


Position = TypedDict('Position', {
    # Line position in a document (zero-based).
    'line': Uint,
    # Character offset on a line in a document (zero-based).
    #
    # The meaning of this offset is determined by the negotiated
    # `PositionEncodingKind`.
    'character': Uint,
})
""" Position in a text document expressed as zero-based line and character
offset. Prior to 3.17 the offsets were always based on a UTF-16 string
representation. So a string of the form `a𐐀b` the character offset of the
character `a` is 0, the character offset of `𐐀` is 1 and the character
offset of b is 3 since `𐐀` is represented using two code units in UTF-16.
Since 3.17 clients and servers can agree on a different string encoding
representation (e.g. UTF-8). The client announces it's supported encoding
via the client capability [`general.positionEncodings`](https://microsoft.github.io/language-server-protocol/specifications/specification-current/#clientCapabilities).
The value is an array of position encodings the client supports, with
decreasing preference (e.g. the encoding at index `0` is the most preferred
one). To stay backwards compatible the only mandatory encoding is UTF-16
represented via the string `utf-16`. The server can pick one of the
encodings offered by the client and signals that encoding back to the
client via the initialize result's property
[`capabilities.positionEncoding`](https://microsoft.github.io/language-server-protocol/specifications/specification-current/#serverCapabilities). If the string value
`utf-16` is missing from the client's capability `general.positionEncodings`
servers can safely assume that the client supports UTF-16. If the server
omits the position encoding in its initialize result the encoding defaults
to the string value `utf-16`. Implementation considerations: since the
conversion from one encoding into another requires the content of the
file / line the conversion is best done where the file is read which is
usually on the server side.

Positions are line end character agnostic. So you can not specify a position
that denotes `\r|\n` or `\n|` where `|` represents the character offset.

@since 3.17.0 - support for negotiated position encoding. """


SelectionRangeOptions = TypedDict('SelectionRangeOptions', {
    'workDoneProgress': NotRequired[bool],
})


CallHierarchyOptions = TypedDict('CallHierarchyOptions', {
    'workDoneProgress': NotRequired[bool],
})
""" Call hierarchy options used during static registration.

@since 3.16.0 """


SemanticTokensOptions = TypedDict('SemanticTokensOptions', {
    # The legend used by the server
    'legend': 'SemanticTokensLegend',
    # Server supports providing semantic tokens for a specific range
    # of a document.
    'range': NotRequired[Union[bool, dict]],
    # Server supports providing semantic tokens for a full document.
    'full': NotRequired[Union[bool, 'SemanticTokensFullDelta']],
    'workDoneProgress': NotRequired[bool],
})
""" @since 3.16.0 """


SemanticTokensEdit = TypedDict('SemanticTokensEdit', {
    # The start offset of the edit.
    'start': Uint,
    # The count of elements to remove.
    'deleteCount': Uint,
    # The elements to insert.
    'data': NotRequired[List[Uint]],
})
""" @since 3.16.0 """


LinkedEditingRangeOptions = TypedDict('LinkedEditingRangeOptions', {
    'workDoneProgress': NotRequired[bool],
})


FileCreate = TypedDict('FileCreate', {
    # A file:// URI for the location of the file/folder being created.
    'uri': str,
})
""" Represents information on a file/folder create.

@since 3.16.0 """


TextDocumentEdit = TypedDict('TextDocumentEdit', {
    # The text document to change.
    'textDocument': 'OptionalVersionedTextDocumentIdentifier',
    # The edits to be applied.
    #
    # @since 3.16.0 - support for AnnotatedTextEdit. This is guarded using a
    # client capability.
    #
    # @since 3.18.0 - support for SnippetTextEdit. This is guarded using a
    # client capability.
    'edits': List[Union['TextEdit', 'AnnotatedTextEdit', 'SnippetTextEdit']],
})
""" Describes textual changes on a text document. A TextDocumentEdit describes all changes
on a document version Si and after they are applied move the document to version Si+1.
So the creator of a TextDocumentEdit doesn't need to sort the array of edits or do any
kind of ordering. However the edits must be non overlapping. """


CreateFile = TypedDict('CreateFile', {
    # A create
    'kind': Literal['create'],
    # The resource to create.
    'uri': 'DocumentUri',
    # Additional options
    'options': NotRequired['CreateFileOptions'],
    # An optional annotation identifier describing the operation.
    #
    # @since 3.16.0
    'annotationId': NotRequired['ChangeAnnotationIdentifier'],
})
""" Create file operation. """


RenameFile = TypedDict('RenameFile', {
    # A rename
    'kind': Literal['rename'],
    # The old (existing) location.
    'oldUri': 'DocumentUri',
    # The new location.
    'newUri': 'DocumentUri',
    # Rename options.
    'options': NotRequired['RenameFileOptions'],
    # An optional annotation identifier describing the operation.
    #
    # @since 3.16.0
    'annotationId': NotRequired['ChangeAnnotationIdentifier'],
})
""" Rename file operation """


DeleteFile = TypedDict('DeleteFile', {
    # A delete
    'kind': Literal['delete'],
    # The file to delete.
    'uri': 'DocumentUri',
    # Delete options.
    'options': NotRequired['DeleteFileOptions'],
    # An optional annotation identifier describing the operation.
    #
    # @since 3.16.0
    'annotationId': NotRequired['ChangeAnnotationIdentifier'],
})
""" Delete file operation """


ChangeAnnotation = TypedDict('ChangeAnnotation', {
    # A human-readable string describing the actual change. The string
    # is rendered prominent in the user interface.
    'label': str,
    # A flag which indicates that user confirmation is needed
    # before applying the change.
    'needsConfirmation': NotRequired[bool],
    # A human-readable string which is rendered less prominent in
    # the user interface.
    'description': NotRequired[str],
})
""" Additional information that describes document changes.

@since 3.16.0 """


FileOperationFilter = TypedDict('FileOperationFilter', {
    # A Uri scheme like `file` or `untitled`.
    'scheme': NotRequired[str],
    # The actual file operation pattern.
    'pattern': 'FileOperationPattern',
})
""" A filter to describe in which file operation requests or notifications
the server is interested in receiving.

@since 3.16.0 """


FileRename = TypedDict('FileRename', {
    # A file:// URI for the original location of the file/folder being renamed.
    'oldUri': str,
    # A file:// URI for the new location of the file/folder being renamed.
    'newUri': str,
})
""" Represents information on a file/folder rename.

@since 3.16.0 """


FileDelete = TypedDict('FileDelete', {
    # A file:// URI for the location of the file/folder being deleted.
    'uri': str,
})
""" Represents information on a file/folder delete.

@since 3.16.0 """


MonikerOptions = TypedDict('MonikerOptions', {
    'workDoneProgress': NotRequired[bool],
})


TypeHierarchyOptions = TypedDict('TypeHierarchyOptions', {
    'workDoneProgress': NotRequired[bool],
})
""" Type hierarchy options used during static registration.

@since 3.17.0 """


InlineValueContext = TypedDict('InlineValueContext', {
    # The stack frame (as a DAP Id) where the execution has stopped.
    'frameId': int,
    # The document range where execution has stopped.
    # Typically the end position of the range denotes the line where the inline values are shown.
    'stoppedLocation': 'Range',
})
""" @since 3.17.0 """


InlineValueText = TypedDict('InlineValueText', {
    # The document range for which the inline value applies.
    'range': 'Range',
    # The text of the inline value.
    'text': str,
})
""" Provide inline value as text.

@since 3.17.0 """


InlineValueVariableLookup = TypedDict('InlineValueVariableLookup', {
    # The document range for which the inline value applies.
    # The range is used to extract the variable name from the underlying document.
    'range': 'Range',
    # If specified the name of the variable to look up.
    'variableName': NotRequired[str],
    # How to perform the lookup.
    'caseSensitiveLookup': bool,
})
""" Provide inline value through a variable lookup.
If only a range is specified, the variable name will be extracted from the underlying document.
An optional variable name can be used to override the extracted name.

@since 3.17.0 """


InlineValueEvaluatableExpression = TypedDict('InlineValueEvaluatableExpression', {
    # The document range for which the inline value applies.
    # The range is used to extract the evaluatable expression from the underlying document.
    'range': 'Range',
    # If specified the expression overrides the extracted expression.
    'expression': NotRequired[str],
})
""" Provide an inline value through an expression evaluation.
If only a range is specified, the expression will be extracted from the underlying document.
An optional expression can be used to override the extracted expression.

@since 3.17.0 """


InlineValueOptions = TypedDict('InlineValueOptions', {
    'workDoneProgress': NotRequired[bool],
})
""" Inline value options used during static registration.

@since 3.17.0 """


InlayHintLabelPart = TypedDict('InlayHintLabelPart', {
    # The value of this label part.
    'value': str,
    # The tooltip text when you hover over this label part. Depending on
    # the client capability `inlayHint.resolveSupport` clients might resolve
    # this property late using the resolve request.
    'tooltip': NotRequired[Union[str, 'MarkupContent']],
    # An optional source code location that represents this
    # label part.
    #
    # The editor will use this location for the hover and for code navigation
    # features: This part will become a clickable link that resolves to the
    # definition of the symbol at the given location (not necessarily the
    # location itself), it shows the hover that shows at the given location,
    # and it shows a context menu with further code navigation commands.
    #
    # Depending on the client capability `inlayHint.resolveSupport` clients
    # might resolve this property late using the resolve request.
    'location': NotRequired['Location'],
    # An optional command for this label part.
    #
    # Depending on the client capability `inlayHint.resolveSupport` clients
    # might resolve this property late using the resolve request.
    'command': NotRequired['Command'],
})
""" An inlay hint label part allows for interactive and composite labels
of inlay hints.

@since 3.17.0 """


MarkupContent = TypedDict('MarkupContent', {
    # The type of the Markup
    'kind': 'MarkupKind',
    # The content itself
    'value': str,
})
""" A `MarkupContent` literal represents a string value which content is interpreted base on its
kind flag. Currently the protocol supports `plaintext` and `markdown` as markup kinds.

If the kind is `markdown` then the value can contain fenced code blocks like in GitHub issues.
See https://help.github.com/articles/creating-and-highlighting-code-blocks/#syntax-highlighting

Here is an example how such a string can be constructed using JavaScript / TypeScript:
```ts
let markdown: MarkdownContent = {
 kind: MarkupKind.Markdown,
 value: [
   '# Header',
   'Some text',
   '```typescript',
   'someCode();',
   '```'
 ].join('\n')
};
```

*Please Note* that clients might sanitize the return markdown. A client could decide to
remove HTML from the markdown to avoid script execution. """


InlayHintOptions = TypedDict('InlayHintOptions', {
    # The server provides support to resolve additional
    # information for an inlay hint item.
    'resolveProvider': NotRequired[bool],
    'workDoneProgress': NotRequired[bool],
})
""" Inlay hint options used during static registration.

@since 3.17.0 """


RelatedFullDocumentDiagnosticReport = TypedDict('RelatedFullDocumentDiagnosticReport', {
    # Diagnostics of related documents. This information is useful
    # in programming languages where code in a file A can generate
    # diagnostics in a file B which A depends on. An example of
    # such a language is C/C++ where marco definitions in a file
    # a.cpp and result in errors in a header file b.hpp.
    #
    # @since 3.17.0
    'relatedDocuments': NotRequired[Dict['DocumentUri', Union['FullDocumentDiagnosticReport', 'UnchangedDocumentDiagnosticReport']]],
    # A full document diagnostic report.
    'kind': Literal['full'],
    # An optional result id. If provided it will
    # be sent on the next diagnostic request for the
    # same document.
    'resultId': NotRequired[str],
    # The actual items.
    'items': List['Diagnostic'],
})
""" A full diagnostic report with a set of related documents.

@since 3.17.0 """


RelatedUnchangedDocumentDiagnosticReport = TypedDict('RelatedUnchangedDocumentDiagnosticReport', {
    # Diagnostics of related documents. This information is useful
    # in programming languages where code in a file A can generate
    # diagnostics in a file B which A depends on. An example of
    # such a language is C/C++ where marco definitions in a file
    # a.cpp and result in errors in a header file b.hpp.
    #
    # @since 3.17.0
    'relatedDocuments': NotRequired[Dict['DocumentUri', Union['FullDocumentDiagnosticReport', 'UnchangedDocumentDiagnosticReport']]],
    # A document diagnostic report indicating
    # no changes to the last result. A server can
    # only return `unchanged` if result ids are
    # provided.
    'kind': Literal['unchanged'],
    # A result id which will be sent on the next
    # diagnostic request for the same document.
    'resultId': str,
})
""" An unchanged diagnostic report with a set of related documents.

@since 3.17.0 """


FullDocumentDiagnosticReport = TypedDict('FullDocumentDiagnosticReport', {
    # A full document diagnostic report.
    'kind': Literal['full'],
    # An optional result id. If provided it will
    # be sent on the next diagnostic request for the
    # same document.
    'resultId': NotRequired[str],
    # The actual items.
    'items': List['Diagnostic'],
})
""" A diagnostic report with a full set of problems.

@since 3.17.0 """


UnchangedDocumentDiagnosticReport = TypedDict('UnchangedDocumentDiagnosticReport', {
    # A document diagnostic report indicating
    # no changes to the last result. A server can
    # only return `unchanged` if result ids are
    # provided.
    'kind': Literal['unchanged'],
    # A result id which will be sent on the next
    # diagnostic request for the same document.
    'resultId': str,
})
""" A diagnostic report indicating that the last returned
report is still accurate.

@since 3.17.0 """


DiagnosticOptions = TypedDict('DiagnosticOptions', {
    # An optional identifier under which the diagnostics are
    # managed by the client.
    'identifier': NotRequired[str],
    # Whether the language has inter file dependencies meaning that
    # editing code in one file can result in a different diagnostic
    # set in another file. Inter file dependencies are common for
    # most programming languages and typically uncommon for linters.
    'interFileDependencies': bool,
    # The server provides support for workspace diagnostics as well.
    'workspaceDiagnostics': bool,
    'workDoneProgress': NotRequired[bool],
})
""" Diagnostic options.

@since 3.17.0 """


PreviousResultId = TypedDict('PreviousResultId', {
    # The URI for which the client knowns a
    # result id.
    'uri': 'DocumentUri',
    # The value of the previous result id.
    'value': str,
})
""" A previous result id in a workspace pull request.

@since 3.17.0 """


NotebookDocument = TypedDict('NotebookDocument', {
    # The notebook document's uri.
    'uri': 'URI',
    # The type of the notebook.
    'notebookType': str,
    # The version number of this document (it will increase after each
    # change, including undo/redo).
    'version': int,
    # Additional metadata stored with the notebook
    # document.
    #
    # Note: should always be an object literal (e.g. LSPObject)
    'metadata': NotRequired['LSPObject'],
    # The cells of a notebook.
    'cells': List['NotebookCell'],
})
""" A notebook document.

@since 3.17.0 """


TextDocumentItem = TypedDict('TextDocumentItem', {
    # The text document's uri.
    'uri': 'DocumentUri',
    # The text document's language identifier.
    'languageId': 'LanguageKind',
    # The version number of this document (it will increase after each
    # change, including undo/redo).
    'version': int,
    # The content of the opened text document.
    'text': str,
})
""" An item to transfer a text document from the client to the
server. """


NotebookDocumentSyncOptions = TypedDict('NotebookDocumentSyncOptions', {
    # The notebooks to be synced
    'notebookSelector': List[Union['NotebookDocumentFilterWithNotebook', 'NotebookDocumentFilterWithCells']],
    # Whether save notification should be forwarded to
    # the server. Will only be honored if mode === `notebook`.
    'save': NotRequired[bool],
})
""" Options specific to a notebook plus its cells
to be synced to the server.

If a selector provides a notebook document
filter but no cell selector all cells of a
matching notebook document will be synced.

If a selector provides no notebook document
filter but only a cell selector all notebook
document that contain at least one matching
cell will be synced.

@since 3.17.0 """


VersionedNotebookDocumentIdentifier = TypedDict('VersionedNotebookDocumentIdentifier', {
    # The version number of this notebook document.
    'version': int,
    # The notebook document's uri.
    'uri': 'URI',
})
""" A versioned notebook document identifier.

@since 3.17.0 """


NotebookDocumentChangeEvent = TypedDict('NotebookDocumentChangeEvent', {
    # The changed meta data if any.
    #
    # Note: should always be an object literal (e.g. LSPObject)
    'metadata': NotRequired['LSPObject'],
    # Changes to cells
    'cells': NotRequired['NotebookDocumentCellChanges'],
})
""" A change event for a notebook document.

@since 3.17.0 """


NotebookDocumentIdentifier = TypedDict('NotebookDocumentIdentifier', {
    # The notebook document's uri.
    'uri': 'URI',
})
""" A literal to identify a notebook document in the client.

@since 3.17.0 """


InlineCompletionContext = TypedDict('InlineCompletionContext', {
    # Describes how the inline completion was triggered.
    'triggerKind': 'InlineCompletionTriggerKind',
    # Provides information about the currently selected item in the autocomplete widget if it is visible.
    'selectedCompletionInfo': NotRequired['SelectedCompletionInfo'],
})
""" Provides information about the context in which an inline completion was requested.

@since 3.18.0
@proposed """


StringValue = TypedDict('StringValue', {
    # The kind of string value.
    'kind': Literal['snippet'],
    # The snippet string.
    'value': str,
})
""" A string value used as a snippet is a template which allows to insert text
and to control the editor cursor when insertion happens.

A snippet can define tab stops and placeholders with `$1`, `$2`
and `${3:foo}`. `$0` defines the final tab stop, it defaults to
the end of the snippet. Variables are defined with `$name` and
`${name:default value}`.

@since 3.18.0
@proposed """


InlineCompletionOptions = TypedDict('InlineCompletionOptions', {
    'workDoneProgress': NotRequired[bool],
})
""" Inline completion options used during static registration.

@since 3.18.0
@proposed """


TextDocumentContentOptions = TypedDict('TextDocumentContentOptions', {
    # The schemes for which the server provides content.
    'schemes': List[str],
})
""" Text document content provider options.

@since 3.18.0
@proposed """


Registration = TypedDict('Registration', {
    # The id used to register the request. The id can be used to deregister
    # the request again.
    'id': str,
    # The method / capability to register for.
    'method': str,
    # Options necessary for the registration.
    'registerOptions': NotRequired['LSPAny'],
})
""" General parameters to register for a notification or to register a provider. """


Unregistration = TypedDict('Unregistration', {
    # The id used to unregister the request or notification. Usually an id
    # provided during the register request.
    'id': str,
    # The method to unregister for.
    'method': str,
})
""" General parameters to unregister a request or notification. """


WorkspaceFoldersInitializeParams = TypedDict('WorkspaceFoldersInitializeParams', {
    # The workspace folders configured in the client when the server starts.
    #
    # This property is only available if the client supports workspace folders.
    # It can be `null` if the client supports workspace folders but none are
    # configured.
    #
    # @since 3.6.0
    'workspaceFolders': NotRequired[Union[List['WorkspaceFolder'], None]],
})


ServerCapabilities = TypedDict('ServerCapabilities', {
    # The position encoding the server picked from the encodings offered
    # by the client via the client capability `general.positionEncodings`.
    #
    # If the client didn't provide any position encodings the only valid
    # value that a server can return is 'utf-16'.
    #
    # If omitted it defaults to 'utf-16'.
    #
    # @since 3.17.0
    'positionEncoding': NotRequired['PositionEncodingKind'],
    # Defines how text documents are synced. Is either a detailed structure
    # defining each notification or for backwards compatibility the
    # TextDocumentSyncKind number.
    'textDocumentSync': NotRequired[Union['TextDocumentSyncOptions', 'TextDocumentSyncKind']],
    # Defines how notebook documents are synced.
    #
    # @since 3.17.0
    'notebookDocumentSync': NotRequired[Union['NotebookDocumentSyncOptions', 'NotebookDocumentSyncRegistrationOptions']],
    # The server provides completion support.
    'completionProvider': NotRequired['CompletionOptions'],
    # The server provides hover support.
    'hoverProvider': NotRequired[Union[bool, 'HoverOptions']],
    # The server provides signature help support.
    'signatureHelpProvider': NotRequired['SignatureHelpOptions'],
    # The server provides Goto Declaration support.
    'declarationProvider': NotRequired[Union[bool, 'DeclarationOptions', 'DeclarationRegistrationOptions']],
    # The server provides goto definition support.
    'definitionProvider': NotRequired[Union[bool, 'DefinitionOptions']],
    # The server provides Goto Type Definition support.
    'typeDefinitionProvider': NotRequired[Union[bool, 'TypeDefinitionOptions', 'TypeDefinitionRegistrationOptions']],
    # The server provides Goto Implementation support.
    'implementationProvider': NotRequired[Union[bool, 'ImplementationOptions', 'ImplementationRegistrationOptions']],
    # The server provides find references support.
    'referencesProvider': NotRequired[Union[bool, 'ReferenceOptions']],
    # The server provides document highlight support.
    'documentHighlightProvider': NotRequired[Union[bool, 'DocumentHighlightOptions']],
    # The server provides document symbol support.
    'documentSymbolProvider': NotRequired[Union[bool, 'DocumentSymbolOptions']],
    # The server provides code actions. CodeActionOptions may only be
    # specified if the client states that it supports
    # `codeActionLiteralSupport` in its initial `initialize` request.
    'codeActionProvider': NotRequired[Union[bool, 'CodeActionOptions']],
    # The server provides code lens.
    'codeLensProvider': NotRequired['CodeLensOptions'],
    # The server provides document link support.
    'documentLinkProvider': NotRequired['DocumentLinkOptions'],
    # The server provides color provider support.
    'colorProvider': NotRequired[Union[bool, 'DocumentColorOptions', 'DocumentColorRegistrationOptions']],
    # The server provides workspace symbol support.
    'workspaceSymbolProvider': NotRequired[Union[bool, 'WorkspaceSymbolOptions']],
    # The server provides document formatting.
    'documentFormattingProvider': NotRequired[Union[bool, 'DocumentFormattingOptions']],
    # The server provides document range formatting.
    'documentRangeFormattingProvider': NotRequired[Union[bool, 'DocumentRangeFormattingOptions']],
    # The server provides document formatting on typing.
    'documentOnTypeFormattingProvider': NotRequired['DocumentOnTypeFormattingOptions'],
    # The server provides rename support. RenameOptions may only be
    # specified if the client states that it supports
    # `prepareSupport` in its initial `initialize` request.
    'renameProvider': NotRequired[Union[bool, 'RenameOptions']],
    # The server provides folding provider support.
    'foldingRangeProvider': NotRequired[Union[bool, 'FoldingRangeOptions', 'FoldingRangeRegistrationOptions']],
    # The server provides selection range support.
    'selectionRangeProvider': NotRequired[Union[bool, 'SelectionRangeOptions', 'SelectionRangeRegistrationOptions']],
    # The server provides execute command support.
    'executeCommandProvider': NotRequired['ExecuteCommandOptions'],
    # The server provides call hierarchy support.
    #
    # @since 3.16.0
    'callHierarchyProvider': NotRequired[Union[bool, 'CallHierarchyOptions', 'CallHierarchyRegistrationOptions']],
    # The server provides linked editing range support.
    #
    # @since 3.16.0
    'linkedEditingRangeProvider': NotRequired[Union[bool, 'LinkedEditingRangeOptions', 'LinkedEditingRangeRegistrationOptions']],
    # The server provides semantic tokens support.
    #
    # @since 3.16.0
    'semanticTokensProvider': NotRequired[Union['SemanticTokensOptions', 'SemanticTokensRegistrationOptions']],
    # The server provides moniker support.
    #
    # @since 3.16.0
    'monikerProvider': NotRequired[Union[bool, 'MonikerOptions', 'MonikerRegistrationOptions']],
    # The server provides type hierarchy support.
    #
    # @since 3.17.0
    'typeHierarchyProvider': NotRequired[Union[bool, 'TypeHierarchyOptions', 'TypeHierarchyRegistrationOptions']],
    # The server provides inline values.
    #
    # @since 3.17.0
    'inlineValueProvider': NotRequired[Union[bool, 'InlineValueOptions', 'InlineValueRegistrationOptions']],
    # The server provides inlay hints.
    #
    # @since 3.17.0
    'inlayHintProvider': NotRequired[Union[bool, 'InlayHintOptions', 'InlayHintRegistrationOptions']],
    # The server has support for pull model diagnostics.
    #
    # @since 3.17.0
    'diagnosticProvider': NotRequired[Union['DiagnosticOptions', 'DiagnosticRegistrationOptions']],
    # Inline completion options used during static registration.
    #
    # @since 3.18.0
    # @proposed
    'inlineCompletionProvider': NotRequired[Union[bool, 'InlineCompletionOptions']],
    # Workspace specific server capabilities.
    'workspace': NotRequired['WorkspaceOptions'],
    # Experimental server capabilities.
    'experimental': NotRequired['LSPAny'],
})
""" Defines the capabilities provided by a language
server. """


ServerInfo = TypedDict('ServerInfo', {
    # The name of the server as defined by the server.
    'name': str,
    # The server's version as defined by the server.
    'version': NotRequired[str],
})
""" Information about the server

@since 3.15.0
@since 3.18.0 ServerInfo type name added. """


VersionedTextDocumentIdentifier = TypedDict('VersionedTextDocumentIdentifier', {
    # The version number of this document.
    'version': int,
    # The text document's uri.
    'uri': 'DocumentUri',
})
""" A text document identifier to denote a specific version of a text document. """


SaveOptions = TypedDict('SaveOptions', {
    # The client is supposed to include the content on save.
    'includeText': NotRequired[bool],
})
""" Save options. """


FileEvent = TypedDict('FileEvent', {
    # The file's uri.
    'uri': 'DocumentUri',
    # The change type.
    'type': 'FileChangeType',
})
""" An event describing a file change. """


FileSystemWatcher = TypedDict('FileSystemWatcher', {
    # The glob pattern to watch. See {@link GlobPattern glob pattern} for more detail.
    #
    # @since 3.17.0 support for relative patterns.
    'globPattern': 'GlobPattern',
    # The kind of events of interest. If omitted it defaults
    # to WatchKind.Create | WatchKind.Change | WatchKind.Delete
    # which is 7.
    'kind': NotRequired['WatchKind'],
})


Diagnostic = TypedDict('Diagnostic', {
    # The range at which the message applies
    'range': 'Range',
    # The diagnostic's severity. To avoid interpretation mismatches when a
    # server is used with different clients it is highly recommended that servers
    # always provide a severity value.
    'severity': NotRequired['DiagnosticSeverity'],
    # The diagnostic's code, which usually appear in the user interface.
    'code': NotRequired[Union[int, str]],
    # An optional property to describe the error code.
    # Requires the code field (above) to be present/not null.
    #
    # @since 3.16.0
    'codeDescription': NotRequired['CodeDescription'],
    # A human-readable string describing the source of this
    # diagnostic, e.g. 'typescript' or 'super lint'. It usually
    # appears in the user interface.
    'source': NotRequired[str],
    # The diagnostic's message. It usually appears in the user interface
    'message': str,
    # Additional metadata about the diagnostic.
    #
    # @since 3.15.0
    'tags': NotRequired[List['DiagnosticTag']],
    # An array of related diagnostic information, e.g. when symbol-names within
    # a scope collide all definitions can be marked via this property.
    'relatedInformation': NotRequired[List['DiagnosticRelatedInformation']],
    # A data entry field that is preserved between a `textDocument/publishDiagnostics`
    # notification and `textDocument/codeAction` request.
    #
    # @since 3.16.0
    'data': NotRequired['LSPAny'],
})
""" Represents a diagnostic, such as a compiler error or warning. Diagnostic objects
are only valid in the scope of a resource. """


CompletionContext = TypedDict('CompletionContext', {
    # How the completion was triggered.
    'triggerKind': 'CompletionTriggerKind',
    # The trigger character (a single character) that has trigger code complete.
    # Is undefined if `triggerKind !== CompletionTriggerKind.TriggerCharacter`
    'triggerCharacter': NotRequired[str],
})
""" Contains additional information about the context in which a completion request is triggered. """


CompletionItemLabelDetails = TypedDict('CompletionItemLabelDetails', {
    # An optional string which is rendered less prominently directly after {@link CompletionItem.label label},
    # without any spacing. Should be used for function signatures and type annotations.
    'detail': NotRequired[str],
    # An optional string which is rendered less prominently after {@link CompletionItem.detail}. Should be used
    # for fully qualified names and file paths.
    'description': NotRequired[str],
})
""" Additional details for a completion item label.

@since 3.17.0 """


InsertReplaceEdit = TypedDict('InsertReplaceEdit', {
    # The string to be inserted.
    'newText': str,
    # The range if the insert is requested
    'insert': 'Range',
    # The range if the replace is requested.
    'replace': 'Range',
})
""" A special text edit to provide an insert and a replace operation.

@since 3.16.0 """


CompletionItemDefaults = TypedDict('CompletionItemDefaults', {
    # A default commit character set.
    #
    # @since 3.17.0
    'commitCharacters': NotRequired[List[str]],
    # A default edit range.
    #
    # @since 3.17.0
    'editRange': NotRequired[Union['Range', 'EditRangeWithInsertReplace']],
    # A default insert text format.
    #
    # @since 3.17.0
    'insertTextFormat': NotRequired['InsertTextFormat'],
    # A default insert text mode.
    #
    # @since 3.17.0
    'insertTextMode': NotRequired['InsertTextMode'],
    # A default data value.
    #
    # @since 3.17.0
    'data': NotRequired['LSPAny'],
})
""" In many cases the items of an actual completion result share the same
value for properties like `commitCharacters` or the range of a text
edit. A completion list can therefore define item defaults which will
be used if a completion item itself doesn't specify the value.

If a completion list specifies a default value and a completion item
also specifies a corresponding value, the rules for combining these are
defined by `applyKinds` (if the client supports it), defaulting to
ApplyKind.Replace.

Servers are only allowed to return default values if the client
signals support for this via the `completionList.itemDefaults`
capability.

@since 3.17.0 """


CompletionItemApplyKinds = TypedDict('CompletionItemApplyKinds', {
    # Specifies whether commitCharacters on a completion will replace or be
    # merged with those in `completionList.itemDefaults.commitCharacters`.
    #
    # If ApplyKind.Replace, the commit characters from the completion item will
    # always be used unless not provided, in which case those from
    # `completionList.itemDefaults.commitCharacters` will be used. An
    # empty list can be used if a completion item does not have any commit
    # characters and also should not use those from
    # `completionList.itemDefaults.commitCharacters`.
    #
    # If ApplyKind.Merge the commitCharacters for the completion will be the
    # union of all values in both `completionList.itemDefaults.commitCharacters`
    # and the completion's own `commitCharacters`.
    #
    # @since 3.18.0
    'commitCharacters': NotRequired['ApplyKind'],
    # Specifies whether the `data` field on a completion will replace or
    # be merged with data from `completionList.itemDefaults.data`.
    #
    # If ApplyKind.Replace, the data from the completion item will be used if
    # provided (and not `null`), otherwise
    # `completionList.itemDefaults.data` will be used. An empty object can
    # be used if a completion item does not have any data but also should
    # not use the value from `completionList.itemDefaults.data`.
    #
    # If ApplyKind.Merge, a shallow merge will be performed between
    # `completionList.itemDefaults.data` and the completion's own data
    # using the following rules:
    #
    # - If a completion's `data` field is not provided (or `null`), the
    #   entire `data` field from `completionList.itemDefaults.data` will be
    #   used as-is.
    # - If a completion's `data` field is provided, each field will
    #   overwrite the field of the same name in
    #   `completionList.itemDefaults.data` but no merging of nested fields
    #   within that value will occur.
    #
    # @since 3.18.0
    'data': NotRequired['ApplyKind'],
})
""" Specifies how fields from a completion item should be combined with those
from `completionList.itemDefaults`.

If unspecified, all fields will be treated as ApplyKind.Replace.

If a field's value is ApplyKind.Replace, the value from a completion item (if
provided and not `null`) will always be used instead of the value from
`completionItem.itemDefaults`.

If a field's value is ApplyKind.Merge, the values will be merged using the rules
defined against each field below.

Servers are only allowed to return `applyKind` if the client
signals support for this via the `completionList.applyKindSupport`
capability.

@since 3.18.0 """


CompletionOptions = TypedDict('CompletionOptions', {
    # Most tools trigger completion request automatically without explicitly requesting
    # it using a keyboard shortcut (e.g. Ctrl+Space). Typically they do so when the user
    # starts to type an identifier. For example if the user types `c` in a JavaScript file
    # code complete will automatically pop up present `console` besides others as a
    # completion item. Characters that make up identifiers don't need to be listed here.
    #
    # If code complete should automatically be trigger on characters not being valid inside
    # an identifier (for example `.` in JavaScript) list them in `triggerCharacters`.
    'triggerCharacters': NotRequired[List[str]],
    # The list of all possible characters that commit a completion. This field can be used
    # if clients don't support individual commit characters per completion item. See
    # `ClientCapabilities.textDocument.completion.completionItem.commitCharactersSupport`
    #
    # If a server provides both `allCommitCharacters` and commit characters on an individual
    # completion item the ones on the completion item win.
    #
    # @since 3.2.0
    'allCommitCharacters': NotRequired[List[str]],
    # The server provides support to resolve additional
    # information for a completion item.
    'resolveProvider': NotRequired[bool],
    # The server supports the following `CompletionItem` specific
    # capabilities.
    #
    # @since 3.17.0
    'completionItem': NotRequired['ServerCompletionItemOptions'],
    'workDoneProgress': NotRequired[bool],
})
""" Completion options. """


HoverOptions = TypedDict('HoverOptions', {
    'workDoneProgress': NotRequired[bool],
})
""" Hover options. """


SignatureHelpContext = TypedDict('SignatureHelpContext', {
    # Action that caused signature help to be triggered.
    'triggerKind': 'SignatureHelpTriggerKind',
    # Character that caused signature help to be triggered.
    #
    # This is undefined when `triggerKind !== SignatureHelpTriggerKind.TriggerCharacter`
    'triggerCharacter': NotRequired[str],
    # `true` if signature help was already showing when it was triggered.
    #
    # Retriggers occurs when the signature help is already active and can be caused by actions such as
    # typing a trigger character, a cursor move, or document content changes.
    'isRetrigger': bool,
    # The currently active `SignatureHelp`.
    #
    # The `activeSignatureHelp` has its `SignatureHelp.activeSignature` field updated based on
    # the user navigating through available signatures.
    'activeSignatureHelp': NotRequired['SignatureHelp'],
})
""" Additional information about the context in which a signature help request was triggered.

@since 3.15.0 """


SignatureInformation = TypedDict('SignatureInformation', {
    # The label of this signature. Will be shown in
    # the UI.
    'label': str,
    # The human-readable doc-comment of this signature. Will be shown
    # in the UI but can be omitted.
    'documentation': NotRequired[Union[str, 'MarkupContent']],
    # The parameters of this signature.
    'parameters': NotRequired[List['ParameterInformation']],
    # The index of the active parameter.
    #
    # If `null`, no parameter of the signature is active (for example a named
    # argument that does not match any declared parameters). This is only valid
    # if the client specifies the client capability
    # `textDocument.signatureHelp.noActiveParameterSupport === true`
    #
    # If provided (or `null`), this is used in place of
    # `SignatureHelp.activeParameter`.
    #
    # @since 3.16.0
    'activeParameter': NotRequired[Union[Uint, None]],
})
""" Represents the signature of something callable. A signature
can have a label, like a function-name, a doc-comment, and
a set of parameters. """


SignatureHelpOptions = TypedDict('SignatureHelpOptions', {
    # List of characters that trigger signature help automatically.
    'triggerCharacters': NotRequired[List[str]],
    # List of characters that re-trigger signature help.
    #
    # These trigger characters are only active when signature help is already showing. All trigger characters
    # are also counted as re-trigger characters.
    #
    # @since 3.15.0
    'retriggerCharacters': NotRequired[List[str]],
    'workDoneProgress': NotRequired[bool],
})
""" Server Capabilities for a {@link SignatureHelpRequest}. """


DefinitionOptions = TypedDict('DefinitionOptions', {
    'workDoneProgress': NotRequired[bool],
})
""" Server Capabilities for a {@link DefinitionRequest}. """


ReferenceContext = TypedDict('ReferenceContext', {
    # Include the declaration of the current symbol.
    'includeDeclaration': bool,
})
""" Value-object that contains additional information when
requesting references. """


ReferenceOptions = TypedDict('ReferenceOptions', {
    'workDoneProgress': NotRequired[bool],
})
""" Reference options. """


DocumentHighlightOptions = TypedDict('DocumentHighlightOptions', {
    'workDoneProgress': NotRequired[bool],
})
""" Provider options for a {@link DocumentHighlightRequest}. """


BaseSymbolInformation = TypedDict('BaseSymbolInformation', {
    # The name of this symbol.
    'name': str,
    # The kind of this symbol.
    'kind': 'SymbolKind',
    # Tags for this symbol.
    #
    # @since 3.16.0
    'tags': NotRequired[List['SymbolTag']],
    # The name of the symbol containing this symbol. This information is for
    # user interface purposes (e.g. to render a qualifier in the user interface
    # if necessary). It can't be used to re-infer a hierarchy for the document
    # symbols.
    'containerName': NotRequired[str],
})
""" A base for all symbol information. """


DocumentSymbolOptions = TypedDict('DocumentSymbolOptions', {
    # A human-readable string that is shown when multiple outlines trees
    # are shown for the same document.
    #
    # @since 3.16.0
    'label': NotRequired[str],
    'workDoneProgress': NotRequired[bool],
})
""" Provider options for a {@link DocumentSymbolRequest}. """


CodeActionContext = TypedDict('CodeActionContext', {
    # An array of diagnostics known on the client side overlapping the range provided to the
    # `textDocument/codeAction` request. They are provided so that the server knows which
    # errors are currently presented to the user for the given range. There is no guarantee
    # that these accurately reflect the error state of the resource. The primary parameter
    # to compute code actions is the provided range.
    'diagnostics': List['Diagnostic'],
    # Requested kind of actions to return.
    #
    # Actions not of this kind are filtered out by the client before being shown. So servers
    # can omit computing them.
    'only': NotRequired[List['CodeActionKind']],
    # The reason why code actions were requested.
    #
    # @since 3.17.0
    'triggerKind': NotRequired['CodeActionTriggerKind'],
})
""" Contains additional diagnostic information about the context in which
a {@link CodeActionProvider.provideCodeActions code action} is run. """


CodeActionDisabled = TypedDict('CodeActionDisabled', {
    # Human readable description of why the code action is currently disabled.
    #
    # This is displayed in the code actions UI.
    'reason': str,
})
""" Captures why the code action is currently disabled.

@since 3.18.0 """


CodeActionOptions = TypedDict('CodeActionOptions', {
    # CodeActionKinds that this server may return.
    #
    # The list of kinds may be generic, such as `CodeActionKind.Refactor`, or the server
    # may list out every specific kind they provide.
    'codeActionKinds': NotRequired[List['CodeActionKind']],
    # Static documentation for a class of code actions.
    #
    # Documentation from the provider should be shown in the code actions menu if either:
    #
    # - Code actions of `kind` are requested by the editor. In this case, the editor will show the documentation that
    #   most closely matches the requested code action kind. For example, if a provider has documentation for
    #   both `Refactor` and `RefactorExtract`, when the user requests code actions for `RefactorExtract`,
    #   the editor will use the documentation for `RefactorExtract` instead of the documentation for `Refactor`.
    #
    # - Any code actions of `kind` are returned by the provider.
    #
    # At most one documentation entry should be shown per provider.
    #
    # @since 3.18.0
    # @proposed
    'documentation': NotRequired[List['CodeActionKindDocumentation']],
    # The server provides support to resolve additional
    # information for a code action.
    #
    # @since 3.16.0
    'resolveProvider': NotRequired[bool],
    'workDoneProgress': NotRequired[bool],
})
""" Provider options for a {@link CodeActionRequest}. """


LocationUriOnly = TypedDict('LocationUriOnly', {
    'uri': 'DocumentUri',
})
""" Location with only uri and does not include range.

@since 3.18.0 """


WorkspaceSymbolOptions = TypedDict('WorkspaceSymbolOptions', {
    # The server provides support to resolve additional
    # information for a workspace symbol.
    #
    # @since 3.17.0
    'resolveProvider': NotRequired[bool],
    'workDoneProgress': NotRequired[bool],
})
""" Server capabilities for a {@link WorkspaceSymbolRequest}. """


CodeLensOptions = TypedDict('CodeLensOptions', {
    # Code lens has a resolve provider as well.
    'resolveProvider': NotRequired[bool],
    'workDoneProgress': NotRequired[bool],
})
""" Code Lens provider options of a {@link CodeLensRequest}. """


DocumentLinkOptions = TypedDict('DocumentLinkOptions', {
    # Document links have a resolve provider as well.
    'resolveProvider': NotRequired[bool],
    'workDoneProgress': NotRequired[bool],
})
""" Provider options for a {@link DocumentLinkRequest}. """


FormattingOptions = TypedDict('FormattingOptions', {
    # Size of a tab in spaces.
    'tabSize': Uint,
    # Prefer spaces over tabs.
    'insertSpaces': bool,
    # Trim trailing whitespace on a line.
    #
    # @since 3.15.0
    'trimTrailingWhitespace': NotRequired[bool],
    # Insert a newline character at the end of the file if one does not exist.
    #
    # @since 3.15.0
    'insertFinalNewline': NotRequired[bool],
    # Trim all newlines after the final newline at the end of the file.
    #
    # @since 3.15.0
    'trimFinalNewlines': NotRequired[bool],
})
""" Value-object describing what options formatting should use. """


DocumentFormattingOptions = TypedDict('DocumentFormattingOptions', {
    'workDoneProgress': NotRequired[bool],
})
""" Provider options for a {@link DocumentFormattingRequest}. """


DocumentRangeFormattingOptions = TypedDict('DocumentRangeFormattingOptions', {
    # Whether the server supports formatting multiple ranges at once.
    #
    # @since 3.18.0
    # @proposed
    'rangesSupport': NotRequired[bool],
    'workDoneProgress': NotRequired[bool],
})
""" Provider options for a {@link DocumentRangeFormattingRequest}. """


DocumentOnTypeFormattingOptions = TypedDict('DocumentOnTypeFormattingOptions', {
    # A character on which formatting should be triggered, like `{`.
    'firstTriggerCharacter': str,
    # More trigger characters.
    'moreTriggerCharacter': NotRequired[List[str]],
})
""" Provider options for a {@link DocumentOnTypeFormattingRequest}. """


RenameOptions = TypedDict('RenameOptions', {
    # Renames should be checked and tested before being executed.
    #
    # @since version 3.12.0
    'prepareProvider': NotRequired[bool],
    'workDoneProgress': NotRequired[bool],
})
""" Provider options for a {@link RenameRequest}. """


PrepareRenamePlaceholder = TypedDict('PrepareRenamePlaceholder', {
    'range': 'Range',
    'placeholder': str,
})
""" @since 3.18.0 """


PrepareRenameDefaultBehavior = TypedDict('PrepareRenameDefaultBehavior', {
    'defaultBehavior': bool,
})
""" @since 3.18.0 """


ExecuteCommandOptions = TypedDict('ExecuteCommandOptions', {
    # The commands to be executed on the server
    'commands': List[str],
    'workDoneProgress': NotRequired[bool],
})
""" The server capabilities of a {@link ExecuteCommandRequest}. """


WorkspaceEditMetadata = TypedDict('WorkspaceEditMetadata', {
    # Signal to the editor that this edit is a refactoring.
    'isRefactoring': NotRequired[bool],
})
""" Additional data about a workspace edit.

@since 3.18.0
@proposed """


SemanticTokensLegend = TypedDict('SemanticTokensLegend', {
    # The token types a server uses.
    'tokenTypes': List[str],
    # The token modifiers a server uses.
    'tokenModifiers': List[str],
})
""" @since 3.16.0 """


SemanticTokensFullDelta = TypedDict('SemanticTokensFullDelta', {
    # The server supports deltas for full documents.
    'delta': NotRequired[bool],
})
""" Semantic tokens options to support deltas for full documents

@since 3.18.0 """


OptionalVersionedTextDocumentIdentifier = TypedDict('OptionalVersionedTextDocumentIdentifier', {
    # The version number of this document. If a versioned text document identifier
    # is sent from the server to the client and the file is not open in the editor
    # (the server has not received an open notification before) the server can send
    # `null` to indicate that the version is unknown and the content on disk is the
    # truth (as specified with document content ownership).
    'version': Union[int, None],
    # The text document's uri.
    'uri': 'DocumentUri',
})
""" A text document identifier to optionally denote a specific version of a text document. """


AnnotatedTextEdit = TypedDict('AnnotatedTextEdit', {
    # The actual identifier of the change annotation
    'annotationId': 'ChangeAnnotationIdentifier',
    # The range of the text document to be manipulated. To insert
    # text into a document create a range where start === end.
    'range': 'Range',
    # The string to be inserted. For delete operations use an
    # empty string.
    'newText': str,
})
""" A special text edit with an additional change annotation.

@since 3.16.0. """


SnippetTextEdit = TypedDict('SnippetTextEdit', {
    # The range of the text document to be manipulated.
    'range': 'Range',
    # The snippet to be inserted.
    'snippet': 'StringValue',
    # The actual identifier of the snippet edit.
    'annotationId': NotRequired['ChangeAnnotationIdentifier'],
})
""" An interactive text edit.

@since 3.18.0
@proposed """


ResourceOperation = TypedDict('ResourceOperation', {
    # The resource operation kind.
    'kind': str,
    # An optional annotation identifier describing the operation.
    #
    # @since 3.16.0
    'annotationId': NotRequired['ChangeAnnotationIdentifier'],
})
""" A generic resource operation. """


CreateFileOptions = TypedDict('CreateFileOptions', {
    # Overwrite existing file. Overwrite wins over `ignoreIfExists`
    'overwrite': NotRequired[bool],
    # Ignore if exists.
    'ignoreIfExists': NotRequired[bool],
})
""" Options to create a file. """


RenameFileOptions = TypedDict('RenameFileOptions', {
    # Overwrite target if existing. Overwrite wins over `ignoreIfExists`
    'overwrite': NotRequired[bool],
    # Ignores if target exists.
    'ignoreIfExists': NotRequired[bool],
})
""" Rename file options """


DeleteFileOptions = TypedDict('DeleteFileOptions', {
    # Delete the content recursively if a folder is denoted.
    'recursive': NotRequired[bool],
    # Ignore the operation if the file doesn't exist.
    'ignoreIfNotExists': NotRequired[bool],
})
""" Delete file options """


FileOperationPattern = TypedDict('FileOperationPattern', {
    # The glob pattern to match. Glob patterns can have the following syntax:
    # - `*` to match one or more characters in a path segment
    # - `?` to match on one character in a path segment
    # - `**` to match any number of path segments, including none
    # - `{}` to group sub patterns into an OR expression. (e.g. `**​/*.{ts,js}` matches all TypeScript and JavaScript files)
    # - `[]` to declare a range of characters to match in a path segment (e.g., `example.[0-9]` to match on `example.0`, `example.1`, …)
    # - `[!...]` to negate a range of characters to match in a path segment (e.g., `example.[!0-9]` to match on `example.a`, `example.b`, but not `example.0`)
    'glob': str,
    # Whether to match files or folders with this pattern.
    #
    # Matches both if undefined.
    'matches': NotRequired['FileOperationPatternKind'],
    # Additional options used during matching.
    'options': NotRequired['FileOperationPatternOptions'],
})
""" A pattern to describe in which file operation requests or notifications
the server is interested in receiving.

@since 3.16.0 """


WorkspaceFullDocumentDiagnosticReport = TypedDict('WorkspaceFullDocumentDiagnosticReport', {
    # The URI for which diagnostic information is reported.
    'uri': 'DocumentUri',
    # The version number for which the diagnostics are reported.
    # If the document is not marked as open `null` can be provided.
    'version': Union[int, None],
    # A full document diagnostic report.
    'kind': Literal['full'],
    # An optional result id. If provided it will
    # be sent on the next diagnostic request for the
    # same document.
    'resultId': NotRequired[str],
    # The actual items.
    'items': List['Diagnostic'],
})
""" A full document diagnostic report for a workspace diagnostic result.

@since 3.17.0 """


WorkspaceUnchangedDocumentDiagnosticReport = TypedDict('WorkspaceUnchangedDocumentDiagnosticReport', {
    # The URI for which diagnostic information is reported.
    'uri': 'DocumentUri',
    # The version number for which the diagnostics are reported.
    # If the document is not marked as open `null` can be provided.
    'version': Union[int, None],
    # A document diagnostic report indicating
    # no changes to the last result. A server can
    # only return `unchanged` if result ids are
    # provided.
    'kind': Literal['unchanged'],
    # A result id which will be sent on the next
    # diagnostic request for the same document.
    'resultId': str,
})
""" An unchanged document diagnostic report for a workspace diagnostic result.

@since 3.17.0 """


NotebookCell = TypedDict('NotebookCell', {
    # The cell's kind
    'kind': 'NotebookCellKind',
    # The URI of the cell's text document
    # content.
    'document': 'DocumentUri',
    # Additional metadata stored with the cell.
    #
    # Note: should always be an object literal (e.g. LSPObject)
    'metadata': NotRequired['LSPObject'],
    # Additional execution summary information
    # if supported by the client.
    'executionSummary': NotRequired['ExecutionSummary'],
})
""" A notebook cell.

A cell's document URI must be unique across ALL notebook
cells and can therefore be used to uniquely identify a
notebook cell or the cell's text document.

@since 3.17.0 """


NotebookDocumentFilterWithNotebook = TypedDict('NotebookDocumentFilterWithNotebook', {
    # The notebook to be synced If a string
    # value is provided it matches against the
    # notebook type. '*' matches every notebook.
    'notebook': Union[str, 'NotebookDocumentFilter'],
    # The cells of the matching notebook to be synced.
    'cells': NotRequired[List['NotebookCellLanguage']],
})
""" @since 3.18.0 """


NotebookDocumentFilterWithCells = TypedDict('NotebookDocumentFilterWithCells', {
    # The notebook to be synced If a string
    # value is provided it matches against the
    # notebook type. '*' matches every notebook.
    'notebook': NotRequired[Union[str, 'NotebookDocumentFilter']],
    # The cells of the matching notebook to be synced.
    'cells': List['NotebookCellLanguage'],
})
""" @since 3.18.0 """


NotebookDocumentCellChanges = TypedDict('NotebookDocumentCellChanges', {
    # Changes to the cell structure to add or
    # remove cells.
    'structure': NotRequired['NotebookDocumentCellChangeStructure'],
    # Changes to notebook cells properties like its
    # kind, execution summary or metadata.
    'data': NotRequired[List['NotebookCell']],
    # Changes to the text content of notebook cells.
    'textContent': NotRequired[List['NotebookDocumentCellContentChanges']],
})
""" Cell changes to a notebook document.

@since 3.18.0 """


SelectedCompletionInfo = TypedDict('SelectedCompletionInfo', {
    # The range that will be replaced if this completion item is accepted.
    'range': 'Range',
    # The text the range will be replaced with if this completion is accepted.
    'text': str,
})
""" Describes the currently selected completion item.

@since 3.18.0
@proposed """


ClientInfo = TypedDict('ClientInfo', {
    # The name of the client as defined by the client.
    'name': str,
    # The client's version as defined by the client.
    'version': NotRequired[str],
})
""" Information about the client

@since 3.15.0
@since 3.18.0 ClientInfo type name added. """


ClientCapabilities = TypedDict('ClientCapabilities', {
    # Workspace specific client capabilities.
    'workspace': NotRequired['WorkspaceClientCapabilities'],
    # Text document specific client capabilities.
    'textDocument': NotRequired['TextDocumentClientCapabilities'],
    # Capabilities specific to the notebook document support.
    #
    # @since 3.17.0
    'notebookDocument': NotRequired['NotebookDocumentClientCapabilities'],
    # Window specific client capabilities.
    'window': NotRequired['WindowClientCapabilities'],
    # General client capabilities.
    #
    # @since 3.16.0
    'general': NotRequired['GeneralClientCapabilities'],
    # Experimental client capabilities.
    'experimental': NotRequired['LSPAny'],
})
""" Defines the capabilities provided by the client. """


TextDocumentSyncOptions = TypedDict('TextDocumentSyncOptions', {
    # Open and close notifications are sent to the server. If omitted open close notification should not
    # be sent.
    'openClose': NotRequired[bool],
    # Change notifications are sent to the server. See TextDocumentSyncKind.None, TextDocumentSyncKind.Full
    # and TextDocumentSyncKind.Incremental. If omitted it defaults to TextDocumentSyncKind.None.
    'change': NotRequired['TextDocumentSyncKind'],
    # If present will save notifications are sent to the server. If omitted the notification should not be
    # sent.
    'willSave': NotRequired[bool],
    # If present will save wait until requests are sent to the server. If omitted the request should not be
    # sent.
    'willSaveWaitUntil': NotRequired[bool],
    # If present save notifications are sent to the server. If omitted the notification should not be
    # sent.
    'save': NotRequired[Union[bool, 'SaveOptions']],
})


WorkspaceOptions = TypedDict('WorkspaceOptions', {
    # The server supports workspace folder.
    #
    # @since 3.6.0
    'workspaceFolders': NotRequired['WorkspaceFoldersServerCapabilities'],
    # The server is interested in notifications/requests for operations on files.
    #
    # @since 3.16.0
    'fileOperations': NotRequired['FileOperationOptions'],
    # The server supports the `workspace/textDocumentContent` request.
    #
    # @since 3.18.0
    # @proposed
    'textDocumentContent': NotRequired[Union['TextDocumentContentOptions', 'TextDocumentContentRegistrationOptions']],
})
""" Defines workspace specific capabilities of the server.

@since 3.18.0 """


TextDocumentContentChangePartial = TypedDict('TextDocumentContentChangePartial', {
    # The range of the document that changed.
    'range': 'Range',
    # The optional length of the range that got replaced.
    #
    # @deprecated use range instead.
    'rangeLength': NotRequired[Uint],
    # The new text for the provided range.
    'text': str,
})
""" @since 3.18.0 """


TextDocumentContentChangeWholeDocument = TypedDict('TextDocumentContentChangeWholeDocument', {
    # The new text of the whole document.
    'text': str,
})
""" @since 3.18.0 """


CodeDescription = TypedDict('CodeDescription', {
    # An URI to open with more information about the diagnostic error.
    'href': 'URI',
})
""" Structure to capture a description for an error code.

@since 3.16.0 """


DiagnosticRelatedInformation = TypedDict('DiagnosticRelatedInformation', {
    # The location of this related diagnostic information.
    'location': 'Location',
    # The message of this related diagnostic information.
    'message': str,
})
""" Represents a related message and source code location for a diagnostic. This should be
used to point to code locations that cause or related to a diagnostics, e.g when duplicating
a symbol in a scope. """


EditRangeWithInsertReplace = TypedDict('EditRangeWithInsertReplace', {
    'insert': 'Range',
    'replace': 'Range',
})
""" Edit range variant that includes ranges for insert and replace operations.

@since 3.18.0 """


ServerCompletionItemOptions = TypedDict('ServerCompletionItemOptions', {
    # The server has support for completion item label
    # details (see also `CompletionItemLabelDetails`) when
    # receiving a completion item in a resolve call.
    #
    # @since 3.17.0
    'labelDetailsSupport': NotRequired[bool],
})
""" @since 3.18.0 """


MarkedStringWithLanguage = TypedDict('MarkedStringWithLanguage', {
    'language': str,
    'value': str,
})
""" @since 3.18.0
@deprecated use MarkupContent instead. """


ParameterInformation = TypedDict('ParameterInformation', {
    # The label of this parameter information.
    #
    # Either a string or an inclusive start and exclusive end offsets within its containing
    # signature label. (see SignatureInformation.label). The offsets are based on a UTF-16
    # string representation as `Position` and `Range` does.
    #
    # To avoid ambiguities a server should use the [start, end] offset value instead of using
    # a substring. Whether a client support this is controlled via `labelOffsetSupport` client
    # capability.
    #
    # *Note*: a label of type string should be a substring of its containing signature label.
    # Its intended use case is to highlight the parameter label part in the `SignatureInformation.label`.
    'label': Union[str, List[Union[Uint, Uint]]],
    # The human-readable doc-comment of this parameter. Will be shown
    # in the UI but can be omitted.
    'documentation': NotRequired[Union[str, 'MarkupContent']],
})
""" Represents a parameter of a callable-signature. A parameter can
have a label and a doc-comment. """


CodeActionKindDocumentation = TypedDict('CodeActionKindDocumentation', {
    # The kind of the code action being documented.
    #
    # If the kind is generic, such as `CodeActionKind.Refactor`, the documentation will be shown whenever any
    # refactorings are returned. If the kind if more specific, such as `CodeActionKind.RefactorExtract`, the
    # documentation will only be shown when extract refactoring code actions are returned.
    'kind': 'CodeActionKind',
    # Command that is ued to display the documentation to the user.
    #
    # The title of this documentation code action is taken from {@linkcode Command.title}
    'command': 'Command',
})
""" Documentation for a class of code actions.

@since 3.18.0
@proposed """


NotebookCellTextDocumentFilter = TypedDict('NotebookCellTextDocumentFilter', {
    # A filter that matches against the notebook
    # containing the notebook cell. If a string
    # value is provided it matches against the
    # notebook type. '*' matches every notebook.
    'notebook': Union[str, 'NotebookDocumentFilter'],
    # A language id like `python`.
    #
    # Will be matched against the language id of the
    # notebook cell document. '*' matches every language.
    'language': NotRequired[str],
})
""" A notebook cell text document filter denotes a cell text
document by different properties.

@since 3.17.0 """


FileOperationPatternOptions = TypedDict('FileOperationPatternOptions', {
    # The pattern should be matched ignoring casing.
    'ignoreCase': NotRequired[bool],
})
""" Matching options for the file operation pattern.

@since 3.16.0 """


ExecutionSummary = TypedDict('ExecutionSummary', {
    # A strict monotonically increasing value
    # indicating the execution order of a cell
    # inside a notebook.
    'executionOrder': Uint,
    # Whether the execution was successful or
    # not if known by the client.
    'success': NotRequired[bool],
})


NotebookCellLanguage = TypedDict('NotebookCellLanguage', {
    'language': str,
})
""" @since 3.18.0 """


NotebookDocumentCellChangeStructure = TypedDict('NotebookDocumentCellChangeStructure', {
    # The change to the cell array.
    'array': 'NotebookCellArrayChange',
    # Additional opened cell text documents.
    'didOpen': NotRequired[List['TextDocumentItem']],
    # Additional closed cell text documents.
    'didClose': NotRequired[List['TextDocumentIdentifier']],
})
""" Structural changes to cells in a notebook document.

@since 3.18.0 """


NotebookDocumentCellContentChanges = TypedDict('NotebookDocumentCellContentChanges', {
    'document': 'VersionedTextDocumentIdentifier',
    'changes': List['TextDocumentContentChangeEvent'],
})
""" Content changes to a cell in a notebook document.

@since 3.18.0 """


WorkspaceClientCapabilities = TypedDict('WorkspaceClientCapabilities', {
    # The client supports applying batch edits
    # to the workspace by supporting the request
    # 'workspace/applyEdit'
    'applyEdit': NotRequired[bool],
    # Capabilities specific to `WorkspaceEdit`s.
    'workspaceEdit': NotRequired['WorkspaceEditClientCapabilities'],
    # Capabilities specific to the `workspace/didChangeConfiguration` notification.
    'didChangeConfiguration': NotRequired['DidChangeConfigurationClientCapabilities'],
    # Capabilities specific to the `workspace/didChangeWatchedFiles` notification.
    'didChangeWatchedFiles': NotRequired['DidChangeWatchedFilesClientCapabilities'],
    # Capabilities specific to the `workspace/symbol` request.
    'symbol': NotRequired['WorkspaceSymbolClientCapabilities'],
    # Capabilities specific to the `workspace/executeCommand` request.
    'executeCommand': NotRequired['ExecuteCommandClientCapabilities'],
    # The client has support for workspace folders.
    #
    # @since 3.6.0
    'workspaceFolders': NotRequired[bool],
    # The client supports `workspace/configuration` requests.
    #
    # @since 3.6.0
    'configuration': NotRequired[bool],
    # Capabilities specific to the semantic token requests scoped to the
    # workspace.
    #
    # @since 3.16.0.
    'semanticTokens': NotRequired['SemanticTokensWorkspaceClientCapabilities'],
    # Capabilities specific to the code lens requests scoped to the
    # workspace.
    #
    # @since 3.16.0.
    'codeLens': NotRequired['CodeLensWorkspaceClientCapabilities'],
    # The client has support for file notifications/requests for user operations on files.
    #
    # Since 3.16.0
    'fileOperations': NotRequired['FileOperationClientCapabilities'],
    # Capabilities specific to the inline values requests scoped to the
    # workspace.
    #
    # @since 3.17.0.
    'inlineValue': NotRequired['InlineValueWorkspaceClientCapabilities'],
    # Capabilities specific to the inlay hint requests scoped to the
    # workspace.
    #
    # @since 3.17.0.
    'inlayHint': NotRequired['InlayHintWorkspaceClientCapabilities'],
    # Capabilities specific to the diagnostic requests scoped to the
    # workspace.
    #
    # @since 3.17.0.
    'diagnostics': NotRequired['DiagnosticWorkspaceClientCapabilities'],
    # Capabilities specific to the folding range requests scoped to the workspace.
    #
    # @since 3.18.0
    # @proposed
    'foldingRange': NotRequired['FoldingRangeWorkspaceClientCapabilities'],
    # Capabilities specific to the `workspace/textDocumentContent` request.
    #
    # @since 3.18.0
    # @proposed
    'textDocumentContent': NotRequired['TextDocumentContentClientCapabilities'],
})
""" Workspace specific client capabilities. """


TextDocumentClientCapabilities = TypedDict('TextDocumentClientCapabilities', {
    # Defines which synchronization capabilities the client supports.
    'synchronization': NotRequired['TextDocumentSyncClientCapabilities'],
    # Defines which filters the client supports.
    #
    # @since 3.18.0
    'filters': NotRequired['TextDocumentFilterClientCapabilities'],
    # Capabilities specific to the `textDocument/completion` request.
    'completion': NotRequired['CompletionClientCapabilities'],
    # Capabilities specific to the `textDocument/hover` request.
    'hover': NotRequired['HoverClientCapabilities'],
    # Capabilities specific to the `textDocument/signatureHelp` request.
    'signatureHelp': NotRequired['SignatureHelpClientCapabilities'],
    # Capabilities specific to the `textDocument/declaration` request.
    #
    # @since 3.14.0
    'declaration': NotRequired['DeclarationClientCapabilities'],
    # Capabilities specific to the `textDocument/definition` request.
    'definition': NotRequired['DefinitionClientCapabilities'],
    # Capabilities specific to the `textDocument/typeDefinition` request.
    #
    # @since 3.6.0
    'typeDefinition': NotRequired['TypeDefinitionClientCapabilities'],
    # Capabilities specific to the `textDocument/implementation` request.
    #
    # @since 3.6.0
    'implementation': NotRequired['ImplementationClientCapabilities'],
    # Capabilities specific to the `textDocument/references` request.
    'references': NotRequired['ReferenceClientCapabilities'],
    # Capabilities specific to the `textDocument/documentHighlight` request.
    'documentHighlight': NotRequired['DocumentHighlightClientCapabilities'],
    # Capabilities specific to the `textDocument/documentSymbol` request.
    'documentSymbol': NotRequired['DocumentSymbolClientCapabilities'],
    # Capabilities specific to the `textDocument/codeAction` request.
    'codeAction': NotRequired['CodeActionClientCapabilities'],
    # Capabilities specific to the `textDocument/codeLens` request.
    'codeLens': NotRequired['CodeLensClientCapabilities'],
    # Capabilities specific to the `textDocument/documentLink` request.
    'documentLink': NotRequired['DocumentLinkClientCapabilities'],
    # Capabilities specific to the `textDocument/documentColor` and the
    # `textDocument/colorPresentation` request.
    #
    # @since 3.6.0
    'colorProvider': NotRequired['DocumentColorClientCapabilities'],
    # Capabilities specific to the `textDocument/formatting` request.
    'formatting': NotRequired['DocumentFormattingClientCapabilities'],
    # Capabilities specific to the `textDocument/rangeFormatting` request.
    'rangeFormatting': NotRequired['DocumentRangeFormattingClientCapabilities'],
    # Capabilities specific to the `textDocument/onTypeFormatting` request.
    'onTypeFormatting': NotRequired['DocumentOnTypeFormattingClientCapabilities'],
    # Capabilities specific to the `textDocument/rename` request.
    'rename': NotRequired['RenameClientCapabilities'],
    # Capabilities specific to the `textDocument/foldingRange` request.
    #
    # @since 3.10.0
    'foldingRange': NotRequired['FoldingRangeClientCapabilities'],
    # Capabilities specific to the `textDocument/selectionRange` request.
    #
    # @since 3.15.0
    'selectionRange': NotRequired['SelectionRangeClientCapabilities'],
    # Capabilities specific to the `textDocument/publishDiagnostics` notification.
    'publishDiagnostics': NotRequired['PublishDiagnosticsClientCapabilities'],
    # Capabilities specific to the various call hierarchy requests.
    #
    # @since 3.16.0
    'callHierarchy': NotRequired['CallHierarchyClientCapabilities'],
    # Capabilities specific to the various semantic token request.
    #
    # @since 3.16.0
    'semanticTokens': NotRequired['SemanticTokensClientCapabilities'],
    # Capabilities specific to the `textDocument/linkedEditingRange` request.
    #
    # @since 3.16.0
    'linkedEditingRange': NotRequired['LinkedEditingRangeClientCapabilities'],
    # Client capabilities specific to the `textDocument/moniker` request.
    #
    # @since 3.16.0
    'moniker': NotRequired['MonikerClientCapabilities'],
    # Capabilities specific to the various type hierarchy requests.
    #
    # @since 3.17.0
    'typeHierarchy': NotRequired['TypeHierarchyClientCapabilities'],
    # Capabilities specific to the `textDocument/inlineValue` request.
    #
    # @since 3.17.0
    'inlineValue': NotRequired['InlineValueClientCapabilities'],
    # Capabilities specific to the `textDocument/inlayHint` request.
    #
    # @since 3.17.0
    'inlayHint': NotRequired['InlayHintClientCapabilities'],
    # Capabilities specific to the diagnostic pull model.
    #
    # @since 3.17.0
    'diagnostic': NotRequired['DiagnosticClientCapabilities'],
    # Client capabilities specific to inline completions.
    #
    # @since 3.18.0
    # @proposed
    'inlineCompletion': NotRequired['InlineCompletionClientCapabilities'],
})
""" Text document specific client capabilities. """


NotebookDocumentClientCapabilities = TypedDict('NotebookDocumentClientCapabilities', {
    # Capabilities specific to notebook document synchronization
    #
    # @since 3.17.0
    'synchronization': 'NotebookDocumentSyncClientCapabilities',
})
""" Capabilities specific to the notebook document support.

@since 3.17.0 """


WindowClientCapabilities = TypedDict('WindowClientCapabilities', {
    # It indicates whether the client supports server initiated
    # progress using the `window/workDoneProgress/create` request.
    #
    # The capability also controls Whether client supports handling
    # of progress notifications. If set servers are allowed to report a
    # `workDoneProgress` property in the request specific server
    # capabilities.
    #
    # @since 3.15.0
    'workDoneProgress': NotRequired[bool],
    # Capabilities specific to the showMessage request.
    #
    # @since 3.16.0
    'showMessage': NotRequired['ShowMessageRequestClientCapabilities'],
    # Capabilities specific to the showDocument request.
    #
    # @since 3.16.0
    'showDocument': NotRequired['ShowDocumentClientCapabilities'],
})


GeneralClientCapabilities = TypedDict('GeneralClientCapabilities', {
    # Client capability that signals how the client
    # handles stale requests (e.g. a request
    # for which the client will not process the response
    # anymore since the information is outdated).
    #
    # @since 3.17.0
    'staleRequestSupport': NotRequired['StaleRequestSupportOptions'],
    # Client capabilities specific to regular expressions.
    #
    # @since 3.16.0
    'regularExpressions': NotRequired['RegularExpressionsClientCapabilities'],
    # Client capabilities specific to the client's markdown parser.
    #
    # @since 3.16.0
    'markdown': NotRequired['MarkdownClientCapabilities'],
    # The position encodings supported by the client. Client and server
    # have to agree on the same position encoding to ensure that offsets
    # (e.g. character position in a line) are interpreted the same on both
    # sides.
    #
    # To keep the protocol backwards compatible the following applies: if
    # the value 'utf-16' is missing from the array of position encodings
    # servers can assume that the client supports UTF-16. UTF-16 is
    # therefore a mandatory encoding.
    #
    # If omitted it defaults to ['utf-16'].
    #
    # Implementation considerations: since the conversion from one encoding
    # into another requires the content of the file / line the conversion
    # is best done where the file is read which is usually on the server
    # side.
    #
    # @since 3.17.0
    'positionEncodings': NotRequired[List['PositionEncodingKind']],
})
""" General client capabilities.

@since 3.16.0 """


WorkspaceFoldersServerCapabilities = TypedDict('WorkspaceFoldersServerCapabilities', {
    # The server has support for workspace folders
    'supported': NotRequired[bool],
    # Whether the server wants to receive workspace folder
    # change notifications.
    #
    # If a string is provided the string is treated as an ID
    # under which the notification is registered on the client
    # side. The ID can be used to unregister for these events
    # using the `client/unregisterCapability` request.
    'changeNotifications': NotRequired[Union[str, bool]],
})


FileOperationOptions = TypedDict('FileOperationOptions', {
    # The server is interested in receiving didCreateFiles notifications.
    'didCreate': NotRequired['FileOperationRegistrationOptions'],
    # The server is interested in receiving willCreateFiles requests.
    'willCreate': NotRequired['FileOperationRegistrationOptions'],
    # The server is interested in receiving didRenameFiles notifications.
    'didRename': NotRequired['FileOperationRegistrationOptions'],
    # The server is interested in receiving willRenameFiles requests.
    'willRename': NotRequired['FileOperationRegistrationOptions'],
    # The server is interested in receiving didDeleteFiles file notifications.
    'didDelete': NotRequired['FileOperationRegistrationOptions'],
    # The server is interested in receiving willDeleteFiles file requests.
    'willDelete': NotRequired['FileOperationRegistrationOptions'],
})
""" Options for notifications/requests for user operations on files.

@since 3.16.0 """


RelativePattern = TypedDict('RelativePattern', {
    # A workspace folder or a base URI to which this pattern will be matched
    # against relatively.
    'baseUri': Union['WorkspaceFolder', 'URI'],
    # The actual glob pattern;
    'pattern': 'Pattern',
})
""" A relative pattern is a helper to construct glob patterns that are matched
relatively to a base URI. The common value for a `baseUri` is a workspace
folder root, but it can be another absolute URI as well.

@since 3.17.0 """


TextDocumentFilterLanguage = TypedDict('TextDocumentFilterLanguage', {
    # A language id, like `typescript`.
    'language': str,
    # A Uri {@link Uri.scheme scheme}, like `file` or `untitled`.
    'scheme': NotRequired[str],
    # A glob pattern, like **​/*.{ts,js}. See TextDocumentFilter for examples.
    #
    # @since 3.18.0 - support for relative patterns. Whether clients support
    # relative patterns depends on the client capability
    # `textDocuments.filters.relativePatternSupport`.
    'pattern': NotRequired['GlobPattern'],
})
""" A document filter where `language` is required field.

@since 3.18.0 """


TextDocumentFilterScheme = TypedDict('TextDocumentFilterScheme', {
    # A language id, like `typescript`.
    'language': NotRequired[str],
    # A Uri {@link Uri.scheme scheme}, like `file` or `untitled`.
    'scheme': str,
    # A glob pattern, like **​/*.{ts,js}. See TextDocumentFilter for examples.
    #
    # @since 3.18.0 - support for relative patterns. Whether clients support
    # relative patterns depends on the client capability
    # `textDocuments.filters.relativePatternSupport`.
    'pattern': NotRequired['GlobPattern'],
})
""" A document filter where `scheme` is required field.

@since 3.18.0 """


TextDocumentFilterPattern = TypedDict('TextDocumentFilterPattern', {
    # A language id, like `typescript`.
    'language': NotRequired[str],
    # A Uri {@link Uri.scheme scheme}, like `file` or `untitled`.
    'scheme': NotRequired[str],
    # A glob pattern, like **​/*.{ts,js}. See TextDocumentFilter for examples.
    #
    # @since 3.18.0 - support for relative patterns. Whether clients support
    # relative patterns depends on the client capability
    # `textDocuments.filters.relativePatternSupport`.
    'pattern': 'GlobPattern',
})
""" A document filter where `pattern` is required field.

@since 3.18.0 """


NotebookDocumentFilterNotebookType = TypedDict('NotebookDocumentFilterNotebookType', {
    # The type of the enclosing notebook.
    'notebookType': str,
    # A Uri {@link Uri.scheme scheme}, like `file` or `untitled`.
    'scheme': NotRequired[str],
    # A glob pattern.
    'pattern': NotRequired['GlobPattern'],
})
""" A notebook document filter where `notebookType` is required field.

@since 3.18.0 """


NotebookDocumentFilterScheme = TypedDict('NotebookDocumentFilterScheme', {
    # The type of the enclosing notebook.
    'notebookType': NotRequired[str],
    # A Uri {@link Uri.scheme scheme}, like `file` or `untitled`.
    'scheme': str,
    # A glob pattern.
    'pattern': NotRequired['GlobPattern'],
})
""" A notebook document filter where `scheme` is required field.

@since 3.18.0 """


NotebookDocumentFilterPattern = TypedDict('NotebookDocumentFilterPattern', {
    # The type of the enclosing notebook.
    'notebookType': NotRequired[str],
    # A Uri {@link Uri.scheme scheme}, like `file` or `untitled`.
    'scheme': NotRequired[str],
    # A glob pattern.
    'pattern': 'GlobPattern',
})
""" A notebook document filter where `pattern` is required field.

@since 3.18.0 """


NotebookCellArrayChange = TypedDict('NotebookCellArrayChange', {
    # The start oftest of the cell that changed.
    'start': Uint,
    # The deleted cells
    'deleteCount': Uint,
    # The new cells, if any
    'cells': NotRequired[List['NotebookCell']],
})
""" A change describing how to move a `NotebookCell`
array from state S to S'.

@since 3.17.0 """


WorkspaceEditClientCapabilities = TypedDict('WorkspaceEditClientCapabilities', {
    # The client supports versioned document changes in `WorkspaceEdit`s
    'documentChanges': NotRequired[bool],
    # The resource operations the client supports. Clients should at least
    # support 'create', 'rename' and 'delete' files and folders.
    #
    # @since 3.13.0
    'resourceOperations': NotRequired[List['ResourceOperationKind']],
    # The failure handling strategy of a client if applying the workspace edit
    # fails.
    #
    # @since 3.13.0
    'failureHandling': NotRequired['FailureHandlingKind'],
    # Whether the client normalizes line endings to the client specific
    # setting.
    # If set to `true` the client will normalize line ending characters
    # in a workspace edit to the client-specified new line
    # character.
    #
    # @since 3.16.0
    'normalizesLineEndings': NotRequired[bool],
    # Whether the client in general supports change annotations on text edits,
    # create file, rename file and delete file changes.
    #
    # @since 3.16.0
    'changeAnnotationSupport': NotRequired['ChangeAnnotationsSupportOptions'],
    # Whether the client supports `WorkspaceEditMetadata` in `WorkspaceEdit`s.
    #
    # @since 3.18.0
    # @proposed
    'metadataSupport': NotRequired[bool],
    # Whether the client supports snippets as text edits.
    #
    # @since 3.18.0
    # @proposed
    'snippetEditSupport': NotRequired[bool],
})


DidChangeConfigurationClientCapabilities = TypedDict('DidChangeConfigurationClientCapabilities', {
    # Did change configuration notification supports dynamic registration.
    'dynamicRegistration': NotRequired[bool],
})


DidChangeWatchedFilesClientCapabilities = TypedDict('DidChangeWatchedFilesClientCapabilities', {
    # Did change watched files notification supports dynamic registration. Please note
    # that the current protocol doesn't support static configuration for file changes
    # from the server side.
    'dynamicRegistration': NotRequired[bool],
    # Whether the client has support for {@link  RelativePattern relative pattern}
    # or not.
    #
    # @since 3.17.0
    'relativePatternSupport': NotRequired[bool],
})


WorkspaceSymbolClientCapabilities = TypedDict('WorkspaceSymbolClientCapabilities', {
    # Symbol request supports dynamic registration.
    'dynamicRegistration': NotRequired[bool],
    # Specific capabilities for the `SymbolKind` in the `workspace/symbol` request.
    'symbolKind': NotRequired['ClientSymbolKindOptions'],
    # The client supports tags on `SymbolInformation`.
    # Clients supporting tags have to handle unknown tags gracefully.
    #
    # @since 3.16.0
    'tagSupport': NotRequired['ClientSymbolTagOptions'],
    # The client support partial workspace symbols. The client will send the
    # request `workspaceSymbol/resolve` to the server to resolve additional
    # properties.
    #
    # @since 3.17.0
    'resolveSupport': NotRequired['ClientSymbolResolveOptions'],
})
""" Client capabilities for a {@link WorkspaceSymbolRequest}. """


ExecuteCommandClientCapabilities = TypedDict('ExecuteCommandClientCapabilities', {
    # Execute command supports dynamic registration.
    'dynamicRegistration': NotRequired[bool],
})
""" The client capabilities of a {@link ExecuteCommandRequest}. """


SemanticTokensWorkspaceClientCapabilities = TypedDict('SemanticTokensWorkspaceClientCapabilities', {
    # Whether the client implementation supports a refresh request sent from
    # the server to the client.
    #
    # Note that this event is global and will force the client to refresh all
    # semantic tokens currently shown. It should be used with absolute care
    # and is useful for situation where a server for example detects a project
    # wide change that requires such a calculation.
    'refreshSupport': NotRequired[bool],
})
""" @since 3.16.0 """


CodeLensWorkspaceClientCapabilities = TypedDict('CodeLensWorkspaceClientCapabilities', {
    # Whether the client implementation supports a refresh request sent from the
    # server to the client.
    #
    # Note that this event is global and will force the client to refresh all
    # code lenses currently shown. It should be used with absolute care and is
    # useful for situation where a server for example detect a project wide
    # change that requires such a calculation.
    'refreshSupport': NotRequired[bool],
})
""" @since 3.16.0 """


FileOperationClientCapabilities = TypedDict('FileOperationClientCapabilities', {
    # Whether the client supports dynamic registration for file requests/notifications.
    'dynamicRegistration': NotRequired[bool],
    # The client has support for sending didCreateFiles notifications.
    'didCreate': NotRequired[bool],
    # The client has support for sending willCreateFiles requests.
    'willCreate': NotRequired[bool],
    # The client has support for sending didRenameFiles notifications.
    'didRename': NotRequired[bool],
    # The client has support for sending willRenameFiles requests.
    'willRename': NotRequired[bool],
    # The client has support for sending didDeleteFiles notifications.
    'didDelete': NotRequired[bool],
    # The client has support for sending willDeleteFiles requests.
    'willDelete': NotRequired[bool],
})
""" Capabilities relating to events from file operations by the user in the client.

These events do not come from the file system, they come from user operations
like renaming a file in the UI.

@since 3.16.0 """


InlineValueWorkspaceClientCapabilities = TypedDict('InlineValueWorkspaceClientCapabilities', {
    # Whether the client implementation supports a refresh request sent from the
    # server to the client.
    #
    # Note that this event is global and will force the client to refresh all
    # inline values currently shown. It should be used with absolute care and is
    # useful for situation where a server for example detects a project wide
    # change that requires such a calculation.
    'refreshSupport': NotRequired[bool],
})
""" Client workspace capabilities specific to inline values.

@since 3.17.0 """


InlayHintWorkspaceClientCapabilities = TypedDict('InlayHintWorkspaceClientCapabilities', {
    # Whether the client implementation supports a refresh request sent from
    # the server to the client.
    #
    # Note that this event is global and will force the client to refresh all
    # inlay hints currently shown. It should be used with absolute care and
    # is useful for situation where a server for example detects a project wide
    # change that requires such a calculation.
    'refreshSupport': NotRequired[bool],
})
""" Client workspace capabilities specific to inlay hints.

@since 3.17.0 """


DiagnosticWorkspaceClientCapabilities = TypedDict('DiagnosticWorkspaceClientCapabilities', {
    # Whether the client implementation supports a refresh request sent from
    # the server to the client.
    #
    # Note that this event is global and will force the client to refresh all
    # pulled diagnostics currently shown. It should be used with absolute care and
    # is useful for situation where a server for example detects a project wide
    # change that requires such a calculation.
    'refreshSupport': NotRequired[bool],
})
""" Workspace client capabilities specific to diagnostic pull requests.

@since 3.17.0 """


FoldingRangeWorkspaceClientCapabilities = TypedDict('FoldingRangeWorkspaceClientCapabilities', {
    # Whether the client implementation supports a refresh request sent from the
    # server to the client.
    #
    # Note that this event is global and will force the client to refresh all
    # folding ranges currently shown. It should be used with absolute care and is
    # useful for situation where a server for example detects a project wide
    # change that requires such a calculation.
    #
    # @since 3.18.0
    # @proposed
    'refreshSupport': NotRequired[bool],
})
""" Client workspace capabilities specific to folding ranges

@since 3.18.0
@proposed """


TextDocumentContentClientCapabilities = TypedDict('TextDocumentContentClientCapabilities', {
    # Text document content provider supports dynamic registration.
    'dynamicRegistration': NotRequired[bool],
})
""" Client capabilities for a text document content provider.

@since 3.18.0
@proposed """


TextDocumentSyncClientCapabilities = TypedDict('TextDocumentSyncClientCapabilities', {
    # Whether text document synchronization supports dynamic registration.
    'dynamicRegistration': NotRequired[bool],
    # The client supports sending will save notifications.
    'willSave': NotRequired[bool],
    # The client supports sending a will save request and
    # waits for a response providing text edits which will
    # be applied to the document before it is saved.
    'willSaveWaitUntil': NotRequired[bool],
    # The client supports did save notifications.
    'didSave': NotRequired[bool],
})


TextDocumentFilterClientCapabilities = TypedDict('TextDocumentFilterClientCapabilities', {
    # The client supports Relative Patterns.
    #
    # @since 3.18.0
    'relativePatternSupport': NotRequired[bool],
})


CompletionClientCapabilities = TypedDict('CompletionClientCapabilities', {
    # Whether completion supports dynamic registration.
    'dynamicRegistration': NotRequired[bool],
    # The client supports the following `CompletionItem` specific
    # capabilities.
    'completionItem': NotRequired['ClientCompletionItemOptions'],
    'completionItemKind': NotRequired['ClientCompletionItemOptionsKind'],
    # Defines how the client handles whitespace and indentation
    # when accepting a completion item that uses multi line
    # text in either `insertText` or `textEdit`.
    #
    # @since 3.17.0
    'insertTextMode': NotRequired['InsertTextMode'],
    # The client supports to send additional context information for a
    # `textDocument/completion` request.
    'contextSupport': NotRequired[bool],
    # The client supports the following `CompletionList` specific
    # capabilities.
    #
    # @since 3.17.0
    'completionList': NotRequired['CompletionListCapabilities'],
})
""" Completion client capabilities """


HoverClientCapabilities = TypedDict('HoverClientCapabilities', {
    # Whether hover supports dynamic registration.
    'dynamicRegistration': NotRequired[bool],
    # Client supports the following content formats for the content
    # property. The order describes the preferred format of the client.
    'contentFormat': NotRequired[List['MarkupKind']],
})


SignatureHelpClientCapabilities = TypedDict('SignatureHelpClientCapabilities', {
    # Whether signature help supports dynamic registration.
    'dynamicRegistration': NotRequired[bool],
    # The client supports the following `SignatureInformation`
    # specific properties.
    'signatureInformation': NotRequired['ClientSignatureInformationOptions'],
    # The client supports to send additional context information for a
    # `textDocument/signatureHelp` request. A client that opts into
    # contextSupport will also support the `retriggerCharacters` on
    # `SignatureHelpOptions`.
    #
    # @since 3.15.0
    'contextSupport': NotRequired[bool],
})
""" Client Capabilities for a {@link SignatureHelpRequest}. """


DeclarationClientCapabilities = TypedDict('DeclarationClientCapabilities', {
    # Whether declaration supports dynamic registration. If this is set to `true`
    # the client supports the new `DeclarationRegistrationOptions` return value
    # for the corresponding server capability as well.
    'dynamicRegistration': NotRequired[bool],
    # The client supports additional metadata in the form of declaration links.
    'linkSupport': NotRequired[bool],
})
""" @since 3.14.0 """


DefinitionClientCapabilities = TypedDict('DefinitionClientCapabilities', {
    # Whether definition supports dynamic registration.
    'dynamicRegistration': NotRequired[bool],
    # The client supports additional metadata in the form of definition links.
    #
    # @since 3.14.0
    'linkSupport': NotRequired[bool],
})
""" Client Capabilities for a {@link DefinitionRequest}. """


TypeDefinitionClientCapabilities = TypedDict('TypeDefinitionClientCapabilities', {
    # Whether implementation supports dynamic registration. If this is set to `true`
    # the client supports the new `TypeDefinitionRegistrationOptions` return value
    # for the corresponding server capability as well.
    'dynamicRegistration': NotRequired[bool],
    # The client supports additional metadata in the form of definition links.
    #
    # Since 3.14.0
    'linkSupport': NotRequired[bool],
})
""" Since 3.6.0 """


ImplementationClientCapabilities = TypedDict('ImplementationClientCapabilities', {
    # Whether implementation supports dynamic registration. If this is set to `true`
    # the client supports the new `ImplementationRegistrationOptions` return value
    # for the corresponding server capability as well.
    'dynamicRegistration': NotRequired[bool],
    # The client supports additional metadata in the form of definition links.
    #
    # @since 3.14.0
    'linkSupport': NotRequired[bool],
})
""" @since 3.6.0 """


ReferenceClientCapabilities = TypedDict('ReferenceClientCapabilities', {
    # Whether references supports dynamic registration.
    'dynamicRegistration': NotRequired[bool],
})
""" Client Capabilities for a {@link ReferencesRequest}. """


DocumentHighlightClientCapabilities = TypedDict('DocumentHighlightClientCapabilities', {
    # Whether document highlight supports dynamic registration.
    'dynamicRegistration': NotRequired[bool],
})
""" Client Capabilities for a {@link DocumentHighlightRequest}. """


DocumentSymbolClientCapabilities = TypedDict('DocumentSymbolClientCapabilities', {
    # Whether document symbol supports dynamic registration.
    'dynamicRegistration': NotRequired[bool],
    # Specific capabilities for the `SymbolKind` in the
    # `textDocument/documentSymbol` request.
    'symbolKind': NotRequired['ClientSymbolKindOptions'],
    # The client supports hierarchical document symbols.
    'hierarchicalDocumentSymbolSupport': NotRequired[bool],
    # The client supports tags on `SymbolInformation`. Tags are supported on
    # `DocumentSymbol` if `hierarchicalDocumentSymbolSupport` is set to true.
    # Clients supporting tags have to handle unknown tags gracefully.
    #
    # @since 3.16.0
    'tagSupport': NotRequired['ClientSymbolTagOptions'],
    # The client supports an additional label presented in the UI when
    # registering a document symbol provider.
    #
    # @since 3.16.0
    'labelSupport': NotRequired[bool],
})
""" Client Capabilities for a {@link DocumentSymbolRequest}. """


CodeActionClientCapabilities = TypedDict('CodeActionClientCapabilities', {
    # Whether code action supports dynamic registration.
    'dynamicRegistration': NotRequired[bool],
    # The client support code action literals of type `CodeAction` as a valid
    # response of the `textDocument/codeAction` request. If the property is not
    # set the request can only return `Command` literals.
    #
    # @since 3.8.0
    'codeActionLiteralSupport': NotRequired['ClientCodeActionLiteralOptions'],
    # Whether code action supports the `isPreferred` property.
    #
    # @since 3.15.0
    'isPreferredSupport': NotRequired[bool],
    # Whether code action supports the `disabled` property.
    #
    # @since 3.16.0
    'disabledSupport': NotRequired[bool],
    # Whether code action supports the `data` property which is
    # preserved between a `textDocument/codeAction` and a
    # `codeAction/resolve` request.
    #
    # @since 3.16.0
    'dataSupport': NotRequired[bool],
    # Whether the client supports resolving additional code action
    # properties via a separate `codeAction/resolve` request.
    #
    # @since 3.16.0
    'resolveSupport': NotRequired['ClientCodeActionResolveOptions'],
    # Whether the client honors the change annotations in
    # text edits and resource operations returned via the
    # `CodeAction#edit` property by for example presenting
    # the workspace edit in the user interface and asking
    # for confirmation.
    #
    # @since 3.16.0
    'honorsChangeAnnotations': NotRequired[bool],
    # Whether the client supports documentation for a class of
    # code actions.
    #
    # @since 3.18.0
    # @proposed
    'documentationSupport': NotRequired[bool],
    # Client supports the tag property on a code action. Clients
    # supporting tags have to handle unknown tags gracefully.
    #
    # @since 3.18.0 - proposed
    'tagSupport': NotRequired['CodeActionTagOptions'],
})
""" The Client Capabilities of a {@link CodeActionRequest}. """


CodeLensClientCapabilities = TypedDict('CodeLensClientCapabilities', {
    # Whether code lens supports dynamic registration.
    'dynamicRegistration': NotRequired[bool],
    # Whether the client supports resolving additional code lens
    # properties via a separate `codeLens/resolve` request.
    #
    # @since 3.18.0
    'resolveSupport': NotRequired['ClientCodeLensResolveOptions'],
})
""" The client capabilities  of a {@link CodeLensRequest}. """


DocumentLinkClientCapabilities = TypedDict('DocumentLinkClientCapabilities', {
    # Whether document link supports dynamic registration.
    'dynamicRegistration': NotRequired[bool],
    # Whether the client supports the `tooltip` property on `DocumentLink`.
    #
    # @since 3.15.0
    'tooltipSupport': NotRequired[bool],
})
""" The client capabilities of a {@link DocumentLinkRequest}. """


DocumentColorClientCapabilities = TypedDict('DocumentColorClientCapabilities', {
    # Whether implementation supports dynamic registration. If this is set to `true`
    # the client supports the new `DocumentColorRegistrationOptions` return value
    # for the corresponding server capability as well.
    'dynamicRegistration': NotRequired[bool],
})


DocumentFormattingClientCapabilities = TypedDict('DocumentFormattingClientCapabilities', {
    # Whether formatting supports dynamic registration.
    'dynamicRegistration': NotRequired[bool],
})
""" Client capabilities of a {@link DocumentFormattingRequest}. """


DocumentRangeFormattingClientCapabilities = TypedDict('DocumentRangeFormattingClientCapabilities', {
    # Whether range formatting supports dynamic registration.
    'dynamicRegistration': NotRequired[bool],
    # Whether the client supports formatting multiple ranges at once.
    #
    # @since 3.18.0
    # @proposed
    'rangesSupport': NotRequired[bool],
})
""" Client capabilities of a {@link DocumentRangeFormattingRequest}. """


DocumentOnTypeFormattingClientCapabilities = TypedDict('DocumentOnTypeFormattingClientCapabilities', {
    # Whether on type formatting supports dynamic registration.
    'dynamicRegistration': NotRequired[bool],
})
""" Client capabilities of a {@link DocumentOnTypeFormattingRequest}. """


RenameClientCapabilities = TypedDict('RenameClientCapabilities', {
    # Whether rename supports dynamic registration.
    'dynamicRegistration': NotRequired[bool],
    # Client supports testing for validity of rename operations
    # before execution.
    #
    # @since 3.12.0
    'prepareSupport': NotRequired[bool],
    # Client supports the default behavior result.
    #
    # The value indicates the default behavior used by the
    # client.
    #
    # @since 3.16.0
    'prepareSupportDefaultBehavior': NotRequired['PrepareSupportDefaultBehavior'],
    # Whether the client honors the change annotations in
    # text edits and resource operations returned via the
    # rename request's workspace edit by for example presenting
    # the workspace edit in the user interface and asking
    # for confirmation.
    #
    # @since 3.16.0
    'honorsChangeAnnotations': NotRequired[bool],
})


FoldingRangeClientCapabilities = TypedDict('FoldingRangeClientCapabilities', {
    # Whether implementation supports dynamic registration for folding range
    # providers. If this is set to `true` the client supports the new
    # `FoldingRangeRegistrationOptions` return value for the corresponding
    # server capability as well.
    'dynamicRegistration': NotRequired[bool],
    # The maximum number of folding ranges that the client prefers to receive
    # per document. The value serves as a hint, servers are free to follow the
    # limit.
    'rangeLimit': NotRequired[Uint],
    # If set, the client signals that it only supports folding complete lines.
    # If set, client will ignore specified `startCharacter` and `endCharacter`
    # properties in a FoldingRange.
    'lineFoldingOnly': NotRequired[bool],
    # Specific options for the folding range kind.
    #
    # @since 3.17.0
    'foldingRangeKind': NotRequired['ClientFoldingRangeKindOptions'],
    # Specific options for the folding range.
    #
    # @since 3.17.0
    'foldingRange': NotRequired['ClientFoldingRangeOptions'],
})


SelectionRangeClientCapabilities = TypedDict('SelectionRangeClientCapabilities', {
    # Whether implementation supports dynamic registration for selection range providers. If this is set to `true`
    # the client supports the new `SelectionRangeRegistrationOptions` return value for the corresponding server
    # capability as well.
    'dynamicRegistration': NotRequired[bool],
})


PublishDiagnosticsClientCapabilities = TypedDict('PublishDiagnosticsClientCapabilities', {
    # Whether the client interprets the version property of the
    # `textDocument/publishDiagnostics` notification's parameter.
    #
    # @since 3.15.0
    'versionSupport': NotRequired[bool],
    # Whether the clients accepts diagnostics with related information.
    'relatedInformation': NotRequired[bool],
    # Client supports the tag property to provide meta data about a diagnostic.
    # Clients supporting tags have to handle unknown tags gracefully.
    #
    # @since 3.15.0
    'tagSupport': NotRequired['ClientDiagnosticsTagOptions'],
    # Client supports a codeDescription property
    #
    # @since 3.16.0
    'codeDescriptionSupport': NotRequired[bool],
    # Whether code action supports the `data` property which is
    # preserved between a `textDocument/publishDiagnostics` and
    # `textDocument/codeAction` request.
    #
    # @since 3.16.0
    'dataSupport': NotRequired[bool],
})
""" The publish diagnostic client capabilities. """


CallHierarchyClientCapabilities = TypedDict('CallHierarchyClientCapabilities', {
    # Whether implementation supports dynamic registration. If this is set to `true`
    # the client supports the new `(TextDocumentRegistrationOptions & StaticRegistrationOptions)`
    # return value for the corresponding server capability as well.
    'dynamicRegistration': NotRequired[bool],
})
""" @since 3.16.0 """


SemanticTokensClientCapabilities = TypedDict('SemanticTokensClientCapabilities', {
    # Whether implementation supports dynamic registration. If this is set to `true`
    # the client supports the new `(TextDocumentRegistrationOptions & StaticRegistrationOptions)`
    # return value for the corresponding server capability as well.
    'dynamicRegistration': NotRequired[bool],
    # Which requests the client supports and might send to the server
    # depending on the server's capability. Please note that clients might not
    # show semantic tokens or degrade some of the user experience if a range
    # or full request is advertised by the client but not provided by the
    # server. If for example the client capability `requests.full` and
    # `request.range` are both set to true but the server only provides a
    # range provider the client might not render a minimap correctly or might
    # even decide to not show any semantic tokens at all.
    'requests': 'ClientSemanticTokensRequestOptions',
    # The token types that the client supports.
    'tokenTypes': List[str],
    # The token modifiers that the client supports.
    'tokenModifiers': List[str],
    # The token formats the clients supports.
    'formats': List['TokenFormat'],
    # Whether the client supports tokens that can overlap each other.
    'overlappingTokenSupport': NotRequired[bool],
    # Whether the client supports tokens that can span multiple lines.
    'multilineTokenSupport': NotRequired[bool],
    # Whether the client allows the server to actively cancel a
    # semantic token request, e.g. supports returning
    # LSPErrorCodes.ServerCancelled. If a server does the client
    # needs to retrigger the request.
    #
    # @since 3.17.0
    'serverCancelSupport': NotRequired[bool],
    # Whether the client uses semantic tokens to augment existing
    # syntax tokens. If set to `true` client side created syntax
    # tokens and semantic tokens are both used for colorization. If
    # set to `false` the client only uses the returned semantic tokens
    # for colorization.
    #
    # If the value is `undefined` then the client behavior is not
    # specified.
    #
    # @since 3.17.0
    'augmentsSyntaxTokens': NotRequired[bool],
})
""" @since 3.16.0 """


LinkedEditingRangeClientCapabilities = TypedDict('LinkedEditingRangeClientCapabilities', {
    # Whether implementation supports dynamic registration. If this is set to `true`
    # the client supports the new `(TextDocumentRegistrationOptions & StaticRegistrationOptions)`
    # return value for the corresponding server capability as well.
    'dynamicRegistration': NotRequired[bool],
})
""" Client capabilities for the linked editing range request.

@since 3.16.0 """


MonikerClientCapabilities = TypedDict('MonikerClientCapabilities', {
    # Whether moniker supports dynamic registration. If this is set to `true`
    # the client supports the new `MonikerRegistrationOptions` return value
    # for the corresponding server capability as well.
    'dynamicRegistration': NotRequired[bool],
})
""" Client capabilities specific to the moniker request.

@since 3.16.0 """


TypeHierarchyClientCapabilities = TypedDict('TypeHierarchyClientCapabilities', {
    # Whether implementation supports dynamic registration. If this is set to `true`
    # the client supports the new `(TextDocumentRegistrationOptions & StaticRegistrationOptions)`
    # return value for the corresponding server capability as well.
    'dynamicRegistration': NotRequired[bool],
})
""" @since 3.17.0 """


InlineValueClientCapabilities = TypedDict('InlineValueClientCapabilities', {
    # Whether implementation supports dynamic registration for inline value providers.
    'dynamicRegistration': NotRequired[bool],
})
""" Client capabilities specific to inline values.

@since 3.17.0 """


InlayHintClientCapabilities = TypedDict('InlayHintClientCapabilities', {
    # Whether inlay hints support dynamic registration.
    'dynamicRegistration': NotRequired[bool],
    # Indicates which properties a client can resolve lazily on an inlay
    # hint.
    'resolveSupport': NotRequired['ClientInlayHintResolveOptions'],
})
""" Inlay hint client capabilities.

@since 3.17.0 """


DiagnosticClientCapabilities = TypedDict('DiagnosticClientCapabilities', {
    # Whether implementation supports dynamic registration. If this is set to `true`
    # the client supports the new `(TextDocumentRegistrationOptions & StaticRegistrationOptions)`
    # return value for the corresponding server capability as well.
    'dynamicRegistration': NotRequired[bool],
    # Whether the clients supports related documents for document diagnostic pulls.
    'relatedDocumentSupport': NotRequired[bool],
    # Whether the clients accepts diagnostics with related information.
    'relatedInformation': NotRequired[bool],
    # Client supports the tag property to provide meta data about a diagnostic.
    # Clients supporting tags have to handle unknown tags gracefully.
    #
    # @since 3.15.0
    'tagSupport': NotRequired['ClientDiagnosticsTagOptions'],
    # Client supports a codeDescription property
    #
    # @since 3.16.0
    'codeDescriptionSupport': NotRequired[bool],
    # Whether code action supports the `data` property which is
    # preserved between a `textDocument/publishDiagnostics` and
    # `textDocument/codeAction` request.
    #
    # @since 3.16.0
    'dataSupport': NotRequired[bool],
})
""" Client capabilities specific to diagnostic pull requests.

@since 3.17.0 """


InlineCompletionClientCapabilities = TypedDict('InlineCompletionClientCapabilities', {
    # Whether implementation supports dynamic registration for inline completion providers.
    'dynamicRegistration': NotRequired[bool],
})
""" Client capabilities specific to inline completions.

@since 3.18.0
@proposed """


NotebookDocumentSyncClientCapabilities = TypedDict('NotebookDocumentSyncClientCapabilities', {
    # Whether implementation supports dynamic registration. If this is
    # set to `true` the client supports the new
    # `(TextDocumentRegistrationOptions & StaticRegistrationOptions)`
    # return value for the corresponding server capability as well.
    'dynamicRegistration': NotRequired[bool],
    # The client supports sending execution summary data per cell.
    'executionSummarySupport': NotRequired[bool],
})
""" Notebook specific client capabilities.

@since 3.17.0 """


ShowMessageRequestClientCapabilities = TypedDict('ShowMessageRequestClientCapabilities', {
    # Capabilities specific to the `MessageActionItem` type.
    'messageActionItem': NotRequired['ClientShowMessageActionItemOptions'],
})
""" Show message request client capabilities """


ShowDocumentClientCapabilities = TypedDict('ShowDocumentClientCapabilities', {
    # The client has support for the showDocument
    # request.
    'support': bool,
})
""" Client capabilities for the showDocument request.

@since 3.16.0 """


StaleRequestSupportOptions = TypedDict('StaleRequestSupportOptions', {
    # The client will actively cancel the request.
    'cancel': bool,
    # The list of requests for which the client
    # will retry the request if it receives a
    # response with error code `ContentModified`
    'retryOnContentModified': List[str],
})
""" @since 3.18.0 """


RegularExpressionsClientCapabilities = TypedDict('RegularExpressionsClientCapabilities', {
    # The engine's name.
    'engine': 'RegularExpressionEngineKind',
    # The engine's version.
    'version': NotRequired[str],
})
""" Client capabilities specific to regular expressions.

@since 3.16.0 """


MarkdownClientCapabilities = TypedDict('MarkdownClientCapabilities', {
    # The name of the parser.
    'parser': str,
    # The version of the parser.
    'version': NotRequired[str],
    # A list of HTML tags that the client allows / supports in
    # Markdown.
    #
    # @since 3.17.0
    'allowedTags': NotRequired[List[str]],
})
""" Client capabilities specific to the used markdown parser.

@since 3.16.0 """


ChangeAnnotationsSupportOptions = TypedDict('ChangeAnnotationsSupportOptions', {
    # Whether the client groups edits with equal labels into tree nodes,
    # for instance all edits labelled with "Changes in Strings" would
    # be a tree node.
    'groupsOnLabel': NotRequired[bool],
})
""" @since 3.18.0 """


ClientSymbolKindOptions = TypedDict('ClientSymbolKindOptions', {
    # The symbol kind values the client supports. When this
    # property exists the client also guarantees that it will
    # handle values outside its set gracefully and falls back
    # to a default value when unknown.
    #
    # If this property is not present the client only supports
    # the symbol kinds from `File` to `Array` as defined in
    # the initial version of the protocol.
    'valueSet': NotRequired[List['SymbolKind']],
})
""" @since 3.18.0 """


ClientSymbolTagOptions = TypedDict('ClientSymbolTagOptions', {
    # The tags supported by the client.
    'valueSet': List['SymbolTag'],
})
""" @since 3.18.0 """


ClientSymbolResolveOptions = TypedDict('ClientSymbolResolveOptions', {
    # The properties that a client can resolve lazily. Usually
    # `location.range`
    'properties': List[str],
})
""" @since 3.18.0 """


ClientCompletionItemOptions = TypedDict('ClientCompletionItemOptions', {
    # Client supports snippets as insert text.
    #
    # A snippet can define tab stops and placeholders with `$1`, `$2`
    # and `${3:foo}`. `$0` defines the final tab stop, it defaults to
    # the end of the snippet. Placeholders with equal identifiers are linked,
    # that is typing in one will update others too.
    'snippetSupport': NotRequired[bool],
    # Client supports commit characters on a completion item.
    'commitCharactersSupport': NotRequired[bool],
    # Client supports the following content formats for the documentation
    # property. The order describes the preferred format of the client.
    'documentationFormat': NotRequired[List['MarkupKind']],
    # Client supports the deprecated property on a completion item.
    'deprecatedSupport': NotRequired[bool],
    # Client supports the preselect property on a completion item.
    'preselectSupport': NotRequired[bool],
    # Client supports the tag property on a completion item. Clients supporting
    # tags have to handle unknown tags gracefully. Clients especially need to
    # preserve unknown tags when sending a completion item back to the server in
    # a resolve call.
    #
    # @since 3.15.0
    'tagSupport': NotRequired['CompletionItemTagOptions'],
    # Client support insert replace edit to control different behavior if a
    # completion item is inserted in the text or should replace text.
    #
    # @since 3.16.0
    'insertReplaceSupport': NotRequired[bool],
    # Indicates which properties a client can resolve lazily on a completion
    # item. Before version 3.16.0 only the predefined properties `documentation`
    # and `details` could be resolved lazily.
    #
    # @since 3.16.0
    'resolveSupport': NotRequired['ClientCompletionItemResolveOptions'],
    # The client supports the `insertTextMode` property on
    # a completion item to override the whitespace handling mode
    # as defined by the client (see `insertTextMode`).
    #
    # @since 3.16.0
    'insertTextModeSupport': NotRequired['ClientCompletionItemInsertTextModeOptions'],
    # The client has support for completion item label
    # details (see also `CompletionItemLabelDetails`).
    #
    # @since 3.17.0
    'labelDetailsSupport': NotRequired[bool],
})
""" @since 3.18.0 """


ClientCompletionItemOptionsKind = TypedDict('ClientCompletionItemOptionsKind', {
    # The completion item kind values the client supports. When this
    # property exists the client also guarantees that it will
    # handle values outside its set gracefully and falls back
    # to a default value when unknown.
    #
    # If this property is not present the client only supports
    # the completion items kinds from `Text` to `Reference` as defined in
    # the initial version of the protocol.
    'valueSet': NotRequired[List['CompletionItemKind']],
})
""" @since 3.18.0 """


CompletionListCapabilities = TypedDict('CompletionListCapabilities', {
    # The client supports the following itemDefaults on
    # a completion list.
    #
    # The value lists the supported property names of the
    # `CompletionList.itemDefaults` object. If omitted
    # no properties are supported.
    #
    # @since 3.17.0
    'itemDefaults': NotRequired[List[str]],
    # Specifies whether the client supports `CompletionList.applyKind` to
    # indicate how supported values from `completionList.itemDefaults`
    # and `completion` will be combined.
    #
    # If a client supports `applyKind` it must support it for all fields
    # that it supports that are listed in `CompletionList.applyKind`. This
    # means when clients add support for new/future fields in completion
    # items the MUST also support merge for them if those fields are
    # defined in `CompletionList.applyKind`.
    #
    # @since 3.18.0
    'applyKindSupport': NotRequired[bool],
})
""" The client supports the following `CompletionList` specific
capabilities.

@since 3.17.0 """


ClientSignatureInformationOptions = TypedDict('ClientSignatureInformationOptions', {
    # Client supports the following content formats for the documentation
    # property. The order describes the preferred format of the client.
    'documentationFormat': NotRequired[List['MarkupKind']],
    # Client capabilities specific to parameter information.
    'parameterInformation': NotRequired['ClientSignatureParameterInformationOptions'],
    # The client supports the `activeParameter` property on `SignatureInformation`
    # literal.
    #
    # @since 3.16.0
    'activeParameterSupport': NotRequired[bool],
    # The client supports the `activeParameter` property on
    # `SignatureHelp`/`SignatureInformation` being set to `null` to
    # indicate that no parameter should be active.
    #
    # @since 3.18.0
    # @proposed
    'noActiveParameterSupport': NotRequired[bool],
})
""" @since 3.18.0 """


ClientCodeActionLiteralOptions = TypedDict('ClientCodeActionLiteralOptions', {
    # The code action kind is support with the following value
    # set.
    'codeActionKind': 'ClientCodeActionKindOptions',
})
""" @since 3.18.0 """


ClientCodeActionResolveOptions = TypedDict('ClientCodeActionResolveOptions', {
    # The properties that a client can resolve lazily.
    'properties': List[str],
})
""" @since 3.18.0 """


CodeActionTagOptions = TypedDict('CodeActionTagOptions', {
    # The tags supported by the client.
    'valueSet': List['CodeActionTag'],
})
""" @since 3.18.0 - proposed """


ClientCodeLensResolveOptions = TypedDict('ClientCodeLensResolveOptions', {
    # The properties that a client can resolve lazily.
    'properties': List[str],
})
""" @since 3.18.0 """


ClientFoldingRangeKindOptions = TypedDict('ClientFoldingRangeKindOptions', {
    # The folding range kind values the client supports. When this
    # property exists the client also guarantees that it will
    # handle values outside its set gracefully and falls back
    # to a default value when unknown.
    'valueSet': NotRequired[List['FoldingRangeKind']],
})
""" @since 3.18.0 """


ClientFoldingRangeOptions = TypedDict('ClientFoldingRangeOptions', {
    # If set, the client signals that it supports setting collapsedText on
    # folding ranges to display custom labels instead of the default text.
    #
    # @since 3.17.0
    'collapsedText': NotRequired[bool],
})
""" @since 3.18.0 """


DiagnosticsCapabilities = TypedDict('DiagnosticsCapabilities', {
    # Whether the clients accepts diagnostics with related information.
    'relatedInformation': NotRequired[bool],
    # Client supports the tag property to provide meta data about a diagnostic.
    # Clients supporting tags have to handle unknown tags gracefully.
    #
    # @since 3.15.0
    'tagSupport': NotRequired['ClientDiagnosticsTagOptions'],
    # Client supports a codeDescription property
    #
    # @since 3.16.0
    'codeDescriptionSupport': NotRequired[bool],
    # Whether code action supports the `data` property which is
    # preserved between a `textDocument/publishDiagnostics` and
    # `textDocument/codeAction` request.
    #
    # @since 3.16.0
    'dataSupport': NotRequired[bool],
})
""" General diagnostics capabilities for pull and push model. """


ClientSemanticTokensRequestOptions = TypedDict('ClientSemanticTokensRequestOptions', {
    # The client will send the `textDocument/semanticTokens/range` request if
    # the server provides a corresponding handler.
    'range': NotRequired[Union[bool, dict]],
    # The client will send the `textDocument/semanticTokens/full` request if
    # the server provides a corresponding handler.
    'full': NotRequired[Union[bool, 'ClientSemanticTokensRequestFullDelta']],
})
""" @since 3.18.0 """


ClientInlayHintResolveOptions = TypedDict('ClientInlayHintResolveOptions', {
    # The properties that a client can resolve lazily.
    'properties': List[str],
})
""" @since 3.18.0 """


ClientShowMessageActionItemOptions = TypedDict('ClientShowMessageActionItemOptions', {
    # Whether the client supports additional attributes which
    # are preserved and send back to the server in the
    # request's response.
    'additionalPropertiesSupport': NotRequired[bool],
})
""" @since 3.18.0 """


CompletionItemTagOptions = TypedDict('CompletionItemTagOptions', {
    # The tags supported by the client.
    'valueSet': List['CompletionItemTag'],
})
""" @since 3.18.0 """


ClientCompletionItemResolveOptions = TypedDict('ClientCompletionItemResolveOptions', {
    # The properties that a client can resolve lazily.
    'properties': List[str],
})
""" @since 3.18.0 """


ClientCompletionItemInsertTextModeOptions = TypedDict('ClientCompletionItemInsertTextModeOptions', {
    'valueSet': List['InsertTextMode'],
})
""" @since 3.18.0 """


ClientSignatureParameterInformationOptions = TypedDict('ClientSignatureParameterInformationOptions', {
    # The client supports processing label offsets instead of a
    # simple label string.
    #
    # @since 3.14.0
    'labelOffsetSupport': NotRequired[bool],
})
""" @since 3.18.0 """


ClientCodeActionKindOptions = TypedDict('ClientCodeActionKindOptions', {
    # The code action kind values the client supports. When this
    # property exists the client also guarantees that it will
    # handle values outside its set gracefully and falls back
    # to a default value when unknown.
    'valueSet': List['CodeActionKind'],
})
""" @since 3.18.0 """


ClientDiagnosticsTagOptions = TypedDict('ClientDiagnosticsTagOptions', {
    # The tags supported by the client.
    'valueSet': List['DiagnosticTag'],
})
""" @since 3.18.0 """


ClientSemanticTokensRequestFullDelta = TypedDict('ClientSemanticTokensRequestFullDelta', {
    # The client will send the `textDocument/semanticTokens/full/delta` request if
    # the server provides a corresponding handler.
    'delta': NotRequired[bool],
})
""" @since 3.18.0 """
