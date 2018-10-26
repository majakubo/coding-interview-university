from single_linked_list import SingleLinkedList


def test_push_front():
    l = SingleLinkedList()
    l.push_front(1)
    assert l.head.data == 1
    assert l.tail.data == 1

    l.push_front(2)
    assert l.head.data == 2
    assert l.tail.data == 1
    assert l.head.next.data, l.tail.data

    l.push_front(3)
    assert l.head.data == 3
    assert l.head.next.data == 2


def test_push_back():
    l = SingleLinkedList()
    l.push_back(1)
    assert l.tail.data == 1
    assert l.head.data == 1

    l.push_back(2)
    assert l.tail.data == 2
    assert l.head.data == 1
    assert l.head.next.data == l.tail.data

    l.push_back(3)
    assert l.tail.data == 3
    assert l.head.next.next.data == 3


def test_push_back_second():
    l = SingleLinkedList()
    for i in range(5):
        l.push_back(i)

    assert l.tail.data == 4
    assert l.head.data == 0


def test_value_at():
    l = SingleLinkedList()
    for i in range(5):
        l.push_back(i)

    assert l.value_at(0) == 0
    assert l.value_at(2) == 2
    assert l.value_at(4) == 4


def test_pop_front():
    l = SingleLinkedList()
    for i in range(5):
        l.push_back(i)

    for i in range(4):
        assert l.pop_front() == i
        assert l.head.data == i + 1

    assert l.head.data == l.tail.data
    assert l.tail.data == 4

    l.pop_front()

    assert l.head == None
    assert l.tail == None


def test_pop_back():
    l = SingleLinkedList()

    l.push_back(1)
    assert l.head.data == 1
    assert l.tail.data == 1

    l.push_back(2)
    assert l.head.data == 1
    assert l.tail.data == 2

    l.push_back(3)
    assert l.head.data == 1
    assert l.tail.data == 3

    assert l.pop_back(), 3
    assert l.pop_back(), 2
    assert l.pop_back(), 1


def test_front():
    l = SingleLinkedList()
    for i in range(10):
        l.push_back(i)
        assert 0 == l.front()

    l = SingleLinkedList()
    for i in range(10):
        l.push_front(i)
        assert i == l.front()


def test_back():
    l = SingleLinkedList()
    for i in range(10):
        l.push_back(i)

    assert 9 == l.tail.data


def test_instert_head():
    l = SingleLinkedList()
    for i in range(5):
        l.push_back(i)

    assert l.head.data == 0
    assert l.tail.data == 4

    l.insert(0, 33)
    assert l.head.data == 33


def test_insert_tail():
    l = SingleLinkedList()
    for i in range(5):
        l.push_back(i)

    l.insert(4, 33)

    assert l.tail.data == 33
    assert l.length == 6


def test_insert_middle():
    l = SingleLinkedList()

    for i in range(10):
        l.push_back(i)

    l.insert(3, 99)

    assert l.head.next.next.next.data == 99
    assert l.head.next.next.next.next.data == 3


def test_erase_head():
    l = SingleLinkedList()
    l.push_front(1)
    assert l.head.data == 1

    l.erase(0)
    assert l.head == None


def test_erase_tail():
    l = SingleLinkedList()
    l.push_back(1)
    assert l.tail.data == 1

    l.push_back(2)
    assert l.tail.data == 2

    l.push_back(3)
    assert l.tail.data == 3

    l.erase(2)

    assert l.tail.data == 2


def test_erase_middle():
    l = SingleLinkedList()
    l.push_back(1)
    l.push_back(2)
    l.push_back(3)

    assert l.head.next.data == 2
    l.erase(1)
    assert l.head.next.data == 3


def test_value_n_from_end():
    l = SingleLinkedList()
    for i in range(10):
        l.push_back(i)

    assert l.value_n_from_end(0) == 9
    assert l.value_n_from_end(3) == 6


def test_reverse():
    l = SingleLinkedList()
    for i in range(5):
        l.push_front(i)

    l.reverse()

    assert l.head.data == 0
    assert l.tail.data == 4
    assert l.tail.next == None

    for i in range(5):
        assert l.pop_front() == i




def test_remove_value_front():
    l = SingleLinkedList()
    for i in range(5):
        l.push_back(i)

    l.remove_value(0)

    assert l.head.data == 1


def test_remove_value_middle():
    l = SingleLinkedList()
    for i in range(5):
        l.push_back(i)

    l.remove_value(2)

    assert l.head.next.next.data == 3


def test_remove_value_back():
    l = SingleLinkedList()
    for i in range(5):
        l.push_back(i)

    l.remove_value(4)

    assert l.tail.data == 3
