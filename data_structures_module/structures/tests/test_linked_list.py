import pytest

from linked_list import Node, LinkedList


@pytest.mark.parametrize("element, expected", [(None, None),
                                               ("string", "string"),
                                               (2, 2),
                                               (1.2, 1.2)])
def test_create_node(element, expected):
    node = Node(element)
    assert node.element == expected


def test_create_next():
    element_1 = Node("1")
    element_2 = Node("2")
    element_1.next = element_2
    assert element_1.next == element_2


def test_create_list():
    link_list = LinkedList()
    assert link_list.head is None


def test_add_last_empty():
    linked_list = LinkedList()
    linked_list.add_last("1")
    assert linked_list.head.element == "1"


def test_add_first_empty():
    linked_list = LinkedList()
    linked_list.add_last("1")
    assert linked_list.head.element == "1"


@pytest.fixture
def linked_list():
    linked_list = LinkedList()
    linked_list.add_last("0")
    linked_list.add_last("1")
    linked_list.add_last("2")
    linked_list.add_last("3")
    return linked_list


def test_add_last_not_empty(linked_list):
    linked_list.add_last("last")
    assert "last" in linked_list and linked_list.get_index("last") == len(linked_list) - 1


def test_add_first_not_empty(linked_list):
    linked_list.add_first("first")
    assert "first" in linked_list and linked_list.head.element == "first"


def test_delete_element(linked_list):
    linked_list.delete_element("1")
    assert linked_list.get_index("1") is None


def test_delete_by_index(linked_list):
    linked_list.delete_by_index(1)
    assert "1" not in linked_list
