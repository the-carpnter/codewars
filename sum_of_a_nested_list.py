def sum_nested(lst):
    if lst == []:
        return 0
    return lst[0] + sum_nested(lst[1:]) if type(lst[0]) is int else sum_nested(lst[0]) + sum_nested(lst[1:])
