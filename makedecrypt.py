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

def decryptmessage(upmessage):
    plaintext = []
    for i in upmessage:
        if i not in alphabet:
            plaintext.append(i)    
            smessage=''.join(plaintext)   
        else:
            pos1 = alphakey.index(i)
            a=alphalist[pos1]
            plaintext.append(a)
            smessage=''.join(plaintext)
    return smessage

newmessage = decryptmessage(message)

print(newmessage)
