def gps(s, x):
     return max(abs(b - a) * 3600 // s for a, b in zip(x, x[1:])) if len(x) > 1 and s > 1 else 0
