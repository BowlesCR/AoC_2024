import fileinput

for line in fileinput.input():
    disk: list[int] = []
    file_id = 0
    for i, c in enumerate(line.strip()):
        if i % 2 == 0:  # File
            disk.extend([file_id] * int(c))
            file_id += 1
        else:  # Space
            disk.extend([-1] * int(c))

    i = 0
    for end in range(len(disk) - 1, -1, -1):

        if disk[end] == -1:
            disk.pop()
            continue

        while i < end and disk[i] != -1:
            i += 1

        if end <= i:
            break

        disk[i] = disk.pop()

    print(sum(i * c for i, c in enumerate(disk) if c != -1))
