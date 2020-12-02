def reverse(n):
    k = []
    while n:
        n, m = divmod(n, 10)
        k += [str(m)]
    return int(''.join(k))

def is_pal(n):
    n = str(n)
    return n == n[::-1]

def palindrome_chain_length(n):
    return 0 if is_pal(n) else 1 + palindrome_chain_length(n + reverse(n))
