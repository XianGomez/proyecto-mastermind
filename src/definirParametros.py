import random

def definirParametros():
    parametros = {}

    parametros['tamanhoPoblacion'] = 100
    parametros['maxGeneraciones'] = 14
    parametros['operadorSeleccion'] = random.choice(["rango", "ruleta", "torneo"])
    parametros['longitudCodigo'] = 4

    return parametros
