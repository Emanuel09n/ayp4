import re


# --------------------------------------------------
# 1. EXPRESIONES REGULARES
# --------------------------------------------------

def validar_correo(correo):
    """
    Valida si un correo electrónico es válido.

    Formato:
    texto@dominio.com

    Ejemplos:
    validar_correo("juan@gmail.com") -> True
    validar_correo("ana123@outlook.co") -> True
    validar_correo("correo@.com") -> False
    validar_correo("correo.com") -> False
    """
    return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', correo) is not None


def extraer_menciones(texto):
    """
    Extrae todas las menciones de un texto.
    Una mención empieza con @ seguido de letras o números.

    Ejemplo:
    extraer_menciones("Hola @juan y @ana123")
    -> ["@juan", "@ana123"]
    """
    return re.findall(r'@[a-zA-Z0-9]+', texto)


def validar_contraseña(password):
    """
    Debe tener:
    - mínimo 8 caracteres
    - al menos una mayúscula
    - al menos un número

    Ejemplo:
    validar_contraseña("Hola1234") -> True
    validar_contraseña("hola1234") -> False
    """
    patron = r'^(?=.*[A-Z])(?=.*\d).{8,}$'
    return re.match(patron, password) is not None


# --------------------------------------------------
# 2. LISTA ENLAZADA
# --------------------------------------------------

class Tarea:
    def __init__(self, nombre, prioridad, completada=False):
        self.nombre = nombre
        self.prioridad = prioridad
        self.completada = completada
        self.siguiente = None

    def __str__(self):
        estado = "✓" if self.completada else "○"
        return f"[{estado}] {self.nombre} - Prioridad: {self.prioridad}"


class ListaTareas:
    def __init__(self):
        self.cabeza = None

    def mostrar(self):
        actual = self.cabeza
        if actual is None:
            print("Sin tareas")
            return
        while actual:
            print(actual)
            actual = actual.siguiente

    def agregar_inicio(self, nombre, prioridad):
        """
        Agrega una tarea al INICIO de la lista.
        """
        nueva = Tarea(nombre, prioridad)
        nueva.siguiente = self.cabeza
        self.cabeza = nueva

    def contar_pendientes(self):
        """
        Retorna cuántas tareas NO están completadas.
        Usar recursividad.
        """
        def contar(nodo):
            if nodo is None:
                return 0
            if nodo.completada:
                return contar(nodo.siguiente)
            return 1 + contar(nodo.siguiente)

        return contar(self.cabeza)

    def eliminar_completadas(self):
        """
        Elimina todas las tareas completadas.
        Usar recursividad.
        """
        def eliminar(nodo):
            if nodo is None:
                return None
            if nodo.completada:
                return eliminar(nodo.siguiente)
            nodo.siguiente = eliminar(nodo.siguiente)
            return nodo

        self.cabeza = eliminar(self.cabeza)


# --------------------------------------------------
# 3. CONJUNTOS
# --------------------------------------------------

equipo_A = {"Luis", "Pedro", "Ana", "Sofia", "Carlos"}
equipo_B = {"Ana", "Carlos", "Jorge", "Marta", "Luis"}
equipo_C = {"Pedro", "Sofia", "Jorge", "Camila", "Luis"}


def en_los_tres():
    """
    Jugadores que están en los tres equipos.
    """
    return equipo_A & equipo_B & equipo_C


def solo_dos_equipos():
    """
    Jugadores que están en EXACTAMENTE dos equipos.
    """
    ab = (equipo_A & equipo_B) - equipo_C
    ac = (equipo_A & equipo_C) - equipo_B
    bc = (equipo_B & equipo_C) - equipo_A
    return ab | ac | bc


def equipos_de_jugador(nombre):
    """
    Retorna en qué equipos está el jugador.
    Ejemplo:
    equipos_de_jugador("Luis") -> ["A", "B", "C"]
    """
    equipos = []

    if nombre in equipo_A:
        equipos.append("A")
    if nombre in equipo_B:
        equipos.append("B")
    if nombre in equipo_C:
        equipos.append("C")

    return equipos


# --------------------------------------------------
# 4. RECURSIVIDAD
# --------------------------------------------------

def formas_saltar(n):
    """
    Puedes saltar 1, 2 o 3 escalones.

    Ejemplo:
    n=3 -> 4 formas
    [1+1+1, 1+2, 2+1, 3]

    Implementar con recursividad pura.
    """
    if n == 0:
        return 1
    if n < 0:
        return 0
    return formas_saltar(n - 1) + formas_saltar(n - 2) + formas_saltar(n - 3)


def formas_saltar_memo(n, memo=None):
    """
    Misma función pero con memorización.
    """
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n == 0:
        return 1
    if n < 0:
        return 0

    memo[n] = (
        formas_saltar_memo(n - 1, memo) +
        formas_saltar_memo(n - 2, memo) +
        formas_saltar_memo(n - 3, memo)
    )
    return memo[n]


# --------------------------------------------------
# 5. PRUEBAS
# --------------------------------------------------

print("----- PRUEBAS REGEX -----")
print(validar_correo("juan@gmail.com"))          # True
print(validar_correo("correo.com"))              # False
print(extraer_menciones("Hola @juan y @ana123"))# ['@juan', '@ana123']
print(validar_contraseña("Hola1234"))            # True
print(validar_contraseña("hola1234"))            # False

print("\n----- PRUEBAS CONJUNTOS -----")
print(en_los_tres())                             # {'Luis'}
print(solo_dos_equipos())                        # {'Ana', 'Carlos', 'Pedro', 'Sofia', 'Jorge'}
print(equipos_de_jugador("Luis"))                # ['A', 'B', 'C']
print(equipos_de_jugador("Camila"))              # ['C']

print("\n----- PRUEBAS RECURSIVIDAD -----")
print(formas_saltar(3))                          # 4
print(formas_saltar(5))                          # 13
print(formas_saltar_memo(5))                     # 13
print(formas_saltar_memo(10))                    # 274

print("\n----- PRUEBAS LISTA ENLAZADA -----")
lista = ListaTareas()
lista.agregar_inicio("Estudiar Python", "Alta")
lista.agregar_inicio("Hacer ejercicio", "Media")
lista.agregar_inicio("Leer", "Baja")

lista.cabeza.completada = True

print("Tareas actuales:")
lista.mostrar()

print("Pendientes:", lista.contar_pendientes())

lista.eliminar_completadas()

print("Después de eliminar completadas:")
lista.mostrar()