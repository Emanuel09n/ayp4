import re


# --------------------------------------------------
# 1. EXPRESIONES REGULARES
# --------------------------------------------------

def validar_usuario(usuario):
    """
    Valida si un nombre de usuario es válido.

    Reglas:
    - Debe comenzar con una letra
    - Puede tener letras, números o guion bajo
    - Debe tener entre 5 y 12 caracteres

    Ejemplos:
    validar_usuario("juan_23") -> True
    validar_usuario("1juan") -> False
    validar_usuario("ab") -> False
    """
    return re.match(r'^[A-Za-z][A-Za-z0-9_]{4,11}$', usuario) is not None


def extraer_numeros(texto):
    """
    Extrae todos los números enteros de un texto.

    Ejemplo:
    extraer_numeros("Compré 3 cuadernos y 12 lápices")
    -> ['3', '12']
    """
    return re.findall(r'\d+', texto)


# --------------------------------------------------
# 2. LISTA ENLAZADA
# --------------------------------------------------

class Cancion:
    def __init__(self, titulo, artista, reproducida=False):
        self.titulo = titulo
        self.artista = artista
        self.reproducida = reproducida
        self.siguiente = None

    def __str__(self):
        estado = "✓" if self.reproducida else "○"
        return f"[{estado}] {self.titulo} - {self.artista}"


class ListaReproduccion:
    def __init__(self):
        self.cabeza = None

    def mostrar(self):
        actual = self.cabeza
        if actual is None:
            print("Sin canciones")
            return
        while actual:
            print(actual)
            actual = actual.siguiente

    def agregar_final(self, titulo, artista):
        """
        Agrega una canción al final de la lista.
        Usar recursividad.
        """
        nueva = Cancion(titulo, artista)

        def agregar_rec(nodo):
            if nodo.siguiente is None:
                nodo.siguiente = nueva
            else:
                agregar_rec(nodo.siguiente)

        if self.cabeza is None:
            self.cabeza = nueva
        else:
            agregar_rec(self.cabeza)

    def contar_no_reproducidas(self):
        """
        Cuenta cuántas canciones no han sido reproducidas.
        Usar recursividad.
        """
        def contar(nodo):
            if nodo is None:
                return 0
            if nodo.reproducida:
                return contar(nodo.siguiente)
            return 1 + contar(nodo.siguiente)

        return contar(self.cabeza)

    def eliminar_reproducidas(self):
        """
        Elimina todas las canciones ya reproducidas.
        Usar recursividad.
        """
        def eliminar(nodo):
            if nodo is None:
                return None
            if nodo.reproducida:
                return eliminar(nodo.siguiente)
            nodo.siguiente = eliminar(nodo.siguiente)
            return nodo

        self.cabeza = eliminar(self.cabeza)


# --------------------------------------------------
# 3. CONJUNTOS
# --------------------------------------------------

curso_python = {"Ana", "Luis", "Pedro", "María", "Camila"}
curso_java = {"Luis", "María", "Jorge", "Sofía", "Elena"}
curso_web = {"Pedro", "Camila", "Jorge", "Elena", "Andrés"}


def en_al_menos_dos():
    """
    Retorna los estudiantes que están en al menos dos cursos.
    """
    py_java = curso_python & curso_java
    py_web = curso_python & curso_web
    java_web = curso_java & curso_web
    return py_java | py_web | java_web


def solo_python():
    """
    Retorna los estudiantes que solo están en Python.
    """
    return curso_python - curso_java - curso_web


def cursos_de_estudiante(nombre):
    """
    Retorna una lista con los cursos en los que está el estudiante.

    Ejemplo:
    cursos_de_estudiante("Luis") -> ["Python", "Java"]
    """
    cursos = []

    if nombre in curso_python:
        cursos.append("Python")
    if nombre in curso_java:
        cursos.append("Java")
    if nombre in curso_web:
        cursos.append("Web")

    return cursos


# --------------------------------------------------
# 4. RECURSIVIDAD
# --------------------------------------------------

def sumar_hasta_n(n):
    """
    Retorna la suma de los números desde 1 hasta n.

    Ejemplo:
    sumar_hasta_n(5) -> 15
    """
    if n == 1:
        return 1
    return n + sumar_hasta_n(n - 1)


def potencia(base, exponente):
    """
    Calcula base elevado a exponente usando recursividad.

    Ejemplo:
    potencia(2, 4) -> 16
    """
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)


# --------------------------------------------------
# 5. PRUEBAS
# --------------------------------------------------

print("----- PRUEBAS REGEX -----")
print(validar_usuario("juan_23"))          # True
print(validar_usuario("1juan"))            # False
print(validar_usuario("ab"))               # False
print(extraer_numeros("Compré 3 cuadernos y 12 lápices"))  # ['3', '12']

print("\n----- PRUEBAS CONJUNTOS -----")
print(en_al_menos_dos())                   # {'Luis', 'María', 'Pedro', 'Camila', 'Jorge', 'Elena'}
print(solo_python())                       # {'Ana'}
print(cursos_de_estudiante("Luis"))        # ['Python', 'Java']
print(cursos_de_estudiante("Andrés"))      # ['Web']

print("\n----- PRUEBAS RECURSIVIDAD -----")
print(sumar_hasta_n(5))                    # 15
print(potencia(2, 4))                      # 16
print(potencia(3, 3))                      # 27

print("\n----- PRUEBAS LISTA ENLAZADA -----")
playlist = ListaReproduccion()
playlist.agregar_final("Monalisa", "Peso Pluma")
playlist.agregar_final("Ojitos Lindos", "Bad Bunny")
playlist.agregar_final("Hawái", "Maluma")

playlist.cabeza.reproducida = True

print("Lista actual:")
playlist.mostrar()

print("No reproducidas:", playlist.contar_no_reproducidas())

playlist.eliminar_reproducidas()

print("Después de eliminar reproducidas:")
playlist.mostrar()