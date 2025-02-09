import fileinput
from collections import defaultdict, namedtuple

Point = namedtuple("Point", ["r", "c"])
Perimeter = namedtuple("Perimeter", ["s", "r", "c"])


class Region:
    def __init__(self, plant: str):
        self.plant = plant
        self.plots: set[Point] = set()
        self.vert_perimeters: list[Perimeter] = []
        self.horz_perimeters: list[Perimeter] = []

    def add_plot(self, plot: Point):
        self.plots.add(plot)

    def area(self) -> int:
        return len(self.plots)

    def price(self) -> int:
        return self.area() * (len(self.vert_perimeters) + len(self.horz_perimeters))

    def sides(self) -> int:
        sides = 0

        last_s = None
        last_r = None
        last_c = None
        for p in sorted(self.horz_perimeters, key=lambda p: (p.s, p.r, p.c)):
            s, r, c = p
            if (s != last_s) or (r != last_r) or (c != last_c + 1):
                sides += 1
            last_s, last_r, last_c = p

        last_s = None
        last_r = None
        last_c = None
        for p in sorted(self.vert_perimeters, key=lambda p: (p.s, p.c, p.r)):
            s, r, c = p
            if (last_s != s) or (c != last_c) or (r != last_r + 1):
                sides += 1
            last_s, last_r, last_c = p

        return sides

    def bulk_price(self):
        return self.area() * self.sides()


class Garden:
    def __init__(self):
        self.garden: defaultdict[str, set[Point]] = defaultdict(set)
        self.regions: list[Region] = []
        self.height = -1
        self.width = -1

    def parse(self):
        for r, line in enumerate(fileinput.input()):
            for c, char in enumerate(line.strip()):
                point = Point(r, c)
                self.garden[char].add(point)
        self.height = r + 1
        self.width = c + 1

    def findRegions(self):
        for char in self.garden:
            while self.garden[char]:
                self.findRegion(char, self.garden[char].pop())

    def findRegion(self, char: str, point: Point, region: Region = None):
        if region is None:
            region = Region(char)
            self.regions.append(region)
        region.add_plot(point)
        for i, p in enumerate(
            [
                Point(point.r - 1, point.c),
                Point(point.r + 1, point.c),
                Point(point.r, point.c - 1),
                Point(point.r, point.c + 1),
            ]
        ):
            if p in region.plots:
                continue
            if p in self.garden[char]:
                self.garden[char].remove(p)
                self.findRegion(char, p, region)
            else:
                if i < 2:
                    region.horz_perimeters.append(Perimeter(-1 if i % 2 == 0 else 1, p.r, p.c))
                else:
                    region.vert_perimeters.append(Perimeter(-1 if i % 2 == 0 else 1, p.r, p.c))

    def total_price(self) -> int:
        return sum(region.bulk_price() for region in self.regions)


def main():
    garden = Garden()
    garden.parse()
    garden.findRegions()

    print(garden.total_price())


if __name__ == "__main__":
    main()
