import pytest

from python_module.unttests.to_test import even_odd, sum_all, Product, Shop


@pytest.mark.parametrize("test_arg, expected", [(1, "odd"),
                                                (2, "even"),
                                                (2.5, "odd"),
                                                (0.000001, "odd"),
                                                (-3, "odd")])
def test_even_odd(test_arg, expected):
    assert even_odd(test_arg) == expected


def test_string_received():
    with pytest.raises(TypeError):
        even_odd("string")


def test_sum_all_with_None():
    with pytest.raises(TypeError):
        sum_all(None, "None")


def test_sum_all_with_positive():
    assert sum_all(5, 2, 8, 9, 1) == 25


def test_sum_all_with_negative():
    assert sum_all(5, -5, 8, -9, -1) == -2


def test_sum_all_with_float():
    assert sum_all(5.5, -5.5, 8.009, -9.022, -1) == -2.013


@pytest.fixture
def product_with_default_quantity():
    """
    :return: Product with default quantity
    """
    return Product("Apple", 90.99)


@pytest.fixture
def product_with_big_quantity():
    return Product("Banana", 90.99, 9999)


def test_product_subtract_quantity_default(product_with_default_quantity):
    product_with_default_quantity.subtract_quantity()
    assert product_with_default_quantity.quantity == 0


@pytest.mark.parametrize("num_of_products, expected", [(1, 9998),
                                                       (-1, 10000),
                                                       (0.5, 9998.5),
                                                       (10000, -1)])
def test_product_subtract_quantity(product_with_big_quantity, num_of_products, expected):
    product_with_big_quantity.subtract_quantity(num_of_products)
    assert product_with_big_quantity.quantity == expected


@pytest.mark.parametrize("num_of_products, expected", [(1, 10000),
                                                       (-1, 9998),
                                                       (0.5, 9999.5),
                                                       (-10000, -1)])
def test_product_add_quantity(product_with_big_quantity, num_of_products, expected):
    product_with_big_quantity.add_quantity(num_of_products)
    assert product_with_big_quantity.quantity == expected


def test_product_add_quantity_default(product_with_default_quantity):
    product_with_default_quantity.add_quantity()
    assert product_with_default_quantity.quantity == 2


def test_product_add_quantity_with_None(product_with_default_quantity):
    with pytest.raises(TypeError):
        product_with_default_quantity.add_quantity(None)


@pytest.mark.parametrize("new_price, expected", [(1, 1),
                                                 (-1, -1),
                                                 (0.5, 0.5)])
def test_product_change_price(product_with_default_quantity, new_price, expected):
    product_with_default_quantity.change_price(new_price)
    assert product_with_default_quantity.price == expected


@pytest.fixture
def empty_shop():
    return Shop()


@pytest.fixture
def shop_with_one_product():
    return Shop(product_with_default_quantity)


def test_shop_create(empty_shop):
    assert empty_shop.products == []


def test_shop_add_two_product(empty_shop, product_with_default_quantity, product_with_big_quantity):
    empty_shop.add_product(product_with_default_quantity)
    empty_shop.add_product(product_with_big_quantity)
    assert empty_shop.products == [product_with_default_quantity, product_with_big_quantity]


def test_shop_add_product(empty_shop, shop_with_one_product):
    empty_shop.add_product(shop_with_one_product)
    assert len(empty_shop.products) == 1


def test_product_get_product_index_None(empty_shop):
    assert empty_shop._get_product_index("None") is None


def test_product_get_product_index():
    shop = Shop(Product("Orange", 90.90, 3))
    assert shop._get_product_index("Orange") == 0


@pytest.fixture
def shop_with_five_product():
    shop = Shop(Product("Apple", 20.0, 5))
    shop.add_product(Product("Orange", 70.0, 3))
    shop.add_product(Product("Pineapple", 100.0, 2))
    shop.add_product(Product("Banana", 30.0, 10))
    shop.add_product(Product("Watermelon", 80.0, 6))
    return shop


def test_product_sell_product(shop_with_five_product):
    assert shop_with_five_product.sell_product("None") is None


def test_product_sell_product_more_qnt(shop_with_five_product):
    with pytest.raises(ValueError):
        shop_with_five_product.sell_product("Orange", 90)


def test_product_sell_product_all_qnt(shop_with_five_product):
    title_product = "Pineapple"
    shop_with_five_product.sell_product(title_product, 2)
    assert shop_with_five_product._get_product_index(title_product) is None


def test_product_sell_product_less_qnt(shop_with_five_product):
    assert shop_with_five_product.sell_product("Banana", 5) == 150.0


def test_product_sell_product_subtract(shop_with_five_product):
    shop_with_five_product.sell_product("Banana", 5)
    index = shop_with_five_product._get_product_index("Banana")
    assert shop_with_five_product.products[index].quantity == 5


def test_product_sell_product_money(shop_with_five_product):
    shop_with_five_product.sell_product("Banana", 5)
    shop_with_five_product.sell_product("Watermelon", 1)
    assert shop_with_five_product.money == 230.0
