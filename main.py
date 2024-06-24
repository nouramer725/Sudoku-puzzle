def solve_sudoku(grid):
    # Find the next empty cell in the grid
    row, col = find_empty_cell(grid)

    # If there are no empty cells, the puzzle is solved
    if row is None:
        return True

    # Try numbers from 1 to 9
    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            # Place the number in the current cell
            grid[row][col] = num

            # Recursively solve the puzzle with the updated grid
            if solve_sudoku(grid):
                return True

            # If the current number leads to an invalid solution, backtrack
            grid[row][col] = 0

    # If no number can be placed in the current cell, backtrack
    return False


def find_empty_cell(grid):
    # Find the next empty cell represented by 0
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None, None


def is_valid_move(grid, row, col, num):
    # Check if the number is already present in the current row
    for i in range(9):
        if grid[row][i] == num:
            return False

    # Check if the number is already present in the current column
    for i in range(9):
        if grid[i][col] == num:
            return False

    # Check if the number is already present in the current 3x3 subgrid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True


# Example puzzle to solve
puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Solve the puzzle
if solve_sudoku(puzzle):
    print("Sudoku puzzle solved:")
    for row in puzzle:
        print(row)
else:
    print("No solution exists for the given puzzle.")