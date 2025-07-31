class ZeroQuantityProduct(Exception):
    """Класс исключений, который отвечает за обработку событий, когда в «Категорию» или «Заказ» добавляется товар
    с нулевым количеством."""

    def __init__(self, message=None):
        super().__init__(message)
