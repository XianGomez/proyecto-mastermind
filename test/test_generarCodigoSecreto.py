from src import generarCodigoSecreto

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

def test_generar_codigo_determinista(monkeypatch):
    codigo = generarCodigoSecreto.generarCodigoAutomatico(generarCodigoSecreto.fichas, n=4)
    assert len(codigo) == 4
