'''
Summary:            RSA Key Generation Principle

Author:             bruno.on.the.road@gmail.com
Version:            0.2
Date:               18 Sep 2018
Platform:           Ubuntu Server 18.04 LTS
python version:     3.6
RSA Key Generation Principle
----------------------------
1. Generate two large random primes, p and q, of approximately equal size
such that their product n = pq is of the required bit length, e.g. 1024 bits.
2. Compute n = pq and (φ) phi = (p-1)(q-1).
3. Choose an integer e, 1 < e < phi, such that gcd(e, phi) = 1.
4. Compute the secret exponent d, 1 < d < phi, such that ed ≡ 1 (mod phi).
   -modular arithmetics or congruences theorem-
5. The public key is (n, e) and the private key is (n, d).
Keep all the values d, p, q and phi secret.
* n is known as the modulus.
* e is known as the public exponent or encryption exponent or
just the exponent.
* d is known as the secret exponent or decryption exponent.
'''

from random import randrange
from math import gcd


def print_title():
    '''
    Prints the program title.
    '''
    print()
    print('Simple RSA encryption example')
    print('-' * 29)
    print()


def input_primes():
    '''
    Function that asks the user for input of primes(p,q).
    1) Returns primes(p,q)
    '''
    p = int(input('Select prime p: '))
    q = int(input('Select prime q: '))
    print()
    return (p, q)


def calc_modulus(primes):
    '''
    1) Modulus calculation with prime variables (p,q).
    2) Checks if variables contain primes.
    3) Returns the value of modulus
    '''
    p, q = primes[0], primes[1]
    n = p * q
    print('modulus n = p * q =  {}'.format(n))
    return n


def calc_phi(primes):
    '''
    1) Phi calculation with the given prime variables (p,q).
    2) Checks if variables contain primes.
    3) Returns the value of Phi.
    '''
    p, q = primes[0], primes[1]
    phi = (p - 1) * (q - 1)
    print('phi = (p - 1) * (q - 1) =  {}'.format(phi))
    print()
    return phi


def pick_public_key(phi):
    '''
    Public key generator (Random).
    1) Checks if random and Phi integer have no common factors except 1.
    2) Returns Public key
    '''
    gcd_is_one = False
    while not gcd_is_one:
        e = randrange(2, phi)
        if gcd(e, phi) == 1:
            gcd_is_one = True
    print('Choose Public key e: {}'.format(e))
    print('[*] {} and {} have no common factors except 1'.format(e, phi))
    print()
    return e


def calc_private_key(e, phi, n):
    '''
    Private key generator
    1) Mod inversion of public key and Phi.
    2) Returns Private key
    '''
    for d in range(1, n - 1):
        if (e * d - 1) % phi == 0:
            break
    print('Computed Private key d: {}'.format(d))
    print('[*] {} * {} mod {} = 1'.format(e, d, phi))
    print()
    return d


def input_message():
    '''
    Function that asks the user for input message(m) to encrypt.
    1) Returns message (m)
    '''
    m = int(input('Select message m: '))
    print()
    return m


def encrypt_message(e, n, m):
    '''
    Function for encryption
    1) Encrypted(c) = Message(m) ^ PublicKey(e) % Modulus(n)
    2) Returns encrypted message(c)
    '''
    # c = m ** e % n
    c = pow(m, e, n)
    print('Encrypted message c = m ** e % n = {}'.format(c))
    return c


def decrypt_message(d, n, c):
    '''
    Function for Decryption
    1) Decrypted(mm) = Encrypted(c) ^ PrivateKey(d) % Modulus(n)
    2) Returns decrypted message(mm)
    '''
    # mm = c ** d % n
    mm = pow(c, d, n)
    print('Decrypted message mm = c ** d % n = {}'.format(mm))
    print()
    return mm


def verify_message(m, mm):
    '''
    Function that verifies encrypted message(m) equals the decrypted message (mm)
    1) Prints message if equals or not-equals
    '''
    print('[*] Is m == mm ? ... ', end="")
    msg = 'OK WORKING EXAMPLE' if m == mm else 'NOT OK -- CHECK FOR ANY ERROR'
    print(msg)
    print()


def main():
    '''
    Main function executes Functions/Methodes/Code inside it accordingly.
    Without the main, the code would be executed even if the script were imported as a module.
    '''


    print_title()
    my_primes = input_primes()
    n = calc_modulus(my_primes)
    phi = calc_phi(my_primes)
    e = pick_public_key(phi)
    d = calc_private_key(e, phi, n)
    m = input_message()
    c = encrypt_message(e, n, m)
    mm = decrypt_message(d, n, c)
    verify_message(m, mm)

if __name__ == '__main__':
    main()