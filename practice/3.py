# pp 2

# que 3

import random

# Parameters
POP_SIZE = 10
CHROMOSOME_LENGTH = 5
GENERATIONS = 20
MUTATION_RATE = 0.1

# Fitness function: f(x) = x^2 + x


def fitness(x):
    return x**2 + x

# Generate random population


def generate_population():
    population = []
    for _ in range(POP_SIZE):
        chromosome = ''.join(random.choice('01')
                             for _ in range(CHROMOSOME_LENGTH))
        population.append(chromosome)
    return population

# Decode binary string to integer


def decode(chromosome):
    return int(chromosome, 2)

# Selection: retain top 50%


def selection(population):
    scored = [(chrom, fitness(decode(chrom))) for chrom in population]
    scored.sort(key=lambda x: x[1], reverse=True)
    selected = [chrom for chrom, _ in scored[:POP_SIZE // 2]]
    return selected

# Crossover: single-point


def crossover(parents):
    offspring = []
    while len(offspring) < POP_SIZE:
        p1, p2 = random.sample(parents, 2)
        point = random.randint(1, CHROMOSOME_LENGTH - 1)
        child = p1[:point] + p2[point:]
        offspring.append(child)
    return offspring

# Mutation: flip one bit with small probability


def mutate(population):
    mutated = []
    for chrom in population:
        if random.random() < MUTATION_RATE:
            idx = random.randint(0, CHROMOSOME_LENGTH - 1)
            bit = '0' if chrom[idx] == '1' else '1'
            chrom = chrom[:idx] + bit + chrom[idx+1:]
        mutated.append(chrom)
    return mutated


# Genetic Algorithm Execution
population = generate_population()

for _ in range(GENERATIONS):
    selected = selection(population)
    offspring = crossover(selected)
    population = mutate(offspring)

# Final best solution
best = max(population, key=lambda chrom: fitness(decode(chrom)))
best_x = decode(best)
max_value = fitness(best_x)

print(f"Best x: {best_x} (Binary: {best}), Maximum f(x): {max_value}")
