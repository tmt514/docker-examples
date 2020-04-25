FROM ubuntu:latest

RUN apt update
RUN apt install -y git

RUN git clone https://github.com/tmt514/docker-examples.git

WORKDIR "/docker-examples"

RUN apt install -y python3

CMD ["python3", "example-01-simple-server/server/server.py"]
