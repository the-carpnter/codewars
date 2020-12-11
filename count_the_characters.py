def count_char(s, c):
    if s:
        return 1 + count_char(s[1:], c) if c.lower() == s[0].lower() else count_char(s[1:], c)
    return 0
