import random
import math

# Define the size of the board (4x4)
N = 4

# Generate a random state (a random arrangement of queens on the board)
def random_state():
    return [random.randint(0, N-1) for _ in range(N)]

# Calculate the number of conflicts (attacking pairs of queens)
def calculate_conflicts(state):
    conflicts = 0
    for i in range(N):
        for j in range(i + 1, N):
            if state[i] == state[j]:  # Same column
                conflicts += 1
            if abs(state[i] - state[j]) == abs(i - j):  # Same diagonal
                conflicts += 1
    return conflicts

# Perform a random move (a small change to the state)
def random_move(state):
    new_state = state[:]
    row = random.randint(0, N-1)
    new_state[row] = random.randint(0, N-1)
    return new_state

# Simulated Annealing algorithm
def simulated_annealing():
    current_state = random_state()
    current_temp = 1000  # Initial temperature
    min_temp = 1         # Minimum temperature to stop
    cooling_rate = 0.95  # Rate at which the temperature decreases
    
    # Loop until the temperature is low enough
    while current_temp > min_temp:
        # Calculate the current number of conflicts
        current_conflicts = calculate_conflicts(current_state)
        
        # If no conflicts, we've found a solution
        if current_conflicts == 0:
            return current_state
        
        # Generate a new candidate by making a random move
        new_state = random_move(current_state)
        new_conflicts = calculate_conflicts(new_state)
        
        # If the new state is better or if we accept it probabilistically
        if new_conflicts < current_conflicts or random.random() < math.exp((current_conflicts - new_conflicts) / current_temp):
            current_state = new_state
        
        # Cool down the temperature
        current_temp *= cooling_rate
    
    # Return the best state found
    return current_state

# Run the simulated annealing algorithm
solution = simulated_annealing()

# Display the solution
print("Solution: ", solution)
print("Conflicts: ", calculate_conflicts(solution))
