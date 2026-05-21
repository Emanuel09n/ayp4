```python id="y5j6e2"
# ============================================================
# CASOS TIPO QUIZ - ALGORITMOS DE ORDENAMIENTO
# TODOS RESUELTOS
# ============================================================


# ============================================================
# CASO 1 — Hospital y pacientes críticos
# ============================================================

"""
Contexto del problema:

Un hospital tiene una lista de pacientes ordenada
por hora de llegada.

Ahora necesita ordenarlos por nivel de gravedad.

IMPORTANTE:
Si dos pacientes tienen la misma gravedad,
deben mantener el orden de llegada original.

Datos clave:
- 300,000 pacientes
- Gravedad entre 1 y 10
- Enteros pequeños
- Estabilidad obligatoria
"""

"""
RESPUESTA:

Algoritmo:
COUNTING SORT

Razón:
- El rango es pequeño (1-10)
- Son enteros
- Necesita estabilidad
- Muy eficiente

Complejidad:
O(n + k)
"""


# ============================================================
# CASO 2 — Satélites de la NASA
# ============================================================

"""
Contexto del problema:

La NASA recibe señales numéricas de satélites.
Cada señal tiene exactamente 15 dígitos.

Necesitan ordenarlas rápidamente.

Datos clave:
- 10 millones de señales
- Longitud fija
- Mucha memoria disponible
"""

"""
RESPUESTA:

Algoritmo:
RADIX SORT

Razón:
- Funciona excelente con dígitos
- Longitud fija
- Más rápido que algoritmos comparativos

Complejidad:
O(d(n+k))
"""


# ============================================================
# CASO 3 — App de citas (Tinder)
# ============================================================

"""
Contexto del problema:

Una app de citas necesita ordenar perfiles
por porcentaje de compatibilidad.

El algoritmo debe ser MUY rápido en promedio
porque trabaja en tiempo real.

Datos clave:
- 5 millones de perfiles
- Memoria limitada
- No importa estabilidad
"""

"""
RESPUESTA:

Algoritmo:
QUICK SORT

Razón:
- Muy rápido en promedio
- Usa poca memoria
- No se necesita estabilidad

Complejidad promedio:
O(n log n)

Peor caso:
O(n²)
"""


# ============================================================
# CASO 4 — Cámaras de tránsito
# ============================================================

"""
Contexto del problema:

Una ciudad almacena velocidades de carros
captadas por cámaras.

Las velocidades van entre 0 y 220 km/h.

Datos clave:
- 50 millones de registros
- Enteros
- Rango pequeño
"""

"""
RESPUESTA:

Algoritmo:
COUNTING SORT

Razón:
- Rango pequeño
- Muchísimos datos
- Muy eficiente

Complejidad:
O(n+k)
"""


# ============================================================
# CASO 5 — Spotify
# ============================================================

"""
Contexto del problema:

Spotify ordena canciones por reproducciones.

Si dos canciones tienen las mismas reproducciones,
deben mantener el orden de lanzamiento.

Datos clave:
- 20 millones de canciones
- Estabilidad obligatoria
- El peor caso importa
"""

"""
RESPUESTA:

Algoritmo:
MERGE SORT

Razón:
- Es estable
- Garantiza O(n log n)
- Rendimiento consistente

Complejidad:
O(n log n)
"""


# ============================================================
# CASO 6 — Plataforma blockchain
# ============================================================

"""
Contexto del problema:

Una plataforma blockchain ordena transacciones.

El sistema NO puede arriesgarse
a tiempos impredecibles.

Datos clave:
- Memoria limitada
- El peor caso importa
"""

"""
RESPUESTA:

Algoritmo:
HEAP SORT

Razón:
- Garantiza O(n log n)
- Usa poca memoria
- Mejor control del peor caso

Complejidad:
O(n log n)
"""


# ============================================================
# CASO 7 — Netflix
# ============================================================

"""
Contexto del problema:

Netflix necesita ordenar películas.

La mayoría YA están casi ordenadas,
porque cada hora solo cambian algunas posiciones.

Datos clave:
- Lista casi ordenada
- Datos pequeños cambios
"""

"""
RESPUESTA:

Algoritmo:
INSERTION SORT

Razón:
- Excelente para listas casi ordenadas
- Puede acercarse a O(n)

Complejidad:
Mejor caso: O(n)
Peor caso: O(n²)
"""


# ============================================================
# CASO 8 — Banco y auditoría
# ============================================================

"""
Contexto del problema:

Un banco necesita ordenar transacciones sospechosas.

NO puede permitirse tiempos impredecibles.

Datos clave:
- 1 millón de registros
- Memoria suficiente
- El peor caso importa
"""

"""
RESPUESTA:

Algoritmo:
MERGE SORT

Razón:
- Garantiza O(n log n)
- Rendimiento estable
- Seguro para auditorías

Complejidad:
O(n log n)
"""


# ============================================================
# CASO 9 — Red social
# ============================================================

"""
Contexto del problema:

Una red social ordena publicaciones
por cantidad de likes.

Los likes van de 0 a 999.

Datos clave:
- Enteros
- Rango pequeño
"""

"""
RESPUESTA:

Algoritmo:
COUNTING SORT

Razón:
- El rango es pequeño
- Son enteros
- Más eficiente que QuickSort

Complejidad:
O(n+k)
"""


# ============================================================
# CASO 10 — Aeropuerto
# ============================================================

"""
Contexto del problema:

Un aeropuerto ordena vuelos
por hora de salida.

Si dos vuelos salen a la misma hora,
deben mantener prioridad original.

Datos clave:
- Estabilidad obligatoria
"""

"""
RESPUESTA:

Algoritmo:
MERGE SORT

Razón:
- Necesita estabilidad
- Mantiene el orden original
- O(n log n)

NO usar:
HeapSort o QuickSort
porque NO son estables.
"""


# ============================================================
# CASO 11 — Universidad
# ============================================================

"""
Contexto del problema:

La universidad necesita ordenar notas finales.

Si dos estudiantes tienen la misma nota,
deben conservar el orden original.

Datos clave:
- 200 estudiantes
- Notas entre 0 y 100
- Enteros
"""

"""
RESPUESTA:

Algoritmo:
COUNTING SORT

Razón:
- Rango pequeño
- Datos enteros
- Necesita estabilidad

Complejidad:
O(n+k)
"""


# ============================================================
# CASO 12 — Servidor de producción
# ============================================================

"""
Contexto del problema:

Un servidor necesita ordenar archivos por tamaño.

Debe terminar SIEMPRE antes de 30 minutos.

Datos clave:
- 50,000 archivos
- Tamaños impredecibles
- El peor caso importa
"""

"""
RESPUESTA:

Algoritmo:
MERGE SORT o HEAP SORT

Razón:
- Garantizan O(n log n)
- Rendimiento predecible

NO usar:
QuickSort

Porque:
Puede caer en O(n²)
"""


# ============================================================
# CASO 13 — Lista pequeña
# ============================================================

"""
Contexto del problema:

Necesitas ordenar una lista de solo 15 números.

Datos clave:
- Lista pequeña
- Importa simplicidad
"""

"""
RESPUESTA:

Algoritmo:
BUBBLE SORT o INSERTION SORT

Razón:
- Son simples
- Funcionan bien en listas pequeñas

Mejor opción:
INSERTION SORT
porque suele hacer menos intercambios.
"""


# ============================================================
# CASO 14 — Códigos postales
# ============================================================

"""
Contexto del problema:

Correos nacionales necesita ordenar
millones de códigos postales.

Todos tienen exactamente 6 dígitos.

Datos clave:
- Longitud fija
- Datos numéricos
"""

"""
RESPUESTA:

Algoritmo:
RADIX SORT

Razón:
- Excelente para números por dígitos
- Longitud fija
- Muy eficiente

Complejidad:
O(d(n+k))
"""


# ============================================================
# CASO 15 — E-commerce
# ============================================================

"""
Contexto del problema:

Una tienda online ordena productos
por precio.

Importa mucho la velocidad promedio.

Datos clave:
- Datos aleatorios
- No importa estabilidad
"""

"""
RESPUESTA:

Algoritmo:
QUICK SORT

Razón:
- Muy rápido en promedio
- Excelente rendimiento práctico

Complejidad promedio:
O(n log n)
"""
```
