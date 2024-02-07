def sequence_element(n):
    sequence_list = [1, 2]
    if sequence_list[n - 1] % 2 == 0:
        sequence_list.append(3*sequence_list[n - 2])
    else:
        sequence_list.append(2*sequence_list[n - 1] - sequence_list[n - 2])
    return sequence_list[n]

sequence_element(3)