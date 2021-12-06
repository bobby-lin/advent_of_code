
line = input()

current_state = line.strip().rstrip().split(",")
current_state = [int(f) for f in current_state]
print(f'Initial state: {current_state}')

end_day = 80

for day in range(0, 80):
    total_new_fish = 0
    for fish_index in range(0, len(current_state)):
        if current_state[fish_index] == 0:
            current_state[fish_index] = 6
            total_new_fish += 1
        else:
            current_state[fish_index] -= 1

    current_state.extend([8] * total_new_fish)

    print(f'After Day {day + 1}: {current_state}')
    print("Number of Fish = " + str(len(current_state)))