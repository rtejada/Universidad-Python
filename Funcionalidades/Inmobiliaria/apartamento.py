from inmueble import *


class Apartamento(Inmueble):
    lavanderias_validas = ("moneda", "incluido", "ninguna")
    balcones_validos = ("si", "no", "solario")

    def __init__(self, balcon='', lavanderia='', **kwargs):
        super().__init__(**kwargs)
        self.balcon = balcon
        self.lavanderia = lavanderia

    def mostrar(self):
        super().mostrar()
        print("DETALLES APARTAMENTO")
        print("lavandería: {}".format(self.lavanderia))
        print("tiene balcón: {}".format(self.balcon))
        print()

    def prompt_init():
        parent_init = Inmueble.prompt_init()
        lavanderia = obtener_input_valido(
                "¿Qué sistema de lavandería "
                "tiene el inmueble? ",
                Apartamento.lavanderias_validas)
        balcon = obtener_input_valido(
                "¿tiene el inmueble balcón?",
                Apartamento.balcones_validos)
        parent_init.update({
            "lavanderia": lavanderia,
            "balcon": balcon
        })
        return parent_init
    prompt_init = staticmethod(prompt_init)

