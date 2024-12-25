import fileinput
from collections import defaultdict
from itertools import combinations

antennas: defaultdict[str, list[tuple[int, int]]] = defaultdict(list)
mapsize = 0
for r, line in enumerate(map(str.strip, fileinput.input())):
    if r == 0:
        mapsize = len(line)
    for c, char in enumerate(line):
        if char == ".":
            continue

        antennas[char].append((r, c))

antinodes: set[tuple[int, int]] = set()
for f_ant in antennas.values():
    for ant_a, ant_b in combinations(f_ant, 2):
        delta_r = ant_b[0] - ant_a[0]
        delta_c = ant_b[1] - ant_a[1]

        anti_r = ant_a[0]
        anti_c = ant_a[1]
        while 0 <= anti_r < mapsize and 0 <= anti_c < mapsize:
            antinodes.add((anti_r, anti_c))
            anti_r -= delta_r
            anti_c -= delta_c

        anti_r = ant_b[0]
        anti_c = ant_b[1]
        while 0 <= anti_r < mapsize and 0 <= anti_c < mapsize:
            antinodes.add((anti_r, anti_c))
            anti_r += delta_r
            anti_c += delta_c
print(len(antinodes))
