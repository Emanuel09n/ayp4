import re


# --------------------------------------------------
# 1. EXPRESIONES REGULARES
# --------------------------------------------------

def validar_fecha(fecha):
    """
    Valida si una fecha tiene el formato correcto: dd/mm/aaaa

    Ejemplos:
    validar_fecha("08/04/2026") -> True
    validar_fecha("1/04/2026") -> False
    validar_fecha("08-04-2026") -> False
    """
    return re.match(r'^\d{2}/\d{2}/\d{4}$', fecha) is not None


def extraer_palabras_mayus(texto):
    """
    Extrae todas las palabras escritas completamente en mayúsculas.

    Ejemplo:
    extraer_palabras_mayus("Hoy fui a la U con ANA y LUIS")
    -> ['ANA', 'LUIS']
    """
    return re.findall(r'\b[A-ZÁÉÍÓÚÑ]+\b', texto)


# --------------------------------------------------
# 2. LISTA ENLAZADA
# --------------------------------------------------

class Estudiante:
    def __init__(self, nombre, nota, aprobo=False):
        self.nombre = nombre
        self.nota = nota
        self.aprobo = aprobo
        self.siguiente = None

    def __str__(self):
        estado = "Aprobó" if self.aprobo else "No aprobó"
        return f"{self.nombre} - Nota: {self.nota} - {estado}"


class ListaEstudiantes:
    def __init__(self):
        self.cabeza = None

    def mostrar(self):
        actual = self.cabeza
        if actual is None:
            print("No hay estudiantes")
            return
        while actual:
            print(actual)
            actual = actual.siguiente

    def agregar_final(self, nombre, nota):
        """
        Agrega un estudiante al final de la lista.
        Usar recursividad.
        """
        nuevo = Estudiante(nombre, nota)

        def agregar_rec(nodo):
            if nodo.siguiente is None:
                nodo.siguiente = nuevo
            else:
                agregar_rec(nodo.siguiente)

        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            agregar_rec(self.cabeza)

    def contar_aprobados(self):
        """
        Cuenta cuántos estudiantes aprobaron.
        Usar recursividad.
        """
        def contar(nodo):
            if nodo is None:
                return 0
            if nodo.aprobo:
                return 1 + contar(nodo.siguiente)
            return contar(nodo.siguiente)

        return contar(self.cabeza)

    def eliminar_no_aprobados(self):
        """
        Elimina todos los estudiantes que no aprobaron.
        Usar recursividad.
        """
        def eliminar(nodo):
            if nodo is None:
                return None
            if not nodo.aprobo:
                return eliminar(nodo.siguiente)
            nodo.siguiente = eliminar(nodo.siguiente)
            return nodo

        self.cabeza = eliminar(self.cabeza)


# --------------------------------------------------
# 3. CONJUNTOS
# --------------------------------------------------

materia_ingles = {"Ana", "Luis", "María", "Pedro", "Camila"}
materia_programacion = {"Luis", "Pedro", "Sofía", "Jorge", "Ana"}
materia_matematicas = {"Pedro", "Camila", "Ana", "Valentina", "Jorge"}


def estudiantes_en_todas():
    """
    Retorna los estudiantes que están en las tres materias.
    """
    return materia_ingles & materia_programacion & materia_matematicas


def estudiantes_solo_una():
    """
    Retorna los estudiantes que están en exactamente una materia.
    """
    solo_ingles = materia_ingles - materia_programacion - materia_matematicas
    solo_programacion = materia_programacion - materia_ingles - materia_matematicas
    solo_matematicas = materia_matematicas - materia_ingles - materia_programacion
    return solo_ingles | solo_programacion | solo_matematicas


def materias_de(nombre):
    """
    Retorna una lista con las materias en las que está inscrito el estudiante.

    Ejemplo:
    materias_de("Pedro") -> ["Inglés", "Programación", "Matemáticas"]
    """
    materias = []

    if nombre in materia_ingles:
        materias.append("Inglés")
    if nombre in materia_programacion:
        materias.append("Programación")
    if nombre in materia_matematicas:
        materias.append("Matemáticas")

    return materias


# --------------------------------------------------
# 4. RECURSIVIDAD
# --------------------------------------------------

def factorial(n):
    """
    Calcula el factorial de un número usando recursividad.

    Ejemplo:
    factorial(5) -> 120
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def suma_pares(n):
    """
    Retorna la suma de los números pares desde 2 hasta n.
    Asume que n es positivo.

    Ejemplo:
    suma_pares(6) -> 12
    porque 2 + 4 + 6 = 12
    """
    if n <= 0:
        return 0
    if n % 2 == 0:
        return n + suma_pares(n - 2)
    return suma_pares(n - 1)


# --------------------------------------------------
# 5. PRUEBAS
# --------------------------------------------------

print("----- PRUEBAS REGEX -----")
print(validar_fecha("08/04/2026"))                 # True
print(validar_fecha("8/04/2026"))                  # False
print(validar_fecha("08-04-2026"))                 # False
print(extraer_palabras_mayus("Hoy fui a la U con ANA y LUIS"))
# ['U', 'ANA', 'LUIS']

print("\n----- PRUEBAS CONJUNTOS -----")
print(estudiantes_en_todas())                      # {'Ana', 'Pedro'}
print(estudiantes_solo_una())                      # {'María', 'Sofía', 'Valentina'}
print(materias_de("Pedro"))                        # ['Inglés', 'Programación', 'Matemáticas']
print(materias_de("Camila"))                       # ['Inglés', 'Matemáticas']

print("\n----- PRUEBAS RECURSIVIDAD -----")
print(factorial(5))                                # 120
print(factorial(3))                                # 6
print(suma_pares(6))                               # 12
print(suma_pares(9))                               # 20

print("\n----- PRUEBAS LISTA ENLAZADA -----")
lista = ListaEstudiantes()
lista.agregar_final("Ana", 4.5)
lista.agregar_final("Luis", 2.8)
lista.agregar_final("María", 3.7)

lista.cabeza.aprobo = True
lista.cabeza.siguiente.aprobo = False
lista.cabeza.siguiente.siguiente.aprobo = True

print("Estudiantes actuales:")
lista.mostrar()

print("Aprobados:", lista.contar_aprobados())

lista.eliminar_no_aprobados()

print("Después de eliminar no aprobados:")
lista.mostrar()