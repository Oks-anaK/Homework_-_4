import pytest

from src.product_categories import Category, Product


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
    assert len(category_smartphones.products_list) == 2
    assert category_smartphones.products_list[0].name == "Xiaomi Redmi Note 11"
    assert category_smartphones.products_list[1].name == "Iphone 15"


def test_category_product_counts(category_smartphones):
    """Тест для проверки количества продуктов в категории."""
    assert Category.product_count == 2  # После создания категории с двумя продуктами


def test_category_counts(category_smartphones):
    """Тест для проверки количества категорий."""
    assert Category.category_count == 1  # После создания одной категории


def test_product_products_list_property(category_smartphones):
    """Тест для проверки вывода списка товаров."""
    expected = (
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    )
    assert category_smartphones.products == expected


def test_product_str(product_xiaomi):
    """Тест для проверки вывода строкового выражения Product."""
    assert str(product_xiaomi) == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."


def test_product__add__(product_xiaomi, product_iphone):
    """Тест для проверки расчета полной стоимости всех товаров на складе."""
    assert product_xiaomi + product_iphone == 2114000.0


def test_product__add__error(product_xiaomi):
    """Тест для проверки возникновения ошибки при суммировании полной стоимости товаров первого типа на складе с
    объектом, не принадлежащим к классу Product."""
    with pytest.raises(TypeError):
        product_xiaomi + [1, 2]


def test_middle_quantity(category_smartphones, category_without_price_list):
    """Тест для проверки правильного расчета среднего ценника товаров в категории."""
    assert category_smartphones.middle_product_price() == 11
    assert category_without_price_list.middle_product_price() == 0


def test_custom_exception(capsys, category_smartphones):
    """Тест для проверки правильного расчета товаров в категории, срабатывания выводов (использование класса исключений
    ZeroQuantityProduct):
    1) при добавлении в категорию продукта с нулевым количеством товаров;
    2) при добавлении в категорию продукта с положительным количеством товаров."""
    assert len(category_smartphones.products_list) == 2

    product_add = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 0)
    category_smartphones.add_product(product_add)
    message = capsys.readouterr()
    assert (
        message.out.strip().split("\n")[-2]
        == "Нельзя добавить товар с нулевым количеством."
    )
    assert (
        message.out.strip().split("\n")[-1] == "Обработка добавления товара завершена."
    )

    product_add = Product("Xiaomi Redmi Note 12", "1024GB, Синий", 35000.0, 6)
    category_smartphones.add_product(product_add)
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2] == "Товар успешно добавлен."
    assert (
        message.out.strip().split("\n")[-1] == "Обработка добавления товара завершена."
    )


def test_category_add_product(category_smartphones):
    """Тест добавления товара в категорию и увеличение счётчика продуктов."""
    initial_count = Category.product_count
    new_product = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    category_smartphones.add_product(new_product)
    assert (
        new_product in category_smartphones._Category__products_list
    )  # Проверяем, что товар добавлен
    assert Category.product_count == initial_count + 1


def test_price_setter(product_xiaomi):
    """Тест сеттера цены с корректным и некорректным значением."""
    product_xiaomi.price = 50000.0
    assert product_xiaomi.price == 50000.0

    # Цена не должна измениться, если передать отрицательное или нулевое значение
    old_price = product_xiaomi.price
    product_xiaomi.price = -100
    assert product_xiaomi.price == old_price

    product_xiaomi.price = 0
    assert product_xiaomi.price == old_price


def test_classmethod_new_product():
    """Тест создания продукта через classmethod new_product с передачей словаря."""
    product_info = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
    product = Product.new_product(product_info)
    assert product.name == product_info["name"]
    assert product.description == product_info["description"]
    assert product.price == product_info["price"]
    assert product.quantity == product_info["quantity"]


def test_category_str(category_smartphones):
    """Тест для проверки вывода строкового выражения Сategory."""
    assert str(category_smartphones) == "Смартфоны, количество продуктов: 22 шт."


def test_category_add_product_error(category_smartphones):
    """Тест для проверки вызова ошибки TypeError при неправильном формате ввода."""
    with pytest.raises(TypeError):
        category_smartphones.add_product(1)


def test_category_add_product_smartphone_1(category_smartphones, product_smartphone_1):
    """Тест для проверки правильной работы метода add_product."""
    category_smartphones.add_product(product_smartphone_1)
    assert category_smartphones.products_list[-1].name == "Samsung Galaxy S23 Ultra"
