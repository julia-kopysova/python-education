"""
Module represents quick sort
"""


def partition(list_sort, left, right):
    """
    Function places smaller than pivot to left of pivot and greater to right
    """
    pivot = left
    for i in range(left + 1, right + 1):
        if list_sort[i] <= list_sort[left]:
            pivot += 1
            list_sort[i], list_sort[pivot] = list_sort[pivot], list_sort[i]
    list_sort[pivot], list_sort[left] = list_sort[left], list_sort[pivot]
    return pivot


def quick_sort(list_sort, left, right):
    """
    Realization of quick sort
    """
    if left < right:
        pivot = partition(list_sort, left, right)
        quick_sort(list_sort, left, pivot - 1)
        quick_sort(list_sort, pivot + 1, right)
