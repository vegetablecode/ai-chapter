import copy
import random
import math
from src.city import City


def get_initial_population(cities, population_size, initial_order):
    population = []
    for _ in range(population_size):
        population.append(random.sample(initial_order, len(initial_order)))
    return population


def calculate_fitness(cities, order):
    cost = 0
    for i in range(len(order) - 1):
        delta_x = abs(cities[order[i]].x - cities[order[i+1]].x)
        delta_y = abs(cities[order[i]].y - cities[order[i+1]].y)
        distance = math.sqrt(delta_x**2 + delta_y**2)
        cost += distance
    return 1 / cost


def normalize_fitness(fitness_scores):
    normalized_fitness_scores = copy.deepcopy(fitness_scores)
    fitness_sum = 0
    for i in range(len(normalized_fitness_scores)):
        fitness_sum += normalized_fitness_scores[i]
    for i in range(len(normalized_fitness_scores)):
        normalized_fitness_scores[i] /= fitness_sum
    return normalized_fitness_scores


def next_generation(cities, population):
    fitness_scores = []
    for i in range(len(population)):
        fitness = calculate_fitness(cities, population[i])
        fitness_scores.append(fitness)
    probabilities = normalize_fitness(fitness_scores)

    new_population = []
    for i in range(len(population)):
        order = pick_one(population, probabilities)
        mutate(order)
        new_population.append(order)
    return new_population


def mutate(order):
    # swap random elements
    i1, i2 = random.sample(range(len(order)), 2)
    order[i1], order[i2] = order[i2], order[i1]


def pick_one(population, probabilities):
    index = 0
    r = random.uniform(0, 1)

    while r > 0:
        r -= probabilities[index]
        index += 1
    index -= 1

    return copy.deepcopy(population[index])


def select_parents(cities, population):
    # get fitness score for each chromosome
    fitnes_scores = []
    for i in range(len(population)):
        population_score = calculate_fitness(cities, population[i])
        fitnes_scores.append(population_score)

    # - ROULETTE RULE -
    parents = []
    roulette_wheel = []
    roulette_wheel[0] = fitnes_scores[0]
    for i in range(1, len(fitnes_scores)):
        roulette_wheel[i] += roulette_wheel[i-1] + fitnes_scores[i]

    # get 1st parent
    result = random.uniform(0, sum(fitnes_scores))
    for i in range(len(roulette_wheel) - 1, 0):
        if roulette_wheel <= result:
            parents.append(i)
            break

    # get 2st parent
    parents.append(parents[0])
    while parents[1] == parents[0]:
        for i in range(len(roulette_wheel) - 1, 0):
            if roulette_wheel <= result:
                parents[1] = result
                break
    return(parents)
