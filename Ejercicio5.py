#Resuelva el problema de colocar las 8 reinas sobre un tablero de ajedrez sin que las mismas se amenacen.
def es_seguro(tablero, fila, columna):
    """
    Comprueba si es seguro colocar una reina en la posición especificada.
    """
    # Verifica si hay otra reina en la misma columna
    for i in range(fila):
        if tablero[i] == columna:
            return False

    # Verifica si hay otra reina en la misma diagonal hacia arriba
    for i, j in zip(range(fila-1, -1, -1), range(columna-1, -1, -1)):
        if tablero[i] == j:
            return False

    # Verifica si hay otra reina en la misma diagonal hacia abajo
    for i, j in zip(range(fila-1, -1, -1), range(columna+1, 8)):
        if tablero[i] == j:
            return False

    return True

def colocar_reinas(tablero, fila):
    """
    Función principal para colocar las reinas utilizando backtracking.
    """
    if fila >= 8:
        return True

    for columna in range(8):
        if es_seguro(tablero, fila, columna):
            tablero[fila] = columna
            if colocar_reinas(tablero, fila + 1):
                return True
            tablero[fila] = -1

    return False

def imprimir_tablero(tablero):
    """
    Imprime el tablero con las reinas colocadas.
    """
    for fila in range(8):
        for columna in range(8):
            if tablero[fila] == columna:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

def resolver_problema_reinas():
    """
    Resuelve el problema de las 8 reinas e imprime la solución.
    """
    tablero = [-1] * 8
    if colocar_reinas(tablero, 0):
        print("Solución encontrada:")
        imprimir_tablero(tablero)
    else:
        print("No se encontró solución.")

# Resolver el problema de las 8 reinas
resolver_problema_reinas()
