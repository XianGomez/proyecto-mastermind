import random

fichas = ["RED", "BLUE", "YELLOW", "GREEN"]
codigo = []

def generarCodigoAutomatico(codigo, fichas):
    for _ in range(4):
        codigo.append(random.choice(fichas) )
        
    print("Código: ", codigo)
    return codigo

def generarCodigoManual(codigo):
    for i in range(4):
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

elegirMetodoGeneracion()

