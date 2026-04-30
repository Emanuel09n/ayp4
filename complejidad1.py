# ============================================
# RESPUESTAS – EJERCICIOS TIPO PARCIAL
# ============================================

# ============================================
# EJERCICIO 1: COMPLEJIDAD
# ============================================

def f1(lista):
    for x in lista:
        print(x)

# Complejidad: O(n)
# Porque: recorre la lista una sola vez


def f2(lista):
    for i in range(len(lista)):
        for j in range(len(lista)):
            print(i, j)

# Complejidad: O(n^2)
# Porque: dos ciclos anidados → n * n


def f3(n):
    while n > 1:
        n = n // 2

# Complejidad: O(log n)
# Porque: divide entre 2 en cada iteración


def f4(lista):
    for x in lista:
        if x in lista:
            print(x)

# Complejidad: O(n^2)
# Porque:
# for → O(n)
# x in lista → O(n)
# Total: O(n * n) = O(n^2)


def f5(n):
    for i in range(n):
        j = 1
        while j < n:
            j *= 2

# Complejidad: O(n log n)
# Porque:
# for externo → O(n)
# while interno → O(log n)
# Total: O(n log n)


# ============================================
# EJERCICIO 2: ORDEN
# ============================================

# O(1)
# O(log n)
# O(n)
# O(n log n)
# O(n^2)
# O(2^n)


# ============================================
# EJERCICIO 3: VERDADERO / FALSO
# ============================================

# 1. FALSO
# O(2n) = O(n) → las constantes no importan

# 2. VERDADERO
# x in set es O(1) en promedio

# 3. FALSO
# depende:
# si el segundo for es fijo → O(n)
# no siempre es O(n^2)

# 4. FALSO
# sorted() es O(n log n)

# 5. FALSO
# para n pequeño puede variar, aunque para n grande O(n^2) crece más


# ============================================
# EJERCICIO 4: CÓDIGO LENTO
# ============================================

def duplicados(lista):
    resultado = []
    for x in lista:
        if x not in resultado:
            resultado.append(x)
    return resultado

# Complejidad: O(n^2)
# Porque:
# for → O(n)
# x not in resultado → O(n)
# Total: O(n^2)

# Mejora:

def duplicados_rapido(lista):
    resultado = []
    vistos = set()

    for x in lista:
        if x not in vistos:
            resultado.append(x)
            vistos.add(x)

    return resultado

# Nueva complejidad: O(n)
# Porque set permite búsqueda O(1)


# ============================================
# EJERCICIO 5: PARES
# ============================================

def pares(lista, k):
    resultado = []
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] + lista[j] == k:
                resultado.append((lista[i], lista[j]))
    return resultado

# Complejidad: O(n^2)

# Versión optimizada:

def pares_rapido(lista, k):
    resultado = []
    vistos = set()

    for x in lista:
        complemento = k - x

        if complemento in vistos:
            resultado.append((complemento, x))

        vistos.add(x)

    return resultado

# Nueva complejidad: O(n)


# ============================================
# EJERCICIO 6: FRECUENCIA
# ============================================

def frecuencia(lista):
    for x in lista:
        count = 0
        for y in lista:
            if x == y:
                count += 1

# Complejidad: O(n^2)

# Optimizado:

def frecuencia_rapida(lista):
    contador = {}

    for x in lista:
        contador[x] = contador.get(x, 0) + 1

    return contador

# Nueva complejidad: O(n)


# ============================================
# EJERCICIO 7: RECURSIÓN
# ============================================

def f(n):
    if n <= 1:
        return 1
    return f(n//2)

# Complejidad: O(log n)
# Porque divide el problema entre 2


# ============================================
# EJERCICIO 8: ESTRUCTURAS
# ============================================

# Para búsqueda rápida:
# set → O(1)

# Para conteo:
# dict → O(n)

# lista → O(n) para buscar (lento)


# ============================================
# EJERCICIO 9: TRAMPA
# ============================================

def f(lista):
    for i in range(len(lista)):
        for j in range(5):
            print(i, j)

# Complejidad: O(n)
# Porque:
# segundo for es constante → O(5)
# O(n * 5) = O(n)


# ============================================
# EJERCICIO 10: NIVEL ALTO
# ============================================

def f(lista):
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            for k in range(j+1, len(lista)):
                print(i, j, k)

# Complejidad: O(n^3)
# Porque hay tres ciclos anidados


# ============================================
# FIN
# ============================================