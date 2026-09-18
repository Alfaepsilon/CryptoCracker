import math
import PaddingOracle

def bleichenbacher(N, e, ciphertext):
    k = (N.bit_length() + 7) // 8
    B = 2 ** (8 * (k - 2))
    M = [2 * B, 3 * B - 1]
    s = 2

    while M[0] != M[1]:
        #Find s such that the ciphertext is PKCS conforming
        while not decrypt_and_check(ciphertext, d, N):
            ciphertext = ciphertext * pow(s, e, N) % N
            s += 1
        a, b = M
        r_min = math.ceil((a * s - 3 * B + 1) / N)
        r_max = math.floor((b * s - 2 * B) / N)

        new_intervals = []

        for r in range(r_min, r_max + 1):
            lower = max(
                a,
                ceildiv(2 * B + r * N, s)
            )
            upper = min(
                b,
                (3 * B - 1 + r * N) // s
            )
            if lower <= upper:
                new_intervals.append((lower, upper))
        M = merge_intervals(
            intersect_sets(M, new_intervals)
        ) 
        #M = [max(M[0], (2 * B + r_min * N) // s), min(M[1], (3 * B - 1 + r_max * N) // s)]
