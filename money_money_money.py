def calculate_years(p, i, t, d):
    return 1 + calculate_years(p + p*i - p*i*t, i, t, d) if p < d else 0
