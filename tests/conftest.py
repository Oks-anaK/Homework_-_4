import pytest

from src.product_categories import Category, Product


@pytest.fixture(autouse=True)
def reset_counts():
    """Сбрасывает счетчики категорий и продуктов перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def product_xiaomi():
    """Фикстура для создания экземпляра Product Xiaomi."""
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def product_iphone():
    """Фикстура для создания экземпляра Product iPhone."""
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def category_smartphones(product_xiaomi, product_iphone):
    """Фикстура для создания экземпляра Category Смартфоны."""
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product_xiaomi, product_iphone],
    )
