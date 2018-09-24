from abc import ABC, abstractmethod
import typing as t


class MessageBus(ABC):
    @abstractmethod
    def add_handler(self, message_class: type, message_handler: t.Callable) -> None:
        pass

    @abstractmethod
    def handle(self, message: object) -> t.List[t.Any]:
        pass

    @abstractmethod
    def has_handler_for(self, message_class: type) -> bool:
        pass


class MessageHandlerMappingRequiresATypeError(TypeError):
    pass


class MessageHandlerNotFoundError(KeyError):
    pass