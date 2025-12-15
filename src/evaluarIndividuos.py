def evaluarIndividuos(individuos, codigoObjetivo):
    resultados = []
    for individuo in individuos:
        aciertos = sum(1 for i in range(len(codigoObjetivo)) if individuo[i] == codigoObjetivo[i])
        resultados.append((individuo, aciertos))
    return resultados

             
