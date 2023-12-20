from typing import ClassVar

from speech_recognition_api.core.common.factory_interface import IFactory
from speech_recognition_api.core.common.model.interface import ISpeechRecognitionModel


class ModelFactory(IFactory):
    container: ClassVar[dict[str, ISpeechRecognitionModel]] = {}

    @classmethod
    def register(cls, name: str, object_: ISpeechRecognitionModel) -> None:
        cls.container[name] = object_

    @classmethod
    def get(cls, name: str) -> ISpeechRecognitionModel:
        return cls.container[name]

    @classmethod
    def is_registered(cls, name: str) -> bool:
        return name in cls.container
