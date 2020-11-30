def is_odd(n):
    if n%1==0:
        n = int(n)
        return bool(abs(n)&1)
    return False
