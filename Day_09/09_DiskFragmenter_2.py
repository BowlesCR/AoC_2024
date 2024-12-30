import fileinput

for line in fileinput.input():
    disk: dict[int, tuple[int, int]] = {}
    file_id = 0
    pos = 0
    for i, c in enumerate(line.strip()):
        if i % 2 == 0:  # File
            disk[pos] = (file_id, int(c))
            file_id += 1
        else:  # Space
            disk[pos] = (-1, int(c))
        pos += int(c)
    del line

    for key in sorted(disk.keys(), reverse=True):
        pos = 0
        file_id, size = disk[key]
        if file_id == -1:
            del disk[key]
            continue

        while pos < key:
            space_size = disk[pos][1]
            if disk[pos][0] != -1:
                pos += space_size
                continue

            if space_size >= size:
                disk[pos] = (file_id, size)
                del disk[key]
                pos += size

                space_size -= size
                if space_size:
                    disk[pos] = (-1, space_size)
                break
            else:
                pos += space_size

    checksum = 0
    for key in disk.keys():
        file_id, size = disk[key]
        if file_id == -1:
            continue
        for pos in range(key, key + size):
            checksum += file_id * pos
    print(checksum)
