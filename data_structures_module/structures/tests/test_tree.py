import pytest

from tree import Tree, Node


def test_create_node():
    node = Node("Animal")
    assert node.element == "Animal" and node.right is None and node.left is None


def test_insert_node_more():
    node = Node(8)
    result = node.insert(9)
    assert result is True and node.right.element == 9


def test_insert_node_equals():
    node = Node(8)
    node.insert(9)
    result = node.insert(9)
    assert result == "This element already in tree"


def test_insert_node_less():
    node = Node(8)
    result = node.insert(2)
    assert result is True and node.left.element == 2


@pytest.mark.parametrize("element, expected", [(10, True),
                                               (8, False)])
def test_lookup_node(element, expected):
    node = Node(9)
    node.insert(10)
    assert node.lookup(element) == expected


def test_create_tree():
    tree = Tree()
    assert tree.root is None


def test_tree_insert_root():
    tree = Tree()
    tree.insert(1)
    assert tree.root.element == 1


@pytest.fixture
def tree():
    tree = Tree()
    tree.insert(5)
    tree.insert(2)
    tree.insert(7)
    tree.insert(8)
    tree.insert(1)
    return tree


@pytest.mark.parametrize("element, expected", [(5, True),
                                               (3, False)])
def test_tree_lookup(tree, element, expected):
    assert tree.lookup(element) == expected