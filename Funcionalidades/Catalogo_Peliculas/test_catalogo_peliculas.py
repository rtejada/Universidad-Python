from peliculas import Pelicula
from catalogo_peliculas import CatalogoPeliculas
import sys

opcion = None
while opcion != "4":
    print("Opciones:")
    print("1. Agregar película")
    print("2. Listar películas")
    print("3. Eliminar catálogo de películas")
    print("4. Salir")
    opcion = input("Escribe tu opción (1-4): ")

    if opcion == "1":
        nombre_pelicula = input("Proporciona el nombre de la pelicula: ")
        pelicula = Pelicula(nombre_pelicula)
        CatalogoPeliculas.agregar_pelicula(pelicula)

    elif opcion == "2":
        CatalogoPeliculas.listar_peliculas()

    elif opcion == "3":
        CatalogoPeliculas.eliminar()

    elif opcion == "4":
        print('Gracias por usar el programa')
        sys.exit(0)

else:
    print("Salimos del programa...")

