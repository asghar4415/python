import random

# Problem size: N-Queens
n = 8  # Change N as needed

# Fitness function: Higher is better (max 1.0 if no conflicts)


def calculate_fitness(individual):
    non_attacking = 0
    total_pairs = n * (n - 1) // 2  # Total possible pairs of queens
    for i in range(n):
        for j in range(i + 1, n):
            if individual[i] != individual[j] and abs(individual[i] - individual[j]) != abs(i - j):
                non_attacking += 1
    return non_attacking / total_pairs

# Create a random individual (permutation of columns)


def create_random_individual():
    return random.sample(range(n), n)

# Select top 50% parents based on fitness


def select_parents(population, fitness_scores):
    sorted_pop = [x for _, x in sorted(
        zip(fitness_scores, population), reverse=True)]
    return sorted_pop[:len(population) // 2]

# Crossover with duplicate fix


def crossover(parent1, parent2):
    point = random.randint(1, n - 2)
    child = parent1[:point] + parent2[point:]

    # Ensure unique columns in child
    missing = set(range(n)) - set(child)
    seen = set()
    for i in range(len(child)):
        if child[i] in seen:
            child[i] = missing.pop()
        else:
            seen.add(child[i])
    return child

# Mutation by swapping two columns


def mutate(individual):
    idx1, idx2 = random.sample(range(n), 2)
    individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
    return individual

# Genetic Algorithm Main Function


def genetic_algorithm():
    population_size = 100
    mutation_rate = 0.1
    max_generations = 100

    population = [create_random_individual() for _ in range(population_size)]
    generation = 0
    best_fitness = 0

    while best_fitness < 1.0 and generation < max_generations:
        fitness_scores = [calculate_fitness(ind) for ind in population]
        best_fitness = max(fitness_scores)
        print(f"Generation {generation} Best Fitness: {best_fitness:.4f}")

        # Stop if perfect solution found
        if best_fitness == 1.0:
            break

        # Selection
        parents = select_parents(population, fitness_scores)

        # Crossover
        new_population = []
        for _ in range(population_size):
            parent1, parent2 = random.sample(parents, 2)
            child = crossover(parent1, parent2)
            new_population.append(child)

        # Mutation
        for i in range(len(new_population)):
            if random.random() < mutation_rate:
                new_population[i] = mutate(new_population[i])

        # Move to next generation
        population = new_population
        generation += 1

    # Get the best solution
    best_individual = max(population, key=calculate_fitness)
    best_fitness = calculate_fitness(best_individual)
    return best_individual, best_fitness


# Run the Genetic Algorithm
solution, fitness = genetic_algorithm()
print("Best Solution:", solution)
print("Best Fitness:", fitness)
