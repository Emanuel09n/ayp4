# =========================================
# EJERCICIOS DE CONJUNTOS EN PYTHON
# Incluye: unión, intersección, diferencia,
# diferencia simétrica, subconjuntos,
# Jaccard en conjuntos y Jaccard en textos
# Basado en las ideas de tu código. :contentReference[oaicite:0]{index=0}
# =========================================


# -------------------------------------------------
# EJERCICIO 1: SERIES VISTAS POR DOS PERSONAS
# -------------------------------------------------
series_andres = {"Dark", "Breaking Bad", "Friends", "Narcos"}
series_luisa = {"Dark", "Friends", "The Office", "Elite"}

print("EJERCICIO 1")
print("En común:", series_andres.intersection(series_luisa))
print("Solo Andrés:", series_andres.difference(series_luisa))
print("Solo Luisa:", series_luisa.difference(series_andres))
print("Todas sin repetir:", series_andres.union(series_luisa))
print("Diferencia simétrica:", series_andres.symmetric_difference(series_luisa))
print()


# -------------------------------------------------
# EJERCICIO 2: ESTUDIANTES EN CURSOS
# -------------------------------------------------
python = {"Ana", "Luis", "Carlos", "María", "Pedro"}
java = {"Luis", "Pedro", "Sofía", "Camila", "Ana"}

print("EJERCICIO 2")
print("Estudiantes en ambos cursos:", python & java)
print("Estudiantes solo en Python:", python - java)
print("Estudiantes solo en Java:", java - python)
print("Todos los estudiantes:", python | java)
print()


# -------------------------------------------------
# EJERCICIO 3: CLIENTES DE DOS TIENDAS
# -------------------------------------------------
tienda_ropa = {"Juan", "Ana", "Camilo", "Laura"}
tienda_zapatos = {"Ana", "Laura", "Pedro", "Diana"}

print("EJERCICIO 3")
print("Clientes compartidos:", tienda_ropa & tienda_zapatos)
print("Clientes exclusivos de ropa:", tienda_ropa - tienda_zapatos)
print("Clientes exclusivos de zapatos:", tienda_zapatos - tienda_ropa)
print("Clientes exclusivos en una sola tienda:", tienda_ropa ^ tienda_zapatos)
print()


# -------------------------------------------------
# EJERCICIO 4: SUBCONJUNTOS
# -------------------------------------------------
numeros_pares = {2, 4, 6}
numeros = {1, 2, 3, 4, 5, 6, 7, 8}

print("EJERCICIO 4")
print("¿pares es subconjunto de numeros?", numeros_pares <= numeros)
print("¿numeros contiene a pares?", numeros >= numeros_pares)
print("¿son iguales?", numeros_pares == numeros)
print()


# -------------------------------------------------
# EJERCICIO 5: CATÁLOGO DE VIDEOJUEGOS POR GÉNERO
# -------------------------------------------------
catalogo_juegos = {
    "FIFA": {"Deportes", "Multijugador"},
    "Call of Duty": {"Acción", "Shooter", "Multijugador"},
    "Minecraft": {"Aventura", "Creatividad", "Multijugador"},
    "The Last of Us": {"Acción", "Aventura", "Drama"},
    "EA FC": {"Deportes", "Multijugador"},
    "Valorant": {"Acción", "Shooter", "Multijugador"},
    "Stardew Valley": {"Simulación", "Aventura", "Creatividad"}
}

print("EJERCICIO 5")
juegos = list(catalogo_juegos.keys())

for i in range(len(juegos)):
    for j in range(i + 1, len(juegos)):
        juego1 = juegos[i]
        juego2 = juegos[j]
        comunes = catalogo_juegos[juego1].intersection(catalogo_juegos[juego2])
        if len(comunes) >= 2:
            print(f"{juego1} y {juego2} comparten 2 o más géneros: {comunes}")
print()


# -------------------------------------------------
# EJERCICIO 6: RECOMENDAR JUEGOS SEGÚN GUSTOS
# -------------------------------------------------
gustos_usuario = {"Acción", "Shooter", "Multijugador"}

print("EJERCICIO 6")
recomendaciones = {}

for juego, generos in catalogo_juegos.items():
    comunes = gustos_usuario.intersection(generos)
    if comunes:
        porcentaje = len(comunes) / len(gustos_usuario) * 100
        recomendaciones[juego] = porcentaje

print("Porcentaje de afinidad por juego:")
for juego, porcentaje in recomendaciones.items():
    print(juego, "->", f"{porcentaje:.2f}%")
print()


# -------------------------------------------------
# EJERCICIO 7: TODOS LOS GÉNEROS SIN REPETIR
# -------------------------------------------------
print("EJERCICIO 7")
generos_unicos = set()

