from collections import deque

def is_goal(state):
    # Goal is to measure exactly 2 liters
    return state[0] == 2 or state[1] == 2

def get_neighbors(state):
    jug1, jug2 = state
    neighbors = []

    # Fill the 4-liter jug
    neighbors.append((4, jug2))

    # Fill the 3-liter jug
    neighbors.append((jug1, 3))

    # Empty the 4-liter jug
    neighbors.append((0, jug2))

    # Empty the 3-liter jug
    neighbors.append((jug1, 0))

    # Pour from 4-liter jug to 3-liter jug
    pour_to_jug2 = min(jug1, 3 - jug2)
    neighbors.append((jug1 - pour_to_jug2, jug2 + pour_to_jug2))

    # Pour from 3-liter jug to 4-liter jug
    pour_to_jug1 = min(jug2, 4 - jug1)
    neighbors.append((jug1 + pour_to_jug1, jug2 - pour_to_jug1))

    return neighbors

def solve_water_jug():
    # Initial state (0, 0) means both jugs are empty
    initial_state = (0, 0)
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()

        if current_state in visited:
            continue

        visited.add(current_state)

        if is_goal(current_state):
            return path + [current_state]

        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                queue.append((neighbor, path + [current_state]))

    return None

def print_solution(solution):
    for step, state in enumerate(solution):
        print(f"Step {step}: {state}")

solution = solve_water_jug()

if solution:
    print("Solution found!")
    print_solution(solution)
else:
    print("No solution exists.")
