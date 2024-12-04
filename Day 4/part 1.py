# with open("Day 4\input.txt") as f:
#     grid = [list(line.strip()) for line in f.readlines()]
#     print(grid)

# Directions: (d_row, d_col)
directions = [
    (0, 1),  # Right
    (0, -1),  # Left
    (1, 0),  # Down
    (-1, 0),  # Up
    (1, 1),  # Diagonal ↘
    (1, -1),  # Diagonal ↙
    (-1, 1),  # Diagonal ↗
    (-1, -1),  # Diagonal ↖
]


def read_input(file_path):
    # Reads the grid from an input file.
    with open(file_path, "r") as file:
        grid = [list(line.strip()) for line in file.readlines()]
    return grid


def check_word(grid, row, col, d_row, d_col):
    """Checks if 'XMAS' exists starting from (row, col) in a given direction."""
    word = "XMAS"
    for i in range(len(word)):
        # Compute new position
        new_row = row + i * d_row
        new_col = col + i * d_col

        # Check bounds
        if (
            new_row < 0
            or new_row >= len(grid)
            or new_col < 0
            or new_col >= len(grid[0])
        ):
            return False

        # Check letter
        if grid[new_row][new_col] != word[i]:
            return False
    return True


def count_xmas(grid):
    """Counts all occurrences of 'XMAS' in the grid."""
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            for d_row, d_col in directions:
                if check_word(grid, row, col, d_row, d_col):
                    count += 1
    return count


file_path = "Day 4/input.txt"
grid = read_input(file_path)
result = count_xmas(grid)
print(result)
