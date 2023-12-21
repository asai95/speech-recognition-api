from io import BytesIO
from typing import IO, Optional
from uuid import uuid4

import boto3
from boto3_type_annotations.s3 import ServiceResource

from speech_recognition_api.core.async_api.file_storage.interface import IFileStorage
from speech_recognition_api.extra.s3_storage.config import s3_storage_config


class S3Storage(IFileStorage):
    def __init__(
        self,
        resource: Optional[ServiceResource] = None,
        bucket_name: Optional[str] = None,
        file_prefix: Optional[str] = None,
    ) -> None:
        if not resource:
            resource = boto3.resource("s3")
        self.resource: ServiceResource = resource
        self.bucket = resource.Bucket(bucket_name or s3_storage_config.bucket_name)
        self.file_prefix = file_prefix or s3_storage_config.file_prefix or ""

    def save_file(self, file: IO) -> str:
        file_id = str(uuid4())
        self.bucket.upload_fileobj(Fileobj=file, Key=self.file_prefix + file_id)
        return file_id

    def get_file(self, file_id: str) -> IO:
        file = BytesIO()
        self.bucket.download_fileobj(Fileobj=file, Key=self.file_prefix + file_id)
        file.seek(0)
        return file
