import random
from generarCodigoSecreto import fichas

def mutacion(individuo, tasaMutacion):
    i = random.randint(0,3)
    if random.random() < tasaMutacion:
        individuo[i] = random.choice(fichas)
    return individuo


def reproduccion(padres, tasaMutacion, tasaCruce):
    hijos = []
    for i in range(0, len(padres), 2):
        padre1 = padres[i]
        padre2 = padres[i + 1] if i + 1 < len(padres) else padres[0]

        if random.random() < tasaCruce:
            puntoCruce = random.randint(1, len(padre1) - 1)
            hijo1 = padre1[:puntoCruce] + padre2[puntoCruce:]
            hijo2 = padre2[:puntoCruce] + padre1[puntoCruce:]
        else:
            hijo1, hijo2 = padre1[:], padre2[:]

        hijo1 = mutacion(hijo1, tasaMutacion)
        hijo2 = mutacion(hijo2, tasaMutacion)

        hijos.append(hijo1)
        hijos.append(hijo2)

    return hijos
