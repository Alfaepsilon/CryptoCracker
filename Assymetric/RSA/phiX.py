from CryptoCracker.Assymetric.RSA import MillerRabin
def phiX():
    X = 100
    a = 0
    for i in range(2, X - 1):
        if(MillerRabin(i) == 0):
            a = a + 1
    print(a)