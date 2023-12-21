from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class S3StorageConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="s3_storage_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )
    bucket_name: Optional[str] = None
    file_prefix: Optional[str] = ""


s3_storage_config = S3StorageConfig()
