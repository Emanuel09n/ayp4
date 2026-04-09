import re


# --------------------------------------------------
# 1. EXPRESIONES REGULARES
# --------------------------------------------------

def validar_telefono(telefono):
    """
    Valida si un número telefónico tiene formato correcto.

    Formatos válidos:
    3001234567
    300-123-4567

    Ejemplos:
    validar_telefono("3001234567") -> True
    validar_telefono("300-123-4567") -> True
    validar_telefono("30-1234567") -> False
    validar_telefono("abc1234567") -> False
    """
    return re.match(r'^\d{10}$|^\d{3}-\d{3}-\d{4}$', telefono) is not None


def extraer_codigos(texto):
    """
    Extrae códigos que empiecen por # y tengan exactamente 4 dígitos.

    Ejemplo:
    extraer_codigos("Tus códigos son #1234 y #5678, pero #123 no")
    -> ['#1234', '#5678']
    """
    return re.findall(r'#\d{4}\b', texto)


# --------------------------------------------------
# 2. LISTA ENLAZADA
# --------------------------------------------------

class Producto:
    def __init__(self, nombre, precio, vendido=False):
        self.nombre = nombre
        self.precio = precio
        self.vendido = vendido
        self.siguiente = None

    def __str__(self):
        estado = "✓" if self.vendido else "○"
        return f"[{estado}] {self.nombre} - ${self.precio}"


class Inventario:
    def __init__(self):
        self.cabeza = None

    def mostrar(self):
        actual = self.cabeza
        if actual is None:
            print("Inventario vacío")
            return
        while actual:
            print(actual)
            actual = actual.siguiente

    def agregar_final(self, nombre, precio):
        """
        Agrega un producto al final de la lista.
        Usar recursividad.
        """
        nuevo = Producto(nombre, precio)

        def agregar_rec(nodo):
            if nodo.siguiente is None:
                nodo.siguiente = nuevo
            else:
                agregar_rec(nodo.siguiente)

        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            agregar_rec(self.cabeza)

    def total_no_vendidos(self):
        """
        Retorna la suma de precios de productos no vendidos.
        Usar recursividad.
        """
        def sumar(nodo):
            if nodo is None:
                return 0
            if nodo.vendido:
                return sumar(nodo.siguiente)
            return nodo.precio + sumar(nodo.siguiente)

        return sumar(self.cabeza)

    def eliminar_vendidos(self):
        """
        Elimina todos los productos vendidos.
        Usar recursividad.
        """
        def eliminar(nodo):
            if nodo is None:
                return None
            if nodo.vendido:
                return eliminar(nodo.siguiente)
            nodo.siguiente = eliminar(nodo.siguiente)
            return nodo

        self.cabeza = eliminar(self.cabeza)


# --------------------------------------------------
# 3. CONJUNTOS
# --------------------------------------------------

peliculas_juan = {"Avatar", "Titanic", "Matrix", "Coco", "Up"}
peliculas_maria = {"Titanic", "Coco", "Frozen", "Shrek", "Up"}
peliculas_pedro = {"Matrix", "Up", "Shrek", "Batman", "Coco"}


def peliculas_en_los_tres():
    """
    Retorna las películas que les gustan a los tres.
    """
    return peliculas_juan & peliculas_maria & peliculas_pedro


def peliculas_solo_de_juan():
    """
    Retorna las películas que solo le gustan a Juan.
    """
    return peliculas_juan - peliculas_maria - peliculas_pedro


def personas_que_gustan_de(pelicula):
    """
    Retorna una lista con las personas a las que les gusta una película.

    Ejemplo:
    personas_que_gustan_de("Up") -> ["Juan", "María", "Pedro"]
    """
    personas = []

    if pelicula in peliculas_juan:
        personas.append("Juan")
    if pelicula in peliculas_maria:
        personas.append("María")
    if pelicula in peliculas_pedro:
        personas.append("Pedro")

    return personas


# --------------------------------------------------
# 4. RECURSIVIDAD
# --------------------------------------------------

def invertir_cadena(texto):
    """
    Invierte una cadena usando recursividad.

    Ejemplo:
    invertir_cadena("hola") -> "aloh"
    """
    if len(texto) <= 1:
        return texto
    return texto[-1] + invertir_cadena(texto[:-1])


def contar_vocales(texto):
    """
    Cuenta cuántas vocales tiene una cadena usando recursividad.

    Ejemplo:
    contar_vocales("casa") -> 2
    """
    if texto == "":
        return 0

    primera = texto[0].lower()
    if primera in "aeiou":
        return 1 + contar_vocales(texto[1:])
    return contar_vocales(texto[1:])


# --------------------------------------------------
# 5. PRUEBAS
# --------------------------------------------------

print("----- PRUEBAS REGEX -----")
print(validar_telefono("3001234567"))          # True
print(validar_telefono("300-123-4567"))        # True
print(validar_telefono("30-1234567"))          # False
print(extraer_codigos("Tus códigos son #1234 y #5678, pero #123 no"))
# ['#1234', '#5678']

print("\n----- PRUEBAS CONJUNTOS -----")
print(peliculas_en_los_tres())                 # {'Coco', 'Up'}
print(peliculas_solo_de_juan())                # {'Avatar'}
print(personas_que_gustan_de("Up"))            # ['Juan', 'María', 'Pedro']
print(personas_que_gustan_de("Batman"))        # ['Pedro']

print("\n----- PRUEBAS RECURSIVIDAD -----")
print(invertir_cadena("hola"))                 # aloh
print(invertir_cadena("python"))               # nohtyp
print(contar_vocales("casa"))                  # 2
print(contar_vocales("universidad"))           # 5

print("\n----- PRUEBAS LISTA ENLAZADA -----")
inventario = Inventario()
inventario.agregar_final("Mouse", 50000)
inventario.agregar_final("Teclado", 80000)
inventario.agregar_final("Monitor", 600000)

inventario.cabeza.siguiente.vendido = True

print("Productos actuales:")
inventario.mostrar()

print("Total no vendidos:", inventario.total_no_vendidos())

inventario.eliminar_vendidos()

print("Después de eliminar vendidos:")
inventario.mostrar()