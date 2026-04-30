# ============================================
# GUÍA PRÁCTICA PARA EXAMEN (BIG-O)
# TODO EXPLICADO CON COMENTARIOS
# ============================================

# ============================================
# 1. REGLAS CLAVE
# ============================================

# Un solo for → O(n)
# Dos for anidados → O(n^2)
# Tres for → O(n^3)
# Dividir entre 2 → O(log n)
# x in lista → O(n)
# x in set → O(1)

# ============================================
# 2. EJEMPLOS BÁSICOS
# ============================================

def ejemplo_lineal(lista):
    # Recorre toda la lista una vez
    # COMPLEJIDAD: O(n)
    total = 0
    for x in lista:
        total += x
    return total


def ejemplo_cuadratico(lista):
    # Dos ciclos anidados
    # COMPLEJIDAD: O(n^2)
    for i in range(len(lista)):
        for j in range(len(lista)):
            print(lista[i], lista[j])


def ejemplo_logaritmico(n):
    # Divide el problema entre 2 en cada paso
    # COMPLEJIDAD: O(log n)
    while n > 1:
        n = n // 2


# ============================================
# 3. BUSCAR ELEMENTOS
# ============================================

def buscar_en_lista(lista, x):
    # Busca recorriendo toda la lista
    # COMPLEJIDAD: O(n)
    return x in lista


def buscar_en_set(lista, x):
    # Convertimos a set
    # COMPLEJIDAD: O(n) para crear set + O(1) búsqueda
    conjunto = set(lista)
    return x in conjunto


# ============================================
# 4. ELIMINAR DUPLICADOS
# ============================================

def unicos_lento(lista):
    # COMPLEJIDAD: O(n^2)
    # Porque:
    # - for recorre n veces
    # - "x not in resultado" cuesta O(n)
    resultado = []
    for x in lista:
        if x not in resultado:
            resultado.append(x)
    return resultado


def unicos_rapido(lista):
    # COMPLEJIDAD: O(n)
    # Porque usamos set (búsqueda O(1))
    resultado = []
    vistos = set()

    for x in lista:
        if x not in vistos:
            resultado.append(x)
            vistos.add(x)

    return resultado


# ============================================
# 5. ELEMENTO MÁS REPETIDO
# ============================================

def mas_repetido_lento(lista):
    # COMPLEJIDAD: O(n^2)
    max_elem = None
    max_count = 0

    for x in lista:
        count = 0
        for y in lista:
            if x == y:
                count += 1

        if count > max_count:
            max_count = count
            max_elem = x

    return max_elem, max_count


def mas_repetido_rapido(lista):
    # COMPLEJIDAD: O(n)
    # Usa diccionario para contar
    contador = {}

    for x in lista:
        contador[x] = contador.get(x, 0) + 1

    max_elem = None
    max_count = 0

    for x in contador:
        if contador[x] > max_count:
            max_count = contador[x]
            max_elem = x

    return max_elem, max_count


# ============================================
# 6. PARES QUE SUMAN K
# ============================================

def pares_lento(lista, k):
    # COMPLEJIDAD: O(n^2)
    pares = []

    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == k:
                pares.append((lista[i], lista[j]))

    return pares


def pares_rapido(lista, k):
    # COMPLEJIDAD: O(n)
    # Estrategia del complemento
    pares = []
    vistos = set()

    for x in lista:
        complemento = k - x

        if complemento in vistos:
            pares.append((complemento, x))

        vistos.add(x)

    return pares


# ============================================
# 7. TRES NÚMEROS QUE SUMAN CERO
# ============================================

def tres_suman_cero(lista):
    # COMPLEJIDAD: O(n^3)
    n = len(lista)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if lista[i] + lista[j] + lista[k] == 0:
                    return True

    return False


# ============================================
# 8. RECURSIÓN LOGARÍTMICA
# ============================================

def gamma(n):
    # COMPLEJIDAD: O(log n)
    # Porque divide entre 2 en cada llamada
    if n <= 1:
        return 1
    return gamma(n // 2) + 1


# ============================================
# 9. RAÍZ CUADRADA
# ============================================

def raiz(n):
    # COMPLEJIDAD: O(√n)
    i = 1

    while i * i <= n:
        i += 1

    return i


# ============================================
# 10. FRASES PARA EXAMEN (IMPORTANTE)
# ============================================

# Usa estas frases:

# "La complejidad es O(n) porque el algoritmo recorre la lista una sola vez."

# "La complejidad es O(n^2) porque hay dos ciclos anidados que recorren la lista."

# "La complejidad es O(log n) porque el problema se divide entre 2 en cada iteración."

# "La complejidad es O(n) porque se usa un set/diccionario que permite búsquedas en O(1)."

# ============================================
# FIN
# ============================================