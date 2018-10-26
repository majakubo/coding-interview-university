"""series of tests testing double linked list data structure"""
from .double_linked_list import DoubleLinkedList


def test_push_front():
    dl = DoubleLinkedList()
    for i in range(3):
        dl.push_front(i)

    assert dl.head.data == 2
    assert dl.tail.data == 0
    assert dl.tail == dl.head.next.next
    assert dl.head == dl.tail.before.before


def test_push_back():
    dl = DoubleLinkedList()
    for i in range(3):
        dl.push_back(i)

    assert dl.head.data == 0
    assert dl.tail.data == 2
    assert dl.tail == dl.head.next.next
    assert dl.head == dl.tail.before.before


def test_pop_front():
    dl = DoubleLinkedList()
    for i in range(3):
        dl.push_front(i)

    assert dl.pop_front() == 2
    assert dl.head.data == 1
    assert dl.head.next == dl.tail

    assert dl.pop_front() == 1
    assert dl.head.data == 0
    assert dl.head == dl.tail

    assert dl.pop_front() == 0
    assert dl.head == None
    assert dl.tail == None


def test_pop_back():
    dl = DoubleLinkedList()
    for i in range(3):
        dl.push_back(i)

    assert dl.pop_back() == 2
    assert dl.tail.data == 1
    assert dl.head.next == dl.tail

    assert dl.pop_back() == 1
    assert dl.tail.data == 0
    assert dl.head == dl.tail


def test_remove_first():
    dl = DoubleLinkedList()
    for i in range(3):
        dl.push_back(i)

    dl.remove(0)

    assert dl.head.data == 1


def test_remove_last():
    dl = DoubleLinkedList()
    for i in range(3):
        dl.push_back(i)

    dl.remove(2)

    assert dl.tail.data == 1


def test_remove_middle():
    dl = DoubleLinkedList()
    for i in range(3):
        dl.push_back(i)

    dl.remove(1)

    assert dl.head.data == 0
    assert dl.tail.data == 2
    assert dl.head.next == dl.tail
    assert dl.tail.before == dl.head


def test_node_at():
    dl = DoubleLinkedList()
    for i in range(5):
        dl.push_back(i)

    assert dl.node_at(3).data == 3


def test_value_at():
    dl = DoubleLinkedList()
    for i in range(5):
        dl.push_back(i)

    assert dl.value_at(4) == 4


def test_insert():
    dl = DoubleLinkedList()
    for i in range(10):
        dl.push_back(i)

    dl[2] = 4
    dl[0] = 1
    assert dl[3] == 4
    assert dl[0] == 1
