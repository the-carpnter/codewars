def sort_dict(d):
    return sorted([(x, y) for x, y in d.items()], key = lambda x : -x[1])
