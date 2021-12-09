# In the output values, how many times do digits 1, 4, 7, or 8 appear?

segments = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
sum = 0


def total_diff(segment, pattern):
    diff_count = 0
    for letter in segment:
        if letter not in pattern:
            diff_count += 1

    return diff_count


while True:
    line = input()
    if line == '':
        break

    signal_input = [n.strip().rstrip() for n in line.split("|")]
    signal_patterns = signal_input[0].split(" ")
    signal_output = signal_input[1].split(" ")

    segment_map = {}
    number_map = {}

    for n in signal_patterns:
        current_len = len(n)
        if current_len == segments[1]:
            segment_map.update({1: n})
            number_map.update({"".join(sorted(n)): 1})
        elif current_len == segments[4]:
            segment_map.update({4: n})
            number_map.update({"".join(sorted(n)): 4})
        elif current_len == segments[7]:
            segment_map.update({7: n})
            number_map.update({"".join(sorted(n)): 7})
        elif current_len == segments[8]:
            segment_map.update({8: n})
            number_map.update({"".join(sorted(n)): 8})

    final_patterns = []
    for n in signal_patterns:
        current_len = len(n)

        if len(n) == 5:
            if segment_map.get(1)[0] in n and segment_map.get(1)[1] in n:
                final_patterns.append(3)
                number_map.update({"".join(sorted(n)): 3})
            else:
                # Compare with 4
                diff_count = total_diff(segment_map.get(4), n)
                if diff_count == 2:
                    final_patterns.append(2)
                    number_map.update({"".join(sorted(n)): 2})
                else:
                    final_patterns.append(5)
                    number_map.update({"".join(sorted(n)): 5})
        elif len(n) == 6:
            diff_count = total_diff(segment_map.get(1), n)
            if diff_count == 1:
                final_patterns.append(6)
                number_map.update({"".join(sorted(n)): 6})
            else:
                diff_count = total_diff(segment_map.get(4), n)
                if diff_count == 1:
                    final_patterns.append(0)
                    number_map.update({"".join(sorted(n)): 0})
                else:
                    final_patterns.append(9)
                    number_map.update({"".join(sorted(n)): 9})
        elif current_len == segments[1]:
            final_patterns.append(1)
        elif current_len == segments[4]:
            final_patterns.append(4)
        elif current_len == segments[7]:
            final_patterns.append(7)
        elif current_len == segments[8]:
            final_patterns.append(8)
        else:
            final_patterns.append(n)

    output_str = ""
    for n in signal_output:
        output_str += str(number_map.get("".join(sorted(n))))

    sum += int(output_str)

print(sum)