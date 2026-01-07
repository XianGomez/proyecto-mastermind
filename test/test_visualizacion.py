from src import visualizacion as vis


def test_graficar_no_errores(monkeypatch):
    monkeypatch.setattr(vis.plt, 'show', lambda: None)

    historial = [
        ['RED', 'BLUE', 'GREEN', 'YELLOW'],
        ['BLUE', 'BLUE', 'BLUE', 'BLUE']
    ]
    codigo = ['RED', 'BLUE', 'GREEN', 'PURPLE']

    # Debe ejecutarse sin lanzar excepciones
    vis.graficar_mastermind(historial, codigo)
