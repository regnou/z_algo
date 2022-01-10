#!/usr/bin/env python3
# arithmetic functions
# christoph dürr - jill-jênn vie - 2013-2015


# snip{ pgcd
def pgcd(a, b):
    """Greatest common divisor for a and b
    """
    return a if b == 0 else pgcd(b, a % b)
# snip}


# snip{ bezout
def bezout(a, b):
    """Bezout coefficients for a and b
    """
    if b == 0:
        return (1, 0)
    else:
        u, v = bezout(b, a % b)
        return (v, u - (a // b) * v)


def inv(a, p):
    """Inverse of a in :math:`{\mathbb Z}_p`
    """
    return bezout(a, p)[0] % p
# snip}


# snip{ binom
def binom(n, k):
    """Binomial coefficients for :math:`n \choose k`
    """
    prod = 1
    for i in range(k):
        prod = (prod * (n - i)) // (i + 1)
    return prod
# snip}


# snip{ binom_modulo
def binom_modulo(n, k, p):
    """Binomial coefficients for :math:`n \choose k`, modulo p
    """
    prod = 1
    for i in range(k):
        prod = (prod * (n - i) * inv(i + 1, p)) % p
    return prod
# snip}
