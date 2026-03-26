#Diccionario de películas 
Catalogo_peliculas = {
    "Inception": {"Acción", "Ciencia ficción", "Thriller"},
    "The Matrix": {"Acción", "Ciencia ficción"},
    "titanic": {"Drama", "Romance","historica"},
    "The notebook": {"Drama", "Romance"},
    "Avengers": {"Acción", "Ciencia ficción", "Aventura"},
    "John wick": {"Acción", "Crimen", "Thriller"},
    "Interstellar": {"Acción", "Ciencia ficción", "Drama"},
    "The Godfather": {"Crimen", "Drama"},
    "Toy story": {"Animación", "Aventura", "Comedia"},
    "Shrek": {"Animación", "Aventura", "Comedia"}
}

#Encontrar peliculas similares, que compartan minimo dos generos
peliculas= list(Catalogo_peliculas.keys())
for i in range(len(peliculas)):
    for j in range (i+1, len(peliculas)):
        pelicula1 = peliculas[i]
        pelicula2 = peliculas[j]
        generos_comunes = Catalogo_peliculas[pelicula1].intersection(Catalogo_peliculas[pelicula2])
        if len(generos_comunes) >= 2:
            print(f"{pelicula1} y {pelicula2} son similares, comparten los géneros: {generos_comunes}")

favoritos = {"Acción", "Crimen", "Aventura"}
#recomendar peliculas segun mis generos favoritos y con que porcentaje
recomendaciones = {}
for pelicula, generos in Catalogo_peliculas.items():
    generos_comunes = favoritos.intersection(generos)
    if generos_comunes:
        porcentaje = len(generos_comunes) / len(favoritos) * 100
        recomendaciones[pelicula] = porcentaje
print(recomendaciones)

#como puedo mostrar todos los generos que hay en catalogo de peliculas sin repetir
generos_unicos = set()## Creamos un conjunto vacío donde guardaremos los géneros sin repetir

for generos in Catalogo_peliculas.values():# Recorremos los valores del diccionario (listas de géneros por película)
    generos_unicos.update(generos)# update() permite añadir varios elementos a la vez
print(generos_unicos)# Imprimimos el conjunto final con todos los géneros únicos    

#peliculas por genero

# Crear diccionario vacío para agrupar por género
peliculas_por_genero = {}

# Recorrer cada película con sus géneros
for pelicula, generos in Catalogo_peliculas.items():
    
    # Recorrer cada género de la película
    for genero in generos:
        
        # Si el género no existe, se crea con lista vacía
        if genero not in peliculas_por_genero:
            peliculas_por_genero[genero] = []
        
        # Agregar la película al género correspondiente
        peliculas_por_genero[genero].append(pelicula)

# Mostrar el diccionario final organizado por género
print(peliculas_por_genero)

"""Lógica fácil

Crear un diccionario vacío porque se necesita guardar infromacionq mientras recorre datos
NO ES CONJUNTO PORQUE EL SET SOLO GUARDA VALORES PERO SE NECESITAN RELACIOANR COSAS
Recorrer cada película

Recorrer sus géneros

Por cada género, guardar la película ahí

Si el género no existe → lo creo CON UNA CLAVE Y UNA LISTA VACIA PARA GUARDAR PELICULAS

Si ya existe → agrego la película"""




#metodoque reciba dos peliculas 
#devuelva el indice de similitud jaccard 


print("MÉTODO DE JACCARD")
# Método que calcula la similitud de Jaccard entre dos películas
#devuelva el indice de simioitud jaccard
def jaccard_similarity(pelicula1, pelicula2):
    generos1 = Catalogo_peliculas.get(pelicula1, set())
    generos2 = Catalogo_peliculas.get(pelicula2, set())
    
    if not generos1 or not generos2:
        return 0.0  # Si alguna película no tiene géneros, la similitud es 0
    
    interseccion = generos1.intersection(generos2)
    union = generos1.union(generos2)
    
    similitud = len(interseccion) / len(union)
    return similitud

# Ejemplo de uso
pelicula_a = "Inception"
pelicula_b = "The Matrix"
similitud = jaccard_similarity(pelicula_a, pelicula_b)
print(f"La similitud de Jaccard entre '{pelicula_a}' y '{pelicula_b}' es: {similitud:.2f}")


#leer dos textos
#calcular su indice de similitud ignorando las stopwords
#si el indice es mayor a 0.6,se copiarion y hacer un print que diga se copiaron
# Conjunto de palabras comunes que se van a eliminar
STOPWORDS = {
    "el", "la", "los", "las", "un", "una", "unos", "unas",
    "de", "del", "al", "a", "en", "con", "por", "para",
    "y", "o", "que", "es", "son", "se", "su", "sus",
    "como", "pero", "más", "este", "esta", "estos", "estas"
}

# Función para calcular similitud de Jaccard entre dos textos
def jaccard_similarity_text(texto1, texto2):
    
    # Limpiar textos: minúsculas, separar palabras y quitar stopwords
    palabras1 = set(texto1.lower().split()) - STOPWORDS
    palabras2 = set(texto2.lower().split()) - STOPWORDS
    
    # Si alguno queda sin palabras, la similitud es 0
    if not palabras1 or not palabras2:
        return 0.0
    
    # Palabras en común
    interseccion = palabras1.intersection(palabras2)
    
    # Todas las palabras sin repetir
    union = palabras1.union(palabras2)
    
    # Calcular índice de Jaccard
    similitud = len(interseccion) / len(union)
    
    return similitud


# Ejemplo de uso
texto_a = "El gato está en el tejado"
texto_b = "El gato se encuentra en el techo"

# Calcular similitud
similitud_texto = jaccard_similarity_text(texto_a, texto_b)

# Mostrar resultado
print(f"La similitud de Jaccard entre los textos es: {similitud_texto:.2f}")

# Evaluar si son similares
if similitud_texto > 0.6:
    print("Los textos son similares, se copiaron")










