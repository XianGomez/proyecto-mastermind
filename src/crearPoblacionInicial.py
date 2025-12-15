import random
from definirParametros import definirParametros


fichas = ["RED", "BLUE", "YELLOW", "GREEN", "ORANGE", "PURPLE"]
poblacionInicial = []

def crearPoblacionInicial(poblacionMaxima):
    

    while len(poblacionInicial) < poblacionMaxima:

        nuevoIndividuo = []
        for _ in range(0,4):
            fichaAleatoria = random.choice(fichas)
            nuevoIndividuo.append(fichaAleatoria)
        
        poblacionInicial.append(nuevoIndividuo)

    return poblacionInicial


    
    
            

crearPoblacionInicial(poblacionMaxima=definirParametros()['tamanhoPoblacion'])