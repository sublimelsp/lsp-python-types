# Setup

Requires py3.10 and up.

Install dependecies:
```
pip install -r requirements.txt
```

Download the latest json schema:
```
python ./download_schemas.py
```

Generate the types:
```
python ./generate.py
```
Copy the `lsp_types.py` file to your project.

The `lsp_types_sublime_text_33.py` file is made specifically for use in Sublime's LSP package using Python 3.3 host that doesn't support class-based `TypedDict` syntax. For all other cases stick with `lsp_types.py`.

NOTE: Do not import types that begin with `__`. These types are internal types and are not meant to be used.
