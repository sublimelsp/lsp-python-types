# Setup

Requires py3.8 and up.

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

NOTE: Do not import types that begin with `__`. These types are internal types and are not meant to be used.
