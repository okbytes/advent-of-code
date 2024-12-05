lhs = []
rhs = []

with open("day-1-input.txt", "r") as file:
    for line in file.read().splitlines():
        left, right = line.split()
        lhs.append(left)
        rhs.append(right)

lhs2 = lhs[:]
rhs2 = rhs[:]
lhs2.sort()
rhs2.sort()

diff = 0

for i in range(len(lhs2)):
    diff += abs(int(lhs2[i]) - int(rhs2[i]))

print("part 1:", diff)

# part 2
total_sim = 0

for numL in lhs:
    sim = 0

    for numR in rhs:
        if numR == numL:
            sim += int(numL)

    total_sim += sim

print("part 2:", total_sim)
