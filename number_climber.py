def climb(n):
    return climb(n>>1) + [n] if n else []   
