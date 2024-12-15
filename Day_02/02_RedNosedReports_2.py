import fileinput


def is_safe(levels: list[int]) -> bool:
    bad_level = False
    for i, level1 in list(enumerate(levels))[:-1]:
        level2 = levels[i + 1]
        if i == 0:
            increasing = level1 < level2

        if increasing and level1 >= level2:
            if bad_level:
                return False
            else:
                bad_level = True
                continue

        if not increasing and level1 <= level2:
            if bad_level:
                return False
            else:
                bad_level = True
                continue

        if not 1 <= abs(level1 - level2) <= 3:
            if bad_level:
                return False
            else:
                bad_level = True
                continue
    return True


safe_count = 0

for line in fileinput.input():
    levels: list[int] = list(map(int, line.strip().split()))
    if is_safe(levels):
        safe_count += 1

print(safe_count)
