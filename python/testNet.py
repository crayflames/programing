#!/usr/bin/python2.7
import socket
target_host = "192.168.1.135"
target_port = 22
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host,target_port))
client.send("GET / HTTP/1.1\r\nHost: 192.168.1.135\r\n\r\n")
responce = client.recv(4096)
print responce