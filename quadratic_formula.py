 def quadratic_formula(a, b, c):
    
    root1 = (-b + (b**2 - 4 * a * c)**0.5) / ( 2 * a)
    
    root2 = (-b - (b**2 - 4 * a * c)**0.5) / ( 2 * a)
    
    return [root1, root2]
