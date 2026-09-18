from .MillerRabin import MillerRabin

def Mersenne():
    n = 2*2
    num = int(input("Enter the number of Mersenne primes you want to find: "))
    count = 0
    while True:
        if not MillerRabin(n - 1):
            print(n - 1)
            count += 1
        if count == num:
            break
        n *= 2
Mersenne()