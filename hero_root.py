def int_rac(n, guess):
    i = 0
    while True:
        i += 1
        if abs(int(n**0.5) - guess) < 1:
            return i
        guess = int((guess + n / guess) / 2)
