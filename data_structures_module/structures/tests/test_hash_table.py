import pytest

from data_structures_module.structures.hast_table import HashTable


@pytest.fixture
def hash_table_empty():
    hash_table_empty = HashTable()
    return hash_table_empty


def test_insert(hash_table_empty):
    hash_table_empty.insert("1", "first")
    assert hash_table_empty.hash_list[19][0] == ("1", "first")


@pytest.fixture
def hash_table():
    hash_table = HashTable()
    hash_table.insert("1", "first")
    hash_table.insert("2", "second")
    hash_table.insert("index", "element")
    return hash_table


def test_lookup(hash_table):
    result = hash_table.lookup("1")
    assert result == "first"


def test_delete(hash_table):
    hash_table.delete_element("index")
    assert hash_table.lookup("index") is None
