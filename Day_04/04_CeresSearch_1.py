import fileinput


class Grid:
    grid: list[list[str]]

    def __init__(self, grid):
        self.grid = grid

    def can_east(self, r: int, c: int, wordlen) -> bool:
        return c + wordlen <= len(self.grid[r])

    def can_west(self, r: int, c: int, wordlen) -> bool:
        return c - wordlen + 1 >= 0

    def can_north(self, r: int, c: int, wordlen) -> bool:
        return r - wordlen + 1 >= 0

    def can_south(self, r: int, c: int, wordlen) -> bool:
        return r + wordlen <= len(self.grid)

    def east(self, r: int, c: int, wordlen) -> str:
        if self.can_east(r, c, wordlen):
            return "".join(self.grid[r][c : c + wordlen])
        return ""

    def west(self, r: int, c: int, wordlen) -> str:
        if self.can_west(r, c, wordlen):
            return "".join(
                self.grid[r][c - wordlen + 1 : c + 1][::-1]
            )  # slice forwards, then reverse to deal with the left edge
        return ""

    def north(self, r: int, c: int, wordlen) -> str:
        if self.can_north(r, c, wordlen):
            return "".join([self.grid[r - i][c] for i in range(wordlen)])
        return ""

    def south(self, r: int, c: int, wordlen) -> str:
        if self.can_south(r, c, wordlen):
            return "".join([self.grid[r + i][c] for i in range(wordlen)])
        return ""

    def ne(self, r: int, c: int, wordlen) -> str:
        if self.can_north(r, c, wordlen) and self.can_east(r, c, wordlen):
            return "".join([self.grid[r - i][c + i] for i in range(wordlen)])
        return ""

    def nw(self, r: int, c: int, wordlen) -> str:
        if self.can_north(r, c, wordlen) and self.can_west(r, c, wordlen):
            return "".join([self.grid[r - i][c - i] for i in range(wordlen)])
        return ""

    def se(self, r: int, c: int, wordlen) -> str:
        if self.can_south(r, c, wordlen) and self.can_east(r, c, wordlen):
            return "".join([self.grid[r + i][c + i] for i in range(wordlen)])
        return ""

    def sw(self, r: int, c: int, wordlen) -> str:
        if self.can_south(r, c, wordlen) and self.can_west(r, c, wordlen):
            return "".join([self.grid[r + i][c - i] for i in range(wordlen)])
        return ""


grid: list[list[str]] = []
for line in fileinput.input():
    grid.append(list(line.strip()))

grid: Grid = Grid(grid)
needle = "XMAS"
count = 0
for r in range(len(grid.grid)):
    for c in range(len(grid.grid[r])):
        if grid.north(r, c, len(needle)) == needle:
            count += 1
        if grid.ne(r, c, len(needle)) == needle:
            count += 1
        if grid.east(r, c, len(needle)) == needle:
            count += 1
        if grid.se(r, c, len(needle)) == needle:
            count += 1
        if grid.south(r, c, len(needle)) == needle:
            count += 1
        if grid.sw(r, c, len(needle)) == needle:
            count += 1
        if grid.west(r, c, len(needle)) == needle:
            count += 1
        if grid.nw(r, c, len(needle)) == needle:
            count += 1

print(count)
