  TALLER: ANÁLISIS DE ALGORITMOS
        Algoritmos y Programación 4
═══════════════════════════════════════════════════════════════════════════════

INSTRUCCIONES GENERALES:
------------------------
- Entregar archivo .py con todas las secciones resueltas
- El código debe ejecutar sin errores

DISTRIBUCIÓN:
- Sección A: Análisis teórico (1.0)         
- Sección B: Investigación (0.5)             
- Sección C: Resolver y optimizar (2.0)      
- Sección D: Proponer y justificar (1.5)     

═══════════════════════════════════════════════════════════════════════════════
"""

import time
import random


# ═══════════════════════════════════════════════════════════════════════════════
#                    SECCIÓN A: ANÁLISIS TEÓRICO (1.0)
#                         
# ═══════════════════════════════════════════════════════════════════════════════

"""
PUNTO A.1 (0.4): Clasificar complejidad

Para cada función, escribe:
  - La complejidad Big-O
  - UNA línea explicando por qué

Escribe tus respuestas como comentarios debajo de cada función.



def alpha(lista):
    total = 0
    for x in lista:
        total += x
    promedio = total / len(lista)
    return promedio

# Complejidad: O(?)
# Porque: _______
#complejidad O(n) porque recorre toda la lista una vez para sumar los elementos y luego hace una operación de división que es O(1).



def beta(lista):
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i] == lista[j] and i != j:
                return True
    return False

# Complejidad: O(?)
# Porque: ___
#complejidad O(n^2) porque tiene dos bucles anidados que recorren la lista completa, comparando cada elemento con todos los demás.  




