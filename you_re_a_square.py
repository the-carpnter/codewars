def is_square(n):    
    try:
        return n**0.5 % 1 == 0
    except TypeError:
        return False
