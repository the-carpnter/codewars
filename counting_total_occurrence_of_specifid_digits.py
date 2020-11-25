from itertools import chain
class List(object):
    def count_spec_digits(self, integers_list, digits_list):
        integers_list = [*map(int, [*chain(*[list(str(abs(i))) for i in integers_list])])]
        return [(i, integers_list.count(i)) for i in digits_list]
