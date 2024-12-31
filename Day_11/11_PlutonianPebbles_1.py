import fileinput

for line in fileinput.input():
    stones: list[int] = list(map(int, line.strip().split()))

    for _ in range(25):
        new_stones: list[int] = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif (digits := len(str(stone))) % 2 == 0:
                new_stones.append(int(str(stone)[: digits // 2]))
                new_stones.append(int(str(stone)[digits // 2 :]))
            else:
                new_stones.append(stone * 2024)
        stones = new_stones

    print(len(stones))
