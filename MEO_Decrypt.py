from passlib.hash import bcrypt
from libs import pingo
import sys
import os
import datetime

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

print("\n*************************************************")
print("MEO DECRYPT")
print("*************************************************")

text_file = open(resource_path ("4_DIGIT_PINS.txt"), "r")

PINS = text_file.read().splitlines()

hash = input('Hash to crack: ')
length = len(PINS)

correct_PIN = ""
found = 0
for (index, PIN) in enumerate(PINS):
    pingo(index, length, prefix='Checking PINS:')
    correct = bcrypt.verify(PIN, hash)
    if (correct):
        correct_PIN = PIN
        found += 1
        break

if (found == 1):
    print("\n\nPIN found:", correct_PIN)
else:
    print("An error has occured, check hash is in correct format")
   
    input('Press Enter to Exit')
