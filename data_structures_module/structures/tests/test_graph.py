import pytest

from data_structures_module.structures.graph import Graph, Node


@pytest.fixture
def graph_empty():
    graph = Graph()
    return graph


@pytest.fixture
def graph():
    graph = Graph()
    graph.insert_node("1")
    graph.insert_node("2", "1")
    graph.insert_node("3", "1", "2")
    return graph


def test_lookup_graph(graph):
    result = graph.lookup("2")
    assert isinstance(result, Node) is True


def test_lookup_graph_None(graph):
    result = graph.lookup("6")
    assert result is None


def test_insert_graph_first_element(graph_empty):
    graph_empty.insert_node("1")
    assert len(graph_empty.node_list) == 1


def test_insert_graph_edge(graph):
    graph.insert_node("4", "1")
    node = graph.lookup("1")
    assert len(node.edges_for_this_node) == 3


def test_insert_graph_edge_node(graph):
    graph.insert_node("4", "1", "2")
    node = graph.lookup("4")
    assert len(node.edges_for_this_node) == 2


def test_insert_edge_exist(graph):
    with pytest.raises(Exception):
        graph.insert_node("4", "1", "1")


def test_insert_edge_not_exist(graph):
    with pytest.raises(Exception):
        graph.insert_node("4", "1", "6")


def test_delete_node(graph):
    graph.delete_node("2")
    assert graph.lookup("2") is None


def test_delete_node_len(graph):
    len_before = len(graph.node_list)
    graph.delete_node("2")
    assert len_before == (len(graph.node_list) + 1)


def test_delete_node_edges(graph):
    graph.delete_node("2")
    node = graph.lookup("1")
    assert len(node.edges_for_this_node) == 1