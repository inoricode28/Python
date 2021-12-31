#cliente
import socket
s=socket.socket()
s.connect(("192.168.1.169",2016))
while True:
    mensaje=input("Diga Su mensaje: ")
    s.send(mensaje)
    reci=s.recv(1024)
    print("Resondio",str(reci))

