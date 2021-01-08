divisible_by_last = lambda n: [False] + [int(x) and int(y) % int(x) == 0 for x, y in zip(str(n), str(n)[1:])]
