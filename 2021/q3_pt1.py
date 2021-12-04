bit_tracker = []

# First line
line = input()
for bit in line:
    bit = int(bit)
    if bit == 0:
        bit_tracker.append(-1)
    else:
        bit_tracker.append(1)

while True:
    line = input()
    if line == '':
        break

    for i in range(0, len(line)):
        bit = int(line[i])

        if bit == 0:
            bit_tracker[i] -= 1
        else:
            bit_tracker[i] += 1

bit_str = ""
for num in bit_tracker:
    if num < 0:
        bit_str = bit_str + "0"
    else:
        bit_str = bit_str + "1"

gamma = int(bit_str, 2)

inverted_bit_str = bit_str.replace('1', '2').replace('0', '1').replace('2', '0')
epsilon = int(inverted_bit_str, 2)

power_consumption = gamma * epsilon
print(power_consumption)