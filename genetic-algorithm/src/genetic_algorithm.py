import copy
import random
import math
from src.city import City


def get_initial_population(cities, population_size, initial_order):
    population = []
    for _ in range(population_size):
        population.append(random.sample(initial_order, len(initial_order)))
    return population


def calculate_distance(city_a, city_b):
    delta_x = abs(city_a.x - city_b.x)
    delta_y = abs(city_a.y - city_b.y)
    return math.sqrt(delta_x**2 + delta_y**2)


def calculate_route_length(cities, order):
    total_length = 0
    for i in range(len(order) - 1):
        total_length += calculate_distance(
            cities[order[i]], cities[order[i+1]])
    return total_length


def calculate_fitness(cities, population):
    fitness_scores = []
    current_record = math.inf
    for i in range(len(population)):
        route_length = calculate_route_length(cities, population[i])
        if route_length < current_record:
            current_record = route_length
        fitness_scores.append(1 / (route_length**8 + 1))
    return fitness_scores, current_record


def normalize_fitness(fitness_scores):
    normalized_fitness_scores = copy.deepcopy(fitness_scores)
    fitness_sum = 0
    for i in range(len(normalized_fitness_scores)):
        fitness_sum += normalized_fitness_scores[i]
    for i in range(len(normalized_fitness_scores)):
        normalized_fitness_scores[i] /= fitness_sum
    return normalized_fitness_scores


def next_generation(cities, population, probabilities):
    # new generation
    new_population = []
    for _ in range(len(population)):
        parent_a = pick_one(population, probabilities)
        parent_b = pick_one(population, probabilities)
        child = crossover(parent_a, parent_b)
        mutate(child, 0.01)
        new_population.append(child)
    return new_population


def mutate(order, mutation_rate):
    for _ in range(len(order)):
        if random.uniform(0, 1) < mutation_rate:
            # swap random elements
            i1 = random.randrange(0, len(order))
            i2 = (i1 + 1) % len(order)
            order[i1], order[i2] = order[i2], order[i1]


def pick_one(population, probabilities):
    index = 0
    r = random.uniform(0, 1)

    while r > 0:
        r -= probabilities[index]
        index += 1
    index -= 1

    return copy.deepcopy(population[index])


def crossover(order_a, order_b):
    start = random.randrange(0, len(order_a)-1)
    end = random.randrange(start + 1, len(order_a)+1)
    new_order = copy.deepcopy(order_a[start:end])
    for i in range(len(order_b)):
        if order_b[i] not in new_order:
            new_order.append(order_b[i])
    return new_order
