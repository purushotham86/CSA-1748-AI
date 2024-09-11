import heapq

# Define the Node class to represent a node in the graph
class Node:
    def __init__(self, position, parent=None, g=0, h=0):
        self.position = position  # Position of the node (x, y) or graph index
        self.parent = parent  # Parent node to reconstruct the path
        self.g = g  # Cost from the start node to this node
        self.h = h  # Heuristic cost (estimated cost to goal)
        self.f = g + h  # Total cost (g + h)

    # Comparison operator for heapq (priority queue)
    def __lt__(self, other):
        return self.f < other.f

# Define the A* search algorithm
def astar_search(start, goal, grid):
    # Initialize open list (priority queue) and closed list (visited nodes)
    open_list = []
    closed_list = set()

    # Create the start node and push it to the open list
    start_node = Node(start, None, 0, heuristic(start, goal))
    heapq.heappush(open_list, start_node)

    # Loop until the open list is empty
    while open_list:
        # Get the node with the lowest f value (g + h)
        current_node = heapq.heappop(open_list)

        # If the goal is reached, reconstruct the path and return the cost
        if current_node.position == goal:
            return reconstruct_path(current_node), current_node.g  # Return path and cost

        # Add the current node to the closed list (visited)
        closed_list.add(current_node.position)

        # Generate neighbors (up, down, left, right)
        neighbors = get_neighbors(current_node.position, grid)

        for neighbor in neighbors:
            if neighbor in closed_list:
                continue

            # Calculate g, h, and f values for the neighbor node
            g = current_node.g + 1  # Assume all moves have a cost of 1
            h = heuristic(neighbor, goal)
            neighbor_node = Node(neighbor, current_node, g, h)

            # Check if the neighbor is already in the open list
            if any(node.position == neighbor and node.f <= neighbor_node.f for node in open_list):
                continue

            # Add the neighbor to the open list
            heapq.heappush(open_list, neighbor_node)

    # Return None if no path is found
    return None, float('inf')  # No path found, return infinite cost

# Heuristic function (Manhattan distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Get valid neighbors (within grid bounds)
def get_neighbors(position, grid):
    neighbors = []
    x, y = position
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
            neighbors.append((nx, ny))

    return neighbors

# Reconstruct the path from goal to start
def reconstruct_path(node):
    path = []
    while node:
        path.append(node.position)
        node = node.parent
    return path[::-1]  # Return reversed path (start to goal)

# Example usage
if __name__ == "__main__":
    # Example grid (0: walkable, 1: obstacle)
    grid = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start = (0, 0)  # Starting point
    goal = (4, 4)  # Goal point

    path, cost = astar_search(start, goal, grid)
    if path:
        print("Path found:", path)
        print("Total cost:", cost)
    else:
        print("No path found.")
