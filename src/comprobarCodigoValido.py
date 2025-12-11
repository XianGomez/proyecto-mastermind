colorPermitido = ["RED", "GREEN", "BLUE", "YELLOW"]

def codigoValido(codigo):
    if len(codigo) != 4:
        return False
    
    for color in codigo:
        if color not in colorPermitido:
            return False
    return True
