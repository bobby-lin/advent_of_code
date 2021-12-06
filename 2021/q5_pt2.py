import numpy
data = []
floor_map = numpy.zeros((1000, 1000))

with open('inputs/q5_input') as file:
    for line in file.readlines():
        line_coordinates = line.rstrip().strip().split(" -> ")
        start_coordinates = [int(n.strip()) for n in line_coordinates[0].split(",")]
        end_coordinates = [int(n.strip()) for n in line_coordinates[1].split(",")]
        data.append([start_coordinates, end_coordinates])

for coordinates in data:
    # Check if this is vertical or horizontal line
    start_row = coordinates[0][0]
    start_col = coordinates[0][1]
    end_row = coordinates[1][0]
    end_col = coordinates[1][1]

    # Horizontal
    if start_row == end_row:
        start = start_col
        end = end_col
        if end_col < start_col:
            start = end_col
            end = start_col

        for i in range(start, end + 1):
            floor_map[i][start_row] += 1

    # Vertical
    elif start_col == end_col:
        start = start_row
        end = end_row
        if end_row < start_row:
            start = end_row
            end = start_row

        for i in range(start, end + 1):
            floor_map[start_col][i] += 1

    # Diagonal
    # Definition for 45 deg diagonal
    # the difference between start_row and end_row is the same as difference between start_col and end_col
    elif abs(start_row - end_row) == abs(start_col - end_col):
        row_inc = 1
        col_inc = 1

        if start_row > end_row:
            row_inc = -1

        if start_col > end_col:
            col_inc = -1

        current_row = start_row
        current_col = start_col

        while (current_row != end_row) and (current_col != end_col):
            floor_map[current_col][current_row] += 1

            if current_col != end_col:
                current_col += col_inc
            if current_row != end_row:
                current_row += row_inc

        floor_map[current_col][current_row] += 1


total = 0
for floor in floor_map:
    total += sum(i >= 2 for i in floor)

print(total)