"""
Class represents a tree
"""


class Node:
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None

    def insert(self, element):
        if self.element > element:
            if self.left:
                return self.left.insert(element)
            else:
                self.left = Node(element)
                return True
        elif self.element < element:
            if self.right:
                return self.right.insert(element)
            else:
                self.right = Node(element)
                return True
        else:
            return "This element already in tree"

    def lookup(self, element):
        if self.element > element:
            if self.left:
                return self.left.lookup(element)
            else:
                return False
        elif self.element < element:
            if self.right:
                return self.right.lookup(element)
            else:
                return False
        else:
            return True


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, element):
        if self.root:
            return self.root.insert(element)
        else:
            self.root = Node(element)
            return True

    def lookup(self, element):
        if self.root:
            return self.root.lookup(element)
        else:
            return False

    def delete(self, element):
        """
        Delete node from tree
        """
        if self.root is None:
            return False
        # If element = root
        elif self.root.element == element:
            # Only root
            if self.root.left is None and self.root.right is None:
                self.root = None
            # Only left part
            elif self.root.left and self.root.right is None:
                self.root = self.root.left
            # Only right part
            elif self.root.left is None and self.root.right:
                self.root = self.root.right
            # Two parts exist
            elif self.root.left and self.root.right:
                delete_patent = self.root
                delete_node = self.root.right
                while delete_node.left:
                    delete_patent = delete_node
                    delete_node = delete_node.left
                self.root.element = delete_node.element
                if delete_node.right:
                    if delete_patent.element > delete_node.element:
                        delete_patent.left = delete_node.right
                    elif delete_patent.element < delete_node.element:
                        delete_patent.right = delete_node.right
                else:
                    if delete_node.element < delete_patent.element:
                        delete_patent.left = None
                    else:
                        delete_patent.right = None

            return True

        parent = None
        node = self.root
        # If not root
        # Search node
        while node and node.element != element:
            parent = node
            if element < node.element:
                node = node.left
            elif element > node.element:
                node = node.right

        # If element doesn't exist
        if node is None or node.element != element:
            return False

        # Node doesn't have element lower
        elif node.left is None and node.right is None:
            if element < parent.element:
                parent.left = None
            else:
                parent.right = None
            return True

        # Only left part
        elif node.left and node.right is None:
            if element < parent.element:
                parent.left = node.left
            else:
                parent.right = node.left
            return True

        # Only right part
        elif node.left is None and node.right:
            if element < parent.element:
                parent.left = node.right
            else:
                parent.right = node.right
            return True

        # Has two part
        else:
            delete_patent = node
            delete_node = node.right
            while delete_node.left:
                delete_patent = delete_node
                delete_node = delete_node.left

            node.element = delete_node.element
            if delete_node.right:
                if delete_patent.element > delete_node.element:
                    delete_patent.left = delete_node.right
                elif delete_patent.element < delete_node.element:
                    delete_patent.right = delete_node.right
            else:
                if delete_node.element < delete_patent.element:
                    delete_patent.left = None
                else:
                    delete_patent.right = None
