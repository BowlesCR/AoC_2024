import fileinput
import itertools

total = 0

for line in fileinput.input():
    line = line.strip().split(" ")
    testval = int(line[0].removesuffix(":"))
    operands = list(map(int, line[1:]))

    for operators in itertools.product("+*", repeat=len(operands) - 1):
        accumulator = operands[0]
        try:
            for operator, operand in zip(operators, operands[1:]):
                if operator == "+":
                    accumulator += operand
                elif operator == "*":
                    accumulator *= operand
                else:
                    assert False

                if accumulator > testval:
                    raise StopIteration
            if accumulator == testval:
                total += testval
                break
        except StopIteration:
            continue
print(total)
