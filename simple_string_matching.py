def solve(a,b):
    if len(a) > len(b) + 1:
        return False
    if a == b:
        return True
    try:
        i = a.index('*')
        j = a[::-1].index('*')
        x = a[-1:-j-1: -1]
        return a[:i]==b[:i] and x == b[::-1][:len(x)]
    except:
        return False
