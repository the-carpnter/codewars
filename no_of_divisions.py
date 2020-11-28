def divisions(n, divisor, times=0):
    return divisions(n//divisor, divisor, times + 1) if n >= divisor else times
