import fileinput
import math
from collections import defaultdict
from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    r: int
    c: int


class Region:
    def __init__(self, plant: str):
        self.plant = plant
        self.plots: set[Point] = set()
        self.perimeter = 0

    def add_plot(self, plot: Point):
        self.plots.add(plot)

    def area(self) -> int:
        return len(self.plots)

    def price(self) -> int:
        return self.area() * self.perimeter


class Garden:
    def __init__(self):
        self.garden: defaultdict[str, set[Point]] = defaultdict(set)
        self.regions: list[Region] = []
        self.width = -1
        self.height = -1

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
        for p in [
            Point(point.r - 1, point.c),
            Point(point.r + 1, point.c),
            Point(point.r, point.c - 1),
            Point(point.r, point.c + 1),
        ]:
            if p in region.plots:
                continue
            if p in self.garden[char]:
                self.garden[char].remove(p)
                self.findRegion(char, p, region)
            else:
                region.perimeter += 1

    def total_price(self) -> int:
        return sum(region.price() for region in self.regions)


def main():
    garden = Garden()
    garden.parse()
    garden.findRegions()

    print(garden.total_price())


if __name__ == "__main__":
    main()
