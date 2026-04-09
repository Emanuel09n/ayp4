import re


# --------------------------------------------------
# 1. EXPRESIONES REGULARES
# --------------------------------------------------

def validar_codigo_producto(codigo):
    """
    Valida si un código de producto es válido.

    Formato:
    - 2 letras mayúsculas
    - guion
    - 4 dígitos

    Ejemplos:
    validar_codigo_producto("AB-1234") -> True
    validar_codigo_producto("XY-0001") -> True
    validar_codigo_producto("ab-1234") -> False
    validar_codigo_producto("ABC-123") -> False
    """
    return re.match(r'^[A-Z]{2}-\d{4}$', codigo) is not None


def extraer_emails(texto):
    """
    Extrae todos los correos electrónicos de un texto.

    Ejemplo:
    extraer_emails("Escribe a ana@gmail.com o a juan123@correo.co")
    -> ["ana@gmail.com", "juan123@correo.co"]
    """
    return re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', texto)


# --------------------------------------------------
# 2. LISTA ENLAZADA
# --------------------------------------------------

class Libro:
    def __init__(self, titulo, autor, prestado=False):
        self.titulo = titulo
        self.autor = autor
        self.prestado = prestado
        self.siguiente = None

    def __str__(self):
        estado = "Prestado" if self.prestado else "Disponible"
        return f"{self.titulo} - {self.autor} ({estado})"


class Biblioteca:
    def __init__(self):
        self.cabeza = None

    def mostrar(self):
        actual = self.cabeza
        if actual is None:
            print("No hay libros")
            return
        while actual:
            print(actual)
            actual = actual.siguiente

    def agregar_inicio(self, titulo, autor):
        """
        Agrega un libro al inicio de la lista.
        """
        nuevo = Libro(titulo, autor)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def contar_disponibles(self):
        """
        Cuenta cuántos libros NO están prestados.
        Usar recursividad.
        """
        def contar(nodo):
            if nodo is None:
                return 0
            if nodo.prestado:
                return contar(nodo.siguiente)
            return 1 + contar(nodo.siguiente)

        return contar(self.cabeza)

    def eliminar_prestados(self):
        """
        Elimina todos los libros prestados.
        Usar recursividad.
        """
        def eliminar(nodo):
            if nodo is None:
                return None
            if nodo.prestado:
                return eliminar(nodo.siguiente)
            nodo.siguiente = eliminar(nodo.siguiente)
            return nodo

        self.cabeza = eliminar(self.cabeza)


# --------------------------------------------------
# 3. CONJUNTOS
# --------------------------------------------------

materia_matematicas = {"Ana", "Luis", "Carlos", "Diana", "Elena"}
materia_fisica = {"Luis", "Diana", "Felipe", "Gabriela", "Ana"}
materia_quimica = {"Carlos", "Ana", "Hugo", "Elena", "Felipe"}


def estudiantes_en_dos_o_mas():
    """
    Retorna los estudiantes que están en dos o más materias.
    """
    mf = materia_matematicas & materia_fisica
    mq = materia_matematicas & materia_quimica
    fq = materia_fisica & materia_quimica
    return mf | mq | fq


def solo_fisica():
    """
    Retorna los estudiantes que solo están en Física.
    """
    return materia_fisica - materia_matematicas - materia_quimica


def materias_de_estudiante(nombre):
    """
    Retorna una lista con las materias en las que está el estudiante.

    Ejemplo:
    materias_de_estudiante("Ana") -> ["Matemáticas", "Física", "Química"]
    """
    materias = []

    if nombre in materia_matematicas:
        materias.append("Matemáticas")
    if nombre in materia_fisica:
        materias.append("Física")
    if nombre in materia_quimica:
        materias.append("Química")

    return materias


# --------------------------------------------------
# 4. RECURSIVIDAD
# --------------------------------------------------

def contar_digitos(n):
    """
    Cuenta cuántos dígitos tiene un número usando recursividad.

    Ejemplo:
    contar_digitos(12345) -> 5
    """
    if n < 10:
        return 1
    return 1 + contar_digitos(n // 10)


def suma_digitos(n):
    """
    Suma los dígitos de un número usando recursividad.

    Ejemplo:
    suma_digitos(1234) -> 10
    """
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)


# --------------------------------------------------
# 5. PRUEBAS
# --------------------------------------------------

print("----- PRUEBAS REGEX -----")
print(validar_codigo_producto("AB-1234"))     # True
print(validar_codigo_producto("ab-1234"))     # False
print(extraer_emails("Escribe a ana@gmail.com o a juan123@correo.co"))
# ['ana@gmail.com', 'juan123@correo.co']

print("\n----- PRUEBAS CONJUNTOS -----")
print(estudiantes_en_dos_o_mas())             # {'Ana', 'Luis', 'Carlos', 'Diana', 'Elena', 'Felipe'}
print(solo_fisica())                          # {'Gabriela'}
print(materias_de_estudiante("Ana"))          # ['Matemáticas', 'Física', 'Química']
print(materias_de_estudiante("Hugo"))         # ['Química']

print("\n----- PRUEBAS RECURSIVIDAD -----")
print(contar_digitos(12345))                  # 5
print(contar_digitos(8))                      # 1
print(suma_digitos(1234))                     # 10
print(suma_digitos(507))                      # 12

print("\n----- PRUEBAS LISTA ENLAZADA -----")
biblio = Biblioteca()
biblio.agregar_inicio("Cien años de soledad", "Gabriel García Márquez")
biblio.agregar_inicio("El principito", "Antoine de Saint-Exupéry")
biblio.agregar_inicio("1984", "George Orwell")

biblio.cabeza.prestado = True

print("Libros actuales:")
biblio.mostrar()

print("Disponibles:", biblio.contar_disponibles())

biblio.eliminar_prestados()

print("Después de eliminar prestados:")
biblio.mostrar()