def gamma(n):
    if n <= 1:
        return 1
    return gamma(n // 2) + 1

# Complejidad: O(?)
# Porque: ___
#complejidad O(log n) porque la función se llama a sí misma con n dividido por 2 en cada llamada, lo que reduce el tamaño del problema a la mitad en cada paso. Esto es característico de algoritmos con complejidad logarítmica.



def delta(lista):
    resultado = set()
    for x in lista:
        resultado.add(x)
    return resultado

# Complejidad: O(?)
# Porque: ___
#complejidad O(n) porque recorre toda la lista una vez para agregar cada elemento a un conjunto. La operación de agregar a un conjunto es O(1) en promedio, por lo que el tiempo total es proporcional al tamaño de la lista.


def epsilon(lista):
    for x in lista:
        if x in lista:
            pass

# Complejidad: O(?)
# Porque: ___
# PISTA: ¿cuánto cuesta `x in lista`?
#complejidad O(n^2) porque el bucle recorre cada elemento de la lista y para cada elemento, la operación `x in lista` también recorre la lista para verificar si el elemento existe, lo que resulta en un tiempo de ejecución proporcional al cuadrado del tamaño de la lista.


def zeta(n):
    for i in range(n):
        j = 1
        while j < n:
            j *= 3

# Complejidad: O(?)
# Porque: ___
#complejidad O(n log n) porque el bucle externo recorre n veces, y el bucle interno tiene una complejidad logarítmica debido a que j se multiplica por 3 en cada iteración, lo que hace que el número de iteraciones del bucle interno sea proporcional a log base 3 de n. Por lo tanto, la complejidad total es O(n log n).


def eta(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izq = eta(lista[:medio])
    der = eta(lista[medio:])
    return izq + der

# Complejidad: O(?)
# Porque: ___
# PISTA: ¿cuánto cuesta lista[:medio]?
#complejidad O(n log n) porque la función se divide recursivamente en dos mitades, lo que genera un árbol de llamadas con una profundidad de log n. En cada nivel del árbol, se procesan todos los elementos de la lista (O(n)) para combinar los resultados, lo que da como resultado una complejidad total de O(n log n).


def theta(n):
    i = 1
    while i * i <= n:
        i += 1
    return i

# Complejidad: O(?)
# Porque: ___
#complejidad O(√n) porque el bucle while se ejecuta mientras i * i sea menor o igual a n, lo que significa que i crece hasta alcanzar la raíz cuadrada de n.

"""
PUNTO A.2 (0.3): Ordenar de menor a mayor complejidad

Ordena las siguientes complejidades de la MÁS RÁPIDA a la MÁS LENTA:

O(n!), O(1), O(n log n), O(2^n), O(n²), O(log n), O(n), O(n³), O(√n)

Tu respuesta (de más rápida a más lenta):
1. O(1)
2. O(log n)
3. O(√n)
4. O(n)
5. O(n log n)
6. O(n²)
7. O(n³)
8. O(2^n)
9. O(n!)
"""


PUNTO A.3 (0.3): Verdadero o Falso

Escribe V o F y justifica brevemente las falsas.

1. __ F __ O(2n) es más lento que O(n)  
   Justificación: __porque en notación Big O las constantes no importan, entonces O(2n) es equivalente a O(n)__  

2. __ F __ Un algoritmo O(n²) siempre es más lento que uno O(n log n)  
   Justificación: __porque no siempre, para valores pequeños de n puede ser más rápido dependiendo de constantes; solo para n grande O(n²) crece más__  

3. __ F __ Si un algoritmo tiene un for de n y dentro un for de 5,  
       su complejidad es O(n²)  
   Justificación: __porque el for interno es constante (5), entonces la complejidad es O(5n) = O(n)__  

4. __ F __ `x in set` tiene la misma complejidad que `x in list`  
   Justificación: __porque en un set es O(1) en promedio y en una lista es O(n)__  

5. __ F __ Un algoritmo recursivo que se llama a sí mismo 2 veces  
       siempre es O(2^n)  
   Justificación: __porque depende de cómo se reduce el problema; no siempre genera crecimiento exponencial__  

6. __ F __ O(n) + O(n²) = O(n³)  
   Justificación: __porque se toma el término dominante, entonces es O(n²)__  

7. __ V __ La complejidad espacial de un algoritmo in-place es O(1)  
   Justificación: __  

8. __ V __ Memoización mejora la complejidad temporal pero empeora la espacial  
   Justificación: __  


# ═══════════════════════════════════════════════════════════════════════════════
#                    SECCIÓN B: INVESTIGACIÓN (0.5)
#                         
# ═══════════════════════════════════════════════════════════════════════════════

"""
PUNTO B.1 (0.25): Complejidad de operaciones de Python

┌──────────────────────────────┬──────────────┬──────────────┐
│ Operación                    │ Lista []     │ Set/Dict {}  │
├──────────────────────────────┼──────────────┼──────────────┤
│ Acceder por índice [i]       │ O(1)         │ N/A          │
│ Buscar elemento (x in ...)   │ O(n)         │ O(1)         │
│ Agregar al final (.append)   │ O(1)         │ O(1) (.add)  │
│ Insertar al inicio           │ O(n)         │ N/A          │
│ Eliminar por valor (.remove) │ O(n)         │ O(1)         │
│ Obtener longitud (len)       │ O(1)         │ O(1)         │
│ Ordenar (.sort / sorted)     │ O(n log n)   │ N/A          │
│ Copiar (.copy / [:])         │ O(n)         │ O(n)         │
└──────────────────────────────┴──────────────┴──────────────┘


Justificación:

- Acceder por índice: es O(1) porque las listas usan acceso directo por posición.
- Buscar elemento en lista: es O(n) porque recorre elemento por elemento.
- Buscar en set/dict: es O(1) en promedio por tablas hash.
- Append / add: O(1) amortizado porque agrega al final sin recorrer.
- Insertar al inicio: O(n) porque desplaza todos los elementos.
- Remove en lista: O(n) porque primero busca el elemento.
- Remove en set/dict: O(1) porque usa hash.
- len(): O(1) porque Python guarda el tamaño internamente.
- Ordenar: O(n log n) por algoritmo Timsort.
- Copiar: O(n) porque debe recorrer todos los elementos.


"""
PUNTO B.2 (0.25): Caso real

Investiga y responde:

1. ¿Qué algoritmo de ordenamiento usa Python internamente (sorted/list.sort)?
   Respuesta: Timsort

2. ¿Cuál es su complejidad en el mejor, peor y caso promedio?
   Mejor: O(n)
   Peor: O(n log n)
   Promedio: O(n log n)

3. ¿Por qué Python eligió ese algoritmo y no Quick Sort?
   Respuesta: Timsort es un algoritmo de ordenamiento estable y eficiente en la práctica, especialmente para datos parcialmente ordenados. Quick Sort, aunque tiene un buen desempeño promedio, no es estable y puede tener un rendimiento variable en el peor caso.
"""

import time
import random
import bisect


# ═══════════════════════════════════════════════════════════════════════════════
#                SECCIÓN C: RESOLVER Y OPTIMIZAR (2.0)
# ═══════════════════════════════════════════════════════════════════════════════

"""
En cada problema:
1. Analiza la versión LENTA y escribe su complejidad
2. Implementa la versión RÁPIDA
3. Escribe la complejidad de tu versión
4. Ejecuta las pruebas para verificar que funciona
"""


# ─── PROBLEMA C.1 (0.4): Elementos únicos ────────────────────────────────────

def unicos_lento(lista):
    """
    Retorna lista sin duplicados manteniendo el orden.
    COMPLEJIDAD: O(n²)
    """
    resultado = []
    for x in lista:
        if x not in resultado:
            resultado.append(x)
    return resultado


def unicos_rapido(lista):
    """
    Misma funcionalidad pero más eficiente.
    USA un set auxiliar para búsqueda O(1).

    COMPLEJIDAD: O(n)
    """
    resultado = []
    vistos = set()

    for x in lista:
        if x not in vistos:
            resultado.append(x)
            vistos.add(x)

    return resultado


# ─── PROBLEMA C.2 (0.4): Frecuencia del más común ────────────────────────────

def mas_comun_lento(lista):
    """
    Retorna el elemento que más se repite y cuántas veces.
    COMPLEJIDAD: O(n²)
    """
    max_elem = None
    max_count = 0
    for x in lista:
        count = 0
        for y in lista:
            if y == x:
                count += 1
        if count > max_count:
            max_count = count
            max_elem = x
    return max_elem, max_count


def mas_comun_rapido(lista):
    """
    Misma funcionalidad usando diccionario contador.

    COMPLEJIDAD: O(n)
    """
    contador = {}

    for x in lista:
        contador[x] = contador.get(x, 0) + 1

    max_elem = None
    max_count = 0

    for elemento, frecuencia in contador.items():
        if frecuencia > max_count:
            max_elem = elemento
            max_count = frecuencia

    return max_elem, max_count


# ─── PROBLEMA C.3 (0.4): Pares que suman K ───────────────────────────────────

def pares_suma_lento(lista, k):
    """
    Retorna todos los pares (i, j) donde lista[i] + lista[j] == k.
    COMPLEJIDAD: O(n²)
    """
    pares = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == k:
                pares.append((lista[i], lista[j]))
    return pares


def pares_suma_rapido(lista, k):
    """
    Misma funcionalidad usando set para buscar complementos.

    Estrategia:
    - Para cada x, el complemento es k - x
    - Si el complemento ya está en un set de "vistos", es un par

    COMPLEJIDAD: O(n)
    """
    pares = []
    vistos = set()

    for x in lista:
        complemento = k - x

        if complemento in vistos:
            pares.append((complemento, x))

        vistos.add(x)

    return pares


# ─── PROBLEMA C.4 (0.4): Anagramas ───────────────────────────────────────────

def son_anagramas_lento(palabra1, palabra2):
    """
    Verifica si dos palabras son anagramas (mismas letras, diferente orden).
    COMPLEJIDAD: O(n log n)
    """
    if len(palabra1) != len(palabra2):
        return False
    return sorted(palabra1) == sorted(palabra2)


def son_anagramas_rapido(palabra1, palabra2):
    """
    Misma funcionalidad sin ordenar.

    Estrategia: contar frecuencia de cada letra con diccionario.

    COMPLEJIDAD: O(n)
    """
    if len(palabra1) != len(palabra2):
        return False

    contador = {}

    for letra in palabra1:
        contador[letra] = contador.get(letra, 0) + 1

    for letra in palabra2:
        if letra not in contador:
            return False

        contador[letra] -= 1

        if contador[letra] < 0:
            return False

    return True


# ─── PROBLEMA C.5 (0.4): Subarray de suma máxima ─────────────────────────────

def max_subarray_lento(lista):
    """
    Encuentra la suma máxima de un subarray contiguo.
    Ejemplo: [-2, 1, -3, 4, -1, 2, 1, -5, 4] → 6 (subarray [4, -1, 2, 1])

    COMPLEJIDAD: O(n³)
    """
    n = len(lista)
    max_suma = lista[0]
    for i in range(n):
        for j in range(i, n):
            suma = 0
            for k in range(i, j + 1):
                suma += lista[k]
            max_suma = max(max_suma, suma)
    return max_suma


def max_subarray_rapido(lista):
    """
    Algoritmo de Kadane: un solo recorrido.

    Idea: mantener la suma actual. Si se vuelve negativa, reiniciar.
    - suma_actual = max(x, suma_actual + x)
    - max_suma = max(max_suma, suma_actual)

    COMPLEJIDAD: O(n)
    """
    suma_actual = lista[0]
    max_suma = lista[0]

    for x in lista[1:]:
        suma_actual = max(x, suma_actual + x)
        max_suma = max(max_suma, suma_actual)

    return max_suma


# ═══════════════════════════════════════════════════════════════════════════════
#                SECCIÓN D: PROPONER Y JUSTIFICAR (1.5)
# ═══════════════════════════════════════════════════════════════════════════════

"""
PUNTO D.1 (0.5): Diseñar un algoritmo

PROBLEMA: Sistema de autocompletado
Un buscador tiene una lista de 1 millón de palabras. Cuando el usuario
escribe las primeras letras, debe mostrar las 5 palabras que empiezan
con ese prefijo.

Ejemplo:
  palabras = ["python", "programar", "programa", "prueba", "pizza", ...]
  autocompletar("pro") → ["programar", "programa"]

Propón DOS soluciones con diferente complejidad:

SOLUCIÓN 1 (fuerza bruta):
  Descripción: recorrer toda la lista de palabras y revisar una por una
  cuáles empiezan con el prefijo dado. Se guardan máximo 5 resultados.
  Complejidad: O(n * m), donde n es la cantidad de palabras y m el tamaño del prefijo.
  Código:
"""


def autocompletar_v1(palabras, prefijo):
    """
    Versión fuerza bruta.
    COMPLEJIDAD: O(n * m)
    """
    resultados = []

    for palabra in palabras:
        if palabra.startswith(prefijo):
            resultados.append(palabra)

        if len(resultados) == 5:
            break

    return resultados


"""
SOLUCIÓN 2 (optimizada):
  Descripción: ordenar previamente las palabras y usar búsqueda binaria
  para encontrar la primera posición donde podrían aparecer las palabras
  con ese prefijo. Luego se toman máximo 5 coincidencias.
  Complejidad: O(log n + r * m), donde r es la cantidad de resultados revisados.
  ¿Qué estructura de datos usarías? Lista ordenada con búsqueda binaria.
  Código:
"""


def autocompletar_v2(palabras_ordenadas, prefijo):
    """
    Versión optimizada.
    PISTA: Si las palabras están ordenadas, puedes usar búsqueda binaria
    para encontrar dónde empiezan las que tienen el prefijo.

    COMPLEJIDAD: O(log n + r * m)
    """
    resultados = []
    inicio = bisect.bisect_left(palabras_ordenadas, prefijo)

    for i in range(inicio, len(palabras_ordenadas)):
        palabra = palabras_ordenadas[i]

        if palabra.startswith(prefijo):
            resultados.append(palabra)
        else:
            break

        if len(resultados) == 5:
            break

    return resultados


"""
PUNTO D.2 (0.5): Analizar un sistema real

ESCENARIO: Red social con 10 millones de usuarios.
Cada usuario tiene una lista de amigos (promedio 200 amigos).

Analiza la complejidad de estas operaciones y propón la mejor
estructura de datos para cada una:

1. Verificar si dos usuarios son amigos
   - Con lista de amigos: O(n)
   - Con set de amigos: O(1)
   - ¿Cuál elegirías? Elegiría set, porque permite buscar amigos mucho más rápido.

2. Encontrar amigos en común entre dos usuarios
   - Con listas: O(n * m)
   - Con sets: O(min(n, m))
   - ¿Cuál elegirías? Elegiría set, porque la intersección es más eficiente.

3. Sugerir "personas que quizás conozcas" (amigos de amigos que no son tus amigos)
   - Describe tu algoritmo: recorrer los amigos del usuario, luego recorrer los amigos
     de cada amigo, guardar los candidatos en un diccionario contador y excluir al usuario
     original y a los amigos que ya tiene.
   - Complejidad estimada: O(a * b), donde a es el número de amigos del usuario y b el
     promedio de amigos de cada amigo. Si ambos son 200, sería aproximadamente O(40.000).
   - ¿Es viable para 10M de usuarios? Sí, si se calcula por usuario bajo demanda o con
     procesos optimizados, pero no sería ideal recalcularlo para todos los usuarios al mismo tiempo.

4. Si cada usuario tiene en promedio 200 amigos y hay 10M de usuarios:
   - ¿Cuánta memoria ocupa almacenar TODAS las relaciones de amistad?
   - Total de relaciones guardadas: 10.000.000 * 200 = 2.000.000.000 relaciones.
   - Con lista: aproximadamente 2.000.000.000 * 8 = 16.000.000.000 bytes, es decir 16 GB.
   - Con set: aproximadamente puede ocupar más memoria por la tabla hash, por ejemplo
     2 o 3 veces más, cerca de 32 GB a 48 GB aproximadamente.
"""


"""
PUNTO D.3 (0.5): Reflexión y comparación

Escribe un párrafo (mínimo 5 líneas) respondiendo:

¿Por qué es importante analizar la complejidad de un algoritmo
ANTES de implementarlo? Da un ejemplo concreto de un caso donde
elegir el algoritmo incorrecto podría causar problemas reales
(tiempo de espera, costos de servidor, mala experiencia de usuario, etc.)

Tu respuesta:
Es importante analizar la complejidad de un algoritmo antes de implementarlo porque
permite saber si una solución será eficiente cuando aumente la cantidad de datos.
Un programa puede funcionar bien con pocos datos, pero volverse muy lento con miles
o millones de registros. Por ejemplo, en una red social, si para buscar amigos en común
se usan listas y se comparan todos contra todos, el sistema podría tardar demasiado
y generar una mala experiencia para el usuario. En cambio, si se usan sets, la búsqueda
es mucho más rápida y se reducen los tiempos de espera y los costos del servidor.
"""


# ═══════════════════════════════════════════════════════════════════════════════
#                         CÓDIGO DE PRUEBA
# ═══════════════════════════════════════════════════════════════════════════════

def medir(funcion, *args):
    inicio = time.time()
    resultado = funcion(*args)
    return resultado, time.time() - inicio


if __name__ == "__main__":
    print("=" * 70)
    print("     TALLER: ANÁLISIS DE ALGORITMOS - PRUEBAS SECCIÓN C")
    print("=" * 70)

    # ── C.1: Únicos ──────────────────────────────────────────────
    print("\n" + "─" * 70)
    print("C.1: ELEMENTOS ÚNICOS")
    print("─" * 70)

    for n in [1000, 5000, 10000]:
        lista = [random.randint(1, n // 2) for _ in range(n)]

        r1, t1 = medir(unicos_lento, lista)
        r2, t2 = medir(unicos_rapido, lista) if unicos_rapido(lista) is not None else (None, 0)

        print(f"  n={n:>6}: lento={t1:.4f}s  rápido={t2:.4f}s", end="")
        if r2 is not None:
            print(f"  ✓ correcto" if r1 == r2 else f"  ✗ DIFERENTE")
        else:
            print("  (sin implementar)")

    # ── C.2: Más común ───────────────────────────────────────────
    print("\n" + "─" * 70)
    print("C.2: ELEMENTO MÁS COMÚN")
    print("─" * 70)

    for n in [500, 2000, 5000]:
        lista = [random.randint(1, 20) for _ in range(n)]

        r1, t1 = medir(mas_comun_lento, lista)
        r2, t2 = medir(mas_comun_rapido, lista) if mas_comun_rapido(lista) is not None else (None, 0)

        print(f"  n={n:>6}: lento={t1:.4f}s  rápido={t2:.4f}s", end="")
        if r2 is not None:
            print(f"  ✓" if r1 == r2 else f"  resultado: {r1} vs {r2}")
        else:
            print("  (sin implementar)")

    # ── C.3: Pares que suman K ───────────────────────────────────
    print("\n" + "─" * 70)
    print("C.3: PARES QUE SUMAN K")
    print("─" * 70)

    for n in [500, 2000, 5000]:
        lista = [random.randint(1, 100) for _ in range(n)]
        k = 50

        r1, t1 = medir(pares_suma_lento, lista, k)
        r2, t2 = medir(pares_suma_rapido, lista, k) if pares_suma_rapido(lista, k) is not None else (None, 0)

        print(f"  n={n:>6}: lento={t1:.4f}s  rápido={t2:.4f}s", end="")
        if r2 is not None:
            print(f"  pares encontrados: {len(r1)} vs {len(r2)}")
        else:
            print("  (sin implementar)")

    # ── C.4: Anagramas ───────────────────────────────────────────
    print("\n" + "─" * 70)
    print("C.4: ANAGRAMAS")
    print("─" * 70)

    casos_anagramas = [
        ("listen", "silent", True),
        ("hello", "world", False),
        ("anagram", "nagaram", True),
        ("python", "typhon", True),
        ("abc", "abcd", False),
    ]

    for p1, p2, esperado in casos_anagramas:
        r_lento = son_anagramas_lento(p1, p2)
        r_rapido = son_anagramas_rapido(p1, p2) if son_anagramas_rapido(p1, p2) is not None else "N/A"
        marca = "✓" if r_rapido == esperado else "✗"
        print(f"  {marca} '{p1}' vs '{p2}': lento={r_lento}, rápido={r_rapido}, esperado={esperado}")

    # ── C.5: Subarray máximo ─────────────────────────────────────
    print("\n" + "─" * 70)
    print("C.5: SUBARRAY DE SUMA MÁXIMA")
    print("─" * 70)

    casos_subarray = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [1, 2, 3, 4, 5],
        [-1, -2, -3, -4],
        [5, -9, 6, -2, 3],
    ]

    for lista in casos_subarray:
        r_lento = max_subarray_lento(lista)
        r_rapido = max_subarray_rapido(lista)
        marca = "✓" if r_rapido == r_lento else "✗"
        print(f"  {marca} {lista} → lento={r_lento}, rápido={r_rapido}")

    for n in [500, 2000, 5000]:
        lista = [random.randint(-50, 50) for _ in range(n)]
        r1, t1 = medir(max_subarray_lento, lista)
        r2, t2 = medir(max_subarray_rapido, lista) if max_subarray_rapido(lista) is not None else (None, 0)
        print(f"  n={n:>6}: lento={t1:.4f}s  rápido={t2:.4f}s")

    # ── D.1: Autocompletar ───────────────────────────────────────
    print("\n" + "─" * 70)
    print("D.1: AUTOCOMPLETAR")
    print("─" * 70)

    palabras = [f"palabra_{random.randint(1000, 9999)}" for _ in range(50000)]
    palabras.extend(["python", "programar", "programa", "prueba", "pizza",
                      "proyecto", "profesor", "promedio", "proceso", "producir"])
    random.shuffle(palabras)
    palabras_ord = sorted(palabras)

    for prefijo in ["pro", "pyt", "piz", "xyz"]:
        r1, t1 = medir(autocompletar_v1, palabras, prefijo) if autocompletar_v1(palabras, prefijo) is not None else (None, 0)
        r2, t2 = medir(autocompletar_v2, palabras_ord, prefijo) if autocompletar_v2(palabras_ord, prefijo) is not None else (None, 0)

        print(f"  Prefijo '{prefijo}': v1={t1:.4f}s  v2={t2:.4f}s", end="")
        if r1:
            print(f"  → {len(r1)} resultados")
        else:
            print("  (sin implementar)")



"""def tiene_duplicados(lista):
    n = (lista)
    for i in range(n):
        for j in range(i+1, n):
            if lista[i] == lista[j]:
                return True
    return False

""" que compila:
f(n) = 1 + n + 2n^2
"""

"""
Lista = [3, 5 , 2, 1, 3]
Algoritmo que me reciba una lista y retorne cual se repite más
"""
def elemento_mas_repetido(lista):
    max_elemento = lista[0]
    max_conteo = 0

    for i in range(len(lista)):
        conteo = 0
        for j in range(len(lista)):
            if lista[i] == lista(j):
                conteo += 1
        if conteo > max_conteo:
            max_conteo = conteo
            max_elemento = lista[i]
    
    return max_elemento, max_conteo

""" que compila:
f(n)= 2n^2+4n+3
O(n^2)
"""

def elemento_mas_repetido(lista):
    frecuencias = {}

    for elemento in lista:
        if elemento in frecuencias:
            frecuencias[elemento] += 1
        else:
            frecuencias[elemento] = 0
    max_elemento = 0
    max_conteo = 0

    for elemento, conteo in frecuencias:
        if conteo > max_conteo:
            max_conteo = conteo
            max_elemento = elemento

    return max_elemento, max_conteo

"""
que compila:
f(n) = 4 + 4n + 3n = 7n + 4
O(n)
"""

"""
Algoritmo que me diga si en la lista si hay 3 numeros que me suman cero y devuelve true 
o false
"""

def elemento_mas_repetido(lista):
    n = len(lista)

    for i in range(i+1, n):
        for k in range(j+1, n):
            if lista[i] + lista[j] + lista[k] == 0
                return True
            
    return False

"""
Que compila:
f(n) = 1 + n + 2n^3
O(n^3)
"""

"""Como mejorar este codigodddd """
