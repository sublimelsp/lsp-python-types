from __future__ import annotations
from typing import TYPE_CHECKING
from utils.helpers import StructureKind, format_type, indentation

if TYPE_CHECKING:
    from lsp_schema import Request


def generate_requests_and_responses(requests: list[Request]) -> list[str]:
    client_request_names: list[str] = []
    server_request_names: list[str] = []
    client_response_names: list[str] = []
    server_response_names: list[str] = []
    res_definitions: list[str] = []
    req_definitions: list[str] = []
    for request in requests:
        message_direction = request['messageDirection']
        # Requests
        req_name, req_definition = generate_request(request)
        if message_direction == 'clientToServer':
            client_request_names.append(req_name)
        elif message_direction == 'serverToClient':
            server_request_names.append(req_name)
        else:
            client_request_names.append(req_name)
            server_request_names.append(req_name)
        req_definitions.append(req_definition)
        # Responses
        res_name, res_definition = generate_response(request)
        if message_direction == 'clientToServer':
            server_response_names.append(res_name)
        elif message_direction == 'serverToClient':
            client_response_names.append(res_name)
        else:
            client_response_names.append(res_name)
            server_response_names.append(res_name)
        res_definitions.append(res_definition)
    client_request_type = f'ClientRequest: TypeAlias = Union[{", ".join(client_request_names)}]'
    server_request_type = f'ServerRequest: TypeAlias = Union[{", ".join(server_request_names)}]'
    client_response_type = f'ClientResponse: TypeAlias = Union[{", ".join(client_response_names)}]'
    server_response_type = f'ServerResponse: TypeAlias = Union[{", ".join(server_response_names)}]'
    return [
        *req_definitions,
        client_request_type,
        server_request_type,
        *res_definitions,
        server_response_type,
        client_response_type,
    ]


def generate_request(request: Request) -> tuple[str, str]:
    method = request['method']
    params = request.get('params')
    name = request['typeName']
    definition = f'class {name}(TypedDict):\n'
    definition += f"{indentation}method: Literal['{method}']\n"
    if params:
        definition += f'{indentation}params: {format_type(params, {"root_symbol_name": ""}, StructureKind.Class)}'
    else:
        definition += f'{indentation}params: None'
    return (name, definition)


def generate_response(request: Request) -> tuple[str, str]:
    method = request['method']
    result = request['result']
    type_name = request['typeName']
    name = f'{type_name.removesuffix("Request")}Response'
    definition = f'class {name}(TypedDict):\n'
    definition += f"{indentation}method: Literal['{method}']\n"
    definition += f'{indentation}result: {format_type(result, {"root_symbol_name": ""}, StructureKind.Class)}'
    return (name, definition)
