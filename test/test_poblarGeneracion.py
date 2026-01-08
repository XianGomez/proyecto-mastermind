from src.poblarGeneracion import poblarGeneracion

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

def test_poblar_generacion_truncar():
    hijos = [[1], [2], [3], [4]]
    nueva = poblarGeneracion(hijos, 2)
    assert nueva == [[1], [2]]


def test_poblar_generacion_corto():
    hijos = [[1], [2]]
    nueva = poblarGeneracion(hijos, 4)
    assert nueva == hijos
