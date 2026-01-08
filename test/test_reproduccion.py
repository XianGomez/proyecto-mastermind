from src import reproduccion as rp

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

def test_mutacion_forzada(monkeypatch):
    individuo = ['RED', 'BLUE', 'YELLOW', 'GREEN']
    monkeypatch.setattr(rp.random, 'choice', lambda seq: 'PURPLE')
    resultado = rp.mutacion(individuo[:], tasaMutacion=1)
    assert all(col == 'PURPLE' for col in resultado)


def test_mutacion_none():
    individuo = ['RED', 'BLUE', 'YELLOW', 'GREEN']
    resultado = rp.mutacion(individuo[:], tasaMutacion=0)
    assert resultado == individuo


def test_reproduccion_cruce(monkeypatch):
    padres = [['A', 'B', 'C', 'D'], ['a', 'b', 'c', 'd']]

    # Forzar cruce y punto de cruce
    monkeypatch.setattr(rp.random, 'random', lambda: 0.0)
    monkeypatch.setattr(rp.random, 'randint', lambda a, b: 2)
    # Evitar que la mutación cambie los hijos durante el test
    monkeypatch.setattr(rp, 'mutacion', lambda ind, tasa: ind)

    hijos = rp.reproduccion(padres, tasaMutacion=0, tasaCruce=1)
    assert hijos[0] == ['A', 'B', 'c', 'd']
    assert hijos[1] == ['a', 'b', 'C', 'D']
