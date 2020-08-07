from empleado import Empleado

class Gerente(Empleado):

    def __init__(self, nombre, empleado, departamento):
        super().__init__(nombre, empleado)
        self.departamento = departamento

    def __str__(self):
        return super().__str__() + ", Departamento: " + str(self.departamento)


'''
gerente = Gerente('roxana', 10000, 'sistemas')
print(gerente)
'''