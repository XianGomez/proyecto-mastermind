import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from parametros import parametros
from crearPoblacionInicial import crearPoblacionInicial
from generarCodigoSecreto import generarCodigoAutomatico, fichas
from evaluarIndividuos import evaluarIndividuos
from seleccionarPadres import seleccionarPadres
from reproduccion import reproduccion
from poblarGeneracion import poblarGeneracion
from visualizacion import graficarMastermind 

tamanhoPoblacion, maxGeneraciones, operadorSeleccion, longitudCodigo, tasaMutacion, tasaCruce = parametros()
codigoObjetivo = generarCodigoAutomatico(fichas, longitudCodigo)
poblacion = crearPoblacionInicial()

historialMejores = [] 
encontrado = False

for generacion in range(maxGeneraciones):
    puntuaciones = evaluarIndividuos(poblacion, codigoObjetivo)
    
    mejorPuntuacion = max(puntuaciones)
    mejorIndividuo = poblacion[puntuaciones.index(mejorPuntuacion)]
    historialMejores.append(mejorIndividuo)
    
    if mejorPuntuacion == longitudCodigo:
        print(f"¡Solución encontrada en Gen {generacion}!")
        encontrado = True
        break
    
    padres = seleccionarPadres(poblacion, puntuaciones)
    hijos = reproduccion(padres, tasaMutacion, tasaCruce)
    poblacion = poblarGeneracion(hijos, tamanhoPoblacion)
else:
    print(f"Se ha llegado al máximo de generaciones ({maxGeneraciones}) sin encontrar la solución.")

graficarMastermind(historialMejores, codigoObjetivo, exito=encontrado)
