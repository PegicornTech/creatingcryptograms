#!/usr/bin/python
import ascii
import random
import string

def keygen():
    alphabet = str(string.ascii_uppercase)
    k = str(''.join(random.sample(alphabet,len(alphabet))))
    return k
key = keygen()
print(key)




