"""
Google Chrome te ha contratado para implementar un sistema de recomendación
y comparación de páginas usando CONJUNTOS y SIMILITUD DE JACCARD.

Debes diseñar e implementar el sistema usando listas enlazadas.

INSTRUCCIONES:
--------------
1. Diseñar la clase Nodo (Etiqueta) con los atributos necesarios
2. Diseñar la clase Lista (ConjuntoEtiquetas) con los métodos requeridos
3. Usar RECURSIVIDAD en los métodos donde se indique
4. No usar listas de Python [], solo tu estructura de nodos
5. Tiempo: 90 minutos

═══════════════════════════════════════════════════════════════════════════════
REQUERIMIENTOS DEL SISTEMA
═══════════════════════════════════════════════════════════════════════════════

PUNTO 1 (1.0): DISEÑO DE ESTRUCTURAS
-------------------------------------

a) Clase NODO (Etiqueta):
   - Debe almacenar: nombre de la etiqueta
   - Debe poder enlazarse con otra etiqueta

b) Clase LISTA (ConjuntoEtiquetas):
   - Debe mantener referencia al inicio de la lista
   - No debe permitir etiquetas repetidas
   - Las etiquetas más recientes van al INICIO

PUNTO 2 (1.5): OPERACIONES DE CONJUNTOS
----------------------------------------
Implementar:
- agregar_etiqueta(nombre)
- pertenece(nombre)                  -> RECURSIVO
- cardinalidad()                     -> RECURSIVO
- union(otro_conjunto)
- interseccion(otro_conjunto)
- diferencia(otro_conjunto)
- diferencia_simetrica(otro_conjunto)

PUNTO 3 (1.5): SIMILITUD DE JACCARD
------------------------------------
Implementar:
- jaccard(otro_conjunto)

PUNTO 4 (1.0): CONSULTAS
-------------------------
Implementar:
- buscar_etiquetas_largas(longitud)  -> RECURSIVO
- eliminar_etiquetas_cortas(limite)  -> RECURSIVO

PUNTO 5 (1.0): CASO DE PRUEBA
------------------------------
Dadas las etiquetas de dos páginas, mostrar:
- Etiquetas de cada página
- Unión
- Intersección
- Diferencia
- Diferencia simétrica
- Similitud de Jaccard
"""


class Etiqueta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None


class ConjuntoEtiquetas:
    def __init__(self):
        self.inicio = None

    def agregar_etiqueta(self, nombre):
        nombre = nombre.lower().strip()
        if nombre == "":
            return False
        if self.pertenece(nombre):
            return False
        nueva = Etiqueta(nombre)
        nueva.siguiente = self.inicio
        self.inicio = nueva
        return True

    def pertenece(self, nombre):
        nombre = nombre.lower().strip()

        def buscar(nodo):
            if nodo is None:
                return False
            if nodo.nombre == nombre:
                return True
            return buscar(nodo.siguiente)

        return buscar(self.inicio)

    def cardinalidad(self):
        def contar(nodo):
            if nodo is None:
                return 0
            return 1 + contar(nodo.siguiente)

        return contar(self.inicio)

    def union(self, otro_conjunto):
        resultado = ConjuntoEtiquetas()

        def copiar_primero(nodo):
            if nodo is None:
                return
            resultado.agregar_etiqueta(nodo.nombre)
            copiar_primero(nodo.siguiente)

        def copiar_segundo(nodo):
            if nodo is None:
                return
            resultado.agregar_etiqueta(nodo.nombre)
            copiar_segundo(nodo.siguiente)

        copiar_primero(self.inicio)
        copiar_segundo(otro_conjunto.inicio)
        return resultado

    def interseccion(self, otro_conjunto):
        resultado = ConjuntoEtiquetas()

        def recorrer(nodo):
            if nodo is None:
                return
            if otro_conjunto.pertenece(nodo.nombre):
                resultado.agregar_etiqueta(nodo.nombre)
            recorrer(nodo.siguiente)

        recorrer(self.inicio)
        return resultado

    def diferencia(self, otro_conjunto):
        resultado = ConjuntoEtiquetas()

        def recorrer(nodo):
            if nodo is None:
                return
            if not otro_conjunto.pertenece(nodo.nombre):
                resultado.agregar_etiqueta(nodo.nombre)
            recorrer(nodo.siguiente)

        recorrer(self.inicio)
        return resultado

    def diferencia_simetrica(self, otro_conjunto):
        return self.diferencia(otro_conjunto).union(otro_conjunto.diferencia(self))

    def jaccard(self, otro_conjunto):
        inter = self.interseccion(otro_conjunto).cardinalidad()
        uni = self.union(otro_conjunto).cardinalidad()
        if uni == 0:
            return 0
        return inter / uni

    def buscar_etiquetas_largas(self, longitud):
        resultado = ConjuntoEtiquetas()

        def buscar(nodo):
            if nodo is None:
                return
            if len(nodo.nombre) >= longitud:
                resultado.agregar_etiqueta(nodo.nombre)
            buscar(nodo.siguiente)

        buscar(self.inicio)
        return resultado

    def eliminar_etiquetas_cortas(self, limite):
        def eliminar(nodo):
            if nodo is None:
                return None
            if len(nodo.nombre) < limite:
                return eliminar(nodo.siguiente)
            nodo.siguiente = eliminar(nodo.siguiente)
            return nodo

        self.inicio = eliminar(self.inicio)

    def __str__(self):
        def construir(nodo):
            if nodo is None:
                return ""
            if nodo.siguiente is None:
                return nodo.nombre
            return nodo.nombre + ", " + construir(nodo.siguiente)

        return "{ " + construir(self.inicio) + " }"


# Ejemplo de uso
if __name__ == "__main__":
    pagina1 = ConjuntoEtiquetas()
    pagina2 = ConjuntoEtiquetas()

    for etiqueta in ["python", "datos", "analisis", "estadistica"]:
        pagina1.agregar_etiqueta(etiqueta)

    for etiqueta in ["python", "machinelearning", "datos", "modelos"]:
        pagina2.agregar_etiqueta(etiqueta)

    print("Etiquetas de la página 1:", pagina1)
    print("Etiquetas de la página 2:", pagina2)

    print("\nUnión:")
    print(pagina1.union(pagina2))

    print("\nIntersección:")
    print(pagina1.interseccion(pagina2))

    print("\nDiferencia página 1 - página 2:")
    print(pagina1.diferencia(pagina2))

    print("\nDiferencia página 2 - página 1:")
    print(pagina2.diferencia(pagina1))

    print("\nDiferencia simétrica:")
    print(pagina1.diferencia_simetrica(pagina2))

    print("\nSimilitud de Jaccard:")
    print(round(pagina1.jaccard(pagina2), 3))

    print("\nEtiquetas largas de la página 1 (>= 8):")
    print(pagina1.buscar_etiquetas_largas(8))

    print("\nPágina 1 después de eliminar etiquetas cortas (< 7):")
    pagina1.eliminar_etiquetas_cortas(7)
    print(pagina1)