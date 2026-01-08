from src.seleccionarPadres import seleccionarPadres

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

def test_total_puntuacion_cero():
    pobl = [['x'], ['y']]
    puntuaciones = [0, 0]
    resultado = seleccionarPadres(pobl, puntuaciones)
    assert resultado == pobl


def test_filtra_ceros():
    pobl = [['a'], ['b'], ['c']]
    puntuaciones = [1, 0, 2]
    resultado = seleccionarPadres(pobl, puntuaciones)
    assert resultado == [['a'], ['c']]
