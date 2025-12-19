from parametros import parametros
from evaluarIndividuos import evaluarIndividuos
from crearPoblacionInicial import crearPoblacionInicial
from generarCodigoSecreto import generarCodigoAutomatico, fichas
tamanhoPoblacion, maxGeneraciones, operadorSeleccion, longitudCodigo, tasaMutacion = parametros()
poblacionInicial = crearPoblacionInicial()
puntuaciones = evaluarIndividuos(poblacionInicial=poblacionInicial, codigoObjetivo=generarCodigoAutomatico(fichas, longitudCodigo))

def seleccionarPadres(poblacion, puntuaciones):
    padres = []
    totalPuntuacion = 0
    for puntoIndividuo in range(len(puntuaciones)):
        totalPuntuacion += puntuaciones[puntoIndividuo]
    
    probabilidadeSerEscogido = [p / totalPuntuacion for p in puntuaciones]

    for i in range(len(poblacion)):
        individuo = poblacion[i]
        if probabilidadeSerEscogido[i] != 0:
            padres.append(individuo)

    print("Total Puntuación: ", totalPuntuacion)
    print("Probabilidades de ser escogido: ", probabilidadeSerEscogido)
    print("Cantidad de padres: ", len(padres))
    print("Padres seleccionados: ", padres)

seleccionarPadres(poblacionInicial, puntuaciones)