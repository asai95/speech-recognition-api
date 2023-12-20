## Speech Recognition API

Simple but extensible API for Speech Recognition.

### Installation

```bash
git clone https://github.com/asai95/speech-recognition-api.git
pip install -r requirements.txt
```

### Usage
Simple dev server:
```bash
python -m speech_recognition_api
```

Gunicorn:
```bash
gunicorn "speech_recognition_api:create_app()" -k uvicorn.workers.UvicornWorker -w 1 -b 127.0.0.1:8888
```

Celery worker:
```bash
celery -A speech_recognition_api.extra.celery_bus worker
```

Huey worker:
```bash
huey_consumer speech_recognition_api.extra.huey_bus.huey
```

### Description

This project is aimed to simplify building and deploying of applications that require
Speech Recognition functionality.

It is designed to work as a microservice, so it does not handle stuff like auth and rate limits.

However, it is also designed to be extensible in 3 major areas:

* Models
* File Storages
* Message Busses

There are two types of APIs available.

### Synchronous API

This API is designed for simple workloads, where the machine that runs the server is capable of
running a model. You probably want to limit the payload size for these routes.

**Routes:**

`POST /sync/v1/transcribe`

Accepts an audio file. File type depends on the model that is being used.

Returns an object with transcription.
[Response model](speech_recognition_api/core/sync_api/dto.py).


### Asynchronous API

This API is designed to process files asynchronously, i.e. to create tasks and process them
on separate workers. Typical client flow here is as follows:

* Create a task and receive task id
* Use this task id to periodically check if it is completed.

**Routes:**

`POST /async/v1/transcribe`

Accepts an audio file. File type depends on the model that is being used.

Returns an object with async task id.
[Response model](speech_recognition_api/core/async_api/dto.py).

`GET /async/v1/transcribe/{task_id}`

Returns an object with status and a transcription (if transcription is available).
[Response model](speech_recognition_api/core/async_api/dto.py).

### Configuring

TODO
