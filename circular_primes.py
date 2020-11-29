from gmpy2 import is_prime
def circular_prime(n):
    n = str(n)
    count = 1
    while True:
        if count > len(str(n)):
            return True
        if not is_prime(int(n)):
            return False
        n = str(n)[1:] + str(n)[0]
        count += 1
