from parametros import parametros
from evaluarIndividuos import evaluarIndividuos
from crearPoblacionInicial import crearPoblacionInicial
from generarCodigoSecreto import generarCodigoAutomatico, fichas
tamanhoPoblacion, maxGeneraciones, operadorSeleccion, longitudCodigo, tasaMutacion, tasaCruce = parametros()
poblacionInicial = crearPoblacionInicial()
puntuaciones = evaluarIndividuos(poblacionInicial=poblacionInicial, codigoObjetivo=generarCodigoAutomatico(fichas, longitudCodigo))

def seleccionarPadres(poblacion, puntuaciones):
    padres = []
    totalPuntuacion = 0
    for puntoIndividuo in range(len(puntuaciones)):
        totalPuntuacion += puntuaciones[puntoIndividuo]
    
    if totalPuntuacion == 0:
        return poblacion #Para que no se detenga el código si totalPuntacion es 0

    probabilidadeSerEscogido = [p / totalPuntuacion for p in puntuaciones]


    for i in range(len(poblacion)):
        individuo = poblacion[i]
        if probabilidadeSerEscogido[i] != 0:
            padres.append(individuo)

    return padres

seleccionarPadres(poblacionInicial, puntuaciones)