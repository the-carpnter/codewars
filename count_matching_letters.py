def count_correct_characters(a, b, i = 0):
    if len(a) != len(b):
        raise "Not Equal Length"
    return (a[i] == b[i]) + count_correct_characters(a, b, i + 1) if a[i:] else 0
