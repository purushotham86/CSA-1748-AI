# Define the graph using an adjacency list
# Each edge has a cost of 1
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': [],
}

# DFS using recursion with cost tracking
def dfs_recursive(graph, start, visited=None, cost=0):
    if visited is None:
        visited = set()
    visited.add(start)
    print(f"{start} (Cost so far: {cost})", end=' ')
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            # Recursively visit the neighbor with updated cost
            cost = dfs_recursive(graph, neighbor, visited, cost + 1)
    
    return cost

# Example usage
print("DFS using recursion with cost:")
total_cost = dfs_recursive(graph, 'A')
print(f"\nTotal cost of traversal: {total_cost}")
