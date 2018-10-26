from ..lists.single_linked_list import SingleLinkedList


class Queue():
    def __init__(self, sequence=None):
        self.buffer = SingleLinkedList(sequence)

    def enqueue(self, value):
        self.buffer.push_front(value)

    def dequeue(self):
        if self.buffer.length == 0:
            raise NotImplementedError("Queue is empty")

        return self.buffer.pop_back()