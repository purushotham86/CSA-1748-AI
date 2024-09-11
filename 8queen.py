# Function to check if a queen can be placed at board[row][col]
def is_safe(board, row, col, n):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

# Function to solve the 8-queen problem using backtracking
def solve_nqueens(board, col, n):
    # If all queens are placed, return True
    if col >= n:
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Recur to place rest of the queens
            if solve_nqueens(board, col + 1, n):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution,
            # then remove the queen (backtrack)
            board[i][col] = 0

    # If the queen cannot be placed in any row in this column, return False
    return False

# Function to print the solution board
def print_solution(board, n):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

# Main function to solve the 8-queen problem
def solve_8queens():
    n = 8
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_nqueens(board, 0, n):
        print("Solution does not exist")
        return

    print_solution(board, n)

# Run the 8-queen solver
solve_8queens()
