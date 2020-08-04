from cuadrado import Cuadrado
from rectangulo import Rectangulo

cuadrado = Cuadrado(4, "rojo")
rectangulo = Rectangulo(8, 'verde')
print(cuadrado.area_cuadrado(), cuadrado.color())
print(rectangulo.area_rectangulo(), rectangulo.color())

#el orden de busqueda es:
#Cuadrado, FiguraGeometrica(izquierda), Color(derecha), Object(Clase Abuela)
#print(Cuadrado.mro())

