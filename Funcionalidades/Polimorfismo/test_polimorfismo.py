from empleado import Empleado
from gerente import Gerente

def imprimir_detalles(objeto):
    print(objeto)
    print(type(objeto), end='\n\n')
    if isinstance(objeto, Gerente):
        print(objeto.departamento)


empleado = Empleado('Roxana', 2000.00)
imprimir_detalles(empleado)

#sin llamar a la funcion imprimir_detalles
print(empleado)

gerente = Gerente('Roxana', 2000.00, 'QA')
imprimir_detalles(gerente)
print(gerente)

