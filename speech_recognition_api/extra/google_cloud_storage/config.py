from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class GoogleCloudStorageConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="google_cloud_storage_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )
    project_id: Optional[str] = None
    bucket_name: Optional[str] = None
    file_prefix: Optional[str] = ""


google_cloud_storage_config = GoogleCloudStorageConfig()
