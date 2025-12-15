import random
from definirParametros import definirParametros

fichas = ["RED", "BLUE", "YELLOW", "GREEN"]
codigoObjetivo = []

def generarCodigoAutomatico(codigoObjetivo, fichas, n=definirParametros()['longitudCodigo']):
    if n > 4:
        raise ValueError("El número de fichas no puede ser mayor a 4")
    for _ in range(n):
        codigoObjetivo.append(random.choice(fichas))

    print("Código: ", codigoObjetivo)
    return codigoObjetivo

def generarCodigoManual(codigoObjetivo, n=definirParametros()['longitudCodigo']):
    if n > 4:
        raise ValueError("El número de fichas no puede ser mayor a 4")
    for i in range(n):
        ficha = input(f"Introduce el color de la ficha {i+1} (RED, BLUE, YELLOW, GREEN): ").upper()
        while ficha not in fichas:
            print("Color no válido. Inténtalo de nuevo.")
            ficha = input(f"Introduce el color de la ficha {i+1} (RED, BLUE, YELLOW, GREEN): ").upper()
        codigoObjetivo.append(ficha)

    print("Código: ", codigoObjetivo)
    return codigoObjetivo

def elegirMetodoGeneracion():
    opcion = input("¿Quieres generar el código manualmente (M) o automáticamente (A)? ").upper()
    if opcion == 'M':
        generarCodigoManual(codigoObjetivo)
    elif opcion == 'A':
        generarCodigoAutomatico(codigoObjetivo, fichas)
    else:
        print("Opción no válida.")


elegirMetodoGeneracion()

