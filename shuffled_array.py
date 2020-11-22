def shuffled_array(s, i=0):
    if s[i] == sum(s[:i]+s[i+1:]):
        return sorted(s[:i]+s[i+1:])
    return shuffled_array(s, i+1)
