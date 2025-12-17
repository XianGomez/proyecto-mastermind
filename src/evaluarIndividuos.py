def evaluarIndividuos(poblacionInicial, codigoObjetivo):
    resultados = []
    for individuo in poblacionInicial:
        aciertos = sum(
            1 for i in range(len(codigoObjetivo)) 
            if individuo[i] == codigoObjetivo[i])
    return resultados

             
