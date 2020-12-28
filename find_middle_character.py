def get_middle(s):
    x = len(s)
    return s[x//2 - (x%2 == 0): x//2 + 1]
