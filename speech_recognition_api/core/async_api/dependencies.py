from speech_recognition_api.core.async_api.file_storage.factory import FileStorageFactory
from speech_recognition_api.core.async_api.file_storage.interface import IFileStorage
from speech_recognition_api.core.async_api.message_bus.factory import MessageBusFactory
from speech_recognition_api.core.async_api.message_bus.interface import IMessageBus
from speech_recognition_api.core.common.model.factory import ModelFactory
from speech_recognition_api.core.common.model.interface import ISpeechRecognitionModel
from speech_recognition_api.core.config import app_config


def get_model() -> ISpeechRecognitionModel:
    return ModelFactory.get(app_config.async_api.model_name)


def get_storage() -> IFileStorage:
    return FileStorageFactory.get(app_config.async_api.storage_name)


def get_message_bus() -> IMessageBus:
    return MessageBusFactory.get(app_config.async_api.message_bus_name)
