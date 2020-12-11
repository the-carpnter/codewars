def shorter_reverse_longer(a,b):
    x, y = sorted([b,a], key = len)
    return x + y[::-1] + x
