from data_structures.heaps.binary_heap import BinaryHeap


def heap_sort(sequence):
    heap = BinaryHeap(sequence)
    l = []
    for i in range(len(sequence) - 1):
        l.append(heap.extract_min())

    return l

