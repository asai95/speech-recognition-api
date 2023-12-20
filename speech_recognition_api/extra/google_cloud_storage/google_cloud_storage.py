from io import BytesIO
from typing import IO, Optional
from uuid import uuid4

from google.cloud import storage

from speech_recognition_api.core.async_api.file_storage.interface import IFileStorage
from speech_recognition_api.extra.google_cloud_storage.config import google_cloud_storage_config


class GoogleCloudStorage(IFileStorage):
    def __init__(
        self,
        project_id: Optional[str] = None,
        bucket_name: Optional[str] = None,
        file_prefix: Optional[str] = None,
    ) -> None:
        self.client = storage.Client(
            project=project_id or google_cloud_storage_config.project_id,
        )
        self.bucket_name = bucket_name or google_cloud_storage_config.bucket_name
        self.file_prefix = file_prefix or google_cloud_storage_config.file_prefix or ""

    def save_file(self, file: IO) -> str:
        file_id = str(uuid4())
        bucket = self.client.get_bucket(self.bucket_name)
        blob = bucket.blob(self.file_prefix + file_id)
        blob.upload_from_file(file)
        return file_id

    def get_file(self, file_id: str) -> IO:
        bucket = self.client.get_bucket(self.bucket_name)
        blob = bucket.blob(self.file_prefix + file_id)
        return BytesIO(blob.download_as_bytes())
