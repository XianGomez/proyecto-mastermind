import random
import parametros
_, _, _, longitudCodigo, _ = parametros.parametros() 

fichas = ["RED", "BLUE", "YELLOW", "GREEN", "ORANGE", "PURPLE"]


def generarCodigoAutomatico(fichas, n=longitudCodigo):
    codigoGenerado = [] 
    if n > 4: 
        raise ValueError("El número de fichas no puede ser mayor a la cantidad de colores disponibles")
    
    for _ in range(n):
        codigoGenerado.append(random.choice(fichas))

    print("Código Secreto Generado: ", codigoGenerado)
    return codigoGenerado