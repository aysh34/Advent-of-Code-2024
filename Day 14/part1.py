# Input parsing
def parse_input(input_file):
    robots = []
    with open(input_file, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            position, velocity = line.split(" ")
            px, py = map(int, position[2:].split(","))
            vx, vy = map(int, velocity[2:].split(","))
            robots.append(((px, py), (vx, vy)))
    return robots


def movement(robots, time, width, height):
    final_positions = []
    for (px, py), (vx, vy) in robots:
        # Calculate new position with wrapping
        new_px = (px + vx * time) % width
        new_py = (py + vy * time) % height
        final_positions.append((new_px, new_py))
    return final_positions


def classify_quadrants(positions, middle_x, middle_y):
    """
    Classifies the positions of robots into four quadrants.
    Robots on the middle row or column are excluded.
    """
    quadrants = {"top_left": 0, "top_right": 0, "bottom_left": 0, "bottom_right": 0}
    for px, py in positions:
        if px == middle_x or py == middle_y:
            continue
        if px < middle_x and py < middle_y:
            quadrants["top_left"] += 1
        elif px > middle_x and py < middle_y:
            quadrants["top_right"] += 1
        elif px < middle_x and py > middle_y:
            quadrants["bottom_left"] += 1
        elif px > middle_x and py > middle_y:
            quadrants["bottom_right"] += 1
    return quadrants


def calculate_safety_factor(quadrants):
    # Calculates the safety factor by multiplying the counts in all quadrants.
    return (
        quadrants["top_left"]
        * quadrants["top_right"]
        * quadrants["bottom_left"]
        * quadrants["bottom_right"]
    )


if __name__ == "__main__":
    width = 101
    height = 103
    time = 100
    middle_x = width // 2
    middle_y = height // 2

    robots = parse_input("Day 14\\input.txt")
    final_positions = movement(robots, time, width, height)
    quadrant_counts = classify_quadrants(final_positions, middle_x, middle_y)
    safety_factor = calculate_safety_factor(quadrant_counts)
    print("Safety Factor:", safety_factor)
