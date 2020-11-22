def product(numbers):
    if not numbers:
        return None
    re = numbers[0]
    for i in numbers[1:]:
        re *= i
    return re
