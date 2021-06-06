"""
Module represents Hash Table on Linked List
"""
from data_structures_module.structures.linked_list import LinkedList


class HashTableLinked:
    """
    Class represents Hash Table on Linked List
    """
    def __init__(self, size):
        """
        Initialized Linked List
        :param size: amount of nodes
        """
        self.size = size
        self.hash_list = [LinkedList() for _ in range(size)]

    def hash_function(self, key):
        """
        Transfers key to hash
        :param key: key of couple
        :return: hash representation
        """
        hash_element = 0
        for char in key:
            hash_element += ord(char)
        return hash_element % self.size

    def __getitem__(self, key):
        """
        Returns element
        :param key: key of couple
        :return: value
        """
        return self.hash_list[self.hash_function(key)].lookup_value(key)

    def __setitem__(self, key, value):
        """
        Add element to list
        :param key: key of couple
        :param value: value of couple
        :return: Nothing
        """
        if self[key] is None:
            self.hash_list[self.hash_function(key)].add_last((key, value))

    def delete_element(self, key):
        """
        Delete element from hash table
        :param key: key of couple
        :return: Nothing
        """
        if self[key] is not None:
            self.hash_list[self.hash_function(key)].delete_element(key)

    def lookup(self, key):
        """
        Returns value if it contains in Hash Table
        """
        if self[key] is not None:
            return self[key]
        else:
            return None

    def insert(self, key, value):
        """
        Adds a couple to Hash Table
        """
        self[key] = value
