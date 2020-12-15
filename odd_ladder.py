def pattern(n):
    return '\n'.join(str(i)*i for i in range(n+1) if i%2)
