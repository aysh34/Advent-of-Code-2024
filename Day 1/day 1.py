import os


def read_file(file_name):
    if not os.path.exists(file_name):
        raise FileNotFoundError(f"File not found: {file_name}")

    with open(file_name, "r") as f:
        lines = [line.strip() for line in f.readlines()]
        return lines


def get_input(lines):
    l = []
    r = []

    for line in lines:
        line = line.replace("   ", " ")
        nums = line.split()
        l.append(int(nums[0]))
        r.append(int(nums[1]))

    l = sorted(l)
    r = sorted(r)

    total = 0
    for i in range(len(l)):
        total += abs(l[i] - r[i])

    print(total)


def get_input2(lines):
    # print(lines)
    l = []
    r = {}

    for line in lines:
        line.replace("   ", " ")
        nums = line.split()
        l.append(int(nums[0]))
        occurences = int(nums[1])
        if occurences in r:
            r[occurences] += 1
        else:
            r[occurences] = 1

    total = 0
    for num in l:
        if num in r:
            total += num * r[num]

    print(total)


def main():
    lines = read_file("Day 1/input.txt")
    get_input2(lines)


if __name__ == "__main__":
    main()
