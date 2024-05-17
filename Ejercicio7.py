#La empresa Netflix nos pone a nuestra disposición los datos de todas las series cargadas en esta plataforma con los siguientes datos: nombre, cantidad de temporadas y cantidad de capítulos
#totales de la serie. Los cuales debemos procesar desarrollando las funciones necesarias para dar solución a las siguientes ítems:
#listar las series ordenadas a cuerdo a los siguientes criterios: por nombre, por cantidad de temporadas, por cantidad de capítulos;
#mostrar toda la información de la serie “Los 100“;
#determinar cuál es la serie con mayor cantidad de temporadas y mayor cantidad de capítulos;
#calcular cuantas series dispone la plataforma y el promedio de temporadas;
#determinar el promedio de capítulos por temporada de la serie “Star Wars: Rebels”;
#listar el TOP 5 de series con mayor cantidad de capítulos y el top 10 de las series con mayor cantidad de temporadas;
#mostrar todas las series con tres o menos temporadas.

# Datos de las series
series = {
    "Breaking Bad": (5, 62),
    "Game of Thrones": (8, 73),
    "Stranger Things": (3, 25),
    "The Crown": (4, 40),
    "Los 100": (7, 100),
    "Friends": (10, 236),
    "Star Wars: Rebels": (4, 75),
    "The Mandalorian": (2, 16),
    "Narcos": (3, 30),
    "Dark": (3, 26)
}

# Funciones para procesar los datos de las series

# Función para listar las series ordenadas según diferentes criterios
def listar_series_ordenadas(criterio):
    return sorted(series.items(), key=lambda x: x[1][criterio])

# Función para mostrar toda la información de una serie específica
def mostrar_informacion_serie(nombre_serie):
    if nombre_serie in series:
        return f"Información de la serie '{nombre_serie}': Temporadas: {series[nombre_serie][0]}, Capítulos: {series[nombre_serie][1]}"
    else:
        return "La serie no se encuentra en la plataforma."

# Función para determinar la serie con mayor cantidad de temporadas y capítulos
def serie_con_mas_temporadas_y_capitulos():
    serie_max_temp = max(series, key=lambda x: series[x][0])
    serie_max_capitulos = max(series, key=lambda x: series[x][1])
    return serie_max_temp, serie_max_capitulos

# Función para calcular la cantidad de series en la plataforma y el promedio de temporadas
def cantidad_series_y_promedio_temporadas():
    cantidad_series = len(series)
    promedio_temporadas = sum(s[0] for s in series.values()) / cantidad_series
    return cantidad_series, promedio_temporadas

# Función para determinar el promedio de capítulos por temporada de una serie específica
def promedio_capitulos_por_temporada(nombre_serie):
    if nombre_serie in series:
        temporadas, capitulos = series[nombre_serie]
        return capitulos / temporadas
    else:
        return "La serie no se encuentra en la plataforma."

# Función para listar el TOP 5 de series con mayor cantidad de capítulos
def top_5_series_capitulos():
    return sorted(series.items(), key=lambda x: x[1][1], reverse=True)[:5]

# Función para listar el TOP 10 de series con mayor cantidad de temporadas
def top_10_series_temporadas():
    return sorted(series.items(), key=lambda x: x[1][0], reverse=True)[:10]

# Función para mostrar todas las series con tres o menos temporadas
def series_con_tres_o_menos_temporadas():
    return [nombre for nombre, datos in series.items() if datos[0] <= 3]

# Ejemplo de uso interactivo
while True:
    print("\n=== Menú de Consulta ===")
    print("1. Listar series ordenadas (por nombre, temporadas o capítulos)")
    print("2. Mostrar información de una serie específica")
    print("3. Serie con mayor cantidad de temporadas y capítulos")
    print("4. Cantidad de series y promedio de temporadas")
    print("5. Promedio de capítulos por temporada de una serie específica")
    print("6. TOP 5 de series con mayor cantidad de capítulos")
    print("7. TOP 10 de series con mayor cantidad de temporadas")
    print("8. Mostrar series con tres o menos temporadas")
    print("9. Salir")
    opcion = input("Ingrese el número de la opción que desea consultar: ")

    if opcion == "1":
        criterio = input("Ingrese el criterio de ordenamiento (nombre, temporadas, capitulos): ")
        if criterio == "nombre":
            print(listar_series_ordenadas(0))
        elif criterio == "temporadas":
            print(listar_series_ordenadas(1))
        elif criterio == "capitulos":
            print(listar_series_ordenadas(1))
        else:
            print("Criterio no válido.")
    elif opcion == "2":
        nombre_serie = input("Ingrese el nombre de la serie que desea consultar: ")
        print(mostrar_informacion_serie(nombre_serie))
    elif opcion == "3":
        print(serie_con_mas_temporadas_y_capitulos())
    elif opcion == "4":
        print(cantidad_series_y_promedio_temporadas())
    elif opcion == "5":
        nombre_serie = input("Ingrese el nombre de la serie que desea consultar: ")
        print(promedio_capitulos_por_temporada(nombre_serie))
    elif opcion == "6":
        print(top_5_series_capitulos())
    elif opcion == "7":
        print(top_10_series_temporadas())
    elif opcion == "8":
        print(series_con_tres_o_menos_temporadas())
    elif opcion == "9":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor ingrese un número del 1 al 9.")
