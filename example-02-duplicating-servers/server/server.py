#!/usr/bin/env python3
import socket
import json
import sys
import os

PORT = 8080
SERVER_NAME = os.environ['SERVER_NAME']

def run_server():
  serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  serversocket.bind(('', PORT))
  serversocket.listen(5)

  
  sys.stderr.write('[Server {}]: Socket up running at port {}.\n'.format(SERVER_NAME, PORT))

  while True:
    (clientsocket, address) = serversocket.accept()
    json_data = ''
    while True:
      partial_data = clientsocket.recv(1024)
      if not partial_data:
        break
      json_data += partial_data.decode('UTF-8')
    
    try:
      task = json.loads(json_data)
      task_string = json.dumps(task, indent=2)
      response = bytes('[Server {}] OK: You have asked about {}\n'.format(SERVER_NAME, task_string), 'UTF-8')
    except Exception as e:
      response = bytes('[Server {}] FAILED: JSON parsing error!\n'.format(SERVER_NAME), 'UTF-8')
      sys.stderr.write('[Server {}] {}\n'.format(SERVER_NAME, e))

    clientsocket.send(response)
    clientsocket.close()


if __name__ == '__main__':
  run_server()
