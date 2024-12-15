import fileinput
import re

mul = re.compile(r"mul\((\d+),(\d+)\)")

total = 0
for line in fileinput.input():
    matches = mul.findall(line)
    for match in matches:
        total += int(match[0]) * int(match[1])

print(total)
