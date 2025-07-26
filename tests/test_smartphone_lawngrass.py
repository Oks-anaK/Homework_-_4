import pytest


def test_smartphone_init(product_smartphone_1):
    assert product_smartphone_1.name == "Samsung Galaxy S23 Ultra"
    assert product_smartphone_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_smartphone_1.price == 180000.0
    assert product_smartphone_1.quantity == 5
    assert product_smartphone_1.efficiency == 95.5
    assert product_smartphone_1.model == "S23 Ultra"
    assert product_smartphone_1.memory == 256
    assert product_smartphone_1.color == "Серый"


def test_smartphone_add(product_smartphone_1, product_smartphone_2):
    assert product_smartphone_1 + product_smartphone_2 == 2580000.0


def test_smartphone_add_error(product_smartphone_1):
    with pytest.raises(TypeError):
        product_smartphone_1 + 23


def test_lawngrass_init(product_lawngrass_1):
    assert product_lawngrass_1.name == "Газонная трава"
    assert product_lawngrass_1.description == "Элитная трава для газона"
    assert product_lawngrass_1.price == 500.0
    assert product_lawngrass_1.quantity == 20
    assert product_lawngrass_1.country == "Россия"
    assert product_lawngrass_1.germination_period == "7 дней"
    assert product_lawngrass_1.color == "Зеленый"


def test_lawngrass_add(product_lawngrass_1, product_lawngrass_2):
    assert product_lawngrass_1 + product_lawngrass_2 == 16750.0


def test_lawngrass_add_error(product_lawngrass_1):
    with pytest.raises(TypeError):
        product_lawngrass_1 + 34
