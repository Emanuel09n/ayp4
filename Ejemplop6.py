import re


# --------------------------------------------------
# 1. EXPRESIONES REGULARES
# --------------------------------------------------

def validar_codigo_estudiante(codigo):
    """
    Valida código tipo:
    EST-2026

    - 3 letras mayúsculas
    - guion
    - 4 dígitos

    Ejemplo:
    validar_codigo_estudiante("EST-2026") -> True
    """
    return re.match(r'^[A-Z]{3}-\d{4}$', codigo) is not None


def extraer_precios(texto):
    """
    Extrae precios con signo $

    Ejemplo:
    "Los precios son $10000 y $2500"
    -> ['$10000', '$2500']
    """
    return re.findall(r'\$\d+', texto)


# --------------------------------------------------
# 2. LISTA ENLAZADA
# --------------------------------------------------

class Pedido:
    def __init__(self, cliente, valor, entregado=False):
        self.cliente = cliente
        self.valor = valor
        self.entregado = entregado
        self.siguiente = None

    def __str__(self):
        estado = "✓" if self.entregado else "○"
        return f"[{estado}] {self.cliente} - ${self.valor}"


class ListaPedidos:
    def __init__(self):
        self.cabeza = None

    def mostrar(self):
        actual = self.cabeza
        if actual is None:
            print("Sin pedidos")
            return
        while actual:
            print(actual)
            actual = actual.siguiente

    def agregar_inicio(self, cliente, valor):
        """
        Agrega un pedido al inicio
        """
        nuevo = Pedido(cliente, valor)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def total_entregados(self):
        """
        Suma valores de pedidos entregados
        Usar recursividad
        """
        def sumar(nodo):
            if nodo is None:
                return 0
            if nodo.entregado:
                return nodo.valor + sumar(nodo.siguiente)
            return sumar(nodo.siguiente)

        return sumar(self.cabeza)

    def eliminar_no_entregados(self):
        """
        Elimina pedidos NO entregados
        Usar recursividad
        """
        def eliminar(nodo):
            if nodo is None:
                return None
            if not nodo.entregado:
                return eliminar(nodo.siguiente)
            nodo.siguiente = eliminar(nodo.siguiente)
            return nodo

        self.cabeza = eliminar(self.cabeza)


# --------------------------------------------------
# 3. CONJUNTOS
# --------------------------------------------------

clientes_app = {"Ana", "Luis", "Carlos", "Diana", "Pedro"}
clientes_web = {"Luis", "Pedro", "Camila", "Sofia", "Ana"}
clientes_tienda = {"Carlos", "Ana", "Pedro", "Jorge", "Diana"}


def clientes_en_dos():
    """
    Clientes que están en exactamente dos plataformas
    """
    aw = (clientes_app & clientes_web) - clientes_tienda
    at = (clientes_app & clientes_tienda) - clientes_web
    wt = (clientes_web & clientes_tienda) - clientes_app
    return aw | at | wt


def clientes_solo_web():
    """
    Clientes solo en web
    """
    return clientes_web - clientes_app - clientes_tienda


def plataformas_de_cliente(nombre):
    """
    Retorna plataformas del cliente
    """
    lista = []

    if nombre in clientes_app:
        lista.append("App")
    if nombre in clientes_web:
        lista.append("Web")
    if nombre in clientes_tienda:
        lista.append("Tienda")

    return lista


# --------------------------------------------------
# 4. RECURSIVIDAD
# --------------------------------------------------

def suma_hasta_n(n):
    """
    Suma de 1 hasta n

    Ejemplo:
    5 -> 15
    """
    if n == 1:
        return 1
    return n + suma_hasta_n(n - 1)


def fibonacci(n):
    """
    Fibonacci clásico

    Ejemplo:
    5 -> 5
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# --------------------------------------------------
# PRUEBAS
# --------------------------------------------------

print("----- REGEX -----")
print(validar_codigo_estudiante("EST-2026"))     # True
print(extraer_precios("Pagos: $10000 y $2500"))
# ['$10000', '$2500']

print("\n----- CONJUNTOS -----")
print(clientes_en_dos())       # {'Luis', 'Carlos', 'Diana'}
print(clientes_solo_web())     # {'Camila', 'Sofia'}
print(plataformas_de_cliente("Ana"))  # ['App', 'Web', 'Tienda']

print("\n----- RECURSIVIDAD -----")
print(suma_hasta_n(5))        # 15
print(fibonacci(6))           # 8

print("\n----- LISTA ENLAZADA -----")
lista = ListaPedidos()
lista.agregar_inicio("Ana", 20000)
lista.agregar_inicio("Luis", 30000)
lista.agregar_inicio("Carlos", 15000)

lista.cabeza.entregado = True
lista.cabeza.siguiente.entregado = False
lista.cabeza.siguiente.siguiente.entregado = True

print("Pedidos:")
lista.mostrar()

print("Total entregados:", lista.total_entregados())

lista.eliminar_no_entregados()

print("Después de eliminar no entregados:")
lista.mostrar()