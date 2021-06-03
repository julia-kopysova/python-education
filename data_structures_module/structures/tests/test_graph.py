import pytest

from data_structures_module.structures.graph import Graph


@pytest.fixture
def graph_empty():
    graph = Graph()
    return graph


def test_insert(graph_empty):
    graph_empty.insert_node("1")
    assert len(graph_empty.node_list) == 1


@pytest.fixture
def graph():
    graph = Graph()
    graph.insert_node("2")
    graph.insert_node("3")
    return graph


def test_lookup_correct(graph):
    with pytest.raises(ValueError):
        graph.lookup("5")


def test_delete_node(graph):
    with pytest.raises(ValueError):
        graph.delete_node("4")
