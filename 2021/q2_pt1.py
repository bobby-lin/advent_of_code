position_x = 0
position_y = 0

while True:
    line = input()
    if line == '':
        break

    line_array = line.split(" ")
    command = line_array[0]
    unit = int(line_array[1])

    if command == "forward":
        position_x += unit
    elif command == "down":
        position_y += unit
    else:
        position_y -= unit

print(position_y * position_x)