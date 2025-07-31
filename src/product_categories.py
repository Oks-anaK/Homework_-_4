from src.base_product import BaseProduct
from src.exceptions import ZeroQuantityProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """Класс для передачи списка товаров. С возможностью подсчета товаров на складе
    и суммирования с другим товаром типа Product."""

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price  # сеттер с проверкой

        # if quantity > 0:
        self.quantity = quantity
        # else:
        #     raise ValueError('Товар с нулевым количеством не может быть добавлен.')
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        # Суммируем стоимость продуктов со стоимостью объекта типа Product
        if type(other) is Product:
            return self.quantity * self.price + other.quantity * other.price
        raise TypeError

    @property
    def price(self):
        return self.__price  # возвращаем приватный атрибут

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, product_info):
        # Ожидаем словарь с ключами: name, description, price, quantity
        return cls(
            product_info["name"],
            product_info["description"],
            product_info["price"],
            product_info["quantity"],
        )


class Category:
    """Класс для представления товаров по категории. А также подсчета категорий и товаров, добавления продукта
    в категорию."""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products_list=None):
        self.name = name
        self.description = description
        self.__products_list = products_list if products_list else []

        Category.category_count += 1
        Category.product_count += len(self.__products_list)

    def __str__(self):
        list_quantity = [product.quantity for product in self.__products_list]
        sum_quantity = sum(list_quantity)
        return f"{self.name}, количество продуктов: {sum_quantity} шт."

    @property
    def products_list(self):
        # Возвращаем список объектов товаров
        return self.__products_list

    def middle_product_price(self):
        try:
            return sum([product.quantity for product in self.__products_list]) / len(
                self.__products_list
            )
        except ZeroDivisionError:
            return 0

    @property
    def products(self):
        # Возвращаем строку с описанием всех товаров, каждый с новой строки
        return "".join(
            f"{str(product.name)}, {product.price} руб. Остаток: {product.quantity} шт.\n"
            for product in self.__products_list
        )

    def add_product(self, product):
        # Добавляем объект типа Product в категорию
        if isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise ZeroQuantityProduct(
                        "Нельзя добавить товар с нулевым количеством."
                    )
            except ZeroQuantityProduct as e:
                print(str(e))
            else:
                self.__products_list.append(product)
                Category.product_count += 1
                print("Товар успешно добавлен.")
            finally:
                print("Обработка добавления товара завершена.")
        else:
            raise TypeError
