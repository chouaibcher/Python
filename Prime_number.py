# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Description:  Three different functions to check whether a given number is a prime.
#               Return True if it is a prime, False otherwise.
#               Those three functions, from a to c, decreases in efficiency
#               (takes longer time).

from math import sqrt


def is_prime_a(n):
    if n < 2:
        return False
    sqrt_n = int(sqrt(n))
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            return False
    return True


def is_prime_b(n):
    if n > 1:
        if n == 2:
            return True
        else:
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True
    return False


def is_prime_c(n):
    divisible = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisible += 1
    if divisible == 2:
        return True
    return False

#usinge sieve_of_eratosthenes algo
def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        if primes[p]:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, limit + 1) if primes[p]]

def is_prime_sieve(n):
    if n < 2:
        return False
    primes = sieve_of_eratosthenes(n)
    return n in primes

