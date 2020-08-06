class Product:
    count_product = 0

    def __init__(self, name, price):
        Product.count_product += 1
        self.__id = Product.count_product
        self.__name = name
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    def __str__(self):

        return 'Id_Product: ' + str(self.__id) + ', Name Product: ' + self.__name + ', Price: ' + str(self.__price)



