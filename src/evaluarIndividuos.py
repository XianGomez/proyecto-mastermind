def evaluarIndividuos(poblacionInicial, codigoObjetivo):
    puntuaciones = []
    for individuo in poblacionInicial:
        aciertos = sum(
            1 for i in range(len(codigoObjetivo)) 
            if individuo[i] == codigoObjetivo[i])
        puntuaciones.append(aciertos)
    return puntuaciones