def obtener_mayor(a,b):
    """
    Método que compara dos números y retorna el mayor.

    Parámetros:
    a (int): Primer número a comparar.
    b (int): Segundo número a comparar.

    Retorna el valor del número más grande

    No se realizan validaciones de tipo o valor en este método,
    se asume que ambos parámetros son números válidos.
    """
    if a>b:
        return a
    else:
        return b
    

x = 2
y = 10
print(obtener_mayor(x, y))
