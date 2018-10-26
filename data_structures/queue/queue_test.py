from .queue import Queue

def test_queue():
    q = Queue()

    for i in range(10):
        q.enqueue(i)

    for i in range(10):
        assert q.dequeue() == i
