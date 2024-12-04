def read_input(file_path):
    with open(file_path, "r") as file:
        grid = [list(line.strip()) for line in file.readlines()]
    return grid

def count_x_mas(grid):
    # Counts all X-MAS patterns in the grid.
    count = 0
    rows, cols = len(grid), len(grid[0])

    # to check if a diagonal forms "MAS" or "SAM"
    def is_valid_mas(x1, y1, x2, y2, x3, y3):
        if (
            0 <= x1 < rows
            and 0 <= y1 < cols
            and 0 <= x2 < rows
            and 0 <= y2 < cols
            and 0 <= x3 < rows
            and 0 <= y3 < cols
        ):
            diag = grid[x1][y1] + grid[x2][y2] + grid[x3][y3]
            return diag == "MAS" or diag == "SAM"
        return False

    # Iterate through every possible center cell
    for row in range(1, rows - 1):  # Avoid edges
        for col in range(1, cols - 1):  # Avoid edges
            if grid[row][col] == "A":  # Center must be "A"
                # Check diagonals
                top_left = (row - 1, col - 1)
                bottom_right = (row + 1, col + 1)
                top_right = (row - 1, col + 1)
                bottom_left = (row + 1, col - 1)

                valid_diagonal_1 = is_valid_mas(*top_left, row, col, *bottom_right)
                valid_diagonal_2 = is_valid_mas(*top_right, row, col, *bottom_left)

                if valid_diagonal_1 and valid_diagonal_2:
                    count += 1
    return count


file_path = "Day 4\\input 2.txt"
grid = read_input(file_path)
result = count_x_mas(grid)
print(result)
