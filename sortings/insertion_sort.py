def insertion_sort(sequence):
    length = len(sequence)
    for i in range(1, length):
        for j in range(i, -1, -1):
            if sequence[j] < sequence[j-1]:
                sequence[j], sequence[j-1] = sequence[j-1], sequence[j]
            else:
                break

    return sequence