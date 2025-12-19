import pytest
from src.generarCodigoSecreto import generarCodigoAutomatico, generarCodigoManual, fichas

def test_generarCodigoAutomatico(monkeypatch):
    codigoObjetivo = []
    choices = ["RED", "BLUE", "YELLOW", "GREEN"]
    monkeypatch.setattr('random.choice', lambda x: choices.pop(0))
    result = generarCodigoAutomatico(codigoObjetivo, fichas, 4)
    assert result == ["RED", "BLUE", "YELLOW", "GREEN"]

def test_generarCodigoAutomatico_error():
    codigoObjetivo = []
    with pytest.raises(ValueError):
        generarCodigoAutomatico(codigoObjetivo, fichas, 5) 
