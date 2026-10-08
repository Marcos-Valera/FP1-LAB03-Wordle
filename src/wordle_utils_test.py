# Pruebas para las funciones de wordle_utils.py

# TODO: Implementa las pruebas que te indica el enunciado

from wordle_utils import es_palabra_valida

def test_es_palabra_valida():
    print("Probando es_palabra_valida...")
    assert es_palabra_valida("casar") == True
    assert es_palabra_valida("casa") == False
    assert es_palabra_valida("casarr") == False
    assert es_palabra_valida("c4sar") == False
    assert es_palabra_valida("casa ") == False
    assert es_palabra_valida(" casa") == False
    assert es_palabra_valida("CASAR") == True

test_es_palabra_valida()
print("✅Todas las pruebas pasaron correctamente.")