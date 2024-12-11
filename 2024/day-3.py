with open("day-3-input.txt") as file:
    input = file.read()


digits = "0123456789"


def valid_mul(str):
    first_arg = ""
    has_comma = False
    second_arg = ""

    for char in str:
        if not has_comma:
            if len(first_arg) > 0 and char == ",":
                has_comma = True
            elif char in digits:
                first_arg += char
            else:
                return None
        else:
            if len(second_arg) > 0 and char == ")":
                return first_arg + "," + second_arg
            elif char in digits:
                second_arg += char
            else:
                return None

    return None


# parse multiplication instructions
def parse_mul(str):
    parsed = []

    for i in range(len(str)):
        mul = str[i : i + 4]

        if mul == "mul(":
            rest = valid_mul(str[i + 4 :])
            if rest is not None:
                parsed.append(rest)

    return parsed


# run multiplications and sum the results
def sum_mul(pairs):
    sum = 0
    for pair in pairs:
        a, b = pair.split(",")
        sum += int(a) * int(b)

    return sum


ex_input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
# print(sum_mul(parse_mul(ex_input)))  # example 161
# print("part 1:", sum_mul(parse_mul(input)))  # 173517243

#
#
# Part 2

str_do = "do()"
str_dont = "don't()"

ex_input2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def parse_do(str):
    parsed = []

    is_do = True

    for i in range(len(str)):
        mul = str[i : i + 4]

        do_str = str[i : i + 4]
        dont_str = str[i : i + 7]

        if do_str == str_do:
            is_do = True

        if dont_str == str_dont:
            is_do = False

        if mul == "mul(" and is_do:
            rest = valid_mul(str[i + 4 :])
            if rest is not None:
                parsed.append(rest)

    return parsed


# print("part 2:", sum_mul(parse_do(ex_input2)))  # ex 2*4 + 8*5 = 48
print("part 2:", sum_mul(parse_do(input)))  # 100450138
