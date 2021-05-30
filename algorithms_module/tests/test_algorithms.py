import pytest

from algorithms_module.binary_search import binary_search
from algorithms_module.factorial import factorial
from algorithms_module.quick_sort import quick_sort


@pytest.fixture
def list_sort():
    list_search = [10, 40, 30, 90, 50, 10, 100, 60, 30, 20, 40, 10, 30, 60, 20, 80]
    return list_search


def test_quick_sort(list_sort):
    assert quick_sort(list_sort, 0, len(list_sort) - 1) == list_sort.sort()


@pytest.fixture
def list_search():
    list_search = [10, 20, 30, 40, 50, 100]
    return list_search


@pytest.mark.parametrize("element, expected", [(10, 0),
                                               (20, 1),
                                               (60, -1)])
def test_binary_search(list_search, element, expected):
    assert binary_search(list_search, element) == expected


@pytest.mark.parametrize("number, expected", [(0, 1),
                                              (2, 2),
                                              (3, 6)])
def test_factorial(number, expected):
    assert factorial(number) == expected


def test_factorial_exception():
    with pytest.raises(ValueError):
        factorial(-3)
