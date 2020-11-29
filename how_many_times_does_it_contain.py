def string_counter(string, char, count=0):
    if not string:
        return count
    if string[0]==char:
        count += 1
    return string_counter(string[1:], char, count)
