def read_input(file_path):
    """Reads the input file and parses the grid and command sequence."""
    with open(file_path, "r") as f:
        lines = f.read().splitlines()

    # Extract the grid
    grid = []
    commands = ""
    for line in lines:
        if line.startswith("#"):
            grid.append(list(line))
        else:
            commands += line.strip()  # Concatenate all command lines

    return grid, commands


def find_robot_and_boxes(grid):
    """Finds the initial position of the robot and all boxes."""
    robot_pos = None
    boxes = set()

    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == "@":
                robot_pos = (r, c)
                grid[r][c] = "."  # Replace robot with empty space
            elif cell == "O":
                boxes.add((r, c))

    return robot_pos, boxes


def move_robot(grid, robot_pos, boxes, commands):
    """Simulates the robot's movements."""
    # Direction vectors: up, down, left, right
    directions = {
        "^": (-1, 0),
        "v": (1, 0),
        "<": (0, -1),
        ">": (0, 1),
    }

    for command in commands:
        dr, dc = directions[command]
        next_robot_pos = (robot_pos[0] + dr, robot_pos[1] + dc)

        if 0 <= next_robot_pos[0] < len(grid) and 0 <= next_robot_pos[1] < len(grid[0]):
            if next_robot_pos in boxes:  # Robot tries to push a box
                next_box_pos = (next_robot_pos[0] + dr, next_robot_pos[1] + dc)
                if (
                    0 <= next_box_pos[0] < len(grid)
                    and 0 <= next_box_pos[1] < len(grid[0])
                    and grid[next_box_pos[0]][next_box_pos[1]]
                    == "."  # Box can move to empty space
                    and next_box_pos not in boxes
                ):
                    boxes.remove(next_robot_pos)  # Remove old box position
                    boxes.add(next_box_pos)  # Add new box position
                    robot_pos = next_robot_pos  # Robot moves to push the box
            elif (
                grid[next_robot_pos[0]][next_robot_pos[1]] == "."
            ):  # Robot moves to empty space
                robot_pos = next_robot_pos

    return boxes


def calculate_gps_sum(boxes):
    """Calculates the GPS sum of all box positions."""
    gps_sum = 0
    for r, c in boxes:
        gps_sum += 100 * r + c
    return gps_sum


def main(file_path):
    # Step 1: Read input
    grid, commands = read_input(file_path)

    # Step 2: Find initial positions
    robot_pos, boxes = find_robot_and_boxes(grid)

    # Step 3: Simulate robot movements
    boxes = move_robot(grid, robot_pos, boxes, commands)

    # Step 4: Calculate GPS sum
    gps_sum = calculate_gps_sum(boxes)

    # Step 5: Output the result
    print(f"Total GPS sum: {gps_sum}")


if __name__ == "__main__":
    # Replace 'input.txt' with the actual path to your input file
    main("Day 15\\input.txt")
