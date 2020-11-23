def get_number_of_squares(n, x=0, sum=0):
    sum = sum + x**2
    if sum >= n:
        return x-1
    x = x+1
    return get_number_of_squares(n, x, sum)
