import pytest

from src.product_categories import Category


@pytest.mark.parametrize(
    "name, description, price, quantity",
    [("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)],
)
def test_init_product(product_xiaomi, name, description, price, quantity):
    """Тест для проверки инициализации товара: смартфона Ксяоми."""
    assert product_xiaomi.name == name
    assert product_xiaomi.description == description
    assert product_xiaomi.price == price
    assert product_xiaomi.quantity == quantity


def test_init_category(category_smartphones, product_xiaomi, product_iphone):
    """Тест для проверки инициализации категории смартфонов."""
    assert category_smartphones.name == "Смартфоны"
    assert len(category_smartphones.products) == 2
    assert category_smartphones.products[0].name == "Xiaomi Redmi Note 11"
    assert category_smartphones.products[1].name == "Iphone 15"


def test_category_product_counts(category_smartphones):
    """Тест для проверки количества продуктов в категории."""
    assert Category.product_count == 2  # После создания категории с двумя продуктами


def test_category_counts(category_smartphones):
    """Тест для проверки количества категорий."""
    assert Category.category_count == 1  # После создания одной категории
