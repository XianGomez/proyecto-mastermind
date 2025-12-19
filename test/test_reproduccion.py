import pytest
from src.reproduccion import reproduccion

def test_reproduccion():
    padres = [["RED", "BLUE", "YELLOW", "GREEN"], ["PURPLE", "ORANGE", "YELLOW", "GREEN"]]
    nuevaPoblacion = reproduccion(padres)
    # Asumiendo que la función está incompleta, por ahora solo verificar que retorna lista
    assert isinstance(nuevaPoblacion, list)
