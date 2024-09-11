import math

# Define the game tree
# Example game tree structure:
# Each node is a dictionary with:
# - 'value': The utility of the terminal node (if it is a leaf node)
# - 'children': A list of child nodes

def minimax(node, depth, maximizing_player):
    if depth == 0 or is_terminal(node):
        return node['value']
    
    if maximizing_player:
        max_eval = -math.inf
        for child in node['children']:
            eval = minimax(child, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for child in node['children']:
            eval = minimax(child, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval

def is_terminal(node):
    return 'value' in node and node['children'] == []

# Example usage
if __name__ == "__main__":
    # Example game tree for demonstration
    game_tree = {
        'value': None,
        'children': [
            {'value': 3, 'children': []},     # Leaf node with utility 3
            {'value': 5, 'children': []},     # Leaf node with utility 5
            {'value': None, 'children': [     # Internal node
                {'value': 2, 'children': []}, # Leaf node with utility 2
                {'value': 7, 'children': []}  # Leaf node with utility 7
            ]}
        ]
    }

    # Compute the optimal value for the root node
    optimal_value = minimax(game_tree, depth=2, maximizing_player=True)
    print(f"Optimal value for the root node: {optimal_value}")
