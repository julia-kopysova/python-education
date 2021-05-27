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
