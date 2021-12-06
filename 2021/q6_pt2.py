# Use a list to keeo track of the number of fishs
# Then on each day, shift the count for each item in the dict
# This method is faster than tracking all fishes individually
line = input()

current_state = line.strip().rstrip().split(",")
current_state = [int(f) for f in current_state]
print(f'Initial state: {current_state}')

end_day = 256


def generate_tracker():
    tracker = [0] * 9
    return tracker


current_tracker = generate_tracker()

for f in current_state:
    count = current_tracker[f] + 1
    current_tracker[f] = count


print(f'Initial state: {current_tracker}')

for day in range(0, end_day):
    new_tracker = [0] * 9

    index = 8

    while index >= 0:
        current_count = current_tracker[index]
        if index == 0:
            new_tracker[8] = current_count
            # Need to add new count for six
            new_tracker[6] = new_tracker[6] + current_count
        else:
            next_index = index - 1
            new_tracker[next_index] = current_count

        index -= 1

    # Update current_tracker
    for i in range(0, 9):
        current_tracker[i] = new_tracker[i]

    total_fishs = 0
    for count in current_tracker:
        total_fishs += count

    print(f'After Day {day + 1}: {total_fishs}')

print(f'Completed')

"""
for day in range(0, end_day):
    total_new_fish = 0
    for fish_index in range(0, len(current_state)):
        if current_state[fish_index] == 0:
            current_state[fish_index] = 6
            total_new_fish += 1
        else:
            current_state[fish_index] -= 1

    current_state.extend([8] * total_new_fish)

    print(f'After Day {day + 1}: Number of Fish = {len(current_state)}')
"""

