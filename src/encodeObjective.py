import random

fichas = ["RED", "BLUE", "YELLOW", "GREEN"]
codigo = []

def generarCodigoAutomatico(codigo, fichas, n=4):
    if n > 4:
        raise ValueError("El número de fichas no puede ser mayor a 4")
    for _ in range(n):
        codigo.append(random.choice(fichas))

    print("Código: ", codigo)
    return codigo

def generarCodigoManual(codigo, n=4):
    if n > 4:
        raise ValueError("El número de fichas no puede ser mayor a 4")
    for i in range(n):
        ficha = input(f"Introduce el color de la ficha {i+1} (RED, BLUE, YELLOW, GREEN): ").upper()
        while ficha not in fichas:
            print("Color no válido. Inténtalo de nuevo.")
            ficha = input(f"Introduce el color de la ficha {i+1} (RED, BLUE, YELLOW, GREEN): ").upper()
        codigo.append(ficha)

    print("Código: ", codigo)
    return codigo

def elegirMetodoGeneracion():
    opcion = input("¿Quieres generar el código manualmente (M) o automáticamente (A)? ").upper()
    if opcion == 'M':
        generarCodigoManual(codigo)
    elif opcion == 'A':
        generarCodigoAutomatico(codigo, fichas)
    else:
        print("Opción no válida.")


if __name__ == "__main__":
   
    test_codigo = []
    resultado = generarCodigoAutomatico(test_codigo, fichas)
    assert len(resultado) == 4, "Código automático debe tener 4 fichas"



