from src import visualizacion as vis

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

def test_graficar_no_errores(monkeypatch):
    monkeypatch.setattr(vis.plt, 'show', lambda: None)

    historial = [
        ['RED', 'BLUE', 'GREEN', 'YELLOW'],
        ['BLUE', 'BLUE', 'BLUE', 'BLUE']
    ]
    codigo = ['RED', 'BLUE', 'GREEN', 'PURPLE']

    # Debe ejecutarse sin lanzar excepciones
    vis.graficarMastermind(historial, codigo)
