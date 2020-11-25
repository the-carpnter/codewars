def swap_adjacent_bits(n):
    x = list(bin(n)[2:])
    x = [0]*(32-len(x)) + x
    for i in range(0,len(x),2):
        try:
            x[i], x[i+1] = x[i+1], x[i]
        except IndexError:
            pass
    return sum(int(bit)*(2**i) for i,bit in enumerate(x[::-1]))
