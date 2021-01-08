single_digit = lambda n: single_digit(bin(n).count('1')) if n > 9 else n
