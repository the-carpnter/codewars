def magic_sum(arr):
    return (arr[0]%2 and ('3' in str(arr[0])) and arr[0]) + magic_sum(arr[1:]) if arr else 0
