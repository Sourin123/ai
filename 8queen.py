def print_board(board):
    """Print the chess board"""
    for row in board:
        print(" ".join(map(str, row)))

def is_safe(board, row, col, n):
    """Check if a queen can be placed on board[row][col]"""
    
    # Check row on left side
    for j in range(col):
        if board[row][j] == 1:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_queens(board, col, n):
    """Solve N Queens problem using backtracking"""
    
    # Base case: If all queens are placed, return True
    if col >= n:
        return True
    
    # Consider this column and try placing this queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place this queen in board[i][col]
            board[i][col] = 1
            
            # Recur to place rest of the queens
            if solve_queens(board, col + 1, n):
                return True
            
            # If placing queen in board[i][col] doesn't lead to a solution,
            # then remove queen from board[i][col]
            board[i][col] = 0
    
    # If queen can't be placed in any row in this column col, return False
    return False

def eight_queens():
    # Initialize the chessboard
    n = 8
    board = [[0 for x in range(n)] for y in range(n)]
    
    if solve_queens(board, 0, n) == False:
        print("Solution does not exist")
        return False
    
    # Print the solution
    print("Solution found:")
    print_board(board)
    return True

# Add function to find all solutions
def print_solution(board):
    """Print a board configuration"""
    for row in board:
        print(" ".join("Q" if x == 1 else "." for x in row))
    print()

def solve_all_queens(board, col, n, solutions):
    """Find all solutions to N Queens problem"""
    
    # Base case: If all queens are placed, add the solution
    if col >= n:
        solutions.append([row[:] for row in board])
        return
    
    # Try placing queen in all rows of this column
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place this queen in board[i][col]
            board[i][col] = 1
            
            # Recur to place rest of the queens
            solve_all_queens(board, col + 1, n, solutions)
            
            # Backtrack
            board[i][col] = 0

def find_all_solutions():
    n = 8
    board = [[0 for x in range(n)] for y in range(n)]
    solutions = []
    
    solve_all_queens(board, 0, n, solutions)
    
    print(f"Found {len(solutions)} solutions:")
    for i, solution in enumerate(solutions, 1):
        print(f"\nSolution {i}:")
        print_solution(solution)

# Main program
if __name__ == "__main__":
    choice = input("Enter '1' for first solution or '2' for all solutions: ")
    
    if choice == '1':
        eight_queens()
    else:
        find_all_solutions()