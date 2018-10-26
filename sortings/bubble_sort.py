def bubble_sort(sequence):
    length = len(sequence)
    for i in range(length):
        for j in range(length - i - 1):
            if sequence[j] > sequence[j+1]:
                sequence[j], sequence[j+1] = sequence[j+1], sequence[j]

    return sequence

