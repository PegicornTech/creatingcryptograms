#!/usr/bin/python
import random
import string
import ascii
import argparse

alphabet = str(string.ascii_uppercase)
key=str(''.join(random.sample(alphabet,len(alphabet))))

print(key)
