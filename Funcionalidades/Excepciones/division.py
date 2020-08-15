def ejemplo_division(numero):
    try:
        return 100 / numero
    except ZeroDivisionError:
        return "¡Es imposible dividir por cero!"

#print(ejemplo_division(0))
#print(ejemplo_division(50.0))
#print(ejemplo_division("hola"))

def ejemplo_division2(numero):
    try:
        if numero == 25:
            raise ValueError("el número 25 no es válido")
        return 100 / numero
    except (ZeroDivisionError, TypeError):
        return "Escribe un número que no sea cero"

#print(ejemplo_division2("hola"))


def ejemplo_division3(numero):
    try:
        if numero == 25:
            raise ValueError("25 no es un número válido")
        return 100 / numero
    except ZeroDivisionError:
        return "Escribe un número que no sea cero"
    except TypeError:
        return "Escribe un valor numérico"
    except ValueError:
        print("El número 25 no vale")
        raise


print(ejemplo_division3(25))
