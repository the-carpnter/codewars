def short_form(s, i=0):
    if i == 0 or i == len(s) - 1:
        return s[i] + short_form(s, i+1)
    if i == len(s):
        return ''
    return short_form(s, i+1) if s[i].lower() in 'aeiou' else s[i] + short_form(s, i+1)
