# Alpha-Beta Pruning algorithm

# Define the utility values for leaf nodes (example tree)
# Positive values represent the utility for the maximizing player
# Negative values represent the utility for the minimizing player

def alpha_beta_pruning(depth, node_index, maximizing_player, values, alpha, beta):
    # Base case: If we have reached a leaf node, return its value
    if depth == 0:
        return values[node_index]
    
    if maximizing_player:
        max_eval = float('-inf')
        
        # Iterate through children of the current node
        for i in range(2):
            eval = alpha_beta_pruning(depth - 1, node_index * 2 + i, False, values, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            
            # Beta cutoff
            if beta <= alpha:
                break
        return max_eval
    
    else:
        min_eval = float('inf')
        
        # Iterate through children of the current node
        for i in range(2):
            eval = alpha_beta_pruning(depth - 1, node_index * 2 + i, True, values, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            
            # Alpha cutoff
            if beta <= alpha:
                break
        return min_eval

# Example usage:

# Define the tree depth and leaf node values
values = [3, 5, 6, 9, 1, 2, 0, -1]  # Leaf node values
depth = 3  # The depth of the tree
node_index = 0  # Start from the root node
maximizing_player = True  # First player is the maximizing player

# Initialize alpha and beta values
alpha = float('-inf')
beta = float('inf')

# Call the Alpha-Beta pruning algorithm
optimal_value = alpha_beta_pruning(depth, node_index, maximizing_player, values, alpha, beta)

print("The optimal value is:", optimal_value)
