#!/usr/local/bin/python3
# Made by @swisscoding on Instagram

from colored import stylize, fg
import string, random

# decoration
print(stylize("\n---- | Password generator | ----\n", fg("red")))

# variables
chars = "".join(string.printable.split())
password = ""

# user interaction
number_of_pws = int(input("Number of passwords: "))
len_of_pws = int(input("Length of each password: "))

# output
print("\nGenerating passwords...\n")

for _ in range(number_of_pws):
    for _ in range(len_of_pws):
        password += random.choice(chars)
    print(">>> " + password)
    password = ""
print()
