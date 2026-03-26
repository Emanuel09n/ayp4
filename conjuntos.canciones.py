# =========================================================
# EJEMPLO 1: CANCIONES (OPERACIONES BÁSICAS DE CONJUNTOS)
# =========================================================

# Definición de conjuntos (no permiten elementos repetidos)
canciones_juan = {"PH", "VVS1", "TRATRA", "CHUPETEO"}
canciones_maria = {"PH", "TRATRA", "SINNOMBRE", "VSS1"}

# INTERSECCIÓN: elementos que están en ambos conjuntos
# Método: intersection() o operador &
compartidas_clases = canciones_juan.intersection(canciones_maria)
print("Canciones que les gustan a ambos:", compartidas_clases)

# DIFERENCIA: elementos que están en el segundo conjunto pero NO en el primero
# Aquí: canciones que María tiene y Juan no → recomendación para Juan
recomendaciones_para_juan = canciones_maria.difference(canciones_juan)
print("Canciones que Juan no tiene:", recomendaciones_para_juan)

# DIFERENCIA inversa: canciones que Juan tiene y María no
solo_juan = canciones_juan - canciones_maria
print("Canciones solo de Juan:", solo_juan)

# UNIÓN: todos los elementos sin repetir
# Método: union() o operador |
todas = canciones_juan | canciones_maria
print("Todas las canciones:", todas)

# DIFERENCIA SIMÉTRICA: elementos que están en uno u otro pero NO en ambos
# Método: symmetric_difference() o operador ^
diferentes = canciones_juan ^ canciones_maria
print("Canciones diferentes:", diferentes)


# =========================================================
# EJEMPLO 2: ESTUDIANTES EN MATERIAS
# =========================================================

# Conjuntos de estudiantes por materia
redes = {"Pablo", "camila", "Diego", "Karla", "Esteban"}
base_datos = {"Carlos","Diana","Elena","Fernando","Gabriela","Hector","Isabel","Jorge","Karla","Luis"}
algoritmos = {"Ana", "Pablo", "Sofia", "Diego", "Laura", "Juan", "Maria", "Pedro", "Luis", "Karla"}

# DIFERENCIA MÚLTIPLE:
# Estudiantes que están SOLO en redes (no en base_datos ni algoritmos)
solo_redes = redes - base_datos - algoritmos

# Estudiantes que están SOLO en base de datos
solo_base = base_datos - redes - algoritmos

# Estudiantes que están SOLO en algoritmos
solo_algoritmos = algoritmos - redes - base_datos

# UNIÓN de los tres resultados:
# todos los estudiantes que están en UNA SOLA materia
resultado = solo_redes | solo_base | solo_algoritmos

print("Estudiantes que están solo en una materia:", resultado)


# =========================================================
# EJEMPLO 3: INTERSECCIONES ENTRE MATERIAS
# =========================================================

# Estudiantes que están en las 3 materias
en_todas = redes & base_datos & algoritmos
print("Estudiantes en todas las materias:", en_todas)

# Estudiantes que están en al menos dos materias
en_redes_y_algoritmos = redes & algoritmos
print("Redes y Algoritmos:", en_redes_y_algoritmos)


# =========================================================
# EJEMPLO 4: SUBCONJUNTOS
# =========================================================

# Verifica si TODOS los elementos de algoritmos están en base_datos
# Operador: <=
if algoritmos <= base_datos:
    print("Algoritmos es un subconjunto de base de datos")
else:
    print("Algoritmos NO es subconjunto de base de datos")


# =========================================================
# EJEMPLO 5: SIMILITUD DE JACCARD
# =========================================================

# Fórmula:
# J(A,B) = |A ∩ B| / |A ∪ B|

interseccion = len(canciones_juan & canciones_maria)
union = len(canciones_juan | canciones_maria)

if union == 0:
    jaccard = 0
else:
    jaccard = interseccion / union

print("Similitud de Jaccard (canciones):", round(jaccard, 3))


# =========================================================
# EJEMPLO 6: JACCARD ENTRE MATERIAS
# =========================================================

# Comparar similitud entre estudiantes de redes y algoritmos
inter = len(redes & algoritmos)
uni = len(redes | algoritmos)

jaccard_estudiantes = inter / uni
print("Jaccard Redes vs Algoritmos:", round(jaccard_estudiantes, 3))
    




      

