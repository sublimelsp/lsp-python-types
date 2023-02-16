# it is up to the author to define how the context will look

from typing import TypedDict

class RequestContext(TypedDict):
    server_name: str
    buffer_id: int
    view_id: int
    window_id: int