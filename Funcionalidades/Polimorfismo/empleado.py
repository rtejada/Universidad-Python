class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def __str__(self):
        return 'Nombre: '+ self.nombre + ', Sueldo: ' + str(self.sueldo)

'''
empleado = Empleado('Roxana', '1000.00')
print(empleado)
'''