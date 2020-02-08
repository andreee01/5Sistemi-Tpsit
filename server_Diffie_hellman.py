import socket
import numpy as np
from random import random

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.10.107",1000)) 
s.listen()
conn, addr = s.accept()         # oggetto connessione(quello che fa scambiare i messaggi tubo di connessione) , indirizzo ip e porta del client
print("connesso con ",conn)

N =  int(conn.recv(4096).decode())
G =  int(conn.recv(4096).decode())
A =  int(conn.recv(4096).decode())


b=random.randint(2, N-1)    #scelgo un b compreso tra 1 e N
B=(G**b)%N
conn.sendall(str(B).encode())    #mando B

k=(A**b)%N                  #calcolo k
print(k)
s.close() 



