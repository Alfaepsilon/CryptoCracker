from .. import cc_powmod
from .. import cc_gcd
import math
from .factorize import factorize


def SquareDiff(N, a):
    #a = relation_building(N)
    b = elimination(N, a)
    #b = sqrt(b_square)
    # a = 1
    # for c in relation:
    #     a = a * sqrt(c)
    k = 1
    for j in a:
        k = k * j
    # i = math.isqrt(i)
    # i = i % N
    k = k % N
    print(f"b: {b}, k: {k}")
    d = cc_gcd(N, (k - b) % N)
    p = d
    q = N // d
    print(f"p: {p}, q: {q}")
    #return [p, q]
    

def relation_building(N):
    #Read chapter about Smooth numbers and Sieves
    # This function should return a list of relations based on the input N

    return a

def elimination(N, a):
    # This function should perform Gaussian elimination on the relation matrix
    # and return a square number b^2
    #GaussianElimination(a)
    ax = []
    b = 1
    print(f"a: {a}")
    for i in a:
        print(cc_powmod(N, i, 2))
        prime_factors = factorize(cc_powmod(N, i, 2))
        p_unique = list(set(prime_factors))
        print(f"prime_factors: {prime_factors}, p_unique: {p_unique}")
        ai = {}
        for j in p_unique:
            ai[j] = prime_factors.count(j)
        ax.append(ai)

    combined = {}
    for dictionary in ax:
        for key, value in dictionary.items():
            combined[key] = combined.get(key, 0) + value
    
    for key in combined:
        b = b * (key ** (combined[key] // 2))
        print(f"key: {key}, value: {combined[key]}, b: {b}")
    #IDEA:
    #   prime_factors = [2, 3, 5, 7, 11]
    #   a1 = {2:2, 3:9, 5:2, 7:2, 11:1}
    #   a2 = {2:1, 3:7, 5:2, 7:1, 11:2}
    #   a3 = {2:3, 3:2, 5:2, 7:7, 11:3}
    # a1^2 * a2^2 * a3^2 = {2: 6, 3: 18, 5: 6, 7: 10, 11: 6}
    # b = 2^3 * 3^9 * 5^3 * 7^5 * 11^3 (DO THIS!)

    #x = np.linalg.solve(A, b)
    return b

SquareDiff(2525891, [1591, 3182, 4773, 5275, 5401])