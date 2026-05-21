# ═══════════════════════════════════════════════════════════════════════════════
#                QUIZ - ALGORITMOS DE ORDENAMIENTO
# ═══════════════════════════════════════════════════════════════════════════════

"""
INSTRUCCIONES:
- En cada caso debes:
    1. ELEGIR el mejor algoritmo justificando complejidad temporal,
       espacial y estabilidad.
    2. EXPLICAR brevemente por qué los OTROS algoritmos no son los más
       adecuados.
    3. IMPLEMENTAR el algoritmo aplicado a la estructura de datos del caso.
"""



# ═══════════════════════════════════════════════════════════════════════════════
# CASO 4 (1.7): Plataforma de Streaming Musical
# ═══════════════════════════════════════════════════════════════════════════════

"""
CONTEXTO:
---------
Una plataforma de música guarda las canciones más reproducidas
del día para generar el TOP 100 global.

Cada canción tiene esta estructura:

    {
        "id": 882,
        "titulo": "Blinding Lights",
        "reproducciones": 985421,
        "fecha_subida": "2025-01-10"
    }

REGLAS:
  R1) Debe ordenarse DESCENDENTE por reproducciones.
  R2) Si dos canciones tienen las mismas reproducciones,
      NO importa el orden entre ellas.
  R3) El sistema tiene poca memoria RAM disponible.

ANÁLISIS:
  1. ¿Qué algoritmo eliges? Heap Sort
  2. Complejidad temporal: O(n log n)
  3. Complejidad espacial: O(1)
  4. Estabilidad: No estable, pero no importa aquí.

¿Por qué no los otros?
- Merge Sort usa memoria extra O(n).
- Bubble, Selection e Insertion son O(n²).
- Quick Sort tiene peor caso O(n²).
"""


def ordenar_canciones(canciones):
    """
    TODO: Ordenar canciones por reproducciones descendente.
    Algoritmo elegido: Heap Sort
    """

    arr = canciones.copy()

    def heapify(n, i):

        mayor = i
        izq = 2 * i + 1
        der = 2 * i + 2

        if izq < n and arr[izq]["reproducciones"] > arr[mayor]["reproducciones"]:
            mayor = izq

        if der < n and arr[der]["reproducciones"] > arr[mayor]["reproducciones"]:
            mayor = der

        if mayor != i:
            arr[i], arr[mayor] = arr[mayor], arr[i]
            heapify(n, mayor)

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(i, 0)

    arr.reverse()
    return arr



# ═══════════════════════════════════════════════════════════════════════════════
# CASO 5 (1.7): Sistema Electoral
# ═══════════════════════════════════════════════════════════════════════════════

"""
CONTEXTO:
---------
La Registraduría necesita ordenar votos por mesa electoral.

Cada voto:

    {
        "mesa": 204,
        "candidato": "Ana Torres",
        "hora": "08:14:22"
    }

REGLAS:
  R1) Orden ascendente por número de mesa.
  R2) Si dos votos pertenecen a la misma mesa,
      DEBE mantenerse el orden original de llegada.
  R3) Existen solo 5000 mesas posibles.

ANÁLISIS:
  1. ¿Qué algoritmo eliges? Counting Sort estable
  2. Complejidad temporal: O(n + k)
  3. Complejidad espacial: O(n + k)
  4. Estabilidad: Sí importa.

¿Por qué no los otros?
- Heap y Quick Sort no son estables.
- Merge Sort sí es estable, pero más lento.
- Bubble e Insertion son O(n²).
"""


def ordenar_votos(votos):
    """
    TODO: Ordenar votos por mesa manteniendo orden original.
    Algoritmo elegido: Counting Sort estable
    """

    if not votos:
        return []

    k = 5000
    conteo = [0] * (k + 1)

    for voto in votos:
        conteo[voto["mesa"]] += 1

    for i in range(1, len(conteo)):
        conteo[i] += conteo[i - 1]

    salida = [None] * len(votos)

    for voto in reversed(votos):

        mesa = voto["mesa"]

        conteo[mesa] -= 1
        salida[conteo[mesa]] = voto

    return salida



# ═══════════════════════════════════════════════════════════════════════════════
# CASO 6 (1.6): Hospital - Pacientes Prioritarios
# ═══════════════════════════════════════════════════════════════════════════════

"""
CONTEXTO:
---------
Un hospital clasifica pacientes por nivel de urgencia.

Cada paciente:

    (id, prioridad, nombre)

Donde:
  prioridad:
    1 = crítica
    2 = alta
    3 = media
    4 = baja

REGLAS:
  R1) Orden ascendente por prioridad.
  R2) Los pacientes con misma prioridad
      deben conservar orden de llegada.
  R3) Solo existen 4 prioridades posibles.

ANÁLISIS:
  1. ¿Qué algoritmo eliges? Counting Sort estable
  2. Complejidad temporal: O(n + k)
  3. Complejidad espacial: O(n + k)
  4. Estabilidad: Sí importa.

¿Por qué no los otros?
- Quick y Heap Sort no garantizan estabilidad.
- Merge Sort usa más memoria.
- Bubble e Insertion son más lentos.
"""


