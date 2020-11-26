def reverse_factorial(num, fact=1, i=1):
    fact = fact * i
    if fact == num:
        return str(i) + '!'
    if fact > num:
        return 'None'
    return reverse_factorial(num, fact, i+1)  
