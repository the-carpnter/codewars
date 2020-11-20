def sum_digits(number):
    return sum(int(i) for i in str(int(abs(number))))
