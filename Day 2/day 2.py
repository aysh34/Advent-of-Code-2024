def part1(reports):
    answer = 0  # To count the safe reports

    for report in reports:
        is_safe = True
        trend = None  # None initially, 'increasing' or 'decreasing'

        for i in range(len(report) - 1):
            diff = report[i + 1] - report[i]

            # Check if the difference is out of the allowed range
            if abs(diff) < 1 or abs(diff) > 3:
                is_safe = False
                break

            # Determine the trend (increasing or decreasing)
            current_trend = "increasing" if diff > 0 else "decreasing"

            # If the trend switches, the report is unsafe
            if trend is None:
                trend = current_trend  # Set initial trend
            elif trend != current_trend:
                is_safe = False
                break

        if is_safe:
            answer += 1
    return answer


def part2(reports):
    answer = 0  # To count the safe reports, considering the Problem Dampener

    for report in reports:
        # First, check if the report is safe as is
        if part1([report]):  # Pass report as a list inside another list for part1
            answer += 1
            continue

        # If the report is unsafe, check if removing a single element makes it safe
        is_safe = False
        for i in range(len(report)):
            new_report = report[:i] + report[i + 1 :]  # Remove one element at index i
            if part1([new_report]):  # Check the report after removing one element
                is_safe = True
                break

        if is_safe:
            answer += 1

    return answer


# Example usage
with open("Day 2/input.txt") as f:
    reports = [[int(i) for i in l.split()] for l in f]

print(part2(reports))
