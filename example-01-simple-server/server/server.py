#!/usr/bin/env python3
import socket
import json

PORT = 8080

def run_server():
  serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  serversocket.bind(('', PORT))
  serversocket.listen(5)
  print('Socket up running at port {}.'.format(PORT))

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
      response = bytes('OK: You have asked about {}\n'.format(task_string), 'UTF-8')
    except Exception as e:
      response = bytes('FAILED: JSON parsing error!\n', 'UTF-8')
      print(e)

    clientsocket.send(response)
    clientsocket.close()


if __name__ == '__main__':
  run_server()
