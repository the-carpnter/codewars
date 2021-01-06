def double_check(strng):
    j = strng[0]
    for x in strng[1:]:
        if x.lower() == j.lower():
            return True
        j = x
    return False
