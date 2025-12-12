def evaluarIndividuos(individuos, codigoObjetivo):
    resultados = []
    for individuo in individuos:
        aciertos = sum(1 for i in range(len(codigoObjetivo)) if individuo[i] == codigoObjetivo[i])
        resultados.append((individuo, aciertos))
    return resultados

             
if __name__ == "__main__":
    individuos1 = [[1, 2, 3, 4]]
    codigoObjetivo1 = [1, 2, 5, 6]
    resultado1 = evaluarIndividuos(individuos1, codigoObjetivo1)
    assert resultado1 == [([1, 2, 3, 4], 2)], f"Se detiene en posicion: {resultado1}"
    
    individuos2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
    codigoObjetivo2 = [9, 0, 1, 2]
    resultado2 = evaluarIndividuos(individuos2, codigoObjetivo2)
    assert resultado2 == [([1, 2, 3, 4], 0), ([5, 6, 7, 8], 0)], f"Se detiene en posicion: {resultado2}"
    
    individuos3 = [[1, 2, 3, 4]]
    codigoObjetivo3 = [1, 2, 3, 4]
    resultado3 = evaluarIndividuos(individuos3, codigoObjetivo3)
    assert resultado3 == [([1, 2, 3, 4], 4)], f"Se detiene en posicion: {resultado3}"
    
    individuos4 = [[1, 2, 3, 4], [1, 5, 3, 6], [7, 8, 9, 0]]
    codigoObjetivo4 = [1, 2, 3, 4]
    resultado4 = evaluarIndividuos(individuos4, codigoObjetivo4)
    assert resultado4 == [([1, 2, 3, 4], 4), ([1, 5, 3, 6], 2), ([7, 8, 9, 0], 0)], f"Se detiene en posicion: {resultado4}"
    