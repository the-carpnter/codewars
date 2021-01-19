convert = lambda n: chr(int(n[:2])) + convert(n[2:]) if n else ''
