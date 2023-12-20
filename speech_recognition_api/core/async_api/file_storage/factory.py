from typing import ClassVar

from speech_recognition_api.core.async_api.file_storage.interface import IFileStorage
from speech_recognition_api.core.common.factory_interface import IFactory


class FileStorageFactory(IFactory):
    container: ClassVar[dict[str, IFileStorage]] = {}

    @classmethod
    def register(cls, name: str, object_: IFileStorage) -> None:
        cls.container[name] = object_

    @classmethod
    def get(cls, storage_name: str) -> IFileStorage:
        return cls.container[storage_name]

    @classmethod
    def is_registered(cls, name: str) -> bool:
        return name in cls.container
