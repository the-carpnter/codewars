def two_count(n):
    return 1 + two_count(n // 2) if n and n % 2 == 0 else 0 
