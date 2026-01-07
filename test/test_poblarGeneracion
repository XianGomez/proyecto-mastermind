from src.poblarGeneracion import poblarGeneracion


def test_poblar_generacion_truncar():
    hijos = [[1], [2], [3], [4]]
    nueva = poblarGeneracion(hijos, 2)
    assert nueva == [[1], [2]]


def test_poblar_generacion_corto():
    hijos = [[1], [2]]
    nueva = poblarGeneracion(hijos, 4)
    assert nueva == hijos
