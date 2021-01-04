def reverse(lst):
    return [lst.pop()] + reverse(lst) if lst else list()   
