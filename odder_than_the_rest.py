def odd_one(arr, i=0):
    if not arr:
        return -1
    if arr[0]&1:
        return i
    return odd_one(arr[1:], i+1)
