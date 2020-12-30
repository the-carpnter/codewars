def filter_even_length_words(words):
    return [*filter(lambda x: len(x) % 2 == 0, words)]
