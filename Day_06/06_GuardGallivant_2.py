import copy
import fileinput
from enum import Enum


class OffGridException(Exception):
    pass


class LoopException(Exception):
    pass


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class Gallivant:
    def __init__(self, input: list[str], first_pass: bool):
        self.grid: list[list[bool]] = []

        for r, row in enumerate(input):
            if "^" in row:
                self.guard_r: int = r
                self.guard_c: int = row.index("^")
                self.guard_dir: Direction = Direction.NORTH

            self.grid.append([x == "#" for x in row])

        self.first_pass = first_pass

        if self.first_pass:
            self.positions: set[tuple[int, int]] = {(self.guard_r, self.guard_c)}
        else:
            self.positions: set[tuple[int, int, Direction]] = {(self.guard_r, self.guard_c, self.guard_dir)}

        # Cache these because calling len() all the time adds up
        self.len_r = len(self.grid)
        self.len_c = len(self.grid[0])

    def move(self):
        match self.guard_dir:
            case Direction.NORTH:
                target_r = self.guard_r - 1
                target_c = self.guard_c
            case Direction.EAST:
                target_r = self.guard_r
                target_c = self.guard_c + 1
            case Direction.SOUTH:
                target_r = self.guard_r + 1
                target_c = self.guard_c
            case Direction.WEST:
                target_r = self.guard_r
                target_c = self.guard_c - 1

        if self.on_grid(target_r, target_c):
            if self.grid[target_r][target_c]:  # Obstructed
                self.turn_right()
            else:
                self.guard_r = target_r
                self.guard_c = target_c
                if self.first_pass:
                    position = (self.guard_r, self.guard_c)
                else:
                    position = (self.guard_r, self.guard_c, self.guard_dir)

                if not self.first_pass and position in self.positions:
                    raise LoopException  # We're now in a loop
                else:
                    self.positions.add(position)
        else:
            raise OffGridException  # Left grid

    def turn_right(self):
        self.guard_dir = Direction((self.guard_dir.value + 1) % len(Direction))

    def on_grid(self, r: int, c: int) -> bool:
        return 0 <= r < self.len_r and 0 <= c < self.len_c

    def left_grid(self):
        return not self.on_grid(self.guard_r, self.guard_c)


input = list(map(str.strip, fileinput.input()))


# First pass, same as part 1
gallivant = Gallivant(input, True)
while True:
    try:
        gallivant.move()
    except OffGridException:
        break

# Bound search space to positions from part 1
obstructions = 0
for r, c in gallivant.positions:
    if gallivant.grid[r][c] or (r == gallivant.guard_r and c == gallivant.guard_c):
        continue

    new_gallivant: Gallivant = Gallivant(input, False)
    new_gallivant.grid[r][c] = True  # Place new obstacle

    while True:
        try:
            new_gallivant.move()
        except OffGridException:
            break
        except LoopException:
            obstructions += 1
            break
print(obstructions)
