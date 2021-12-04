# AOC question 1 - part 1
from sys import stdin

total_depth_increase = 0
prev_measurement = None

while True:
    line = input()
    if line == '':
        break

    variable = int(line)

    if prev_measurement != None:
        if variable > prev_measurement:
            total_depth_increase = 1 + total_depth_increase

    prev_measurement = variable


print(total_depth_increase)

