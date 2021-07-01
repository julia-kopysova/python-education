import pytest

from data_structures_module.structures.hash_table_linked_list import HashTableLinked


@pytest.fixture
def hash_table_empty():
    hash_table_empty = HashTableLinked(3)
    return hash_table_empty


def test_hash_function(hash_table_empty):
    result = hash_table_empty.hash_function("first")
    assert result == 0


@pytest.fixture
def hash_table():
    hash_table = HashTableLinked(3)
    hash_table.insert("1", "first")
    hash_table.insert("2", "second")
    hash_table.insert("firstt", "element")
    return hash_table


def test_get(hash_table):
    assert hash_table["1"] == "first"


def test_set(hash_table):
    hash_table["5"] = "five"
    assert hash_table["5"] == "five"


def test_insert(hash_table):
    hash_table.insert("6", "six")
    assert hash_table["6"] == "six"


def test_delete(hash_table):
    hash_table.delete_element("firstt")
    assert hash_table["firstt"] is None


def test_lookup(hash_table):
    assert hash_table.lookup("firstt") == "element"


def test_lookup_None(hash_table):
    assert hash_table.lookup("ttt") is None
