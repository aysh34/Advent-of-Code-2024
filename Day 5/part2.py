import part1
from collections import defaultdict, deque


# reorder the pages according to rules to correct the incorrect upadte
def topological_sort(upadte, rules):
    graph = defaultdict(list)  # key: page, value: list of pages that depend on key.
    # All pages start with in-degree of 0
    in_degree = defaultdict(
        int
    )  # key: page, value: how many pages must come before this page.
    pages = set(upadte)

    for x, y in rules:
        if x in pages and y in pages:
            graph[x].append(
                y
            )  # Rule 47|53 -> graph[47].append(53 -> graph = {47: [53]}
            in_degree[y] += 1  # in_degree = {47: 0,  53: 1 }
            if x not in in_degree:
                in_degree[x] = 0  # in_degree = {47: 0,  53: 1 }

    queue = deque([x for x in pages if in_degree[x] == 0])  # pages with no dependencies
    result = []

    while queue:
        x = queue.popleft()
        result.append(x)
        for y in graph[x]:
            in_degree[y] -= 1
            if in_degree[y] == 0:
                queue.append(y)

    return result


def process_incorrect_updates(input_data):
    rules, updates = part1.read_input(input_data)
    middle_sum = 0

    for update in updates:
        if not part1.is_valid_update(update, rules):
            # Reorder the update using topological sort
            ordered_update = topological_sort(update, rules)
            # Add the middle page number
            middle_sum += ordered_update[len(ordered_update) // 2]

    return middle_sum


if __name__ == "__main__":
    with open("Day 5\\input2.txt", "r") as f:
        input_data = f.read()
    print(process_incorrect_updates(input_data))
