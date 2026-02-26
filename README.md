# Setup

Requires py3.8 and up.

## Setup

Install dependecies:
```sh
pip install -r requirements.txt
```

## Update types

Download the latest json schema:
```sh
python ./download_schemas.py
```

Generate the types:
```sh
python ./generate.py
```
Copy the `lsp_types.py` file to your project.

NOTE: Do not import types that begin with `__`. These types are internal types and are not meant to be used.
