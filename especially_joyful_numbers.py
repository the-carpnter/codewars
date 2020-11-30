def number_joy(n):
    x = [*map(int,str(n))]
    return sum(x)*int(str(sum(x))[::-1]) == n
