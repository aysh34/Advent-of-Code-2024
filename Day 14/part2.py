import numpy as np
from typing import List, Tuple


def parse_input(filename: str) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    robots = []
    with open(filename, "r") as f:
        for line in f:
            pos_str, vel_str = line.strip().split(" ")
            px, py = map(int, pos_str[2:].split(","))
            vx, vy = map(int, vel_str[2:].split(","))
            robots.append(((px, py), (vx, vy)))
    return robots


def simulate_robots(
    robots: List[Tuple[Tuple[int, int], Tuple[int, int]]],
    time: int,
    width: int,
    height: int,
) -> np.ndarray:
    """
    Simulate robot movements and count robot positions after given time.
    Returns:
        numpy array of robot count per tile
    """
    # Initialize grid to track robot positions
    grid = np.zeros((height, width), dtype=int)

    for (px, py), (vx, vy) in robots:
        # Calculate final position after time, with wraparound
        final_x = (px + vx * time) % width
        final_y = (py + vy * time) % height
        grid[final_y, final_x] += 1

    return grid


def is_christmas_tree(grid: np.ndarray) -> bool:
    """
    Check if the robot positions form a Christmas tree pattern.
    """
    tree_pattern = [
        [0, 0, 1, 0, 0],  # top of tree
        [0, 1, 1, 1, 0],  # middle of tree
        [1, 1, 1, 1, 1],  # base of tree
    ]

    height, width = grid.shape

    # Search for the pattern in the grid
    for y in range(height - len(tree_pattern)):
        for x in range(width - len(tree_pattern[0])):
            # Check if this section matches the tree pattern
            match = True
            for dy, row in enumerate(tree_pattern):
                for dx, val in enumerate(row):
                    if val == 1 and grid[y + dy, x + dx] == 0:
                        match = False
                        break
                if not match:
                    break

            if match:
                return True

    return False


def find_christmas_tree_time(
    filename: str, max_time: int = 10000, width: int = 101, height: int = 103
) -> int:
    """
    Find the earliest time when robots form a Christmas tree pattern.
    """
    robots = parse_input(filename)

    # Search for Christmas tree pattern
    for time in range(max_time):
        # Simulate robot positions
        grid = simulate_robots(robots, time, width, height)

        # Check for Christmas tree pattern
        if is_christmas_tree(grid):
            return time

    return -1  # No pattern found within max_time


# Solve problem
result = find_christmas_tree_time("Day 14\\input.txt")
print(result)
