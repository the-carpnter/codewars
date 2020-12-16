def sum_of_a_beach(beach):
    b = beach.lower()
    return b.count('sand') + b.count('water') + b.count('fish') + b.count('sun')
