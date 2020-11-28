def solve(n):
    for i in range(int(n**0.5), 0, -1):
        a = i
        b = n//a
        if n%i == 0:
            if (b - a)%2 == 0 and a != b:
                return ((b - a)//2)**2
    return -1
