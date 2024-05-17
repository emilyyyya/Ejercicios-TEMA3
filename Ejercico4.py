#sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no queden más objetos en la mochila;
#determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sa- car para encontrarlo;
#Utilizar un vector para representar la mochila.

def buscar_sable_de_luz(mochila):
    """
    Busca un sable de luz en la mochila.

    Args:
        mochila (list): Una lista que representa los objetos en la mochila.

    Returns:
        tuple: Una tupla que indica si se encontró un sable de luz (bool)
               y el número de objetos necesarios para encontrarlo (int).
    """
    objetos_necesarios = 0
    for objeto in mochila:
        objetos_necesarios += 1
        if objeto == 'sable de luz':
            return True, objetos_necesarios
    return False, objetos_necesarios

def main():
    # Ejemplo de mochila
    mochila = ['comida', 'brújula', 'mapa', 'agua', 'linterna', 'sable de luz', 'botiquín']

    # Buscar un sable de luz en la mochila
    sable_encontrado, objetos_necesarios = buscar_sable_de_luz(mochila)

    # Imprimir resultados
    if sable_encontrado:
        print(f"¡Se encontró un sable de luz en la mochila después de {objetos_necesarios} objetos!")
    else:
        print("No se encontró un sable de luz en la mochila.")

if __name__ == "__main__":
    main()
