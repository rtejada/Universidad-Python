class Monitor:
    count = 0

    def __init__(self, brand, size):
        Monitor.count += 1
        self.__id_monitor = Monitor.count
        self.__brand = brand
        self.__size = size

    def __str__(self):
        return (
            f"ID: {self.__id_monitor}, "
            f"Brand: {self.__brand}, "
            f"Size: {self.__size}"
        )

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size


#monitor = Monitor('hp', '20 pulgadas')
#print(monitor)
