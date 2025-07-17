class ProductIterator:
    def __init__(self, cat_obj):
        self.cat = cat_obj
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.cat.products_list):
            product = self.cat.products_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
