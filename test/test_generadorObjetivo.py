import random
from encondeObjetive import generarCodigoAutomatico, fichas

def test_codigo_automatico():
    test_codigo = []
    resultado = generarCodigoAutomatico(test_codigo, fichas)
    assert len(resultado) == 4