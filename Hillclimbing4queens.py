import random

def calculate_conflicts(state):
    """Heuristic: number of pairs of queens attacking each other."""
    conflicts = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def generate_neighbors(state):
    """Generate all neighbor states by moving one queen in its column."""
    neighbors = []
    n = len(state)
    for col in range(n):
        for row in range(n):
            if state[col] != row:
                new_state = state.copy()
                new_state[col] = row
                neighbors.append(new_state)
    return neighbors

def hill_climbing(n=4):
    # Initial random state
    state = [random.randint(0, n - 1) for _ in range(n)]
    current_cost = calculate_conflicts(state)

    steps = []
    steps.append((state.copy(), current_cost))

    while True:
        neighbors = generate_neighbors(state)
        best_neighbor = min(neighbors, key=calculate_conflicts)
        best_cost = calculate_conflicts(best_neighbor)

        steps.append((best_neighbor.copy(), best_cost))

        if best_cost >= current_cost:  # Local optimum
            break
        state, current_cost = best_neighbor, best_cost

    return state, current_cost, steps

# Run for 4-Queens
solution, cost, steps = hill_climbing(4)

print("Final State:", solution)
print("Final Cost:", cost)
print("\nSteps (state, cost):")
for s, c in steps:
    print(s, "Cost:", c)
