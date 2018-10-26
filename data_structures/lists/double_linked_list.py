class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.before = None


class DoubleLinkedListIterator():
    def __init__(self, head):
        self.current = head

    def __next__(self):
        if self.current == None:
            raise StopIteration

        value = self.current.data
        self.current = self.current.next

        return value


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        return DoubleLinkedListIterator(self.head)

    def __str__(self):
        list_str = ''
        for element in self:
            list_str += ' ' + str(element) +','

        return '[' + list_str[1:-1] +']'

    def __getitem__(self, index):
        return self.value_at(index)

    def __setitem__(self, index, value):
        self.insert(index, value)

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
        current_node = self.head

        while current_node != None:
            if current_node.data == value:
                if current_node == self.head:
                    self.pop_front()
                elif current_node == self.tail:
                    self.pop_back()
                else:
                    current_node.before.next = current_node.next
                    current_node.next.before = current_node.before
                    self.length -= 1

                break

            current_node = current_node.next

    def insert(self, index, value):
        """at position index adds Node with given value"""
        if index == 0:
            self.push_front(value)
        elif index == self.length - 1:
            self.push_back(value)
        else:
            node_at_index = self.node_at(index)
            new_node = Node(value)
            node_at_index.before.next = new_node
            new_node.before = node_at_index.before
            new_node.next = node_at_index
            node_at_index.before = new_node
            self.length += 1

    def node_at(self, index):
        """returns node at given index"""
        current_node = self.head
        for i in range(index):
            current_node = current_node.next

        return current_node

    def value_at(self, index):
        """returns value at given index"""
        return self.node_at(index).data

if __name__ == '__main__':
    dl = DoubleLinkedList()
    for i in range(10):
        dl.push_back(i)

    print(dl)