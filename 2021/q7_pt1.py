positions = input().strip().rstrip()

position_arr = [int(n) for n in positions.split(",")]
print(len(position_arr))
unique_position_arr = set(position_arr)
print(len(unique_position_arr))

lowest_diff = 0

for n in range(0, max(unique_position_arr)):
    diff = 0
    for i in position_arr:
       diff += abs(n - i)

    if lowest_diff == 0:
        lowest_diff = diff
    else:
        lowest_diff = min(lowest_diff, diff)

    print(diff)

print(lowest_diff)