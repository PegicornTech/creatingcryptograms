#!/usr/bin/python
import random
import string
import ascii
alphabet = str(string.ascii_uppercase)
key=str(''.join(random.sample(alphabet,len(alphabet))))

alphalist = list(alphabet)
alphakey = list(key)

#print(alphalist)
#print(alphakey)

mess = 'secret encrypted message'
message=mess.upper()

def encryptmessage(message):
    sec = []
    for i in message:
        if i not in alphabet:
            sec.append(i)
            secret=''.join(sec)
        else:
            pos = alphakey.index(i)
            s=alphalist[pos]
            sec.append(s)
            secret=''.join(sec)
    return secret
getsecret = encryptmessage(message)
print(getsecret)

def decryptmessage(getsecret):
    plaintext = []
    for i in getsecret:
        if i not in alphabet:
            plaintext.append(i)    
            asecret=''.join(plaintext)    
        else:
            pos1 = alphalist.index(i)
            a=alphakey[pos1]
            plaintext.append(a)
            asecret=''.join(plaintext)
    return asecret
agetseceret = decryptmessage(getsecret)
print(agetseceret)
print(key)
