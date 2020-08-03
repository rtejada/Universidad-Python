class Persona:
    def __init__(this, n, e, *v, **d):
        this.nombre = n
        this.edad = e
        this.valores = v
        this.diccionario = d

    def desplegar(this):
        print("Nombre: ", this.nombre)
        print("Edad: ", this.edad)
        print("Valores (Tupla):", this.valores)
        print("Diccionario: ", this.diccionario)


p1 = Persona("Juan", 28)
p1.desplegar()
print()

p2 = Persona("Karla", 30, 2, 4, 5)
p2.desplegar()
print()

p3 = Persona("Paola", 33, 4, 9, m="manzana", p="pera", j="jicama")
p3.desplegar()