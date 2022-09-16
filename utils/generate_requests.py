from typing import List
from lsp_schema import Request


def generate_requests(requests: List[Request]) -> str:
    request_names = [f"'{request['method']}'" for request in requests]
    result = f"Methods = Literal[{', '.join(request_names)}]"
    return result
