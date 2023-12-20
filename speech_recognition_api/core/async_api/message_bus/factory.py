from typing import ClassVar

from speech_recognition_api.core.async_api.message_bus.interface import IMessageBus
from speech_recognition_api.core.common.factory_interface import IFactory


class MessageBusFactory(IFactory[IMessageBus]):
    container: ClassVar[dict[str, IMessageBus]] = {}

    @classmethod
    def register(cls, name: str, object_: IMessageBus) -> None:
        cls.container[name] = object_

    @classmethod
    def get(cls, name: str) -> IMessageBus:
        return cls.container[name]

    @classmethod
    def is_registered(cls, name: str) -> bool:
        return name in cls.container
