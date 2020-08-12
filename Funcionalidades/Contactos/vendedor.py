from contacto import Contacto
from conteneder_direccion import ContenedorDireccion


class Vendedor(Contacto, ContenedorDireccion):

    def __init__(self, nombre, email, telefono, calle, ciudad, provincia, codigo):
        Contacto.__init__(self, nombre, email)
        ContenedorDireccion.__init__(self, calle, ciudad, provincia, codigo)
        self.telefono = telefono

