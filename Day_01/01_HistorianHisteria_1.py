import fileinput

left: list[int] = []
right: list[int] = []
for line in fileinput.input():
    locations = line.strip().split("   ")
    left.append(int(locations[0]))
    right.append(int(locations[1]))

left.sort()
right.sort()

deltas = [abs(pair[0] - pair[1]) for pair in zip(left, right)]

print(sum(deltas))
