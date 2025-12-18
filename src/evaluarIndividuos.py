from parametros import parametros
tamanhoPoblacion, maxGeneraciones, operadorSeleccion, longitudCodigo, tasaMutacion = parametros()
from  crearPoblacionInicial import crearPoblacionInicial
poblacionInicial = crearPoblacionInicial()
from generarCodigoSecreto import generarCodigoAutomatico, fichas
codigoObjetivo = generarCodigoAutomatico(fichas, longitudCodigo)

def evaluarIndividuos(poblacionInicial, codigoObjetivo):
    puntuaciones = []
    for individuo in poblacionInicial:
        aciertos = sum(
            1 for i in range(len(codigoObjetivo)) 
            if individuo[i] == codigoObjetivo[i])
        puntuaciones.append(aciertos)
    print(puntuaciones)

evaluarIndividuos(poblacionInicial=poblacionInicial, codigoObjetivo=codigoObjetivo)