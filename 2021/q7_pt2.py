positions = input().strip().rstrip()

position_arr = [int(n) for n in positions.split(",")]
print(len(position_arr))
unique_position_arr = set(position_arr)
print(len(unique_position_arr))


def calculate_energy(main_position, position):
    diff = abs(main_position - position)
    return ((1 + diff) * diff) / 2


def get_lowest_diff(unique_position_arr, position_arr):
    lowest_diff = 0

    for n in range(0, max(unique_position_arr)):
        diff = 0
        print(f'Number: {n}')
        for i in position_arr:
            energy = calculate_energy(n, i)
            print(energy)
            diff += energy

        if lowest_diff == 0:
            lowest_diff = diff
        else:
            lowest_diff = min(lowest_diff, diff)

    return lowest_diff


print(get_lowest_diff(unique_position_arr, position_arr))
