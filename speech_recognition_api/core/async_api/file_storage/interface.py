from abc import ABC, abstractmethod
from typing import IO


class IFileStorage(ABC):
    @abstractmethod
    def save_file(self, file: IO) -> str:
        ...

    @abstractmethod
    def get_file(self, file_id: str) -> IO:
        ...
