def square_digits(num, n=0):
    return square_digits(num//10, (num%10)**2 * 10**(len(str(n))) + n if n else (num%10)**2) if num else n
