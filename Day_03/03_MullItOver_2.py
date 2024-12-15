import fileinput
import re

mul = re.compile(r"(mul(?=\((\d+),(\d+)\))|do(?=\(\))|don't(?=\(\)))")  # mul with a positive lookahead for the parens

total = 0
enabled = True
for line in fileinput.input():
    matches = mul.findall(line)
    for match in matches:
        if match[0] == "do":
            enabled = True
        elif match[0] == "don't":
            enabled = False
        elif enabled and match[0] == "mul":
            total += int(match[1]) * int(match[2])

print(total)
