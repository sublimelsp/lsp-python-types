# Setup

Install dependecies:
```
pip install -r requirements.txt
```

Generate the types:
```
python ./generate.py
```

Copy the `lsp_types.py` file to your project.

Requires py3.8 and up.

The `lsp_types_legacy.py` file is made specifically for use in Sublime's LSP package and relies on custom typings and is likely not usable anywhere else.

NOTE: Do not import types that begin with `__`. These types are internal types and are not meant to be used.
