def odd_ball(arr):
    return any(arr.index(i) in arr for i in arr if i == 'odd')
