class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.before = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push_front(self, value):
        """add value at front of list"""
        if self.length == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            buffer = self.head
            self.head = Node(value)
            self.head.next = buffer
            buffer.before = self.head

        self.length += 1

    def pop_front(self):
        """removes value from front and returns it"""
        if self.length == 0:
            raise NotImplementedError("List is empty")
        elif self.length == 1:
            value = self.head.data
            self.head = None
            self.tail = None
        else:
            value = self.head.data
            self.head = self.head.next
            self.head.before = None

        self.length -= 1
        return value

    def push_back(self, value):
        """add calue to the back of the list"""
        if self.length == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            buffer = self.tail
            self.tail = Node(value)
            self.tail.before = buffer
            buffer.next = self.tail

        self.length += 1

    def pop_back(self):
        """removes value from the end of list and returns it"""
        if self.length == 0:
            raise NotImplementedError("List is empty")
        elif self.length == 1:
            value = self.tail.data
            self.tail = None
            self.head = None
        else:
            value = self.tail.data
            self.tail = self.tail.before
            self.tail.next = None

        self.length -= 1
        return value

    def remove(self, value):
        """removes first node with given value in list"""
        pass

    def insert(self, index, value):
        """at position index adds Node with given value"""
        pass

    def node_at(self, index):
        """returns node at given index"""
        pass

    def value_at(self, index):
        """returns value at given index"""
        pass
