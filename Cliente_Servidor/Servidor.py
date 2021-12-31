#Servidor en python Raspberry
import socket
a=True
s=socket.socket()
s.bind(("192.168.1.103",2016))
s.listen(10)
sc,addrc = s.accept()
while a==True:
    mensaje = sc.recv(1024)
    print mensaje
    if mensaje=="F":
        a=False
    respuesta=raw_input("Diga su respuesta: ")
    sc.send(respuesta)
s.close()
print "Bye Bye"
