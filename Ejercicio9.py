#Dada una lista de las naves (y vehículos) de Star Wars –consideraremos a todos como naves– de las que conocemos su nombre, largo, tripulación y cantidad de pasajeros, desarrollar los algo- ritmos necesarios para resolver las actividades detalladas a continuación:
#realizar un listado ordenado por nombre de las naves de manera ascendente y por largo de las mismas de manera descendente;
#mostrar toda la información del “Halcón Milenario” y la “Estrella de la Muerte”;
#determinar cuáles son las cinco naves con mayor cantidad de pasajeros;
#indicar cuál es la nave que requiere mayor cantidad de tripulación;
#mostrar todas las naves que comienzan con AT;
#listar todas las naves que pueden llevar seis o más pasajeros;
#mostrar toda la información de la nave más pequeña y la más grande.

# Lista de naves de Star Wars
naves = [
    {"nombre": "Halcón Milenario", "largo": 34.37, "tripulacion": 4, "pasajeros": 75},
    {"nombre": "X-wing", "largo": 12.5, "tripulacion": 1, "pasajeros": 0},
    {"nombre": "Estrella de la Muerte", "largo": 160, "tripulacion": 342953, "pasajeros": 843342},
    {"nombre": "AT-AT", "largo": 22.5, "tripulacion": 5, "pasajeros": 40},
    {"nombre": "Slave 1", "largo": 21.5, "tripulacion": 1, "pasajeros": 6},
    {"nombre": "TIE Fighter", "largo": 6.4, "tripulacion": 1, "pasajeros": 0},
    {"nombre": "Millennium Falcon", "largo": 34.37, "tripulacion": 4, "pasajeros": 75},
    {"nombre": "AT-ST", "largo": 8.6, "tripulacion": 2, "pasajeros": 0},
    {"nombre": "Star Destroyer", "largo": 1600, "tripulacion": 37000, "pasajeros": 0}
]

# Funciones para procesar la lista de naves de Star Wars

# Función para listar las naves ordenadas por nombre de manera ascendente y por largo de manera descendente
def listar_naves_ordenadas():
    return sorted(naves, key=lambda x: (x["nombre"], -x["largo"]))

# Función para mostrar toda la información de una nave específica
def mostrar_informacion_nave(nombre_nave):
    for nave in naves:
        if nave["nombre"] == nombre_nave:
            return nave
    return "La nave no se encuentra en la lista."

# Función para determinar las cinco naves con mayor cantidad de pasajeros
def cinco_naves_con_mas_pasajeros():
    return sorted(naves, key=lambda x: x["pasajeros"], reverse=True)[:5]

# Función para indicar cuál es la nave que requiere mayor cantidad de tripulación
def nave_con_mas_tripulacion():
    return max(naves, key=lambda x: x["tripulacion"])

# Función para mostrar todas las naves que comienzan con AT
def naves_que_comienzan_con_AT():
    return [nave for nave in naves if nave["nombre"].startswith("AT")]

# Función para listar todas las naves que pueden llevar seis o más pasajeros
def naves_con_seis_o_mas_pasajeros():
    return [nave for nave in naves if nave["pasajeros"] >= 6]

# Función para mostrar toda la información de la nave más pequeña y la más grande
def informacion_nave_mas_pequena_y_mas_grande():
    nave_mas_pequena = min(naves, key=lambda x: x["largo"])
    nave_mas_grande = max(naves, key=lambda x: x["largo"])
    return nave_mas_pequena, nave_mas_grande

# Ejemplo de uso interactivo
while True:
    print("\n=== Menú de Consulta ===")
    print("1. Listar naves ordenadas por nombre y largo")
    print("2. Mostrar información de una nave específica")
    print("3. Mostrar las cinco naves con mayor cantidad de pasajeros")
    print("4. Indicar la nave que requiere mayor cantidad de tripulación")
    print("5. Mostrar todas las naves que comienzan con AT")
    print("6. Listar naves que pueden llevar seis o más pasajeros")
    print("7. Mostrar información de la nave más pequeña y la más grande")
    print("8. Salir")
    opcion = input("Ingrese el número de la opción que desea consultar: ")

    if opcion == "1":
        print(listar_naves_ordenadas())
    elif opcion == "2":
        nombre_nave = input("Ingrese el nombre de la nave que desea consultar: ")
        print(mostrar_informacion_nave(nombre_nave))
    elif opcion == "3":
        print(cinco_naves_con_mas_pasajeros())
    elif opcion == "4":
        print(nave_con_mas_tripulacion())
    elif opcion == "5":
        print(naves_que_comienzan_con_AT())
    elif opcion == "6":
        print(naves_con_seis_o_mas_pasajeros())
    elif opcion == "7":
        print(informacion_nave_mas_pequena_y_mas_grande())
   
