from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class WhisperModelConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="whisper_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )
    name: Optional[str] = None


whisper_config = WhisperModelConfig()
