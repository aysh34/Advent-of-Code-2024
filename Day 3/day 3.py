import re

def part1(input):
    with open(input) as f:
        corrupted_memory = f.read()

    valid_pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"  # mul(111, 2)

    valid_instructions = re.findall(valid_pattern, corrupted_memory)

    result = 0
    for instruction in valid_instructions:
        numbers = re.findall(r"[0-9]+", instruction)  # extract numbers from instruction

        if numbers:
            result += int(numbers[0]) * int(numbers[1])

    return result


def part2(input):
    with open(input) as f:
        corrupted_memory = f.read()

    valid_instructions = re.findall(
        r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)", corrupted_memory
    )  # returning an array of strings
    # print(valid_instructions)

    mul_enabled = True
    result = 0
    for instruction in valid_instructions:
        if instruction == "do()":
            mul_enabled = True
        elif instruction == "don't()":
            mul_enabled = False
        elif instruction.startswith("mul"):
            numbers = re.findall(
                r"[0-9]+", instruction
            )  # extract numbers from instruction
            if numbers and mul_enabled:
                result += int(numbers[0]) * int(numbers[1])
    return result


if __name__ == "__main__":
    print(part1("Day 3\\input.txt"))
    print(part2("Day 3\\input2.txt"))
