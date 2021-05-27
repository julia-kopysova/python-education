import pytest

from stack import Stack


@pytest.fixture
def stack():
    stack = Stack()
    return stack


def test_push(stack):
    stack.push(1)
    assert stack.head == stack.tail and stack.head.element == 1


def test_push_two_elements(stack):
    stack.push(1)
    stack.push(2)
    assert len(stack) == 2


@pytest.fixture
def stack_with_two():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    return stack


def test_pop_one_time(stack_with_two):
    result = stack_with_two.pop()
    assert result == 2


def test_pop_two_time(stack_with_two):
    stack_with_two.pop()
    result = stack_with_two.pop()
    assert result == 1


def test_pop_exception(stack_with_two):
    stack_with_two.pop()
    stack_with_two.pop()
    with pytest.raises(Exception):
        stack_with_two.pop()


def peek(stack_with_two):
    assert stack_with_two.peek() == 2