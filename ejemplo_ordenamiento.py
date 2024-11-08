import time
import random

# Función de ordenamiento por selección con conteo de pasadas y tiempo
def selection_sort(arr):
    items = arr[:]
    n = len(items)
    pasadas = 0
    start_time = time.time()
    for i in range(n):
        print(f"Selección - pasada {pasadas + 1}: {items}")
        min_idx = i
        for j in range(i + 1, n):
            if items[j] < items[min_idx]:
                min_idx = j
        items[i], items[min_idx] = items[min_idx], items[i]
        pasadas += 1
    end_time = time.time()
    return items, pasadas, end_time - start_time

# Función de ordenamiento por inserción con conteo de pasadas y tiempo
def insertion_sort(arr):
    items = arr[:]
    pasadas = 0
    start_time = time.time()
    for i in range(1, len(items)):
        key = items[i]
        j = i - 1
        while j >= 0 and key < items[j]:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = key
        pasadas += 1
        print(f"Inserción - pasada {pasadas}: {items}")
    end_time = time.time()
    return items, pasadas, end_time - start_time

# Función de ordenamiento por burbuja con conteo de pasadas y tiempo
def bubble_sort(arr):
    items = arr[:]
    n = len(items)
    pasadas = 0
    start_time = time.time()
    for i in range(n):
        print(f"Burbuja - pasada {pasadas + 1}: {items}")
        for j in range(0, n - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
        pasadas += 1
    end_time = time.time()
    return items, pasadas, end_time - start_time

# Crear un arreglo de números aleatorios
arreglo = [random.randint(1, 100) for _ in range(10)]
print("Arreglo original:", arreglo)

# Contar pasadas y medir tiempo para selección
print("\nOrdenamiento por Selección:")
arr_seleccion = arreglo[:]
arr_ordenado_seleccion, pasadas_seleccion, tiempo_seleccion = selection_sort(arr_seleccion)
print("Arreglo ordenado por Selección:", arr_ordenado_seleccion)
print("Pasadas de Selección:", pasadas_seleccion)
print("Tiempo de Selección:", tiempo_seleccion)

# Contar pasadas y medir tiempo para inserción
print("\nOrdenamiento por Inserción:")
arr_insercion = arreglo[:]
arr_ordenado_insercion, pasadas_insercion, tiempo_insercion = insertion_sort(arr_insercion)
print("Arreglo ordenado por Inserción:", arr_ordenado_insercion)
print("Pasadas de Inserción:", pasadas_insercion)
print("Tiempo de Inserción:", tiempo_insercion)

# Contar pasadas y medir tiempo para burbuja
print("\nOrdenamiento por Burbuja:")
arr_burbuja = arreglo[:]
arr_ordenado_burbuja, pasadas_burbuja, tiempo_burbuja = bubble_sort(arr_burbuja)
print("Arreglo ordenado por Burbuja:", arr_ordenado_burbuja)
print("Pasadas de Burbuja:", pasadas_burbuja)
print("Tiempo de Burbuja:", tiempo_burbuja)

# Comparar los tiempos
min_time = min(tiempo_seleccion, tiempo_insercion, tiempo_burbuja)
if min_time == tiempo_seleccion:
    best_method_time = "Selección"
elif min_time == tiempo_insercion:
    best_method_time = "Inserción"
else:
    best_method_time = "Burbuja"

# Comparar las pasadas
min_pasadas = min(pasadas_seleccion, pasadas_insercion, pasadas_burbuja)
if min_pasadas == pasadas_seleccion:
    best_method_pasadas = "Selección"
elif min_pasadas == pasadas_insercion:
    best_method_pasadas = "Inserción"
else:
    best_method_pasadas = "Burbuja"

print(f"\nEl método más rápido es: {best_method_time} con un tiempo de {min_time:.6f} segundos.")
print(f"El método con menos pasadas es: {best_method_pasadas} con {min_pasadas} pasadas.")
