#!/usr/local/bin/python3

import string
import random
import os
import time

os.system("clear" if os.name == "posix" else "cls")

# variables
chars = "".join(string.printable.split())
string = "Password Generator"
password = ""

print("="*len(string))
print(string)
print("="*len(string))

number_of_pws = int(input("\nNumber of Passwords: "))
len_of_pws = int(input("Length of each Password: "))

print("\nGenerating Passwords...\n")
time.sleep(2)

for _ in range(number_of_pws):
    for _ in range(len_of_pws):
        password += random.choice(chars)
    print(">>> " + password)
    password = ""
    time.sleep(0.5)
print()
