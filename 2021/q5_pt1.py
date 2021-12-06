import numpy
data = []
floor_map = numpy.zeros((10, 10))

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

    if start_row == end_row:
        start = start_col
        end = end_col
        if end_col < start_col:
            start = end_col
            end = start_col

        for i in range(start, end + 1):
            floor_map[i][start_row] += 1

    elif start_col == end_col:
        start = start_row
        end = end_row
        if end_row < start_row:
            start = end_row
            end = start_row

        for i in range(start, end + 1):
            floor_map[start_col][i] += 1

total = 0
for floor in floor_map:
    print(floor)
    total += sum(i >= 2 for i in floor)

print(total)