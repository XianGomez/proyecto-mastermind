from src.evaluarIndividuos import evaluarIndividuos

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

def test_evaluar_individuos():
    poblacion = [
        ['RED', 'BLUE', 'GREEN', 'YELLOW'],
        ['RED', 'RED', 'RED', 'RED']
    ]
    codigo = ['RED', 'BLUE', 'GREEN', 'PURPLE']

    puntuaciones = evaluarIndividuos(poblacion, codigo)
    assert puntuaciones == [3, 1]
