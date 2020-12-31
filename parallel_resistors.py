def resistor_parallel(*args):
    return 1/sum(1/i for i in args)
