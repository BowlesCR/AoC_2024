import fileinput


def findTrail(r: int, c: int, visited: set[(int, int)]) -> (int, int):
    h = grid[r][c]
    if h == 9:
        return {(r, c)}

    visited.add((r, c))
    reachable = set()
    if r - 1 >= 0 and (r - 1, c) not in visited and grid[r - 1][c] == h + 1:
        reachable.update(findTrail(r - 1, c, visited))
    if r + 1 < len(grid) and (r + 1, c) not in visited and grid[r + 1][c] == h + 1:
        reachable.update(findTrail(r + 1, c, visited))
    if c - 1 >= 0 and (r, c - 1) not in visited and grid[r][c - 1] == h + 1:
        reachable.update(findTrail(r, c - 1, visited))
    if c + 1 < len(grid[0]) and (r, c + 1) not in visited and grid[r][c + 1] == h + 1:
        reachable.update(findTrail(r, c + 1, visited))
    return reachable


grid: list[list[int]] = []

for line in fileinput.input():
    grid.append(list(map(int, list(line.strip()))))

score = 0
for r, row in enumerate(grid):
    for c in (c for c, cell in enumerate(row) if cell == 0):
        score += len(findTrail(r, c, set()))
print(score)
