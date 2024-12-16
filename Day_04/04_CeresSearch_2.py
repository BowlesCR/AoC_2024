import fileinput


class Grid:
    grid: list[list[str]]

    def __init__(self, grid):
        self.grid = grid

    def can_east_west(self, r: int, c: int, wordlen) -> bool:
        return (c - wordlen // 2) >= 0 and (c + wordlen // 2) <= len(self.grid[r])

    def can_north_south(self, r: int, c: int, wordlen) -> bool:
        return (r - wordlen // 2) >= 0 and (r + wordlen // 2) <= len(self.grid)

    def east_west(self, r: int, c: int, wordlen) -> str:
        if self.can_east_west(r, c, wordlen):
            return "".join([self.grid[r][c + i] for i in range(-1 * (wordlen // 2), wordlen // 2 + 1)])
        return ""

    def north_south(self, r: int, c: int, wordlen) -> str:
        if self.can_north_south(r, c, wordlen):
            return "".join([self.grid[r + i][c] for i in range(-1 * (wordlen // 2), wordlen // 2 + 1)])
        return ""

    def nw_se(self, r: int, c: int, wordlen) -> str:
        if self.can_north_south(r, c, wordlen) and self.can_east_west(r, c, wordlen):
            return "".join([self.grid[r + i][c + i] for i in range(-1 * (wordlen // 2), wordlen // 2 + 1)])
        return ""

    def sw_ne(self, r: int, c: int, wordlen) -> str:
        if self.can_north_south(r, c, wordlen) and self.can_east_west(r, c, wordlen):
            return "".join([self.grid[r - i][c + i] for i in range(-1 * (wordlen // 2), wordlen // 2 + 1)])
        return ""


grid: list[list[str]] = []
for line in fileinput.input():
    grid.append(list(line.strip()))
del line

grid: Grid = Grid(grid)
needle = "MAS"
count = 0
for r in range(1, len(grid.grid) - 1):
    for c in range(1, len(grid.grid[r]) - 1):
        # ns = grid.north_south(r, c, len(needle))
        # ew = grid.east_west(r, c, len(needle))
        #
        # if (ns == needle or ns == needle[::-1]) and (ew == needle or ew == needle[::-1]):
        #     count += 1
        #
        # del ns, ew

        nw_se = grid.nw_se(r, c, len(needle))
        sw_ne = grid.sw_ne(r, c, len(needle))

        if (nw_se == needle or nw_se == needle[::-1]) and (sw_ne == needle or sw_ne == needle[::-1]):
            count += 1

        del nw_se, sw_ne

print(count)
