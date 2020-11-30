def find_next_square(sq):
    if sq**0.5%1:
        return -1
    while True:
        sq += 1
        if sq**0.5%1 == 0:
            return sq
