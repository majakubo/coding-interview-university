from data_structures.heaps.binary_heap import BinaryHeap


def heap_sort(sequence):
    heap = BinaryHeap(sequence)
    l = []
    for i in range(len(sequence) - 1):
        l.append(heap.extract_min())

    return l

if __name__ == '__main__':
    l = [1, 2, 3, 4, 3, 2, 1]
    g = heap_sort(l)

    print(g)