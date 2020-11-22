def negation_value(s, val):
    if s == '':
        return bool(val)
    return negation_value(s[1:], not val)
