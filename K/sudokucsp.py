class SudokuSolver:
    def __init__(self, grid):
        self.grid = grid
        self.row_num = len(grid)
        self.col_num = len(grid[0])

    def is_valid(self, row, col, num):
        # Check if number already exists in the row
        for x in range(self.col_num):
            if self.grid[row][x] == num:
                return False

        # Check if number already exists in the column
        for x in range(self.row_num):
            if self.grid[x][col] == num:
                return False

        # Check if number already exists in the box
        start_row, start_col = row - row % 3, col - col % 3
        for i in range(3):
            for j in range(3):
                if self.grid[i + start_row][j + start_col] == num:
                    return False

        return True

    def solve_sudoku(self):
        for i in range(self.row_num):
            for j in range(self.col_num):
                if self.grid[i][j] == 0:
                    for num in range(1, 10):
                        if self.is_valid(i, j, num):
                            self.grid[i][j] = num

                            if self.solve_sudoku():
                                return True

                            self.grid[i][j] = 0

                    return False

        return True

# Define a sudoku puzzle
grid = [
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

solver = SudokuSolver(grid)
solver.solve_sudoku()

# Print the solved puzzle
for row in solver.grid:
    print(row)
