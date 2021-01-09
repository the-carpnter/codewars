sum_times_tables = lambda t, a, b: sum(t)*a + sum_times_tables(t, a+1, b) if a <= b else 0
