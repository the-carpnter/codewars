def case_sensitive(s):
    if s == '':
        return [True, []]
    if s[0].isupper():
        return [False, [s[0]]]
    return case_sensitive(s[1:])
