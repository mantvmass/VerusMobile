import socket
import json
from pprint import pprint

username = 'RQpWNdNZ4LQ5yHUM3VAVuhUmMMiMuGLUhT.atom'
password = 0

host    = 'ap.luckpool.net'
port    = 3956

print("Connect to {}:{}".format(host,port))

# server connection
sock    = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host,port))

# subscribe
sock.sendall(b'{"id": 1, "method": "mining.subscribe", "params": []}\n')
response = json.loads(sock.recv(1024))
pprint(response)

# authorize workers
sock.sendall(b'{"params": ["RQpWNdNZ4LQ5yHUM3VAVuhUmMMiMuGLUhT.atom", "x"], "id": 2, "method": "mining.authorize"}\n')
response = json.loads(sock.recv(1024))
pprint(response)

response = ''
while response.count('\n') < 4:
    response += sock.recv(1024).decode("utf-8")

#get rid of empty lines
responses = [json.loads(res) for res in response.split('\n') if len(res.strip())>0]

pprint(responses)

sock.close()