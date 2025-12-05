import random

fichas = ["RED", "BLUE", "YELLOW", "GREEN"]
codigo = []

def generar_codigo(codigo, fichas):
    for _ in range(4):
        codigo.append(random.choice(fichas) )
    print("Código: ", codigo)
    return codigo
    

generar_codigo(codigo, fichas)

