def square_it(digits):
    try:
        digits = str(digits)
        n = len(digits)**0.5
        x = n if n%1 else int(n)
        return '\n'.join(digits[i:i+x] for i in range(0,len(digits),x))
    except TypeError:
        return 'Not a perfect square!'