for generos in catalogo_juegos.values():
    generos_unicos.update(generos)

print("Géneros únicos:", generos_unicos)
print()


# -------------------------------------------------
# EJERCICIO 8: AGRUPAR JUEGOS POR GÉNERO
# -------------------------------------------------
print("EJERCICIO 8")
juegos_por_genero = {}

for juego, generos in catalogo_juegos.items():
    for genero in generos:
        if genero not in juegos_por_genero:
            juegos_por_genero[genero] = []
        juegos_por_genero[genero].append(juego)

for genero, lista_juegos in juegos_por_genero.items():
    print(genero, "->", lista_juegos)
print()


# -------------------------------------------------
# EJERCICIO 9: SIMILITUD DE JACCARD ENTRE DOS JUEGOS
# -------------------------------------------------
print("EJERCICIO 9")

def jaccard_juegos(juego1, juego2):
    generos1 = catalogo_juegos.get(juego1, set())
    generos2 = catalogo_juegos.get(juego2, set())

    if not generos1 or not generos2:
        return 0.0

    interseccion = generos1.intersection(generos2)
    union = generos1.union(generos2)

    return len(interseccion) / len(union)

print("FIFA vs EA FC:", jaccard_juegos("FIFA", "EA FC"))
print("Call of Duty vs Valorant:", jaccard_juegos("Call of Duty", "Valorant"))
print("Minecraft vs FIFA:", jaccard_juegos("Minecraft", "FIFA"))
print()


# -------------------------------------------------
# EJERCICIO 10: RECOMENDAR EL JUEGO MÁS PARECIDO A UNO DADO
# -------------------------------------------------
print("EJERCICIO 10")

def recomendar_similar(juego_base):
    mejor_juego = None
    mejor_valor = -1

    for juego in catalogo_juegos:
        if juego != juego_base:
            similitud = jaccard_juegos(juego_base, juego)
            if similitud > mejor_valor:
                mejor_valor = similitud
                mejor_juego = juego

    return mejor_juego, mejor_valor

juego_recomendado, valor = recomendar_similar("Call of Duty")
print("Juego más parecido a Call of Duty:", juego_recomendado, "con similitud", round(valor, 2))
print()


# -------------------------------------------------
# EJERCICIO 11: DOCUMENTOS CON ETIQUETAS
# -------------------------------------------------
doc1 = {"python", "datos", "análisis", "estadística"}
doc2 = {"python", "machinelearning", "datos", "modelos"}
doc3 = {"historia", "literatura", "ensayo"}

print("EJERCICIO 11")
print("Jaccard doc1-doc2:", len(doc1 & doc2) / len(doc1 | doc2))
print("Jaccard doc1-doc3:", len(doc1 & doc3) / len(doc1 | doc3))
print()


# -------------------------------------------------
# EJERCICIO 12: JACCARD ENTRE TEXTOS IGNORANDO STOPWORDS
# -------------------------------------------------
print("EJERCICIO 12")

STOPWORDS = {
    "el", "la", "los", "las", "un", "una", "unos", "unas",
    "de", "del", "al", "a", "en", "con", "por", "para",
    "y", "o", "que", "es", "son", "se", "su", "sus",
    "como", "pero", "más", "este", "esta", "estos", "estas"
}

def jaccard_textos(texto1, texto2):
    palabras1 = set(texto1.lower().split()) - STOPWORDS
    palabras2 = set(texto2.lower().split()) - STOPWORDS

    if not palabras1 or not palabras2:
        return 0.0

    interseccion = palabras1.intersection(palabras2)
    union = palabras1.union(palabras2)

    return len(interseccion) / len(union)

texto_a = "El gato negro duerme en el sofá de la sala"
texto_b = "El gato duerme en el sofá de la casa"

sim_texto = jaccard_textos(texto_a, texto_b)
print("Similitud:", round(sim_texto, 2))

if sim_texto > 0.6:
    print("Los textos son muy similares")
else:
    print("Los textos no son tan similares")
print()


# -------------------------------------------------
# EJERCICIO 13: DETECTOR SIMPLE DE COPIA
# -------------------------------------------------
print("EJERCICIO 13")

trabajo1 = "Python es un lenguaje muy usado en análisis de datos y programación"
trabajo2 = "Python es un lenguaje usado en programación y análisis de datos"

indice = jaccard_textos(trabajo1, trabajo2)
print("Índice de similitud:", round(indice, 2))

if indice > 0.6:
    print("Posible copia")
else:
    print("No parece copia")
print()


# -------------------------------------------------
# EJERCICIO 14: PALABRAS CLAVE COMPARTIDAS ENTRE NOTICIAS
# -------------------------------------------------
noticia1 = {"economia", "inflacion", "colombia", "mercado", "tasas"}
noticia2 = {"tasas", "banco", "economia", "mercado", "credito"}

