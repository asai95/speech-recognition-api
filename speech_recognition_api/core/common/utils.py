from importlib import import_module
from typing import Type

from speech_recognition_api.core.common.factory_interface import IFactory


def fill_factory(factory_class: Type[IFactory], factory_config: dict[str, str] | None) -> None:
    if factory_config:
        for name, class_path in factory_config.items():
            if factory_class.is_registered(name):
                factory_class.get(name)
            else:
                split_path = class_path.split(".")
                module_path = ".".join(split_path[:-1])
                class_name = split_path[-1]
                module = import_module(module_path)
                klass = getattr(module, class_name)
                factory_class.register(name, klass())
