from .stack import Stack

def test_stack():
    s = Stack()
    for i in range(10):
        s.push(i)

    for i in range(10):
        assert s.pop() == 9 - i