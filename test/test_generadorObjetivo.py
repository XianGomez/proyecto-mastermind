import pytest
from src.generarCodigoSecreto import generarCodigoAutomatico, fichas

def test_generarCodigoAutomatico_length(monkeypatch):
    test_codigo = []
    monkeypatch.setattr('random.choice', lambda x: "RED")
    resultado = generarCodigoAutomatico(test_codigo, fichas)
    assert len(resultado) == 4  
