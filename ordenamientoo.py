# Caso 1: Sistema de notas finales de un semestre universitario

#contexto del problema
"""La universidad necesita generar el listado oficial de calificaciones al final del semestre. Tiene
una base de datos con 200 estudiantes de un curso, cada uno con una nota final en escala 0-100
(numeros enteros). El sistema debe imprimir el listado ordenado de menor a mayor para publicarlo
en la cartelera oficial.
"""

#datos clave
"""
Tamaño: n = 200 estudiantes
Restricción: si dos estudiantes tienen la misma nota, debe quedar en el orden en que aparecen en la
lista originar (orden alfabetico previo).
No hay limitación de memoria
"""

# -------------------------------------------

### Caso 3: Limpieza de archivos en un servidor de producción

"""Contexto del problema:

Eres administrador de un servidor con 50,000 archivos. Necesitas ordenarlos por tamaño para 
identificar los más grandes y liberar espacio. El servidor ejecuta este proceso durante la madrugada 
como tarea programada y **debe terminar en una ventana fija de 30 minutos**, sin importar la
 distribución de los datos. No puedes permitir que el algoritmo se demore más de lo previsto.

Datos clave:
Tamaño: n = 50,000 archivos
Tipo de dato: enteros (bytes), desde 1KB (1024) hasta 10GB (10^10)
Distribución: muy variada e impredecible
Memoria: disponible (servidor de producción con buena RAM)
"""
import random
import time

def generar_jugadores(n):
    paises = ["Argentina", "Brasil", "Chile", "Colombia", "Perú", "Uruguay", "Venezuela"]
    nombres = ["Alex", "Sam", "Juan", "Camila", "Alicia", "Camilo"]

    jugadores = []
    for i in range(n):
        jugadores.append({
            "id": i + 1,
            "nombre": f"{random.choice(nombres)}_{i}",
            "puntos": random.randint(100, 10000),
            "horas": random.randint(10, 1000),
            "pais": random.choice(paises)
        })

    return jugadores

lista_jugadores = generar_jugadores(1000)
#print(lista_jugadores)

#Mejorada

def merge(izq, der):
    resultado = []
    i = j = 0
    while i < len(izq) and j < len(der):
        a = izq[i]
        b = der[j]
        if a["puntos"] > b["puntos"]:
            resultado.append(a)
            i += 1
        elif a["puntos"] == b["puntos"] and a["horas"] < b["horas"]:
            resultado.append(a)
            i += 1
        else:
            resultado.append(b)
            j += 1
    # Agregar cualquier elemento restante de las listas
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izq = merge_sort(lista[:medio])
    der = merge_sort(lista[medio:])
    return merge(izq, der)

lista_ordenada = merge_sort(lista_jugadores)
print(lista_ordenada)

def heapify(arr, n, i):
    mayor = i
    izq = 2 * i + 1
    der = 2 * i + 2

    if izq < n and arr[izq]["puntos"] > arr[mayor]["puntos"]:
        mayor = izq
    
    if der < n and arr[der]["puntos"] > arr[mayor]["puntos"]:
        mayor = der
    
    if mayor != i:
        arr[i], arr[mayor] = arr[mayor], arr[i]
        heapify(arr, n, mayor)
    
def heapsort(lista, k):
    arr = lista.copy(9)
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    resultado = []
    tamaño = n

    for i in range(min(k, n)):
        resultado.append(arr[0])
        tamaño -= 1
        arr[0] = arr[tamaño]
        heapify(arr, tamaño, 0)
    return resultado

def quicksort(arr, low, high):
    if low < high:
        pi = particion(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)   

def particion(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

arr = [10, 7, 8, 9, 1, 5]
n = len
quicksort(arr, 0, n - 1)

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    conteo = [0] * 10

    for i in range(n):
        index = (arr[i] // exp) % 10
        conteo[index] += 1

    for i in range(1, 10):
        conteo[i] += conteo[i - 1]
    
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[conteo[index] - 1] = arr[i]
        conteo[index] -= 1
        i -= 1
        

def radix_sort(arr):
    max_elemento = max(arr)
    exp = 1
    while max_elemento // exp > 0:
        counting_sort(arr, exp)
        exp *= 10



def counting_sort(arr):
    if len(arr)==0:
        return arr
    max_value=max(arr)
    count=[0]*(max_value+1)

    for num in arr:
        count[num]+=1

    sorted_arr=[]
    for i in range(len(count)):
        sorted_arr.extend([i]*count[i])
    return sorted_arr