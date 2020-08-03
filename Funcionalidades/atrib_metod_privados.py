class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad


p1 = Persona("Juan", 18)
# print(p1.__nombre)  marca un error
print(p1.get_nombre())
print(p1.get_edad())

# p1.__nombre = "Karla" marca un error
p1.set_nombre("Karla")
p1.set_edad(20)
print(p1.get_nombre())
print(p1.get_edad())


'************************************************'

class Persona:
    def __init__(self, nombre, ape_paterno, ape_materno):
        self.nombre = nombre
        self._apellido_paterno = ape_paterno
        self.__apellido_materno = ape_materno

    def metodo_publico(self):
        self.__metodo_privado()

    def __metodo_privado(self):
        print(self.nombre)
        print(self._apellido_paterno)
        print(self.__apellido_materno)

    def get_apellido_materno(self):
        return self.__apellido_materno

    def set_apellido_materno(self, ape_materno):
        self.__apellido_materno = ape_materno


p1 = Persona("Juan", "Lopez", "Perez")
# p1.__metodo_privado() no se puede acceder debido a que es privado
p1.metodo_publico()

print(p1.nombre)
print(p1._apellido_paterno)
# print(p1.__apellido_materno) manda un error por ser privado
print(p1.get_apellido_materno())