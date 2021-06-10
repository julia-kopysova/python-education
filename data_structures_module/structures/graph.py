"""
Module represents a Graph
"""
from data_structures_module.structures.linked_list import LinkedList


class Node:
    """
    Class represents a Node
    """
    def __init__(self, element):
        """
        Initializes Node
        :param element: element of Graph Node
        """
        self.element = element
        self.edges_for_this_node = LinkedList()


class Graph:
    """
    Class represents a logic of Graph
    """

    def __init__(self):
        """
        Initialized in Graph
        """
        self.node_list = LinkedList()

    def insert_node(self, element, *elements_link):
        """
        Add a new Node with the element to the Graph.
        """
        new_node = Node(element)
        self.node_list.add_last(new_node)
        if elements_link is not None:
            for element_link in elements_link:
                node_graph = self.lookup(element_link)
                # print("Node_graph", node_graph)
                if node_graph not in new_node.edges_for_this_node:
                    if node_graph:
                        node_graph.edges_for_this_node.add_last(new_node)
                        new_node.edges_for_this_node.add_last(node_graph)
                    else:
                        raise Exception("Node wasn't found")
                else:
                    raise Exception("Graph have already contained this edge")

    def lookup(self, element):
        """
        Returns Graph-Node if it contains in Graph
        """
        result_node = None
        for ind in range(len(self.node_list)):
            # вытянули ноду c Linked List в которой элемент = нода Graph
            node_from_list = self.node_list.get_node_by_index(ind)
            if element == node_from_list.element.element:
                result_node = node_from_list
        if result_node:
            return result_node.element
        else:
            return None

    def delete_node(self, element):
        """
        Deletes the node in Graph and delete edges
        """
        node_graph = self.lookup(element)
        for ind in range(len(self.node_list)):
            node_from_list = self.node_list.get_node_by_index(ind)
            if node_graph in node_from_list.element.edges_for_this_node:
                node_from_list.element.edges_for_this_node.delete_el_gr(node_graph)
        self.node_list.delete_el_gr(node_graph)


if __name__ == "__main__":
    gra = Graph()
    gra.insert_node("1")

    gra.insert_node("2", "1")
    gra.insert_node("3", "1", "2")
    gra.insert_node("4", "1")
    gra.node_list.display_list()

    print("Lookup 3:", gra.lookup("3"))

    node = gra.lookup("1")
    print("1: ", len(node.edges_for_this_node))
    node2 = gra.lookup("2")
    print("2: ", len(node2.edges_for_this_node))
    node3 = gra.lookup("3")
    print("3: ", len(node3.edges_for_this_node))

    print("Delete")
    gra.delete_node("3")
    gra.node_list.display_list()

    print("Lookup 3 after deleted:", gra.lookup("3"))

    node = gra.lookup("1")
    print("1: ", len(node.edges_for_this_node))
    node2 = gra.lookup("2")
    print("2: ", len(node2.edges_for_this_node))
