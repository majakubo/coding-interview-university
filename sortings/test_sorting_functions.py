from .bubble_sort import bubble_sort
from .selection_sort import selection_sort

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