from .binary_heap import BinaryHeap

def test_heap_build_and_extract():
    hp = BinaryHeap([0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1])

    assert hp.extract_min() == 0
    assert hp.extract_min() == 1
    assert hp.extract_min() == 1
    assert hp.extract_min() == 2
    assert hp.extract_min() == 2
    assert hp.extract_min() == 3
    assert hp.extract_min() == 3
    assert hp.extract_min() == 4
    assert hp.extract_min() == 4
    assert hp.extract_min() == 5
    assert hp.extract_min() == 5
    assert hp.extract_min() == 6


def test_heap_build_and_extract_two():
    hp = BinaryHeap(list(range(10, -1, -1)))
    for i in range(11):
        assert hp.extract_min() == i


def test_insert_and_extract():
    hp = BinaryHeap()
    for i in range(50, -1, -1):
        hp.insert_key(i)

    for i in range(0, 51):
        assert hp.extract_min() == i


def test_decrease_key_and_extract():
    hp = BinaryHeap(list(range(50)))
    hp.decrease_key(30, -3)

    assert hp.extract_min() == -3
