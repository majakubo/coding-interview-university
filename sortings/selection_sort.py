def selection_sort(sequence):
    length = len(sequence)

    for i in range(length):
        minimal = i
        for j in range(i, length):
            if sequence[j] < sequence[minimal]:
                minimal = j

        sequence[i], sequence[minimal] = sequence[minimal], sequence[i]

    return sequence


if __name__ == '__main__':
    l = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    l = selection_sort(l)
