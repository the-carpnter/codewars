def eight_bit_number(n):
    try:
        return 0 <= int(n) < 256 and len(n) == len(str(int(n)))
    except ValueError:
        return False
