from .. import cc_powmod
from .. import cc_gcd
import math
import numpy as np






def relation_building(N, limit=1000):
    """
    Build a list of relations for the quadratic sieve.

    Returns:
        relations"""
    

# ---------------------------
# GF(2) RREF and Nullspace
# ---------------------------

def rref_gf2(A):
    A = A.copy().astype(np.uint8)

    rows, cols = A.shape
    pivots = []
    row = 0

    for col in range(cols):

        candidates = np.flatnonzero(A[row:, col])

        if len(candidates) == 0:
            continue

        pivot = row + candidates[0]

        A[[row, pivot]] = A[[pivot, row]]

        mask = A[:, col] == 1
        mask[row] = False

        A[mask] ^= A[row]

        pivots.append(col)
        row += 1

        if row == rows:
            break

    return A, pivots


def nullspace_gf2(A):
    """
    Return a basis of the nullspace of A over GF(2).
    """

    R, pivots = rref_gf2(A)

    rows, cols = R.shape

    free_cols = [c for c in range(cols) if c not in pivots]

    basis = []

    for free_col in free_cols:

        x = np.zeros(cols, dtype=np.uint8)
        x[free_col] = 1

        for pivot_row, pivot_col in reversed(list(enumerate(pivots))):
            x[pivot_col] = (
                np.dot(
                    R[pivot_row, pivot_col + 1:],
                    x[pivot_col + 1:]
                ) % 2
            )

        basis.append(x)

    return basis


# ---------------------------
# Factor-base utilities
# ---------------------------

def exponent_vector(n, factor_base):
    """
    Return parity vector of factorization of n over factor_base.

    Returns:
        row, exponents

    or

        None, None

    if n is not factor-base smooth.
    """

    exponents = []

    for p in factor_base:
        e = 0

        while n % p == 0:
            n //= p
            e += 1

        exponents.append(e)

    if n != 1:
        return None, None

    parity = [e % 2 for e in exponents]

    return parity, exponents


# ---------------------------
# Relation matrix builder
# ---------------------------

def build_relation_matrix(N, relations, factor_base):
    """
    Build matrix whose rows are exponent parities.

    Uses:
        Q(a) = a^2 mod N

    for demonstration purposes.
    """

    rows = []
    exponent_rows = []
    relation_values = []

    for a in relations:

        q = cc_powmod(N, a, 2)

        parity, exponents = exponent_vector(q, factor_base)

        if parity is None:
            continue

        rows.append(parity)
        exponent_rows.append(exponents)
        relation_values.append(a)

    if not rows:
        raise ValueError("No factor-base smooth relations found.")

    return (
        np.array(rows, dtype=np.uint8),
        exponent_rows,
        relation_values,
    )


# ---------------------------
# Congruence-of-squares step
# ---------------------------

def square_differences(N, relations, factor_base):

    A, exponent_rows, smooth_relations = build_relation_matrix(
        N,
        relations,
        factor_base,
    )

    print("Relation matrix:")
    print(A)

    #
    # Dependencies among relations:
    #
    # A has shape:
    #   (#relations, #primes)
    #
    # We need vectors selecting rows:
    #
    dependencies = nullspace_gf2(A.T)

    print("\nDependencies:")
    for d in dependencies:
        print(d)

    factors = []

    for dep in dependencies:

        selected = np.where(dep == 1)[0]

        if len(selected) == 0:
            continue

        #
        # X = product of selected relations
        #
        X = 1

        for idx in selected:
            X = (X * smooth_relations[idx]) % N

        #
        # Sum exponent vectors
        #
        total_exp = [0] * len(factor_base)

        for idx in selected:
            row_exp = exponent_rows[idx]

            for j in range(len(factor_base)):
                total_exp[j] += row_exp[j]

        #
        # Dependency guarantees these are even
        #
        if any(e % 2 for e in total_exp):
            continue

        Y = 1

        for p, e in zip(factor_base, total_exp):
            Y *= p ** (e // 2)

        d = math.gcd((X - Y) % N, N)

        if 1 < d < N:
            factors.append((d, N // d))

    return factors


# ---------------------------
# Example
# ---------------------------

if __name__ == "__main__":

    N = 2525891

    # Example relations
    relations = relation_building(N)

    factor_base = [
        2, 3, 5, 7, 11, 13, 17, 19, 23
    ]

    try:
        result = square_differences(
            N,
            relations,
            factor_base,
        )

        print("\nFactors found:")
        print(result)

    except ValueError as e:
        print(e)