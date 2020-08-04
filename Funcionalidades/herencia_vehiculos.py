'''Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Coche y Bicicleta, las cuales heredan
de la clase Padre Vehiculo
La clase padre debe tener los siguientes atributos y métodos
Vehiculo (Clase Padre):
-Atributos (color, ruedas)
-Métodos ( __init__() y __str__ )
Coche  (Clase Hija de Vehículo) (Además de los atributos y métodos heradados de Vehículo):
-Atributos ( velocidad (km/hr) )
-Métodos ( __init__() y __str__() )
Bicicleta  (Clase Hija de Vehículo) (Además de los atributos y métodos heradados de Vehículo):
-Atributos ( tipo (urbana/montaña/etc )
-Métodos ( __init__() y __str__() )'''


class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "El color del vehiculo es: " + self.color + ", tamaño de ruedas: " + self.ruedas


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__() + ", velocidad: " + str(self.velocidad) + "km/hr"


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas,)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + ", y es de tipo: " + self.tipo


print('Inserte los datos del vehiculo: ')
color = input('Color del Vehiculo: ')
ruedas = input('Tamaño de las ruedas: ')
velocidad = int(input('velocidad: '))
tipo = input('Tipo de vehiculo (urbana/montaña/etc ): ')


vehiculo = Vehiculo(color, ruedas)
print(vehiculo)

coche = Coche(color, ruedas, velocidad)
print(coche)

bicicleta = Bicicleta(color, ruedas, tipo)
print(bicicleta)




