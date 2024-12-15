import fileinput
from collections import Counter

left: list[int] = []
right: list[int] = []

for line in fileinput.input():
    locations = line.strip().split("   ")
    left.append(int(locations[0]))
    right.append(int(locations[1]))

right: Counter = Counter(right)
score = 0

for i in left:
    score += i * right[i]

print(score)
