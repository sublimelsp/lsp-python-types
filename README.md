# Setup

Requires py3.8 and up.

## Setup

Use UV to manage virtual environment and run scripts.

Install dependecies:
```sh
uv venv
```

## Update types

Download the latest json schema:
```sh
uv run download-schemas.py
```

Generate the types:
```sh
uv run generate.py
```

And finally fix linting and formatting issues:
```sh
uv ruff check --fix --unsafe-fixes
uv ruff format
```
Copy the `lsp_types.py` file to your project.

NOTE: Do not import types that begin with `__`. These types are internal types and are not meant to be used.
