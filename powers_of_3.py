def largest_power(N, i=0):
    if 3**i >= N:
        return i-1
    return largest_power(N, i+1)
