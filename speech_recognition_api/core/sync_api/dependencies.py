from speech_recognition_api.core.common.model.factory import ModelFactory
from speech_recognition_api.core.common.model.interface import ISpeechRecognitionModel
from speech_recognition_api.core.config import app_config


def get_model() -> ISpeechRecognitionModel:
    return ModelFactory.get(app_config.async_api.model_name)
