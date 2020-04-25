#!/bin/bash
docker build -t example02 .
for i in {0..9}
do
  docker run -p 1990$i:8080 -e SERVER_NAME="S$i" example02:latest &
done
