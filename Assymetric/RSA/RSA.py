from CryptoCracker.Assymetric.Miscellaneous import cc_powmod
from CryptoCracker.Assymetric.Miscellaneous import cc_gcd
from .MillerRabin import MillerRabin
from CryptoCracker.Assymetric.Miscellaneous import exeucalgo

def setup():
    p = int(input("Enter first large prime: "))
    while(MillerRabin(p)):
        p = int(input("Error, number not prime. Try again: "))
    q = int(input("Enter second large prime: "))
    while(MillerRabin(p)):
        q = int(input("Error, number not prime. Try again: "))
    N = p*q
    e = int(input("Enter encryption exponent."))
    while(cc_gcd(e, (p - 1)*(q - 1)) != 1):
        e = int(input("Error, exponent not prime relative prime to product of p - 1 and q - 1. Try again: "))

    plaintext = 101500
    print(plaintext)
    ciphertext = encrypt(plaintext, e, N)
    decrypt(ciphertext, p, q, e, N)

def encrypt(plaintext, e, N):
    ciphertext = cc_powmod(N, plaintext, e)
    print(ciphertext)
    return ciphertext

def decrypt(ciphertext, p, q, e, N):
    d = exeucalgo(e, (p - 1)*(q - 1), 1)
    plaintext = cc_powmod(N, ciphertext, d)
    print(plaintext)

setup()