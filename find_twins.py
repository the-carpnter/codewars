from collections import Counter
def elimination(arr):
    c = Counter(arr)
    for i in c:
        if c[i] > 1:
            return i
    return None
