import math
import numpy  



def isPrime(n): #verifico se il numero inserito è primo

    for p in range(2, int(numpy.sqrt(n)) + 1):
        if (n % p == 0):
            return False
    return True


while True:
    print("Inserire p:")    #inserisco i due numeri
    p = int(input())

    print("inserire q:")
    q = int(input())

    if isPrime(p):      #controllo che entrambi siano primi
        if isPrime(q):
            break
        else:
            print("numero q non primo riprovare")
    else:
        print("numero p non primo riprovare")



n = int(p * q) #calcolo n

print("n =", n)

m = 0

if(p>q):
    maggiore = p
else:
    maggiore = q

while(m==0):
    if((maggiore % (p-1) == 0) and (maggiore % (q-1) == 0)): #cerco mcm
        m = maggiore
        break
    maggiore = maggiore + 1

print("m =", m) 

#inserimento c
while(True):
    print("Inserire un c che sia compreso tra 1 e m e che verifici la condizione mcd(m,c)=1:")
    c = int(input())
    if(math.gcd(c, m)==1):  #condizione affinché c sia valido
        break
    else:
        print("Il numero inserito non è compreso tra 1 e m o non rispetta la condizione mcd(m,c)=1:")

d = 0

while(True):
    if((c*d)%m == 1): #cerco d, d deve essere compreso tra 0 ed m tale che (cd)MOD m=1
        break
    else:
        d = d + 1

print("d =", d)

print("Chiave pubblica: n=", n," c=", c)

print("Chiave privata: m=", m," d=", d) 

#criptazione dato
a = int(input("Inserisci un numero: "))
cryptedA = (a**c)%n 
print(f"Numero cryptato [{a}]: {cryptedA}")

#Decriptazione dato
uncryptedA = (cryptedA**d)%n
print(f"Numero decriptato[{cryptedA}]: {uncryptedA}")
