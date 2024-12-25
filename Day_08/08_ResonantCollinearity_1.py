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

        c1_r = ant_a[0] - delta_r
        c1_c = ant_a[1] - delta_c
        if 0 <= c1_r < mapsize and 0 <= c1_c < mapsize:
            antinodes.add((c1_r, c1_c))

        c2_r = ant_b[0] + delta_r
        c2_c = ant_b[1] + delta_c
        if 0 <= c2_r < mapsize and 0 <= c2_c < mapsize:
            antinodes.add((c2_r, c2_c))

print(len(antinodes))
