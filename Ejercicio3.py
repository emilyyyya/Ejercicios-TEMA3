#Implementar una función que calcule la suma de todos los números enteros comprendidos entre cero y un número entero positivo dado.def suma_enteros(n):

def suma_enteros(n):
    if n <= 0:
        return 0
    else:
        return n + suma_enteros(n - 1)

# Ejemplo de uso
numero = int(input("Introduce un número entero positivo: "))
resultado = suma_enteros(numero)
print(f"La suma de todos los números enteros entre 0 y {numero} es {resultado}")

