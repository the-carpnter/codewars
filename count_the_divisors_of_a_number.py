def divisors(n):
    count = 0
    x = n
    while True:
        if x == 0:
            return count
        if n%x == 0:
            count += 1
        x -= 1 
