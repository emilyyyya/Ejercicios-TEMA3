# Lista de canciones
canciones = [
    {"cancion": "Smells Like Teen Spirit", "artista": "Nirvana", "año": 1991},
    {"cancion": "Black Hole Sun", "artista": "Soundgarden", "año": 1994},
    {"cancion": "Fake Tales of San Francisco", "artista": "Arctic Monkeys", "año": 2005},
    {"cancion": "Cochise", "artista": "Audioslave", "año": 2002},
    {"cancion": "Under the Bridge", "artista": "Red Hot Chili Peppers", "año": 1992},
    {"cancion": "Gimme Shelter", "artista": "The Rolling Stones", "año": 1969}
]

# Funciones para procesar la lista de canciones

# Función para listar las canciones ordenadas según diferentes criterios
def listar_canciones_ordenadas(criterio):
    return sorted(canciones, key=lambda x: x[criterio])

# Función para determinar si existe alguna canción de un artista específico
def existe_cancion_de_artista(artista):
    return any(cancion["artista"] == artista for cancion in canciones)

# Función para mostrar todas las canciones de un artista específico
def mostrar_canciones_de_artista(artista):
    return [cancion for cancion in canciones if cancion["artista"] == artista]

# Función para agregar una nueva canción a la lista y volver a ordenar por nombre de canción
def agregar_nueva_cancion(cancion, artista, año):
    nueva_cancion = {"cancion": cancion, "artista": artista, "año": año}
    canciones.append(nueva_cancion)
    return listar_canciones_ordenadas("cancion")

# Función para determinar cuántas canciones hay de un artista específico
def cantidad_canciones_de_artista(artista):
    return sum(1 for cancion in canciones if cancion["artista"] == artista)

# Función para mostrar toda la información de una canción específica
def mostrar_informacion_cancion(nombre_cancion):
    for cancion in canciones:
        if cancion["cancion"] == nombre_cancion:
            return cancion
    return "La canción no se encuentra en la lista."

# Ejemplo de uso interactivo
while True:
    print("\n=== Menú de Consulta ===")
    print("1. Listar canciones ordenadas por nombre de canción")
    print("2. Listar canciones ordenadas por artista")
    print("3. Listar canciones ordenadas por año de lanzamiento")
    print("4. Determinar si existe alguna canción de un artista específico")
    print("5. Mostrar todas las canciones de un artista específico")
    print("6. Agregar una nueva canción a la lista")
    print("7. Determinar cuántas canciones hay de un artista específico")
    print("8. Mostrar toda la información de una canción específica")
    print("9. Salir")
    opcion = input("Ingrese el número de la opción que desea consultar: ")

    if opcion == "1":
        print(listar_canciones_ordenadas("cancion"))
    elif opcion == "2":
        print(listar_canciones_ordenadas("artista"))
    elif opcion == "3":
        print(listar_canciones_ordenadas("año"))
    elif opcion == "4":
        artista = input("Ingrese el nombre del artista que desea consultar: ")
        print(existe_cancion_de_artista(artista))
    elif opcion == "5":
        artista = input("Ingrese el nombre del artista del que desea ver las canciones: ")
        print(mostrar_canciones_de_artista(artista))
    elif opcion == "6":
        cancion = input("Ingrese el nombre de la nueva canción: ")
        artista = input("Ingrese el nombre del artista de la nueva canción: ")
        año = input("Ingrese el año de lanzamiento de la nueva canción: ")
        print("Lista de canciones actualizada:")
        print(agregar_nueva_cancion(cancion, artista, año))
    elif opcion == "7":
        artista = input("Ingrese el nombre del artista del que desea saber la cantidad de canciones: ")
        print(cantidad_canciones_de_artista(artista))
    elif opcion == "8":
        cancion = input("Ingrese el nombre de la canción que desea consultar: ")
        print(mostrar_informacion_cancion(cancion))
    elif opcion == "9":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor ingrese un número del 1 al 9.")
