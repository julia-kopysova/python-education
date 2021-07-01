"""
Module represents Hash Table
"""


class HashTable:
    """
    Class represents logic of Hash Table
    """
    def __init__(self):
        """
        Initializes list that contains couples key - value
        """
        self.hash_list = [[] for i in range(30)]

    @staticmethod
    def hash_function(key):
        """
        Hash function
        :param key: key of couple
        :return: hash og key
        """
        hash_element = 0
        for char in key:
            hash_element += ord(char)
        return hash_element % 30

    def lookup(self, key):
        """
        Find value with entering key
        :param key: key of couple
        :return: None or value
        """
        index = self.hash_function(key)
        for element in self.hash_list[index]:
            if element[0] == key:
                return element[1]
            else:
                return None

    def insert(self, key, value):
        """
        Insert a couple in hashtable
        :param key: key that will be hashed
        :param value: value of couple
        :return: Nothing
        """
        hash_index = self.hash_function(key)
        found = False
        for index, element in enumerate(self.hash_list[hash_index]):
            if len(element) == 2 and element[0] == key:
                self.hash_list[hash_index][index] = (key, value)
                found = True
        if not found:
            self.hash_list[hash_index].append((key, value))

    def delete_element(self, key):
        """
        Delete couple by key
        :param key: key of couple
        :return: Nothing
        """
        hash_index = self.hash_function(key)
        for index, element in enumerate(self.hash_list[hash_index]):
            if element[0] == key:
                del self.hash_list[hash_index][index]
