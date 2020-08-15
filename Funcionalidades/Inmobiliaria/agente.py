from inmueble import *
from alquiler_compra_casa_apartamento import CasaAlquiler, CasaCompra, ApartamentoAlquiler, ApartamentoCompra

class Agente:
    type_map = {
        ("casa", "alquiler"): CasaAlquiler,
        ("casa", "compra"): CasaCompra,
        ("apartamento", "alquiler"): ApartamentoAlquiler,
        ("apartamento", "compra"): ApartamentoCompra
        }
    def __init__(self):
        self.inmueble_list = []

    def mostrar_inmuebles(self):
        for inmueble in self.inmueble_list:
            inmueble.mostrar()

    def add_inmueble(self):
        tipo_inmueble = obtener_input_valido(
                "¿Qué tipo de inmueble? ",
                ("casa", "apartamento")).lower()
        tipo_pago = obtener_input_valido(
                "¿Qué tipo de pago? ",
                ("compra", "alquiler")).lower()

        inmuebleClass = self.type_map[(tipo_inmueble, tipo_pago)]
        init_args = inmuebleClass.prompt_init()
        self.inmueble_list.append(inmuebleClass(**init_args))


agente = Agente()
agente.add_inmueble()
agente.mostrar_inmuebles()
