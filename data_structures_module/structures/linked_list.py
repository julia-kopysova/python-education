"""
This module represents Linked List
"""


class Node:
    """
    Class contains the node of linked list
    """
    def __init__(self, element=None):
        self.element = element
        self.next = None


class LinkedList:
    """
    Class represents logic of Linked List
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        if self.head is None:
            count = 0
        else:
            count = 1
            element = self.head
            while element.next:
                count += 1
                element = element.next
        return count

    def __contains__(self, item):
        node = self.head
        while node is not None:
            if node.element == item:
                return True
            node = node.next
        return False

    def display_list(self):
        node = self.head
        if node is None:
            print("Linked List is empty")
        else:
            while node is not None:
                print(node.element)
                node = node.next

    def get_element_by_index(self, index):
        if index >= len(self):
            raise IndexError("Index out of Linked List")
        index_element = 0
        node = self.head
        while True:
            node = node.next
            if index_element == index:
                return node.element
            index_element += 1

    def get_index(self, element):
        if element in self:
            node = self.head
            index_element = 0
            while index_element <= len(self):
                if node.element == element:
                    return index_element
                node = node.next
                index_element += 1
        else:
            return None

    def add_first(self, new_element):
        node = Node(new_element)
        head_node = self.head
        # node.next = self.head
        self.head = node
        node.next = head_node
        if len(self) == 1:
            self.tail = self.head

    def add_last(self, new_element):
        node = Node(new_element)
        if len(self) == 0:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

        # if self.head is not None:
        #     last_node = self.head
        #     while last_node.next:
        #         last_node = last_node.next
        #     last_node.next = node
        # else:
        #     self.head = node

    def delete_by_index(self, index):
        node = self.head
        if index == 0:
            self.head = node.next
            node = None
        elif index >= len(self):
            raise IndexError("Index out of Linked List")
        else:
            index_element = 0
            while index_element < index - 1:
                node = node.next
                index_element += 1
            node_next = node.next.next
            node.next = None
            node.next = node_next

    def insert(self, new_element, index):
        node = Node(new_element)
        if index < 0:
            raise ValueError("Index is less than needed")
        elif index == 0:
            node.next = self.head
            self.head = node
        else:
            temp = self.head
            for i in range(0, index - 1):
                if temp is not None:
                    temp = temp.next
            if temp is not None:
                node.next = temp.next
                temp.next = node

    def get_node_by_element(self, element):
        if element in self:
            node = self.head
            index_element = 0
            while index_element <= len(self):
                if node.element == element:
                    return node
                node = node.next
                index_element += 1
        else:
            return None

    def get_node_by_index(self, index):
        if index >= len(self):
            raise IndexError("Index out of Linked List")
        index_element = 0
        node = self.head
        while True:
            if index_element == index:
                return node
            node = node.next
            index_element += 1

    def delete_element(self, element):
        """
        Deletes elements
        """
        node = self.head
        if node is None:
            print("Linked List is empty")
        else:
            index = 0

            while node is not None:
                if node.element[0] == element:
                    self.delete_by_index(index)
                else:
                    index += 1
                node = node.next

    def lookup_value(self, key):
        """
        Returns value by key
        """
        node = self.head
        while node is not None:
            if node.element[0] == key:
                return node.element[1]
            node = node.next
        return None

    def delete_el_gr(self, element):
        temp = self.head
        if temp is not None:
            if temp.element == element:
                self.head = temp.next
                temp = None
                return
        prev = None
        while temp is not None:
            if temp.element == element:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None
