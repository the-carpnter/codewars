differences = lambda lst: differences([abs(x - y) for x, y in zip(lst, lst[1:])]) if len(lst) > 1 else lst[0]
