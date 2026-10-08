# Pruebas para las funciones de wordle_utils.py

# TODO: Implementa las pruebas que te indica el enunciado
from datetime import datetime
from wordle_utils import es_palabra_valida, calcula_minutos_y_segundos

def test_es_palabra_valida():
    print("Probando es_palabra_valida...")
    assert es_palabra_valida("casar") == True
    assert es_palabra_valida("casa") == False
    assert es_palabra_valida("casarr") == False
    assert es_palabra_valida("c4sar") == False
    assert es_palabra_valida("casa ") == False
    assert es_palabra_valida(" casa") == False
    assert es_palabra_valida("CASAR") == True

def test_calcula_minutos_y_segundos():
    assert calcula_minutos_y_segundos(datetime(2024, 1, 1, 23, 0, 0), datetime(2024, 1, 1, 23, 0, 30)) == (0, 30)
    assert calcula_minutos_y_segundos(datetime(2024, 1, 1, 23, 0, 0), datetime(2024, 1, 1, 23, 3, 45)) == (3, 45)
    assert calcula_minutos_y_segundos(datetime(2024, 1, 1, 23, 0, 0), datetime(2024, 1, 2, 0, 1, 15)) == (61, 15)

test_es_palabra_valida()
test_calcula_minutos_y_segundos()
print("✅Todas las pruebas pasaron correctamente.")