import fileinput
from collections import deque, Counter

for line in fileinput.input():
    stones: Counter[int] = Counter(map(int, line.strip().split()))

    for blinks in range(75):

        new_stones: Counter[int] = Counter()
        for stone, count in stones.items():
            if stone == 0:
                new_stones[1] += count
            elif (digits := len(s := str(stone))) % 2 == 0:
                new_stones[int(s[: digits // 2])] += count
                new_stones[int(s[digits // 2 :])] += count
            else:
                new_stones[stone * 2024] += count
        stones = new_stones
        print(blinks)

    print(stones.total())
