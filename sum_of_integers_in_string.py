def sum_of_integers_in_string(s):
    return sum(map(int,''.join(i if i.isnumeric() else ' ' for i in s).split()))
