# AOC question 1 - part 1
from sys import stdin

total_depth_increase = 0
prev_average_measurement = None
measurement_list = []

def average(measurement_list):
    return sum(measurement_list) / len(measurement_list)

while True:
    line = input()
    if line == '':
        break

    variable = int(line)

    # Fill up the list if it is empty
    if len(measurement_list) < 3:
        measurement_list.append(variable)
    else:
        prev_average_measurement = sum(measurement_list) / len(measurement_list)

        measurement_list.pop(0)
        measurement_list.append(variable)

        current_average_measurement = average(measurement_list)

        if current_average_measurement > prev_average_measurement:
                total_depth_increase = 1 + total_depth_increase


print(total_depth_increase)
