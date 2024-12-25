import fileinput
from itertools import product

locks: set[tuple[int, int, int, int, int]] = set()
keys: set[tuple[int, int, int, int, int]] = set()

PIN_SPACE = 7

input = list(fileinput.input())
for r in range(0, len(input), PIN_SPACE + 1):
    is_lock = input[r][0] == "#"

    p0 = sum(1 for i in range(PIN_SPACE) if input[r + i][0] == "#") - 1
    p1 = sum(1 for i in range(PIN_SPACE) if input[r + i][1] == "#") - 1
    p2 = sum(1 for i in range(PIN_SPACE) if input[r + i][2] == "#") - 1
    p3 = sum(1 for i in range(PIN_SPACE) if input[r + i][3] == "#") - 1
    p4 = sum(1 for i in range(PIN_SPACE) if input[r + i][4] == "#") - 1

    if is_lock:
        locks.add((p0, p1, p2, p3, p4))
    else:
        keys.add((p0, p1, p2, p3, p4))

del input, p0, p1, p2, p3, p4

count = 0
for lock, key in product(locks, keys):
    try:
        for p in range(5):
            if lock[p] + key[p] >= (PIN_SPACE - 1):
                raise StopIteration
        count += 1
    except StopIteration:
        continue

print(count)
