def count_guard_path(grid):
    # Parse the grid and find the starting position and direction
    rows = len(grid)
    cols = len(grid[0])
    directions = ["N", "E", "S", "W"]
    moves = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}

    # Find the guard's starting position and direction
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in "^>v<":
                start_pos = (r, c)
                direction = {"^": "N", ">": "E", "v": "S", "<": "W"}[grid[r][c]]
                break

    visited = set()
    position = start_pos
    visited.add(position)

    while True:
        # Calculate the position directly in front of the guard
        dr, dc = moves[direction]
        next_r, next_c = position[0] + dr, position[1] + dc

        # Check if it's out of bounds
        if not (0 <= next_r < rows and 0 <= next_c < cols):
            break

        # Check the cell in front
        if grid[next_r][next_c] == "#":
            # Turn 90 degrees to the right
            direction = directions[(directions.index(direction) + 1) % 4]
        else:
            # Move forward
            position = (next_r, next_c)
            visited.add(position)

    return len(visited)


if __name__ == "__main__":
    with open("Day 6\\input1.txt", "r") as file:
        grid = file.read().splitlines()
        
    print(count_guard_path(grid))  # Output the number of distinct positions visited
