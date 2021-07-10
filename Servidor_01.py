#!/usr/bin/env python3

import socket

HOST = '192.168.1.169'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            """
            if not data:
                break
            """
            if data.decode()== "exit":
                break
            print('Received',data.decode())
            respuesta=input("Diga su respuesta: ")
            #conn.sendall(data)
            conn.sendall(respuesta.encode())
