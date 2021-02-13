from math import gcd
def calculate_ratio(w, h):
    x = gcd(w, h)
    return '{}:{}'.format(w//x, h//x) if w and h else 'You threw an error'
