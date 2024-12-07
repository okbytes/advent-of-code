with open("day-2-ex.txt", "r") as file:
    ex_reports = file.read().splitlines()

with open("day-2-input.txt", "r") as file:
    reports = file.read().splitlines()


def is_safe_diff(a, b):
    diff = abs(a - b)
    return diff == 1 or diff == 2 or diff == 3


def is_inc(a, b, dir):
    return a < b and (dir is None or dir == "inc")


def is_dec(a, b, dir):
    return a > b and (dir is None or dir == "dec")


def base_case(a, b, dir):
    return int(is_inc(a, b, dir) or is_dec(a, b, dir))


def checkr(levels, dir):
    a = int(levels[0])
    b = int(levels[1])
    # print(dir, levels, "diff:", abs(a - b))

    if is_safe_diff(a, b):
        if len(levels) == 2:
            return base_case(a, b, dir)

        if is_inc(a, b, dir):
            return checkr(levels[1:], "inc")

        if is_dec(a, b, dir):
            return checkr(levels[1:], "dec")

    return 0


def part1(reports):
    total_safe = 0

    for report in reports:
        ans = checkr(report.split(), None)
        # print("safe:", ans, "\n")

        total_safe += ans

    return total_safe


# print("part 1 ex:", part1(ex_reports))  # output: 2
# print("part 1:", part1(reports))  # output: 314

#
# part 2
#


def rmidx(arr, index):
    """Creates a new array with the specified index removed."""
    return arr[:index] + arr[index + 1 :]


def dampenr(report):
    safe = 0
    levels = report.split()

    if checkr(levels, None):
        return 1

    # loop through all permutations of list to see if any succeed with one removed
    for i in range(len(levels)):
        ans = checkr(rmidx(levels, i), None)
        if ans == 1:
            return ans

    return safe


def part2(reports):
    total_safe = 0

    for report in reports:
        total_safe += dampenr(report)

    return total_safe


print("part 2 ex:", part2(ex_reports))  # output: 4
print("part 2:", part2(reports))  # output: 373
