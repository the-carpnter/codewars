def find_digit(n, i):
    if i < 0:
        return -1
    n, m = divmod(abs(n), 10)
    return m if i==1 else find_digit(n, i-1)
