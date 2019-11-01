import random
import math
from src.city import City


def generate_data(numb_of_cities, max_distance):
    # calculate circle params
    middle = max_distance / 2
    r = (max_distance - 2) / 2

    # generate random cities
    cities = []
    for i in range(numb_of_cities):
        alpha = random.uniform(middle, middle + r)
        x = middle + r * math.cos(alpha)
        y = middle + r * math.sin(alpha)
        cities.append(City(i, x, y))
    return cities
