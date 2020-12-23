f = lambda x: x[0] - x[1]
def process_data(data):
    return f(data[0]) * process_data(data[1:]) if data else 1
