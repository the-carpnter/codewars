def arithmetic(a, b, operator):
    return {'add': lambda x,y: x+y, 'subtract': lambda x,y: x-y, 'multiply': lambda x,y:x*y, 'divide': lambda x,y: x/y}[operator](a,b)
