def find(n):
    return sum(i for i in range(1,n+1) if i%15==0 or i%5==0 or i%3==0)
