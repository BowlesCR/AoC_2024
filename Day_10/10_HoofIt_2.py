import fileinput


def findTrail(r: int, c: int, visited: list[str]) -> set[str]:
    h = grid[r][c]
    visited.append(f"({r},{c})")
    if h == 9:
        return {";".join(visited)}

    paths: set[str] = set()
    if r - 1 >= 0 and (r - 1, c) not in visited and grid[r - 1][c] == h + 1:
        paths.update(findTrail(r - 1, c, visited))
    if r + 1 < len(grid) and (r + 1, c) not in visited and grid[r + 1][c] == h + 1:
        paths.update(findTrail(r + 1, c, visited))
    if c - 1 >= 0 and (r, c - 1) not in visited and grid[r][c - 1] == h + 1:
        paths.update(findTrail(r, c - 1, visited))
    if c + 1 < len(grid[0]) and (r, c + 1) not in visited and grid[r][c + 1] == h + 1:
        paths.update(findTrail(r, c + 1, visited))
    return paths


grid: list[list[int]] = []

for line in fileinput.input():
    grid.append(list(map(int, list(line.strip()))))

score = 0
for r, row in enumerate(grid):
    for c in (c for c, cell in enumerate(row) if cell == 0):
        score += len(findTrail(r, c, []))
print(score)
