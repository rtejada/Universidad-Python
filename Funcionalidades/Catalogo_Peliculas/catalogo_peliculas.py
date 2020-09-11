import os


class CatalogoPeliculas:

    ruta_archivo = "peliculas.txt"

    @staticmethod
    def agregar_pelicula(pelicula):

        archivo = ''
        try:
            # "a" - modo append
            archivo = open(CatalogoPeliculas.ruta_archivo, "a")
            archivo.write(pelicula.__str__() + "\n")

        except Exception as e:
            print("Ocurrió una excepción al agregar: ", e)

        finally:
            archivo.close()

    @staticmethod
    def listar_peliculas():

        archivo = ''

        try:
            archivo = open(CatalogoPeliculas.ruta_archivo, "r")
            print("Catálogo de Películas:")
            print(archivo.read())

        except Exception as e:
            print("Ocurrió un error al listar películas: ", e)

        finally:
            archivo.close()

    @staticmethod
    def eliminar():

        try:
            os.remove(CatalogoPeliculas.ruta_archivo)
            print("archivo eliminado: ", CatalogoPeliculas.ruta_archivo)

        except Exception as e:
            print("Ocurrió un error al eliminar películas:", e)