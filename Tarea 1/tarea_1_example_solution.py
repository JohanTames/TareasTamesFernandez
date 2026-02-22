def filtrar_vocales(cadena, bandera):
    """
    Método que filtra vocales o consonantes de una cadena.

    Parámetros:
    cadena (str): Cadena de entrada a evaluar.
    bandera (bool): Si es True retorna solo vocales,
    si es False retorna solo consonantes.

    Retorna una tupla de la forma: (codigo_estado, resultado)
        codigo_estado:
            0: éxito
            -100: cadena no es string
            -200: cadena contiene caracteres no alfabéticos
            -300: cadena vacía
            -400: cadena mayor a 30 caracteres
            -500: bandera no es booleano
        resultado:
            string filtrado en caso de éxito
            None en caso de error
    """

    # Comprueba que cadena sea un string
    if not isinstance(cadena, str):
        return -100, None

    # Comprueba que cadena no esté vacía, se coloca primero
    # que isalpha() porque sino devuelve -200 si cadena está vacío
    if cadena == "":
        return -300, None

    # Comprueba que cadena solo contenga letras del abecedario
    if not cadena.isalpha():
        return -200, None

    # Cadena no debe ser mayor a 30 caracteres
    if len(cadena) > 30:
        return -400, None

    # Comprueba que bandera sea un booleano
    if not isinstance(bandera, bool):
        return -500, None

    # Para comparar con los caracteres de cadena
    vocales = "aeiouAEIOU"

    # Variable para almacenar el resultado filtrado
    resultado = ""

    # Si bandera es True, se filtran las vocales,
    # sino se filtran las consonantes
    if bandera:
        for c in cadena:
            if c in vocales:
                resultado += c
    else:
        for c in cadena:
            if c not in vocales:
                resultado += c

    return 0, resultado


def encontrar_extremos(lista_numeros):
    """
    Método que encuentra el valor mínimo y máximo de una lista.

    Parámetro:
    lista_numeros (list): Lista de números (peuden ser int o float).

    Retorna una tupla de la forma: (codigo_estado, minimo, maximo)

        codigo_estado:
            0: éxito
            -600: No es una lista
            -700: Contiene elementos no numéricos
            -800: Lista vacía
            -900: Lista con más de 15 elementos

        minimo:
            Valor mínimo en caso de éxito
            None en caso de error

        maximo:
            Valor máximo en caso de éxito
            None en caso de error
    """

    # Comprueba que el parámetro sea una lista
    if not isinstance(lista_numeros, list):
        return -600, None, None

    # Comprueba que la lista solo contenga elementos numéricos (int o float)
    for elemento in lista_numeros:
        # Bool es subclase de int, por lo que se valida que no lo sea
        if (
            not isinstance(elemento, (int, float))
            or isinstance(elemento, bool)
        ):
            return -700, None, None

    # Comprueba que la lista no esté vacía
    if len(lista_numeros) == 0:
        return -800, None, None

    # Comprueba que la lista no tenga más de 15 elementos
    if len(lista_numeros) > 15:
        return -900, None, None

    # Si pasa todas las validaciones, se calculan el mínimo y máximo
    minimo = min(lista_numeros)
    maximo = max(lista_numeros)

    return 0, minimo, maximo
