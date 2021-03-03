# password manager
import random
import string
import hashlib
import binascii
import os

def store_pw():

    # Username
    username = input("Your username: ")

    # Website
    website = str(input("Website: "))

    # generate random password
    string.ascii_letters
    digit = int(input("How many digits do you want? (INT ONLY)"))
    password = ""

    for i in range(digit):
        char = random.choice(string.ascii_letters)
        password += char

    f = open("password.txt", "a")
    f.write(f"Username: {username} / Website: {website} / Password: {password}")
    f.close()

    return password

def search():
    pass    

print(store_pw())
