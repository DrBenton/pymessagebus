import typing as t

import pymessagebus.api as api
from pymessagebus._messagebus import MessageBus


class CommandBus(api.CommandBus):
    def __init__(self):
        self._messagebus = MessageBus()

    def add_handler(self, message_class: type, message_handler: t.Callable) -> None:
        if self._messagebus.has_handler_for(message_class):
            raise api.CommandHandlerAlreadyRegisteredForATypeError(
                f"A command handler is already registed for message class '{message_class}'."
            )
        self._messagebus.add_handler(message_class, message_handler)

    def handle(self, message: object) -> t.Any:
        if not self._messagebus.has_handler_for(message.__class__):
            raise api.CommandHandlerNotFoundError(
                f"No command handler is registed for message class '{message.__class__}'."
            )
        result = self._messagebus.handle(message)
        return result[0]

    def has_handler_for(self, message_class: type) -> bool:
        return self._messagebus.has_handler_for(message_class)