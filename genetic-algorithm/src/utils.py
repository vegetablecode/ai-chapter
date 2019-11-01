from src.city import City


def get_cities_from_lists(x, y):
    cities = []
    for i in range(len(x)):
        cities.append(City(i, x[i], y[i]))
    return cities


def get_id_list(cities):
    return list((o.id for o in cities))


def get_x_list(cities):
    return list((o.x for o in cities))


def get_y_list(cities):
    return list((o.y for o in cities))
