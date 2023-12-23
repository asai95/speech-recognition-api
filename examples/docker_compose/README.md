## Docker Compose example

This example demonstrates one of the ways to build containers:
API server and async worker.

In this example they communicate using Huey and Redis, saving data to
a local folder.

### Running the example

```bash
docker compose up
```

The service is going to be available at http://localhost:8888

You can visit http://localhost:8888/docs to try it right in your browser.
