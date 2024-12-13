from sympy import symbols, Eq, solve


def find_minimum_cost(prize_x, prize_y, ax, ay, bx, by, cost_a, cost_b):
    # Define variables for the number of button presses
    a, b = symbols("a b", integer=True)

    # Equations for aligning the claw to the prize
    eq1 = Eq(ax * a + bx * b, prize_x)  # X-axis alignment
    eq2 = Eq(ay * a + by * b, prize_y)  # Y-axis alignment

    # Solve the equations for a and b
    solutions = solve((eq1, eq2), (a, b), dict=True)

    # Filter for integer solutions and calculate the costs
    valid_solutions = []
    for sol in solutions:
        a_val = sol[a]
        b_val = sol[b]
        # Check if the solution is valid and non-negative
        if a_val >= 0 and b_val >= 0:
            cost = cost_a * a_val + cost_b * b_val
            valid_solutions.append((a_val, b_val, cost))

    # Return the solution with the minimum cost
    if valid_solutions:
        return min(valid_solutions, key=lambda x: x[2])  # Sort by cost
    else:
        return None  # No valid solution


# Function to read input from a file and process multiple machines
def process_machines(input_file):
    with open(input_file, "r") as file:
        data = file.read().strip().split("\n\n")  # Separate each machine block

    results = []

    for machine in data:
        lines = machine.split("\n")

        # Parse Button A and B movements
        ax, ay = map(
            int, lines[0].split(": ")[1].replace("X+", "").replace("Y+", "").split(", ")
        )
        bx, by = map(
            int, lines[1].split(": ")[1].replace("X+", "").replace("Y+", "").split(", ")
        )

        # Parse Prize location
        prize_x, prize_y = map(
            int, lines[2].split(": ")[1].replace("X=", "").replace("Y=", "").split(", ")
        )

        # Define costs for buttons
        cost_a, cost_b = 3, 1

        # Find the solution for this machine
        solution = find_minimum_cost(prize_x, prize_y, ax, ay, bx, by, cost_a, cost_b)

        if solution:
            a_presses, b_presses, total_cost = solution
            results.append((a_presses, b_presses, total_cost))
        else:
            results.append(None)

    return results


# Process the input file and print results
input_file = "Day 13\\input.txt"  # Replace with your input file path
results = process_machines(input_file)

total_cost = 0
for idx, result in enumerate(results):
    if result:
        a_presses, b_presses, total_cost_machine = result
        total_cost += total_cost_machine
        print(
            f"Machine {idx + 1}: Press Button A {a_presses} times and Button B {b_presses} times. Minimum cost: {total_cost_machine} tokens."
        )
    else:
        print(f"Machine {idx + 1}: No valid solution to win the prize.")

print(f"Total minimum cost to win all possible prizes: {total_cost} tokens.")
