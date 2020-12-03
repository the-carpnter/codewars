def adjacent_element_product(a, max=None, i=0):
    if i == len(a)-1:
        return max
    if max is None or a[i]*a[i+1] > max:
        max = a[i]*a[i+1]
    return adjacent_element_product(a, max, i+1)
