class Product:
    """Класс для передачи списка товаров."""

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price  # сеттер с проверкой
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        return self.quantity * self.price + other.quantity * other.price

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
    """Класс для представления товаров по категории. А также подсчета категорий и товаров."""

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

    @property
    def products(self):
        # Возвращаем строку с описанием всех товаров, каждый с новой строки
        return "".join(
            f"{str(product.name)}, {product.price} руб. Остаток: {product.quantity} шт.\n"
            for product in self.__products_list
        )

    def add_product(self, product):
        self.__products_list.append(product)
        Category.product_count += 1
