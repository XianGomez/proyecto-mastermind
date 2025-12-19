import pytest
from src.crearPoblacionInicial import crearPoblacionInicial, fichas

def test_crearPoblacionInicial():
    poblacion = crearPoblacionInicial(10)
    
    assert len(poblacion) == 10
    for individuo in poblacion:
        assert len(individuo) == 4
        for color in individuo:
            assert color in fichas
