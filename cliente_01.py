#!/usr/bin/env python3

import socket
a=True
HOST = '192.168.1.169'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #s.sendall(b'Hello, world')
    while a==True:
        mensaje = input("Diga su mensaje: ")
        if mensaje == "exit":
           a=False
        s.send(mensaje.encode())
        data = s.recv(1024)
        
        print('Received', data.decode())
