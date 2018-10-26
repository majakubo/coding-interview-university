from ..lists.single_linked_list import SingleLinkedList

class Stack:
    def __init__(self, sequence=None):
        self.buffer = SingleLinkedList(sequence)

    def push(self, value):
        self.buffer.push_front(value)

    def pop(self):
        if self.buffer.length == 0:
            raise NotImplementedError("Stack is empty")
        return self.buffer.pop_front()