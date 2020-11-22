def distinct_digit_year(year):
    while True:
        year += 1
        if len(set(str(year)))==4:
            return year
