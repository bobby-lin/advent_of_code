horizontal = 0
depth = 0
aim = 0

while True:
    line = input()
    if line == '':
        break

    line_array = line.split(" ")
    command = line_array[0]
    unit = int(line_array[1])

    if command == "forward":
        horizontal += unit
        depth += (aim * unit)

    elif command == "down":
        aim += unit
    else:
        aim -= unit

print(depth * horizontal)