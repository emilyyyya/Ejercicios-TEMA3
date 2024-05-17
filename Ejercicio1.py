#TDA PILA
class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

    def esta_vacia(self):
        return len(self.items) == 0

    def tamano(self):
        return len(self.items)

    def cima(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            return None

    def obtener_elemento_desde_fondo(self, posicion):
        if 0 <= posicion < self.tamano():
            return self.items[-(posicion + 1)]
        else:
            return None

    def mostrar_elementos(self):
        for item in reversed(self.items):
            print(item)

def mostrar_planetas_visitados(pila):
    print("\nPlanetas visitados en orden:")
    pila.mostrar_elementos()

def total_creditos_y_mayor_fortuna(misiones_cazarrecompensas):
    max_fortuna = 0
    cazarrecompensas_rico = None
    for cazarrecompensas, pila in misiones_cazarrecompensas.items():
        total_creditos = sum(mision[1] for mision in pila.items)
        print(f"{cazarrecompensas} recaudó un total de {total_creditos} créditos galácticos.")
        if total_creditos > max_fortuna:
            max_fortuna = total_creditos
            cazarrecompensas_rico = cazarrecompensas
    print(f"El cazarrecompensas con mayor fortuna es {cazarrecompensas_rico} con {max_fortuna} créditos galácticos.")

def posicion_mision_han_solo(pila):
    for i in range(pila.tamano()):
        mision = pila.obtener_elemento_desde_fondo(i)
        if mision[2]:  # Si capturó a Han Solo
            print(f"Capturó a Han Solo en la misión {i + 1} desde el fondo de la pila.")
            return

def capturas_por_cazarrecompensas(pila):
    capturas = sum(1 for mision in pila.items if mision[2])
    print(f"Realizó {capturas} capturas.")

# Ejemplo de datos
misiones_cazarrecompensas = {
    'Boba Fett': Pila(),
    'Jango Fett': Pila(),
    'Cad Bane': Pila()
}

misiones_cazarrecompensas['Boba Fett'].apilar(('Tatooine', 500, False))
misiones_cazarrecompensas['Boba Fett'].apilar(('Bespin', 1000, True))  # Capturó a Han Solo
misiones_cazarrecompensas['Boba Fett'].apilar(('Endor', 300, False))

misiones_cazarrecompensas['Jango Fett'].apilar(('Kamino', 700, False))
misiones_cazarrecompensas['Jango Fett'].apilar(('Geonosis', 900, False))
misiones_cazarrecompensas['Jango Fett'].apilar(('Naboo', 400, False))

misiones_cazarrecompensas['Cad Bane'].apilar(('Coruscant', 600, False))
misiones_cazarrecompensas['Cad Bane'].apilar(('Nal Hutta', 800, False))
misiones_cazarrecompensas['Cad Bane'].apilar(('Mustafar', 1200, False))

# Función principal para interactuar con el usuario
def main():
    while True:
        nombre = input("Introduce el nombre del cazarrecompensas (o 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break
        elif nombre in misiones_cazarrecompensas:
            pila = misiones_cazarrecompensas[nombre]
            print(f"\nDatos para {nombre}:")
            mostrar_planetas_visitados(pila)
            capturas_por_cazarrecompensas(pila)
            if nombre == 'Boba Fett':
                posicion_mision_han_solo(pila)
        else:
            print("Nombre no reconocido. Inténtalo de nuevo.")
    
    print("\nResumen de créditos y fortuna:")
    total_creditos_y_mayor_fortuna(misiones_cazarrecompensas)

# Ejecutar el programa principal
main()
