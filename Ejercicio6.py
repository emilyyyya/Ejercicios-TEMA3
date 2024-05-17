import random
import time

# Algoritmo de ordenamiento por casilleros (Bucket Sort)
def bucket_sort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]  # Crear n buckets
    for num in arr:
        index = int(num * n / 1000000)  # Calcular el índice correcto para el bucket
        buckets[index].append(num)
    for i in range(n):
        buckets[i].sort()
    result = []
    for bucket in buckets:
        result.extend(bucket)
    return result


# Algoritmo de ordenamiento Shell (Shell Sort)
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

# Algoritmo de ordenamiento Radix (Radix Sort)
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

# Función de búsqueda para comparar
def busqueda(lista, elemento):
    return elemento in lista

# Generar lista aleatoria
def generar_lista(tamano):
    return [random.randint(1, 1000000) for _ in range(tamano)]

# Medir tiempo de ejecución de un algoritmo de ordenamiento
def medir_tiempo_ordenamiento(algoritmo, lista):
    inicio = time.time()
    algoritmo(lista)
    fin = time.time()
    return fin - inicio

# Medir tiempo de ejecución de una búsqueda
def medir_tiempo_busqueda(lista, elemento):
    inicio = time.time()
    busqueda(lista, elemento)
    fin = time.time()
    return fin - inicio

# Ejemplo de uso
tamanos = [100000, 1000000, 10000000]
elemento = random.randint(1, 1000000)

print("Tiempo de ejecución de ordenamiento:")
for tamano in tamanos:
    lista = generar_lista(tamano)
    tiempo_bucket = medir_tiempo_ordenamiento(bucket_sort, lista.copy())
    tiempo_shell = medir_tiempo_ordenamiento(shell_sort, lista.copy())
    tiempo_radix = medir_tiempo_ordenamiento(radix_sort, lista.copy())
    print(f"Tamaño: {tamano}, Bucket Sort: {tiempo_bucket:.6f} segundos, Shell Sort: {tiempo_shell:.6f} segundos, Radix Sort: {tiempo_radix:.6f} segundos")

print("\nTiempo de ejecución de búsqueda:")
for tamano in tamanos:
    lista = generar_lista(tamano)
    tiempo_busqueda = medir_tiempo_busqueda(lista, elemento)
    print(f"Tamaño: {tamano}, Tiempo de búsqueda: {tiempo_busqueda:.6f} segundos")

