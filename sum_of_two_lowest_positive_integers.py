def sum_two_smallest_numbers(n):
    k = [n[0], n[1]] if n[0] < n[1] else [n[1], n[0]]
    for x in n[2:]:
        if x < k[1]:
            k[1] = x
        if x < k[0]:
            k[0], k[1] = k[1], k[0]
    return sum(k)
