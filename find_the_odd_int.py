def find_it(seq):
    for x,y in {i:seq.count(i) for i in seq}.items():
        if y&1:
            return x
