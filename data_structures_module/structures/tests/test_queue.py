import pytest

from queue import Queue


@pytest.fixture
def queue():
    queue = Queue()
    return queue


def test_enqueue(queue):
    queue.enqueue(1)
    assert queue.head == queue.tail and queue.head.element == 1


def test_enqueue_two_elements(queue):
    queue.enqueue(1)
    queue.enqueue(2)
    assert len(queue) == 2


@pytest.fixture
def queue_with_three():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    return queue


def test_dequeue_one_time(queue_with_three):
    result = queue_with_three.dequeue()
    assert result == 1


def test_dequeue_two_time(queue_with_three):
    queue_with_three.dequeue()
    result = queue_with_three.dequeue()
    assert result == 2


def test_dequeue_three_time(queue_with_three):
    queue_with_three.dequeue()
    queue_with_three.dequeue()
    result = queue_with_three.dequeue()
    assert result == 3


def test_dequeue_exception(queue_with_three):
    queue_with_three.dequeue()
    queue_with_three.dequeue()
    queue_with_three.dequeue()
    with pytest.raises(Exception):
        queue_with_three.dequeue()


def peek(queue_with_three):
    assert queue_with_three.peek() == 3

