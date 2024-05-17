#Funcion recursiva
#Implementar una función que permita obtener el valor en la sucesión de Fibonacci para un número dado.

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Ejemplo de uso
numero = int(input("Introduce un número para calcular su valor en la sucesión de Fibonacci: "))
resultado = fibonacci(numero)
print(f"El valor de Fibonacci para el número {numero} es {resultado}")
