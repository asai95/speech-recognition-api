FROM python:3.11-slim as base

RUN apt-get update && apt-get install -y ffmpeg
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cpu

FROM base as api
CMD [ \
	"gunicorn", \
	"speech_recognition_api:create_app()", \
	"-k", \
	"uvicorn.workers.UvicornWorker", \
	"-w", \
	"1", \
	"-b", \
	"0.0.0.0:8888" \
]

FROM base as worker
CMD [ \
	"huey_consumer", \
	"speech_recognition_api.extra.huey_bus.huey" \
]
