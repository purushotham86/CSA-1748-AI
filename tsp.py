import itertools

# Function to calculate the total distance of a specific route
def calculate_total_distance(route, distance_matrix):
    total_distance = 0
    num_cities = len(route)
    
    for i in range(num_cities - 1):
        total_distance += distance_matrix[route[i]][route[i+1]]
    total_distance += distance_matrix[route[-1]][route[0]]  # Return to starting city
    
    return total_distance

# Function to solve the TSP using brute-force
def tsp_bruteforce(distance_matrix):
    num_cities = len(distance_matrix)
    cities = list(range(num_cities))
    
    # Generate all possible permutations of city visits
    all_possible_routes = itertools.permutations(cities)
    
    # Initialize the shortest route and shortest distance
    shortest_route = None
    shortest_distance = float('inf')
    
    # Evaluate each possible route
    for route in all_possible_routes:
        current_distance = calculate_total_distance(route, distance_matrix)
        
        # Update if current route is shorter
        if current_distance < shortest_distance:
            shortest_distance = current_distance
            shortest_route = route
    
    return shortest_route, shortest_distance

# Example usage
if __name__ == "__main__":
    # Define a distance matrix (symmetric matrix where element [i][j] represents the distance from city i to city j)
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    
    shortest_route, shortest_distance = tsp_bruteforce(distance_matrix)
    
    print("Shortest Route:", shortest_route)
    print("Shortest Distance:", shortest_distance)