def ordenar_pacientes(lista):
    """
    TODO: Ordenar pacientes por prioridad.
    Algoritmo elegido: Counting Sort estable
    """

    if not lista:
        return []

    k = 4
    conteo = [0] * (k + 1)

    for paciente in lista:
        prioridad = paciente[1]
        conteo[prioridad] += 1

    for i in range(1, len(conteo)):
        conteo[i] += conteo[i - 1]

    salida = [None] * len(lista)

    for paciente in reversed(lista):

        prioridad = paciente[1]

        conteo[prioridad] -= 1
        salida[conteo[prioridad]] = paciente

    return salida



# ═══════════════════════════════════════════════════════════════════════════════
# CASO 7 (1.7): E-commerce - Productos por Precio
# ═══════════════════════════════════════════════════════════════════════════════

"""
CONTEXTO:
---------
Una tienda online necesita ordenar 2 millones de productos
por precio para mostrar resultados al usuario.

Cada producto:

    {
        "id": 1,
        "nombre": "Teclado",
        "precio": 150000
    }

REGLAS:
  R1) Orden ascendente por precio.
  R2) El orden entre precios iguales NO importa.
  R3) El servidor tiene memoria limitada.
  R4) El peor caso importa mucho.

ANÁLISIS:
  1. ¿Qué algoritmo eliges? Heap Sort
  2. Complejidad temporal: O(n log n)
  3. Complejidad espacial: O(1)
  4. Estabilidad: No estable, pero no importa.

¿Por qué no los otros?
- Merge Sort usa memoria O(n).
- Quick Sort tiene peor caso O(n²).
- Bubble, Selection e Insertion son O(n²).
"""


def ordenar_productos(productos):
    """
    TODO: Ordenar productos por precio ascendente.
    Algoritmo elegido: Heap Sort
    """

    arr = productos.copy()

    def heapify(n, i):

        mayor = i
        izq = 2 * i + 1
        der = 2 * i + 2

        if izq < n and arr[izq]["precio"] > arr[mayor]["precio"]:
            mayor = izq

        if der < n and arr[der]["precio"] > arr[mayor]["precio"]:
            mayor = der

        if mayor != i:
            arr[i], arr[mayor] = arr[mayor], arr[i]
            heapify(n, mayor)

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    for i in range(n - 1, 0, -1):

        arr[0], arr[i] = arr[i], arr[0]
        heapify(i, 0)

    return arr



# ═══════════════════════════════════════════════════════════════════════════════
# CASO 8 (1.6): Sensores IoT
# ═══════════════════════════════════════════════════════════════════════════════

"""
CONTEXTO:
---------
Miles de sensores generan temperaturas por segundo.

Cada dato:

    (sensor_id, temperatura)

Las temperaturas van de -20°C a 80°C.

REGLAS:
  R1) Orden ascendente por temperatura.
  R2) Hay MUCHÍSIMOS datos.
  R3) El rango de temperaturas es PEQUEÑO.

ANÁLISIS:
  1. ¿Qué algoritmo eliges? Counting Sort
  2. Complejidad temporal: O(n + k)
  3. Complejidad espacial: O(n + k)

¿Por qué no los otros?
- Quick, Merge y Heap son O(n log n).
- Bubble, Selection e Insertion son O(n²).
- Counting Sort aprovecha el rango pequeño.
"""


def ordenar_temperaturas(datos):
    """
    TODO: Ordenar temperaturas.
    Algoritmo elegido: Counting Sort
    """

    if not datos:
        return []

    min_temp = -20
    max_temp = 80

    rango = max_temp - min_temp + 1

    conteo = [0] * rango

    for dato in datos:

        temperatura = dato[1]

        conteo[temperatura - min_temp] += 1

    for i in range(1, len(conteo)):
        conteo[i] += conteo[i - 1]

    salida = [None] * len(datos)

    for dato in reversed(datos):

        temperatura = dato[1]
        indice = temperatura - min_temp

        conteo[indice] -= 1
        salida[conteo[indice]] = dato

    return salida



# ═══════════════════════════════════════════════════════════════════════════════
# CASO 9 (1.7): Plataforma de Videojuegos
# ═══════════════════════════════════════════════════════════════════════════════

"""
CONTEXTO:
---------
Una plataforma necesita ordenar puntajes de jugadores.

Cada registro:

    {
        "jugador": "Carlos",
        "puntaje": 999999
    }

REGLAS:
  R1) Orden descendente por puntaje.
  R2) El sistema necesita rendimiento promedio muy rápido.
  R3) No importa estabilidad.
  R4) El peor caso ocurre rara vez.

ANÁLISIS:
  1. ¿Qué algoritmo eliges? Quick Sort
  2. Complejidad promedio: O(n log n)
  3. Complejidad peor caso: O(n²)
  4. Estabilidad: No estable.

¿Por qué no los otros?
- Heap Sort suele ser más lento en promedio.
- Merge Sort usa memoria extra.
- Bubble e Insertion son O(n²).
"""


