import random

# Heuristic function: Counts the number of pairs of attacking queens


def calculate_conflicts(state):
    conflicts = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            # Check for same column or diagonal conflict
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts

# Generate neighbors by moving one queen at a time in each row


def get_neighbors(state):
    neighbors = []
    n = len(state)
    for row in range(n):
        for col in range(n):
            if col != state[row]:  # Only move if different column
                new_state = list(state)
                new_state[row] = col
                neighbors.append(new_state)
    return neighbors

# Simple Hill Climbing Algorithm


def simple_hill_climbing(n):
    current_state = [random.randint(0, n - 1) for _ in range(n)]
    current_conflicts = calculate_conflicts(current_state)

    while True:
        neighbors = get_neighbors(current_state)
        next_state = None
        next_conflicts = current_conflicts

        # Find the first better neighbor
        for neighbor in neighbors:
            neighbor_conflicts = calculate_conflicts(neighbor)
            if neighbor_conflicts < next_conflicts:
                next_state = neighbor
                next_conflicts = neighbor_conflicts
                break  # Move to the first better neighbor

        # If no better neighbor found, stop
        if next_conflicts >= current_conflicts:
            break

        # Move to better neighbor
        current_state = next_state
        current_conflicts = next_conflicts

    return current_state, current_conflicts


# Run Hill Climbing for N-Queens
n = 4  # Change N for different board sizes
solution, conflicts = simple_hill_climbing(n)

# Print results
if conflicts == 0:
    print(f"Solution found for {n}-Queens problem:")
    print(solution)
else:
    print(
        f"Could not find a solution. Stuck at state with {conflicts} conflicts:")
    print(solution)
