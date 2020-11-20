def solution(x):
    max = 0
    for i,_ in enumerate(x):
        a = int(x[i:i+5])
        if a > max:
            max = a
    return max
