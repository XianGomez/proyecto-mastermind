import pytest
from src.evaluarIndividuos import evaluarIndividuos

def test_evaluarIndividuos():
    codigoObjetivo = ["RED", "BLUE", "YELLOW", "GREEN"]
    poblacion = [
        ["RED", "BLUE", "YELLOW", "GREEN"],  # 4 aciertos
        ["RED", "BLUE", "YELLOW", "PURPLE"],  # 3 aciertos
        ["RED", "BLUE", "ORANGE", "GREEN"],  # 3 aciertos
        ["PURPLE", "ORANGE", "YELLOW", "GREEN"]  # 2 aciertos
    ]
    
    puntuaciones = evaluarIndividuos(poblacion, codigoObjetivo)
    
    assert puntuaciones == [4, 3, 3, 2]
    
