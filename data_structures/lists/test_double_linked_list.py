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