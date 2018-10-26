from .bubble_sort import bubble_sort
from .selection_sort import selection_sort
from .insertion_sort import insertion_sort
from .merge_sort import merge_sort
from .heap_sort import heap_sort

def test_bubble():
    l = list(range(9, -1, -1))
    l = bubble_sort(l)

    for i in range(10):
        assert l[i] == i


def test_selection():
    l = list(range(9, -1, -1))
    l = selection_sort(l)

    for i in range(10):
        assert l[i] == i

    l = [0, 1, 2, 3, 4, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4]
    l = selection_sort(l)

    assert l == [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]


def test_insertion():
    l = [4, 3, 2, 1, 1, 2, 3, 0, 3, 2, 1, 0]
    l = selection_sort(l)

    assert [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4] == l


def test_heap_sort():
    l = [4, 3, 2, 1, 0, 1, 2, 3, 4, 0, 1, 2, 3, 3, 2, 1]
    l = heap_sort(l)

    assert l == [0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4]

    l = list(range(50, -1, -1))
    l = heap_sort(l)

    assert l == list(range(0, 51))
