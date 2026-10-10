from datetime import datetime


def es_palabra_valida(cadena: str) -> bool:
    '''
    Comprueba si la cadena es una palabra válida:
    - Tiene 5 letras
    - Solo contiene letras a-z o A-Z

    Parámetros:
        cadena: la cadena a comprobar
    Devuelve:
        True si la cadena es una palabra válida, False en otro caso
    '''
    if len(cadena) == 5 and cadena.isalpha():
        return True
    else:
        return False

def calcula_minutos_y_segundos(inicio: datetime, fin: datetime) -> tuple:
    """ 
    Recibe dos datetime y devuelve la diferencia en minutos y segundos.

    Parámetros:
        inicio: datetime de inicio
        fin: datetime de fin
    Devuelve:
        Una tupla (minutos, segundos) con la diferencia entre los dos datetime
    """
    diferencia = (fin - inicio)
    diferencia_segundos = diferencia.total_seconds() % 60
    diferencia_minutos = diferencia.total_seconds() // 60

    return (int(diferencia_minutos), int(diferencia_segundos))

def quitar_letra(cadena: str, caracter: str) -> str:
    cadena_resuelta = ""
    caracter_quitado = False
    for char in cadena:
        if char != caracter:
            cadena_resuelta += char
        elif caracter_quitado == True:
            cadena_resuelta += char
        else:
            caracter_quitado = True

    return cadena_resuelta




def marcar_verdes(palabra_secreta: str, intento: str) -> str:
    aciertos = ""
    restantes = ""

    for i in range(len(intento)):
        if intento[i] == palabra_secreta[i]:
            aciertos += "V"
        else:
            aciertos += "_"
            restantes += palabra_secreta[i]

    return (aciertos, restantes)

print(marcar_verdes("astas","latas"))

def marcar_amarillos(intento: str, verdes: str, restantes: str) -> str:
    colores = ""
    for i in range(len(intento)):
        if verdes[i] == "V":
            colores += "V"
        elif intento[i] in restantes:
            colores += "A"
            restantes = quitar_letra(restantes, intento[i])
        else:
            colores += "_"

    return colores


def obtener_pistas(palabra_secreta: str, intento: str) -> str:
    """
    Devuelve la cadena de pistas para un intento dado.
    Parámetros:
        palabra_secreta: la palabra secreta
        intento: la palabra del intento
    Devuelve:
        Una cadena de 5 caracteres con 'V', 'A' y '_'
    """

    verdes, restantes = marcar_verdes(palabra_secreta, intento)
    pistas = marcar_amarillos(intento, verdes, restantes)

    return pistas