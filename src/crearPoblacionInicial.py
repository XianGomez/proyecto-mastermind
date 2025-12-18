import random
import parametros 
tamanhoPoblacion, maxGeneraciones, operadorSeleccion, longitudCodigo, tasaMutacion = parametros.parametros()

fichas = ["RED", "BLUE", "YELLOW", "GREEN", "ORANGE", "PURPLE"]
poblacionInicial = []

def crearPoblacionInicial(TAMANHOPOBLACION=tamanhoPoblacion):

    while len(poblacionInicial) < TAMANHOPOBLACION:

        nuevoIndividuo = []
        for _ in range(0,4):
            fichaAleatoria = random.choice(fichas)
            nuevoIndividuo.append(fichaAleatoria)
        
        poblacionInicial.append(nuevoIndividuo)

    return poblacionInicial
