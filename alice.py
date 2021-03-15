#repl.it
from Crypto.PublicKey import RSA #Python cryptography libray
from Crypto.Hash import SHA256 #hash libray
from Crypto.Signature import pss #message authentication
import socket

key = RSA.generate(2048)

# this generates the private key
getPublicKey=key.publickey()
private_Key=key.export_key().decode()


#write private key to a file privatekey.dat
file=open("C:/Users/willi/Desktop/A2/SectionA/privatekey.dat", mode='w')
for y in private_Key:
    file.write(y)
file.close()


#generates the public key
getPublicKey=key.publickey()
public_Key=getPublicKey.export_key().decode()


#store the public key to the file publickey.dat
file=open("C:/Users/willi/Desktop/A2/publickey.dat", mode='w')
for x in public_Key:
    file.write(x)# 
file.close()




# initiating communication
s=socket.socket()
host=socket.gethostname()
port=1345
s.connect((host,port))


#sending a message to bob
msg="To prevent the spread of germs, you should wash your hands with soap and water for at least 20 seconds or use a hand sanitizer with at least 60% alcohol toclean hand"

privKey=RSA.import_key(open('privatekey.dat').read())#the private key is loaded from the file
print("Hashing message")
hashed_obj=SHA256.new(msg)#creating a fresh SHA256 hash object
signature=pss.new(privKey).sign(hashed_obj)#alice signs the message

s.send(signature)#signature sent
confirmed=s.recv(2048).decode()

s.send(msg)#message sent
print("Sending message...")
confirmed= s.recv(2048).decode()
print(confirmed)
s.close()
























