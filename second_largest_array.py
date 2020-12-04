def find_2nd_largest(arr):
    a = [i for i in arr if type(i) in (int, float)]
    try:
        return sorted(set(a), reverse = True)[1]
    except IndexError:
        return None
