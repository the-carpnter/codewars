def pattern(n, x = ''):
    if n <= 0:
        return ''
    x = str(n) + x
    return x if n == 1 else pattern(n-1, x) + '\n' + x
