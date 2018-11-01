def quick_sort(seq, first=None, last=None):
    if first == None and last == None:
        first = 0
        last = len(seq) - 1

    if first < last:
        split = partition(seq, first, last)

        quick_sort(seq, first, split - 1)
        quick_sort(seq, split + 1, last)


def partition(seq, first, last):
    pivot = seq[first]

    left = first + 1
    right = last

    done = False
    while not done:

        while left <= right and seq[left] <= pivot:
            left = left + 1

        while seq[right] >= pivot and right >= left:
            right = right - 1

        if right < left:
            done = True
        else:
            seq[left], seq[right] = seq[right], seq[left]

    seq[left], seq[right] = seq[right], seq[left]

    return right


seq = list(range(10, 0, -1))
quick_sort(seq)
print(seq)