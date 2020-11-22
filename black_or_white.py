def square_color(file, rank):
    return ['white','black'][(ord(file) + rank)%2 == 0]
