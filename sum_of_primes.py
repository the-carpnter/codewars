from gmpy2 import is_prime
def sum_primes(l, u):
    return sum(filter(is_prime, range(max(l,0), u+1)))
