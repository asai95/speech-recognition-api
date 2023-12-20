from typing import Any

from fastapi import FastAPI

from speech_recognition_api.core.async_api.async_api import async_router
from speech_recognition_api.core.async_api.file_storage.factory import FileStorageFactory
from speech_recognition_api.core.async_api.message_bus.factory import MessageBusFactory
from speech_recognition_api.core.common.model.factory import ModelFactory
from speech_recognition_api.core.common.utils import fill_factory
from speech_recognition_api.core.config import app_config
from speech_recognition_api.core.sync_api.sync_api import sync_router


def initialize_factories() -> None:
    fill_factory(ModelFactory, app_config.models)
    fill_factory(MessageBusFactory, app_config.message_busses)
    fill_factory(FileStorageFactory, app_config.storages)


def create_app(**fastapi_kwargs: Any) -> FastAPI:  # noqa: ANN401
    initialize_factories()

    if "title" not in fastapi_kwargs:
        fastapi_kwargs["title"] = "Speech Recognition API"

    if "description" not in fastapi_kwargs:
        fastapi_kwargs["description"] = "Simple but extensible API for Speech Recognition."

    if "version" not in fastapi_kwargs:
        fastapi_kwargs["version"] = "0.1.0"

    app = FastAPI(**fastapi_kwargs)
    app.include_router(sync_router)
    app.include_router(async_router)
    return app
