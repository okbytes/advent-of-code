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


def fn1(levels, dir):
    a = int(levels[0])
    b = int(levels[1])
    # print(dir, levels, "diff:", abs(a - b))

    if is_safe_diff(a, b):
        if len(levels) == 2:
            return base_case(a, b, dir)

        if is_inc(a, b, dir):
            return fn1(levels[1:], "inc")

        if is_dec(a, b, dir):
            return fn1(levels[1:], "dec")

    return 0


def part1(reports):
    total_safe = 0

    for report in reports:
        ans = fn1(report.split(), None)
        # print("safe:", ans, "\n")

        total_safe += ans

    return total_safe


# print("part 1 ex:", part1(ex_reports))  # output: 2
# print("part 1:", part1(reports))  # output: 314

#
# part 2
#


def fn2(levels, dir, damp):
    a = int(levels[0])
    b = int(levels[1])
    # print(dir, levels, "diff:", abs(a - b))

    if is_safe_diff(a, b):
        if len(levels) == 2:
            return base_case(a, b, dir)

        if is_inc(a, b, dir):
            return fn2(levels[1:], "inc", damp)

        if is_dec(a, b, dir):
            return fn2(levels[1:], "dec", damp)

    return 0


def part2(reports):
    total_safe = 0

    for report in reports:
        ans = fn2(report.split(), None, False)
        # print("safe:", ans, "\n")

        total_safe += ans

    return total_safe


print("part 2 ex:", part2(ex_reports))  # output: 4
# print("part 2:", part2(reports))
