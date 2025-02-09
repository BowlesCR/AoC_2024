import fileinput
import math
import re
from collections import namedtuple
from typing import Optional

Point = namedtuple("Point", ["x", "y"])
Velocity = namedtuple("Velocity", ["x", "y"])
Size = namedtuple("Size", ["x", "y"])

SIZE = Size(101, 103)


class Robot:
    def __init__(self, pos: Point, velocity: Velocity):
        self.pos = pos
        self.velocity = velocity

    def move(self, moves: int):
        x, y = self.pos
        x += self.velocity.x * moves
        x %= SIZE.x
        y += self.velocity.y * moves
        y %= SIZE.y
        self.pos = Point(x, y)

    def get_quadrant(self) -> Optional[int]:
        mid_x = SIZE.x // 2
        mid_y = SIZE.y // 2
        if self.pos.x == mid_x or self.pos.y == mid_y:
            return None
        if self.pos.y < mid_y:
            if self.pos.x < mid_x:
                return 0
            else:
                return 1
        else:
            if self.pos.x < mid_x:
                return 2
            else:
                return 3

    def __str__(self):
        return f"{self.pos.__str__()} {self.get_quadrant()}"


def main():
    robots: list[Robot] = []

    parser = re.compile(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)")

    for line in fileinput.input():
        match = parser.match(line.strip())
        robots.append(
            Robot(
                Point(int(match.group(1)), int(match.group(2))),
                Velocity(int(match.group(3)), int(match.group(4))),
            )
        )

    quadrants: list[int] = [0] * 4
    for robot in robots:
        robot.move(100)
        quad = robot.get_quadrant()
        if quad is not None:
            quadrants[quad] += 1

    robots.sort(key=lambda r: r.pos)
    print(math.prod(quadrants))


if __name__ == "__main__":
    main()
