import uvicorn

from speech_recognition_api.bootstrap import create_app

if __name__ == "__main__":
    app = create_app()
    uvicorn.run(app, host="localhost", port=8888)
