def even_numbers_before_fixed(sequence, fixed_element, count = 0):
    while sequence:
        x = sequence.pop(0)
        if x == fixed_element:
            return count
        if x % 2 == 0:
            count += 1
    return -1
