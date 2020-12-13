def solution(n):
    k = [0, 0, 0]
    while n:
        n -= 1
        if n == 0:
            return k
        if n%15 == 0:
            k[2] += 1
        if n%5 == 0 and n%3:
            k[1] += 1
        if n%3 == 0 and n%5:
            k[0] += 1
