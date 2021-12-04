input_list = []


def get_common_bit(criteria, bit_list, position):
    if len(bit_list) == 1:
        return bit_list

    if position >= len(bit_list[0]):
        return bit_list

    zero_list = []
    ones_list = []
    bit_tracker = 0

    for line in bit_list:
        bit = int(line[position])

        if bit == 0:
            bit_tracker -= 1
            zero_list.append(line)
        else:
            bit_tracker += 1
            ones_list.append(line)

    if criteria == "most":
        if bit_tracker < 0:
            return get_common_bit(criteria, zero_list, position + 1)
        else:
            return get_common_bit(criteria, ones_list, position + 1)
    else:
        if bit_tracker < 0:
            # This means one is the least common
            return get_common_bit(criteria, ones_list, position + 1)
        else:
            return get_common_bit(criteria, zero_list, position + 1)


while True:
    line = input()
    if line == '':
        break
    input_list.append(line)


oxygen_generator_rating = int(get_common_bit("most", input_list, 0)[0], 2)
co2_scrubber_rating = int(get_common_bit("least", input_list, 0)[0], 2)
print(oxygen_generator_rating * co2_scrubber_rating)

