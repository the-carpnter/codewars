def abundant_number(num, i=2, sum=0):
    while i <= num // 2:
        sum += 0 if num % i else num // i
        i += 1
    return sum > num
