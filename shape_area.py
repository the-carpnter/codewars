def shape_area(n):
    sum = 0
    while n:
        sum += 4*(n-1)
        n -= 1
    return sum + 1
