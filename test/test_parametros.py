import pytest
from src.parametros import parametros

def test_parametros():
    tamanhoPoblacion, maxGeneraciones, operadorSeleccion, longitudCodigo, tasaMutacion = parametros()
    
    assert tamanhoPoblacion == 100
    assert maxGeneraciones == 14
    assert operadorSeleccion in ["rango", "ruleta", "torneo"]
    assert longitudCodigo == 4
    assert tasaMutacion == 0.02 
