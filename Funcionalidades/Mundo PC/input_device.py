class InputDevice:
    def __init__(self, brand, entry_type):
        #atributos protegidos (accesibles desde una subclase)
        self._brand = brand
        self._entry_type = entry_type

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @property
    def entry_type(self):
        return self._entry_type

    @entry_type.setter
    def entry_type(self, entry_type):
        self._entry_type = entry_type

