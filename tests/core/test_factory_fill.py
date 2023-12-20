from speech_recognition_api.core.common.model.factory import ModelFactory
from speech_recognition_api.core.common.utils import fill_factory
from speech_recognition_api.core.config import app_config
from tests.core.conftest import DummyModel


def test_factory_fill():
    ModelFactory.container = {}
    fill_factory(ModelFactory, app_config.models)
    dummy_model = ModelFactory.get("dummy")
    assert isinstance(dummy_model, DummyModel)
    ModelFactory.container = {}
