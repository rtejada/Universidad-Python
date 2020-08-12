
class ListaContactos(list):
    def buscar(self, nombre):
        '''Devuelve todos los contactos que contienen el valor de
        busqueda en su nombre'''

        contactos_coincidentes = []
        for contacto in self:
            if nombre in contacto.nombre:
                contactos_coincidentes.append(contacto)

        return contactos_coincidentes


class NombreLargoDict(dict):

    def clave_maslarga(self):
        maslarga = None
        for key in self:
            if not maslarga or len(key) > len(maslarga):
                maslarga = key

        return maslarga





clavelarga = NombreLargoDict()
clavelarga['hola']=1
clavelarga['la mas larga']=5
print(clavelarga.clave_maslarga())