import random
def quick_sort(sequence):
    if len(sequence) > 1:
        left = []
        right = []
        # choose pivot for partitoning sequence
        pivot_index = random.choice(range(len(sequence)))
        pivot = sequence.pop(pivot_index)
        left.append(pivot)

        while sequence:
            element = sequence.pop(0)
            if element < pivot:
                left.append(element)
            else:
                right.append(element)

        sequence = quick_sort(left) + quick_sort(right)

    return sequence

print(quick_sort([5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5]))