def ordenar_puntajes(datos):
    """
    TODO: Ordenar puntajes descendente.
    Algoritmo elegido: Quick Sort
    """

    if len(datos) <= 1:
        return datos

    pivote = datos[len(datos) // 2]["puntaje"]

    mayores = [x for x in datos if x["puntaje"] > pivote]
    iguales = [x for x in datos if x["puntaje"] == pivote]
    menores = [x for x in datos if x["puntaje"] < pivote]

    return ordenar_puntajes(mayores) + iguales + ordenar_puntajes(menores)



# ═══════════════════════════════════════════════════════════════════════════════
# CASO 10 (1.7): Biblioteca Universitaria
# ═══════════════════════════════════════════════════════════════════════════════

"""
CONTEXTO:
---------
La biblioteca organiza libros por código ISBN.

Cada ISBN tiene entre 10 y 13 dígitos.

REGLAS:
  R1) Hay millones de libros.
  R2) El rango de valores posibles es enorme.
  R3) Se busca rendimiento cercano a lineal.

ANÁLISIS:
  1. ¿Qué algoritmo eliges? Radix Sort
  2. Complejidad temporal: O(d * (n + b))
  3. Complejidad espacial: O(n + b)

¿Por qué no los otros?
- Counting Sort no sirve por rango enorme.
- Quick, Merge y Heap son O(n log n).
- Bubble e Insertion son O(n²).
"""


def counting_sort_por_digito(arr, exp):

    n = len(arr)

    salida = [0] * n
    conteo = [0] * 10

    for num in arr:

        indice = (num // exp) % 10

        conteo[indice] += 1

    for i in range(1, 10):
        conteo[i] += conteo[i - 1]

    for i in range(n - 1, -1, -1):

        num = arr[i]
        indice = (num // exp) % 10

        conteo[indice] -= 1
        salida[conteo[indice]] = num

    return salida


def ordenar_isbn(lista):
    """
    TODO: Ordenar ISBN.
    Algoritmo elegido: Radix Sort
    """

    arr = lista.copy()

    maximo = max(arr)

    exp = 1

    while maximo // exp > 0:

        arr = counting_sort_por_digito(arr, exp)

        exp *= 10

    return arr



# ═══════════════════════════════════════════════════════════════════════════════
# CÓDIGO DE PRUEBA
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":

    print("=" * 60)
    print("PRUEBAS DEL QUIZ DE ORDENAMIENTO")
    print("=" * 60)


    # ── CASO 4 ──

    print("\n--- CASO 4: Canciones ---")

    canciones = [
        {"id": 1, "titulo": "A", "reproducciones": 5000},
        {"id": 2, "titulo": "B", "reproducciones": 12000},
        {"id": 3, "titulo": "C", "reproducciones": 8000},
    ]

    resultado = ordenar_canciones(canciones)

    for c in resultado:
        print(c)


    # ── CASO 5 ──

    print("\n--- CASO 5: Votos ---")

    votos = [
        {"mesa": 3, "candidato": "Ana"},
        {"mesa": 1, "candidato": "Luis"},
        {"mesa": 2, "candidato": "Pedro"},
    ]

    resultado = ordenar_votos(votos)

    for v in resultado:
        print(v)


    # ── CASO 6 ──

    print("\n--- CASO 6: Pacientes ---")

    pacientes = [
        (1, 3, "Carlos"),
        (2, 1, "Ana"),
        (3, 2, "Pedro"),
    ]

    resultado = ordenar_pacientes(pacientes)

    for p in resultado:
        print(p)


    # ── CASO 7 ──

    print("\n--- CASO 7: Productos ---")

    productos = [
        {"id": 1, "precio": 50000},
        {"id": 2, "precio": 10000},
        {"id": 3, "precio": 70000},
    ]

    resultado = ordenar_productos(productos)

    for p in resultado:
        print(p)


    # ── CASO 8 ──

    print("\n--- CASO 8: Temperaturas ---")

    temperaturas = [
        ("S1", 30),
        ("S2", -5),
        ("S3", 15),
    ]

    resultado = ordenar_temperaturas(temperaturas)

    for t in resultado:
        print(t)


    # ── CASO 9 ──

    print("\n--- CASO 9: Puntajes ---")

    puntajes = [
        {"jugador": "Carlos", "puntaje": 900},
        {"jugador": "Ana", "puntaje": 1200},
        {"jugador": "Luis", "puntaje": 700},
    ]

    resultado = ordenar_puntajes(puntajes)

    for p in resultado:
        print(p)


    # ── CASO 10 ──

    print("\n--- CASO 10: ISBN ---")

    isbn = [9876543210, 1234567890, 5555555555]

    resultado = ordenar_isbn(isbn)

    print(resultado)