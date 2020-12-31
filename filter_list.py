filter_list = lambda l : [l[0]] * (type(l[0]) is int) + filter_list(l[1:]) if l else []
