from collections import deque

# Define the goal state
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]  # The blank space is represented by 0
]

# Directions for moving the blank space (up, down, left, right)
directions = [
    (-1, 0),  # Up
    (1, 0),   # Down
    (0, -1),  # Left
    (0, 1)    # Right
]

# Function to find the position of the blank space (0)
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Function to check if the current state is the goal state
def is_goal(state):
    return state == goal_state

# Function to generate new states by moving the blank space
def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)

    for direction in directions:
        new_x, new_y = x + direction[0], y + direction[1]

        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append(new_state)

    return neighbors

# BFS algorithm to solve the 8-puzzle problem
def solve_puzzle(start_state):
    queue = deque([(start_state, [])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()

        if is_goal(current_state):
            return path + [current_state]

        visited.add(tuple(map(tuple, current_state)))

        for neighbor in get_neighbors(current_state):
            neighbor_tuple = tuple(map(tuple, neighbor))

            if neighbor_tuple not in visited:
                queue.append((neighbor, path + [current_state]))

    return None

# Function to print the puzzle state
def print_state(state):
    for row in state:
        print(" ".join(str(tile) if tile != 0 else " " for tile in row))
    print()

# Example usage
start_state = [
    [1, 2, 3],
    [4, 5, 0],
    [6, 7, 8]
]

solution = solve_puzzle(start_state)

if solution:
    print("Solution found in", len(solution) - 1, "moves:")
    for state in solution:
        print_state(state)
else:
    print("No solution found.")
