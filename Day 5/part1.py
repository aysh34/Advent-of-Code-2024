# input handling
def read_input(input_data):
    # split the input in two sections on for rules and one for updates
    sections = input_data.strip().split("\n\n")
    # sections = [rules, updates]
    # rules =[
    # "1|2"
    # "3|4"
    # ...]
    # updates = [
    # "1,2,3,4"
    # "5,67,88,90"
    # ... ]

    # rules -> ["1|2" "3|4" ...] -> [(1,2), (3,4)]
    # updates -> ["1,2,3,4" "5,67,88,90"] -> [[1,2,3,4], [5,67,88,90]]

    rules = [tuple(map(int, rule.split("|"))) for rule in sections[0].split("\n")]
    updates = [list(map(int, update.split(","))) for update in sections[1].split("\n")]

    return rules, updates


def is_valid_update(update, rules):
    # filter only those rules relevant to the update
    relevant_rules = [rule for rule in rules if rule[0] in update and rule[1] in update]

    for x, y in relevant_rules:  # rule(x,y)
        # page x must apprear before page y in the update
        if update.index(x) > update.index(y):
            return False  # invalid update
    return True  # valid update


def find_middle(update):
    return update[len(update) // 2]


def process_upadtes(input_data):
    rules, updates = read_input(input_data)  # get the rules and updates
    middle_sum = 0

    for update in updates:
        if is_valid_update(update, rules):
            middle_sum += find_middle(update)

    return middle_sum


if __name__ == "__main__":
    with open("Day 5\\input1.txt", "r") as f:
        input_data = f.read()
    print(process_upadtes(input_data))
