from __future__ import annotations

from typing import TYPE_CHECKING
from utils.helpers import format_type
from utils.helpers import GeneratorContext
from utils.helpers import indentation

if TYPE_CHECKING:
    from lsp_schema import Notification


def generate_notifications(notifications: list[Notification], context: GeneratorContext) -> list[str]:
    client_notification_names: list[str] = []
    server_notification_names: list[str] = []
    definitions: list[str] = []
    for notification in notifications:
        message_direction = notification['messageDirection']
        name, definition = generate_notification(notification, context)
        if message_direction == 'clientToServer':
            client_notification_names.append(name)
        elif message_direction == 'serverToClient':
            server_notification_names.append(name)
        else:
            client_notification_names.append(name)
            server_notification_names.append(name)
        definitions.append(definition)
    client_request_type = f'ClientNotification: TypeAlias = Union[{", ".join(client_notification_names)}]'
    server_request_type = f'ServerNotification: TypeAlias = Union[{", ".join(server_notification_names)}]'
    return [
        *definitions,
        client_request_type,
        server_request_type,
    ]


def generate_notification(notification: Notification, context: GeneratorContext) -> tuple[str, str]:
    method = notification['method']
    params = notification.get('params')
    name = notification['typeName']
    definition = f'class {name}(TypedDict):\n'
    definition += f"{indentation}method: Literal['{method}']\n"
    if params:
        definition += f'{indentation}params: {format_type(params, context)}'
    else:
        definition += f'{indentation}params: None'
    return (name, definition)
