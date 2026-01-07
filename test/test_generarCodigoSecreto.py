from src import generarCodigoSecreto


def test_generar_codigo_determinista(monkeypatch):
    monkeypatch.setattr(generarCodigoSecreto.random, 'choice', lambda seq: 'BLUE')
    codigo = generarCodigoSecreto.generarCodigoAutomatico(generarCodigoSecreto.fichas, n=4)
    assert len(codigo) == 4
    assert all(c == 'BLUE' for c in codigo)
