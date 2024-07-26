#Walter Harrison
#Sudoku Solver
#08/10/2023

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True

    row, col = empty_cell
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0

    return False

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

# Example Sudoku puzzle (replace with your own puzzle)
sudoku_board = [
    [0, 2, 8, 0, 0, 0, 7, 0, 0],
    [0, 0, 7, 0, 0, 0, 0, 9, 3],
    [0, 0, 0, 0, 0, 0, 4, 0, 0],

    [0, 0, 4, 0, 0, 0, 3, 0, 0],
    [0, 0, 0, 0, 0, 5, 0, 1, 0],
    [0, 8, 0, 1, 6, 9, 0, 0, 0],
    
    [0, 0, 0, 0, 1, 0, 0, 0, 9],
    [5, 0, 0, 0, 0, 0, 0, 3, 0],
    [0, 0, 9, 2, 0, 4, 0, 0, 0]
]

if solve_sudoku(sudoku_board):
    print("Solved Sudoku:")
    print_board(sudoku_board)
else:
    print("No solution exists for the Sudoku puzzle.")
