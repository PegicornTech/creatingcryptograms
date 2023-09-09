#!/usr/bin/python
import random
import string
import ascii
import argparse

argParser = argparse.ArgumentParser()
argParser.add_argument("-m", "--message", help="Message you want to encrypt")
argParser.add_argument("-k", "--key", help="Key to encrypt message with")

args = argParser.parse_args()
message = args.message
key = args.key

alphabet = str(string.ascii_uppercase)

alphalist = list(alphabet)
alphakey = list(key)

upmessage=message.upper()

def encryptmessage(upmessage):
    sec = []
    for i in upmessage:
        if i not in alphabet:
            sec.append(i)
            secret=''.join(sec)
        else:
            pos = alphalist.index(i)
            s=alphakey[pos]
            sec.append(s)
            secret=''.join(sec)
    return secret
    

    
getsecret = encryptmessage(upmessage)
print(getsecret)
