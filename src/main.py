from parametros import parametros
from crearPoblacionInicial import crearPoblacionInicial
from generarCodigoSecreto import generarCodigoAutomatico, fichas
from evaluarIndividuos import evaluarIndividuos
from seleccionarPadres import seleccionarPadres
from reproduccion import reproduccion
from poblarGeneracion import poblarGeneracion
from visualizacion import graficar_mastermind 

tamanhoPoblacion, maxGeneraciones, operadorSeleccion, longitudCodigo, tasaMutacion, tasaCruce = parametros()
codigoObjetivo = generarCodigoAutomatico(fichas, longitudCodigo)
poblacion = crearPoblacionInicial()

historial_mejores = [] 

for generacion in range(maxGeneraciones):
    puntuaciones = evaluarIndividuos(poblacion, codigoObjetivo)
    
    mejor_puntuacion = max(puntuaciones)
    mejor_individuo = poblacion[puntuaciones.index(mejor_puntuacion)]
    historial_mejores.append(mejor_individuo)
    
    if mejor_puntuacion == longitudCodigo:
        print(f"¡Solución encontrada en Gen {generacion}!")
        break
    
    padres = seleccionarPadres(poblacion, puntuaciones)
    hijos = reproduccion(padres, tasaMutacion, tasaCruce)
    poblacion = poblarGeneracion(hijos, tamanhoPoblacion)

graficar_mastermind(historial_mejores, codigoObjetivo)

