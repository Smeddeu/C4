#!/usr/bin/python3

'''
Title:         RSA Key Generation
Version:       2.0
Author:        Desmet Tom
E-mail:        desmet_t@hotmail.com
Date:          29/10/2018
'''

import random

#----------Function to find greatest common divisor----------#
def gcd(e, phi):
    '''
    Finds greatest common divisor
    '''
    while phi != 0:
        e, phi = phi, e % phi
    return e

#----------Function Mod Inverser-----------------------------#
def modinv(e, phi):
    '''
    Finds Mod inverser
    '''
    for x in range(1, phi):
        if (e * x) % phi == 1:
            return x
    return None

#----------Check if Prime------------------------------------#
def if_prime(num):
    '''
    Checks if number is prime
    '''
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
            break
        else:
            return True
    else:
        return False

#----------Title---------------------------------------------#
def print_title():
    '''
    Prints program title
    '''
    print("Simple RSA Encryption example:")
    print("------------------------------------""\n")

#----------User Input + Check--------------------------------#
def if_int():
    '''
    Asks User for input of two prime numbers as integers.

    1)User input of prime 'p'
    2)Check if 'p' type is Integer with if_integer()
    3)Check if 'p' is prime number with if_prime()
    4)User input of prime 'q'
    2)Check if 'q' type is Integer with if_integer()
    3)Check if 'q' is prime number with if_prime()
    '''
    global p
    global q
    while True:
        try:
            p = int(input("Select prime p: "))
            pprime = if_prime(p)
        except Exception:
            print("Only integers allowed")
            continue
        if pprime == False:
            print("Not A prime number")
            continue
        else:
            break


    while True:
        try:
            q = int(input("Select prime q: "))
            qprime = if_prime(q)
        except Exception:
            print("Only integers allowed")
            continue
        if qprime == False:
            print("Not A prime number")
            continue
        else:
            break

#----------Calculate Mod-------------------------------------#
def cal_mod():
    '''
    Modulus 'n' calculation with prime variables 'p' & 'q'
    '''
    global n
    n = p * q
    print("Modulus: n = p*q = {} * {} = {}".format(p, q, n))
    print("")

#----------Calculate Phi-------------------------------------#
def cal_phi():
    '''
    Phi 'phi' calculation with the given prime variables 'p' & 'q'
    '''
    global phi
    phi = (p-1)*(q-1)
    print("phi = (p-1)*(q-1) = ({}-1)*({}-1) = {}".format(p, q, phi))
    print("")

#----------Choose Random E-----------------------------------#
def cal_pub_key():
    '''
    Public key generator (Random).
    Checks if random and Phi integer have no common factors except 1.
    '''
    global e
    e = random.randrange(1,phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    print("Choose Public Key e: {}".format(e))
    print("[*]{} and {} have no common factors except 1".format(e, phi))
    print("")

#----------Calculate PrivateKey------------------------------#
def cal_priv_key():
    '''
    Private key generator
    Mod inversion of public key and Phi.
    '''
    global d
    d = modinv(e, phi)
    print("Computed Private Key d: " + str(d))
    print("[*]{}*{} mod {} = 1".format(e, d, phi))
    print("")

#----------Message to encryot--------------------------------#
def message():
    '''
    Function that asks the user for input message(m) to encrypt.

    1)User input of message 'm'
    2)Check if 'm' type is Integer with if_integer()
    3)Check if message 'm' is smaller then modulus 'n'
    '''
    global m
    while True:
        try:
            m = int(input("Select Message m: "))
        except Exception:
            print("Only integers allowed")
            continue
        if m >= n:
            print("Message needs to be smaller than modulus N")
            continue
        else:
            break

#----------ENCRYPT Message(c)--------------------------------#
def encrypt_message():
    '''
    Encrypts message
    '''
    global c
    c = m ** e % n
    print("Encrypted message c = m ** e % n = {}".format(c))

#----------DECRYPT Message(mm)-------------------------------#
def decrypt_message():
    '''
    Decrypts message
    '''
    global mm
    mm = c ** d % n
    print("Decrypted message mm = c ** d % n = {}".format(mm))

#----------Verify Message------------------------------------#
def verify_message():
    '''
    Prints message if equals or not-equals
    Function that verifies encrypted message(m) equals the decrypted message (mm)
    '''
    print('[*] Is m == mm ? ... ', end="")
    msg = 'OK WORKING EXAMPLE' if m == mm else 'NOT OK -- CHECK FOR ANY ERROR'
    print(msg)
    print()

#----------MAIN - BEGINNING-----------------------------------------#
def main():
    '''
    Main function executes Functions/Methodes/Code inside it accordingly.
    '''
    print_title()
    if_int()
    cal_mod()
    cal_phi()
    cal_pub_key()
    cal_priv_key()
    message()
    encrypt_message()
    decrypt_message()
    verify_message()


if __name__ == "__main__":
    main()