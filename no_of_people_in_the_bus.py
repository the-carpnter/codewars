def number(bus_stops):
    x,y = zip(*bus_stops)
    return sum(x) - sum(y)
