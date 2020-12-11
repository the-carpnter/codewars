def digits(n):
    return [n%10] + digits(n//10) if n else [] 

def digitize(n):
    return digits(n)[::-1] if digits(n) else [0] 
