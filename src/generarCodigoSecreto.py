import random
import parametros
_, _, _, longitudCodigo, _, _ = parametros.parametros() 

fichas = ["RED", "BLUE", "YELLOW", "GREEN", "ORANGE", "PURPLE"]


def generarCodigoAutomatico(fichas, n=longitudCodigo):
    codigoGenerado = [] 
    
    for _ in range(n):
        codigoGenerado.append(random.choice(fichas))

    print("Código Secreto Generado: ", codigoGenerado)
    return codigoGenerado