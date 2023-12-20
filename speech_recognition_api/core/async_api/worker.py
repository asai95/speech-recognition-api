def process_file(file_id: str) -> dict[str, str]:
    from speech_recognition_api.bootstrap import initialize_factories  # noqa: PLC0415
    from speech_recognition_api.core.async_api.dependencies import get_model, get_storage  # noqa: PLC0415

    initialize_factories()

    storage = get_storage()
    file = storage.get_file(file_id)
    model = get_model()
    transcription = model.process_file(file)
    return {"transcription": transcription}
