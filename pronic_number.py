def is_pronic(n):
    try:
        x = int(n**0.5)
        return x * (x + 1) == n
    except:
        return False
