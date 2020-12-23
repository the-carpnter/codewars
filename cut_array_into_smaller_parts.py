def make_parts(arr, c):
    return [arr[:c]] + make_parts(arr[c:], c) if arr else []
