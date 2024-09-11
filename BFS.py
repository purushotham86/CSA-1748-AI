from collections import deque

def bfs_shortest_path(graph, start, goal):
    # Keep track of the nodes that have been visited
    visited = set()
    
    # Queue for BFS that stores the path to reach each node
    queue = deque([[start]])
    
    # Loop until the queue is empty
    while queue:
        # Get the first path from the queue
        path = queue.popleft()
        # Get the last node from the path
        node = path[-1]
        
        # If the node is the goal, return the path
        if node == goal:
            return path
        
        # If the node has not been visited, process it
        if node not in visited:
            visited.add(node)
            # Add all unvisited neighbors to the queue with the new path
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    
    # If no path is found
    return None

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': ['G'],
    'G': []
}

start_node = 'A'
goal_node = 'G'

path = bfs_shortest_path(graph, start_node, goal_node)
if path:
    print(f"Shortest path from {start_node} to {goal_node}: {path}")
else:
    print(f"No path found from {start_node} to {goal_node}.")
