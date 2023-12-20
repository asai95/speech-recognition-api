from typing import Dict, Optional

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class FactoryConfig(BaseModel):
    items: dict[str, str]


class AsyncAPIConfig(BaseModel):
    model_config = SettingsConfigDict(protected_namespaces=())

    model_name: str
    storage_name: str
    message_bus_name: str


class SyncAPIConfig(BaseModel):
    model_config = SettingsConfigDict(protected_namespaces=())

    model_name: str


class AppConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        extra="ignore",
    )

    # Factories
    models: Optional[Dict[str, str]] = None
    storages: Optional[Dict[str, str]] = None
    message_busses: Optional[Dict[str, str]] = None

    # APIs
    async_api: AsyncAPIConfig
    sync_api: SyncAPIConfig


app_config = AppConfig()  # type: ignore[call-arg]
