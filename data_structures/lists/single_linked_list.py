from node import Node


class SingleLinkedListIterator:
    def __init__(self, current_node):
        self.current_node = current_node

    def __next__(self):
        if self.current_node == None:
            raise StopIteration
        else:
            buffer = self.current_node
            self.current_node = self.current_node.next
            return buffer.data


class SingleLinkedList:
    def __init__(self, sequence=None):
        self.length = 0
        self.head = None
        self.tail = None
        if sequence:
            for element in sequence:
                self.push_back(element)

    def __iter__(self):
        return SingleLinkedListIterator(self.head)

    def __str__(self):
        list_str = ''
        for element in self:
            list_str += ' ' + str(element) + ','

        list_str = list_str[1:-1]
        return '[' + list_str +']'

    def size(self):
        """returns number of data elements in list"""
        return self.length

    def empty(self):
        """bool returns true if empty"""
        return True if self.length == 0 else False

    def value_at(self, index):
        return self.node_at(index).data

    def node_at(self, index):
        """returns the value of the nth item (startig at 0 for first)"""
        if index >= self.length:
            raise IndexError("To large index")

        current_node = self.head

        for i in range(index):
            current_node = current_node.next

        return current_node

    def push_front(self, value):
        """adds an item to the front of the list"""
        if self.length == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            buffer = self.head
            self.head = Node(value)
            self.head.next = buffer

        self.length += 1

    def pop_front(self):
        """remove front item from front and return its value"""
        if self.length == 0:
            raise NotImplementedError("no implementation for popping from empty list")

        buffer = self.head
        self.head = self.head.next

        self.length -= 1

        if self.length == 0:
            self.tail = None
            self.head = None

        return buffer.data

    def push_back(self, value):
        """adds an item at the end"""
        if self.length == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            buffer = self.tail
            self.tail.next = Node(value)
            self.tail = self.tail.next

        self.length += 1

    def pop_back(self):
        """removes item from end of lits and return its value"""
        if self.length == 0:
            raise NotImplementedError("no implementation for popping from empty list")

        last = self.tail.data
        penultimate = self.node_at(self.length - 2)
        self.tail = penultimate

        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return last

    def front(self):
        """get value of front item"""
        return self.head.data

    def back(self):
        """get value of end item"""
        return self.head.tail

    def insert(self, index, value):
        """insert value at index"""
        if index > self.length:
            raise NotImplementedError("There is no implementation "
                                      "for inserting outside a list")
        if index == 0:
            self.push_front(value)
        elif index == self.length - 1:
            self.push_back(value)
        else:
            before_index = self.node_at(index - 1)
            buffer = Node(value)
            buffer.next = before_index.next
            before_index.next = buffer
            self.length += 1

    def erase(self, index):
        """removes node at given index"""
        if index >= self.length:
            raise IndexError("index out of bounds")

        if index == 0:
            self.pop_front()
        elif index == self.length - 1:
            self.pop_back()
        else:
            before_index = self.node_at(index - 1)
            before_index.next = before_index.next.next
            self.length -= 1

    def value_n_from_end(self, n):
        """returns the value of the node at nth position from the end of the list"""
        return self.value_at(self.length - n - 1)

    def reverse(self):
        """reverses the list"""
        if self.length == 0:
            return

        before_current = None
        current_node = self.head

        while current_node != None:
            next_node = current_node.next
            current_node.next = before_current
            before_current = current_node
            current_node = next_node

        self.head, self.tail = self.tail, self.head

    def remove_value(self, value):
        """removes first node that has value equal to given one"""
        if self.head.data == value:
            self.pop_front()
            return

        before_node = self.head
        current_node = self.head.next

        while current_node != None:
            if current_node.data == value:
                if current_node == self.tail:
                    self.pop_back()
                    return

                before_node.next = current_node.next
                self.length -= 1
                break

            before_node = current_node
            current_node = current_node.next


if __name__ == '__main__':
    l = SingleLinkedList()
    for i in range(10):
        l.push_front(i)
    print(l)