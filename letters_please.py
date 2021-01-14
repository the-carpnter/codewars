import string
remove_chars = lambda s:''.join(i for i in s if i in string.ascii_letters or i == ' ')
