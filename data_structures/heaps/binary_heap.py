def parent(index):
    return index // 2


def left_child(index):
    return index * 2


def right_child(index):
    return index * 2 + 1


class BinaryHeap:
    def __init__(self, sequence=None):
        if sequence == None:
            sequence = []
        self.heap = sequence
        self.heap.insert(0, 0)
        self.build_heap()

    def build_heap(self):
        middle = len(self.heap) // 2 - 1
        for index in range(middle, 0, -1):
            self.heapify(index)

    def bubble_up(self, index):
        up = parent(index)
        if index > 1:
            if self.heap[index] < self.heap[up]:
                self.heap[index], self.heap[up] = self.heap[up], self.heap[index]
                self.bubble_up(up)

    def heapify(self, index):
        length = len(self.heap)
        left = left_child(index)
        right = right_child(index)
        smallest = index

        if left < length and self.heap[smallest] > self.heap[left]:
            smallest = left

        if right < length and self.heap[smallest] > self.heap[right]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify(smallest)

    def insert_key(self, value):
        self.heap.append(value)
        index = len(self.heap) - 1
        self.bubble_up(index)

    def decrease_key(self, index, new_value):
        self.heap[index] = new_value
        self.bubble_up(index)

    def extract_min(self):
        if len(self.heap) > 2:
            minimal = self.heap[1]
            last = self.heap.pop()
            self.heap[1] = last
            self.heapify(1)
        else:
            minimal = self.heap.pop()

        return minimal

    def get_min(self):
        return self.heap[1]


if __name__ == '__main__':
    hp = BinaryHeap()
    for i in range(50, 0, -1):
        hp.insert_key(i)

    for i in range(1,51):
        print(hp.extract_min())


