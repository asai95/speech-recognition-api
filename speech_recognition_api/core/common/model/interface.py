from abc import ABC, abstractmethod
from typing import IO


class ISpeechRecognitionModel(ABC):
    @abstractmethod
    def process_file(self, file: IO) -> str:
        ...
