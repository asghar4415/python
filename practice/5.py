import random

# 1. Initial Population Function


def initial_population(pop_size, chromosome_length):
    return [[random.randint(0, 1) for _ in range(chromosome_length)] for _ in range(pop_size)]

# 2. Fitness Function (Example: maximize number of 1s - you can customize for book constraints)


def fitness(individual):
    return sum(individual)

# 3. Roulette Selection Function


def roulette_selection(population, fitnesses):
    total_fitness = sum(fitnesses)
    probabilities = [f / total_fitness for f in fitnesses]
    selected = random.choices(population, weights=probabilities, k=2)
    return selected

# 4. Two-Point Crossover Function


def crossover(parent1, parent2):
    point1 = random.randint(1, len(parent1)-2)
    point2 = random.randint(point1, len(parent1)-1)

    child1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
    child2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]

    return child1, child2

# 5. Binary Mutation Function


def mutate(individual, mutation_rate=0.01):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]  # Flip bit
    return individual

# 6. Main Genetic Algorithm Function


def genetic_algorithm():
    pop_size = 10
    chromosome_length = 8
    generations = 50

    population = initial_population(pop_size, chromosome_length)

    for _ in range(generations):
        fitnesses = [fitness(ind) for ind in population]
        new_population = []

        while len(new_population) < pop_size:
            parent1, parent2 = roulette_selection(population, fitnesses)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1)
            child2 = mutate(child2)
            new_population.extend([child1, child2])

        population = new_population[:pop_size]

    best_individual = max(population, key=fitness)
    print("Best solution:", best_individual)
    print("Best fitness:", fitness(best_individual))


# Run the genetic algorithm
genetic_algorithm()
