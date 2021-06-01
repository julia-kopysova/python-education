"""
Module for recursive function factorial
"""


def factorial(number: int) -> int:
    """
    Function calculates factorial
    """
    if number == 0:
        return 1
    elif number < 0:
        raise ValueError("Number must be more 0")
    else:
        return factorial(number - 1) * number
