class ClaseRectangulo():

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
         return self.base * self.altura


base = int(input('Inserta la base: '))
altura = int(input('Inserta la altura: '))

rectangulo = ClaseRectangulo(base, altura)
print('El area es:', rectangulo.calcular_area())


