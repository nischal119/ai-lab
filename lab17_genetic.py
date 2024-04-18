import random
import string


def generate_random_string(length):
    return "".join(random.choice(string.ascii_lowercase) for _ in range(length))


def fitness(target, test_string):
    score = 0
    for i in range(len(target)):
        if target[i] == test_string[i]:
            score += 1
    return score


def select_parents(population, target):
    parents = []
    for _ in range(2):
        parents.append(max(population, key=lambda x: fitness(target, x)))
        population.remove(parents[-1])
    return parents


def crossover(parents):
    crossover_point = random.randint(1, len(parents[0]) - 1)
    child1 = parents[0][:crossover_point] + parents[1][crossover_point:]
    child2 = parents[1][:crossover_point] + parents[0][crossover_point:]
    return child1, child2


def mutate(child, mutation_rate):
    mutated_child = ""
    for char in child:
        if random.random() < mutation_rate:
            mutated_child += random.choice(string.ascii_lowercase)
        else:
            mutated_child += char
    return mutated_child


def genetic_algorithm(target, population_size=100, mutation_rate=0.01):
    population = [generate_random_string(len(target)) for _ in range(population_size)]
    generations = 0
    while True:
        generations += 1
        for i in range(population_size):
            if population[i] == target:
                return population[i], generations
        parents = select_parents(population, target)
        child1, child2 = crossover(parents)
        mutated_child1 = mutate(child1, mutation_rate)
        mutated_child2 = mutate(child2, mutation_rate)
        population.extend([mutated_child1, mutated_child2])


genetic_target = "hello"
solution, generations_taken = genetic_algorithm(genetic_target)
print(f"Solution found: {solution}, Generations taken: {generations_taken}")
