import fileinput
from collections import defaultdict


class Rules:
    def __init__(self):
        self.rules: defaultdict[int, set[int]] = defaultdict(set)

    def add_rule(self, x: int, y: int):
        self.rules[x].add(y)

    def check_rules(self, pages: list[int]) -> bool:
        for i, page in enumerate(pages):
            if any(rule in pages and pages.index(rule) < i for rule in self.rules[page]):
                return False
        return True


rules = Rules()

total = 0

for line in fileinput.input():
    if "|" in line:
        x, y = line.strip().split("|")
        rules.add_rule(int(x), int(y))

    elif line == "\n":
        continue

    elif "," in line:
        pages: list[int] = list(map(int, line.strip().split(",")))
        if rules.check_rules(pages):
            total += pages[len(pages) // 2]

    else:
        assert False

print(total)
