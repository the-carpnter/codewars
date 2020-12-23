def equalize(arr):
    return ['+' + str(x - arr[0]) if x - arr[0] >= 0 else str(x - arr[0]) for x in arr]