print("EJERCICIO 14")
print("Palabras clave en común:", noticia1 & noticia2)
print("Palabras clave totales:", noticia1 | noticia2)
print("Jaccard:", len(noticia1 & noticia2) / len(noticia1 | noticia2))
print()


# -------------------------------------------------
# EJERCICIO 15: AMIGOS EN REDES SOCIALES
# -------------------------------------------------
amigos_instagram = {"Ana", "Luis", "Pedro", "Camila", "Laura"}
amigos_facebook = {"Pedro", "Laura", "Andrés", "Diana", "Luis"}

print("EJERCICIO 15")
print("Amigos en ambas redes:", amigos_instagram & amigos_facebook)
print("Solo en Instagram:", amigos_instagram - amigos_facebook)
print("Solo en Facebook:", amigos_facebook - amigos_instagram)
print("Amigos que están en una sola red:", amigos_instagram ^ amigos_facebook)
print()


# -------------------------------------------------
# EJERCICIO 16: HABILIDADES DE CANDIDATOS
# -------------------------------------------------
candidato1 = {"Python", "SQL", "Excel", "Power BI"}
candidato2 = {"Python", "R", "SQL", "Tableau"}

print("EJERCICIO 16")
print("Habilidades compartidas:", candidato1 & candidato2)
print("Jaccard candidatos:", len(candidato1 & candidato2) / len(candidato1 | candidato2))
print()


# -------------------------------------------------
# EJERCICIO 17: MÚSICA Y GÉNEROS FAVORITOS
# -------------------------------------------------
catalogo_canciones = {
    "Cancion1": {"Reggaeton", "Fiesta"},
    "Cancion2": {"Pop", "Romántica"},
    "Cancion3": {"Reggaeton", "Fiesta", "Baile"},
    "Cancion4": {"Rock", "Alternativo"},
    "Cancion5": {"Pop", "Baile"}
}

gustos = {"Reggaeton", "Baile", "Fiesta"}

print("EJERCICIO 17")
for cancion, generos in catalogo_canciones.items():
    similitud = len(gustos & generos) / len(gustos | generos)
    print(cancion, "->", round(similitud, 2))
print()


# -------------------------------------------------
# EJERCICIO 18: CLASIFICAR PELÍCULAS MUY PARECIDAS
# -------------------------------------------------
catalogo_peliculas = {
    "Inception": {"Acción", "Ciencia ficción", "Thriller"},
    "The Matrix": {"Acción", "Ciencia ficción"},
    "Titanic": {"Drama", "Romance", "Histórica"},
    "The Notebook": {"Drama", "Romance"},
    "Avengers": {"Acción", "Ciencia ficción", "Aventura"},
    "John Wick": {"Acción", "Crimen", "Thriller"}
}

print("EJERCICIO 18")

def jaccard_peliculas(pelicula1, pelicula2):
    generos1 = catalogo_peliculas.get(pelicula1, set())
    generos2 = catalogo_peliculas.get(pelicula2, set())

    if not generos1 or not generos2:
        return 0.0

    return len(generos1 & generos2) / len(generos1 | generos2)

pelis = list(catalogo_peliculas.keys())

for i in range(len(pelis)):
    for j in range(i + 1, len(pelis)):
        p1 = pelis[i]
        p2 = pelis[j]
        similitud = jaccard_peliculas(p1, p2)
        if similitud >= 0.5:
            print(f"{p1} y {p2} son bastante parecidas -> {similitud:.2f}")
print()


# -------------------------------------------------
# EJERCICIO 19: COMPRAS DE SUPERMERCADO
# -------------------------------------------------
compra_semana1 = {"arroz", "huevos", "leche", "pan", "fruta"}
compra_semana2 = {"pan", "leche", "pollo", "fruta", "jugo"}

print("EJERCICIO 19")
print("Productos repetidos:", compra_semana1 & compra_semana2)
print("Productos nuevos en semana 2:", compra_semana2 - compra_semana1)
print("Índice Jaccard de compras:", len(compra_semana1 & compra_semana2) / len(compra_semana1 | compra_semana2))
print()


# -------------------------------------------------
# EJERCICIO 20: PALABRAS USADAS POR DOS ESTUDIANTES
# -------------------------------------------------
respuesta1 = {"vivienda", "déficit", "hogar", "calidad", "territorio"}
respuesta2 = {"vivienda", "territorio", "política", "calidad", "hábitat"}

print("EJERCICIO 20")
print("Palabras compartidas:", respuesta1 & respuesta2)
print("Palabras diferentes:", respuesta1 ^ respuesta2)
print("Similitud Jaccard:", len(respuesta1 & respuesta2) / len(respuesta1 | respuesta2))
print()