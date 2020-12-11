def reverse_number(n):
    return int(str(abs(n))[::-1]) * n//abs(n) if n else 0
