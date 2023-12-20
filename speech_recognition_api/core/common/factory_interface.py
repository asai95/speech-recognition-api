from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class IFactory(Generic[T], ABC):
    @classmethod
    @abstractmethod
    def register(cls, name: str, object_: T) -> None:
        ...

    @classmethod
    @abstractmethod
    def get(cls, name: str) -> T:
        ...

    @classmethod
    @abstractmethod
    def is_registered(cls, name: str) -> bool:
        ...
