def hamming_distance(a, b, count=0):
    if a and b:
        if a[0] != b[0]:
            count += 1
        return hamming_distance(a[1:], b[1:], count)
    return count
