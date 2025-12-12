import random

def definirParametros():
    parametros = {}

    parametros['tamanhoPoblacion'] = 100
    parametros['maxGeneraciones'] = 14
    parametros['OperadorSeleccion'] = random.choice(["rango", "ruleta", "torneo"])
    parametros['LongitudCodigo'] = 4

    return parametros
