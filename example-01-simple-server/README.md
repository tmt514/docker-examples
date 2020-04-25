# How To Start?

First you build the image from the Dockerfile.

```
$ docker build -t example01 . --no-cache
```

If you build multiple times, you can omit `--no-cache` in order to save time.
After the above step, you will have an image tagged with `example01:latest`.

To run the CMD specified in the Dockerfile, you run this:

```
$ docker run -p 12345:8080 example01:latest
```

Where 12345 is the port you want to forward to, and 8080 is the port you exposed
from the container. After the server is up, you can test locally by throwing
messages to `localhost:12345`. The simplest way is to use the netcat tool `nc`.

```
$ nc localhost 12345
{"message": "Good Morning!"}
```
