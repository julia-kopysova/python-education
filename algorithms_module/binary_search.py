"""
Module represents binary search algorithm
"""


def binary_search(list_searched, search_element):
    """
    Binary search algorithm
    :param list_searched: list for searching
    :param search_element: element that can be found
    :return: index of element or -1 if element wasn't found
    """
    start = 0
    end = len(list_searched) - 1
    index = -1
    while start <= end and index == -1:
        middle = (start + end) // 2
        if list_searched[middle] == search_element:
            index = middle
        else:
            if search_element < list_searched[middle]:
                end = middle - 1
            else:
                start = middle + 1
    return index
