from math import log2, ceil
def fold_to(distance):
    if distance < 0:
        return None
    return max(ceil(log2(distance/0.0001)),0) if distance >= 0.0001 else 0 
