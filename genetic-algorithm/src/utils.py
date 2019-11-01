from src.city import City


def get_cities_from_lists(x, y):
    cities = []
    for i in range(len(x)):
        cities.append(City(i, x[i], y[i]))
    return cities


def get_x_list(cities, order):
    values = []
    for i in range(len(order)):
        values.append(cities[order[i]].x)
    return values


def get_y_list(cities, order):
    values = []
    for i in range(len(order)):
        values.append(cities[order[i]].y)
    return values
