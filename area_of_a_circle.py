from math import pi
def circle_area(r):
    try:
        return round(pi*r**2,  2) if r>0 else False
    except TypeError:
        return False
