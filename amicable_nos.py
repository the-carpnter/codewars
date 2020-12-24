def s(n):
    re, x = 0, 2
    while x < n // 2 + 1:
        re += 0 if n % x else n // x
        x += 1
    return re + 1
        
def amicable_numbers(n1,n2):
    return s(n1) == n2 and s(n2) == n1
