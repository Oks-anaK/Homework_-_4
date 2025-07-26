from src.product_categories import Product
from src.smartphone_lawngrass import LawnGrass, Smartphone


def test_print_mixin(capsys):
    Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    message = capsys.readouterr()
    assert (
        message.out.strip()
        == "Product(Xiaomi Redmi Note 11, 1024GB, Синий, 31000.0, 14)"
    )

    Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )
    message = capsys.readouterr()
    assert (
        message.out.strip()
        == "Smartphone(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"
    )

    LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый",
    )
    message = capsys.readouterr()
    assert (
        message.out.strip()
        == "LawnGrass(Газонная трава 2, Выносливая трава, 450.0, 15)"
    )
