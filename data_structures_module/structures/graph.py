"""
Module represents a Graph
"""
from linked_list import LinkedList


class Node:
    """
    Class represents a Node
    """
    def __init__(self, element):
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
        if elements_link:
            for element_link in elements_link:
                if element_link in self.node_list:
                    new_node.edges_for_this_node.add_last(element_link)
                    node_link_index = self.node_list.get_index(element_link)
                    node_link = self.node_list.get_node_by_index(node_link_index)
                    node_link.edges_for_this_node.add_last(new_node)
                else:
                    raise ValueError("This node doesn't contain in Graph")

    def lookup(self, element):
        """
        Returns node if it contains in Graph
        """
        node = self.node_list.get_node_by_element(element)
        if node:
            return node
        else:
            raise ValueError("Node not in Graph")

    def has_node(self, element):
        """
        Return True if element is contained in the Graph
        and False if element is not contained in the Graph.
        """
        if element in self.node_list:
            return True
        else:
            return False

    def delete_node(self, element):
        """
        Deletes the node in Graph
        """
        if element in self.node_list:
            self.node_list.delete_element(element)
        else:
            raise ValueError("Element doesn't exist")
