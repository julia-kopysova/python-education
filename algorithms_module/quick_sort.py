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
    Realization of recursive quick sort
    """
    if left < right:
        pivot = partition(list_sort, left, right)
        quick_sort(list_sort, left, pivot - 1)
        quick_sort(list_sort, pivot + 1, right)


def quick_sort_iterative(list_sort, left, right):
    """
    Realization of iterative quick sort
    """
    size = right - left + 1
    stack = [0] * size
    top = -1
    top = top + 1
    stack[top] = left
    top = top + 1
    stack[top] = right
    while top >= 0:
        right = stack[top]
        top = top - 1
        left = stack[top]
        top = top - 1
        pivot = partition(list_sort, left, right)
        if pivot - 1 > left:
            top = top + 1
            stack[top] = left
            top = top + 1
            stack[top] = pivot - 1
        if pivot + 1 < right:
            top = top + 1
            stack[top] = pivot + 1
            top = top + 1
            stack[top] = right
