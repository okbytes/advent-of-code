with open("day-4-input.txt") as file:
    input = file.read()

ex1 = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""


def make_grid(multstr):
    grid = []

    for line in multstr.splitlines():
        grid.append(line)

    return grid


def xmas(grid):
    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            has_down = i + 3 < len(grid)  # rows
            has_right = j + 3 < len(grid[i])  # cols
            has_up = i - 3 >= 0
            has_left = j - 3 >= 0

            # horizontal, forward
            if grid[i][j : j + 4] == "XMAS":
                # print(grid[i][j : j + 4])
                count += 1

            # horizontal, backward
            if grid[i][j - 4 : j] == "SAMX":
                # print(grid[i][j - 4 : j])
                count += 1

            # vertical, down
            if (
                has_down
                and grid[i][j] == "X"
                and grid[i + 1][j] == "M"
                and grid[i + 2][j] == "A"
                and grid[i + 3][j] == "S"
            ):
                # print(grid[i][j] + grid[i + 1][j] + grid[i + 2][j] + grid[i + 3][j])
                count += 1

            # vertical, up
            if (
                has_up
                and grid[i][j] == "X"
                and grid[i - 1][j] == "M"
                and grid[i - 2][j] == "A"
                and grid[i - 3][j] == "S"
            ):
                # print(grid[i][j] + grid[i - 1][j] + grid[i - 2][j] + grid[i - 3][j])
                count += 1

            # diagonal, down, right
            if (
                has_down
                and has_right
                and grid[i][j] == "X"
                and grid[i + 1][j + 1] == "M"
                and grid[i + 2][j + 2] == "A"
                and grid[i + 3][j + 3] == "S"
            ):
                # print(
                #     grid[i][j]
                #     + grid[i + 1][j + 1]
                #     + grid[i + 2][j + 2]
                #     + grid[i + 3][j + 3]
                # )
                count += 1

            # diagonal, down, left
            if (
                has_down
                and has_left
                and grid[i][j] == "X"
                and grid[i + 1][j - 1] == "M"
                and grid[i + 2][j - 2] == "A"
                and grid[i + 3][j - 3] == "S"
            ):
                # print(
                #     grid[i][j]
                #     + grid[i + 1][j - 1]
                #     + grid[i + 2][j - 2]
                #     + grid[i + 3][j - 3]
                # )
                count += 1

            # diagonal, up, right
            if (
                has_up
                and has_right
                and grid[i][j] == "X"
                and grid[i - 1][j + 1] == "M"
                and grid[i - 2][j + 2] == "A"
                and grid[i - 3][j + 3] == "S"
            ):
                count += 1

            # diagonal, up, left
            if (
                has_up
                and has_left
                and grid[i][j] == "X"
                and grid[i - 1][j - 1] == "M"
                and grid[i - 2][j - 2] == "A"
                and grid[i - 3][j - 3] == "S"
            ):
                count += 1

    return count


# print("part 1:", xmas(make_grid(ex1)))  # ex 18
# print("part 1:", xmas(make_grid(input)))  # 2336


#
#
# Part 2
#
def check_pts(tl, tr, bl, br):
    first = (tl == "M" and br == "S") or (tl == "S" and br == "M")
    second = (tr == "S" and bl == "M") or (tr == "M" and bl == "S")

    return first and second


def mas(grid):
    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            has_down = i + 1 < len(grid)  # rows
            has_right = j + 1 < len(grid[i])  # cols
            has_up = i - 1 >= 0
            has_left = j - 1 >= 0

            if not (has_down and has_right and has_up and has_left):
                continue

            tl = grid[i - 1][j - 1]
            tr = grid[i - 1][j + 1]
            bl = grid[i + 1][j - 1]
            br = grid[i + 1][j + 1]

            # use the A to pivot and check
            if grid[i][j] == "A" and check_pts(tl, tr, bl, br):
                count += 1

    return count


# print("part 2:", mas(make_grid(ex1)))  # ex 9
print("part 2:", mas(make_grid(input)))  # 1831
