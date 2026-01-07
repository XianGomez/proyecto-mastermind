from src.evaluarIndividuos import evaluarIndividuos


def test_evaluar_individuos():
    poblacion = [
        ['RED', 'BLUE', 'GREEN', 'YELLOW'],
        ['RED', 'RED', 'RED', 'RED']
    ]
    codigo = ['RED', 'BLUE', 'GREEN', 'PURPLE']

    puntuaciones = evaluarIndividuos(poblacion, codigo)
    assert puntuaciones == [3, 1]
