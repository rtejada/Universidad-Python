from inmueble import *

class Compra:
    def __init__(self, precio='', impuestos='', **kwargs):
        super().__init__(**kwargs)
        self.precio = precio
        self.impuestos = impuestos

    def mostrar(self):
        super().mostrar()
        print("DETALLES COMPRAS")
        print("precio venta: {}".format(self.precio))
        print("impuestos estimados: {}".format(self.impuestos))

    def prompt_init():
        return dict(
            precio=input("¿Cuál es el precio de venta? "),
            impuestos=input("¿Cuáles son los impuestos estimados? "))
    prompt_init = staticmethod(prompt_init)


class Alquiler:
    def __init__(self, amueblado='', ajuar='',
            alquiler='', **kwargs):
        super().__init__(**kwargs)
        self.amueblado = amueblado
        self.alquiler = alquiler
        self.ajuar = ajuar

    def mostrar(self):
        super().mostrar()
        print("DETALLES ALQUILER")
        print("alquiler: {}".format(self.alquiler))
        print("ajuar estimado: {}".format(self.ajuar))
        print("amueblado: {}".format(self.amueblado))

    def prompt_init():
        return dict(
            alquiler=input("¿Cuál es el alquiler mensual? "),
            ajuar=input("¿Cuál es el ajuar estimado? "),
            amueblado=obtener_input_valido("¿Está amueblado el inmueble? ",
                    ("si", "no")))
    prompt_init = staticmethod(prompt_init)
