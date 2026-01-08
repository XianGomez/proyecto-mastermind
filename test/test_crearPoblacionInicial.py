import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import crearPoblacionInicial 

def test_crear_poblacion_determinista(monkeypatch):
    crearPoblacionInicial.poblacionInicial = []
    
    monkeypatch.setattr(crearPoblacionInicial.random, 'choice', lambda seq: 'RED')

    poblacion = crearPoblacionInicial.crearPoblacionInicial(TAMANHOPOBLACION=3)
    
    assert len(poblacion) == 3
    for individuo in poblacion:
        assert len(individuo) == 4
        assert all(color == 'RED' for color in individuo)
