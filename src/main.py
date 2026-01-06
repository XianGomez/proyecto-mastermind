from parametros import parametros
from crearPoblacionInicial import crearPoblacionInicial
from generarCodigoSecreto import generarCodigoAutomatico, fichas
from evaluarIndividuos import evaluarIndividuos
from seleccionarPadres import seleccionarPadres
from reproduccion import reproduccion
from poblarGeneracion import poblarGeneracion


tamanhoPoblacion, maxGeneraciones, operadorSeleccion, longitudCodigo, tasaMutacion, tasaCruce = parametros()
codigoObjetivo = generarCodigoAutomatico(fichas, longitudCodigo) 

poblacion = crearPoblacionInicial()

print(f"Objetivo a encontrar: {codigoObjetivo}")

for generacion in range(maxGeneraciones):
    
    puntuaciones = evaluarIndividuos(poblacion, codigoObjetivo)
    
    if max(puntuaciones) == longitudCodigo:
        indiceGanador = puntuaciones.index(longitudCodigo)
        print(f"--- ¡SOLUCIÓN ENCONTRADA en Gen {generacion}! ---")
        print(f"Código: {poblacion[indiceGanador]}")
        break
    
    padres = seleccionarPadres(poblacion, puntuaciones)
    
    hijos = reproduccion(padres, tasaMutacion, tasaCruce)
    
    poblacion = poblarGeneracion(hijos, tamanhoPoblacion)
    
    print(f"Generación {generacion} | Mejor puntuación: {max(puntuaciones)}")

else:
    print("Se alcanzó el máximo de generaciones sin encontrar la solución exacta.")