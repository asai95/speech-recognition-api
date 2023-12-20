from abc import ABC, abstractmethod
from typing import Literal

SUCCESS = "SUCCESS"
PENDING = "PENDING"
FAILED = "FAILED"

TASK_STATUS = Literal["SUCCESS", "PENDING", "FAILED"]


class IMessageBus(ABC):
    @abstractmethod
    def create_task(self, file_id: str) -> str:
        ...

    @abstractmethod
    def get_task_status(self, task_id: str) -> TASK_STATUS:
        ...

    @abstractmethod
    def get_task_result(self, task_id: str) -> str:
        ...
