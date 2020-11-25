def arr2bin(arr):
    try:
        if not all(type(i)==int for i in arr):
            raise TypeError
        return bin(sum(arr))[2:]
    except TypeError:
        return False
