f = lambda x : ord(x) - ord('A') + 1
def title_to_number(title, i = 0):
    return f(title[-1]) * 26**i + title_to_number(title[:-1], i + 1) if title else 0
