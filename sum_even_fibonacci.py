def SumEvenFibonacci(limit, a=1, b=1):
    sum = 0
    while True:
        a, b = b, a+b
        if a > limit:
            break
        if a%2==0:
            sum += a
    return sum
