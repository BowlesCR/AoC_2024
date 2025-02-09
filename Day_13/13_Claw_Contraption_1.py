import fileinput
import re
from typing import Optional
import numpy as np


class ClawMachine:

    def __init__(self, a: tuple[int, int], b: tuple[int, int], prize: tuple[int, int]) -> None:
        self.a = a
        self.b = b
        self.prize = prize

    def solve(self) -> Optional[tuple[int, int]]:
        A = np.array(
            [
                [self.a[0], self.b[0]],
                [self.a[1], self.b[1]],
            ]
        )
        b = np.array([self.prize[0], self.prize[1]])

        x = np.linalg.solve(A, b)
        if all(round(i, 5).is_integer() for i in x):
            return round(x[0]), round(x[1])
        else:
            return None

    def cost(self) -> int:
        s = self.solve()
        if s:
            a, b = s
            return (3 * a) + (1 * b)
        else:
            return 0


def main():
    RE_BUTTON = re.compile(r"Button [AB]: X([+-]\d+), Y([+-]\d+)")
    RE_PRIZE = re.compile(r"Prize: X=(\d+), Y=(\d+)")

    a: Optional[tuple[int, int]] = None
    b: Optional[tuple[int, int]] = None
    prize: Optional[tuple[int, int]] = None

    tokens = 0
    for i, line in enumerate(fileinput.input()):
        match i % 4:
            case 0:
                m = RE_BUTTON.match(line)
                a = (int(m.group(1)), int(m.group(2)))
            case 1:
                m = RE_BUTTON.match(line)
                b = (int(m.group(1)), int(m.group(2)))
            case 2:
                m = RE_PRIZE.match(line)
                prize = (int(m.group(1)), int(m.group(2)))
            case 3:
                cost = ClawMachine(a, b, prize).cost()
                tokens += cost

    # Handle ragged edge
    cost = ClawMachine(a, b, prize).cost()
    tokens += cost

    print(tokens)


if __name__ == "__main__":
    main()
