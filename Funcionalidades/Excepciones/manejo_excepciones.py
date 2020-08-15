try:
    10 / 0
except Exception as e:
    print("Ocurrió un error", e)

print("continuamos")


resultado = None
a = 'hola'
b = 0
try:
    resultado = a / b
except ZeroDivisionError as e:
    print("Ocurrió un error con ZeroDivisionError", e)
    print(type(e))
except TypeError as e:
    print("Ocurrió un error con TypeError", e)
    print(type(e))
except Exception as e:
    print("Ocurrió un error con exception", e)
    print(type(e))

print("resultado: ", resultado)
print("continuamos...")
