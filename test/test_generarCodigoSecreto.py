from src import generarCodigoSecreto

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

def test_generar_codigo_determinista(monkeypatch):
    monkeypatch.setattr(generarCodigoSecreto.random, 'choice', lambda seq: 'BLUE')
    codigo = generarCodigoSecreto.generarCodigoAutomatico(generarCodigoSecreto.fichas, n=4)
    assert len(codigo) == 4
    assert all(c == 'BLUE' for c in codigo)
