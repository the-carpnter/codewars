f = lambda s: sum(ord(c) for c in s.upper()) if s and all(c.isalpha() for c in s) else 0
def compare(s1,s2):
    return f(s1) == f(s2)
