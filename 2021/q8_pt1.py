# In the output values, how many times do digits 1, 4, 7, or 8 appear?

segments = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
sum = 0

while True:
    line = input()
    if line == '':
        break

    signal_input = [n.strip().rstrip() for n in line.split("|")]
    signal_patterns = signal_input[0].split(" ")
    signal_output = signal_input[1].split(" ")
    for n in signal_output:
        current_len = len(n)
        if current_len == segments[1] or current_len == segments[4] or current_len == segments[7] or current_len == segments[8]:
            sum += 1

print(sum)

