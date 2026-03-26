class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Conjunto:
    def __init__(self,elemento=None):
        self.cabeza = None
        self.tamaño = 0
        if elemento:
            for a in elemento:
                self.agregar(a)

    def está_vacío(self):

        return self.cabeza is None

    def cardinalidad(self):
         return self.tamaño
    
    def pertenece(self, elemento):
        actual = self.cabeza
        while actual:
            if actual.valor == elemento:
                return True
            actual = actual.siguiente
        return False
    
    def agregar(self, x):
        if self.pertenece(x):
            return False
        nuevo_nodo = Nodo(x)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
        self.tamaño += 1
        return True
    
    def eliminar(self, x):
        if self.está_vacío():
            return False
        if self.cabeza.valor == x:
            self.cabeza = self.cabeza.siguiente
            self.tamaño -= 1
            return True
        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.valor == x:
                actual.siguiente = actual.siguiente.siguiente
                self.tamaño -= 1
                return True
            actual = actual.siguiente
        return False    
    
    def vaciar(self):
        self.cabeza = None
        self.tamaño = 0

    def unión(self, otro_conjunto):
        resultado = Conjunto()
        actual = self.cabeza
        while actual:
            resultado.agregar(actual.valor)
            actual = actual.siguiente
        actual_otro = otro_conjunto.cabeza
        while actual_otro:
            resultado.agregar(actual_otro.valor)
            actual_otro = actual_otro.siguiente
        return resultado
    
    def intersección(self, otro_conjunto):
        resultado = Conjunto()
        actual = self.cabeza
        while actual:
            if otro_conjunto.pertenece(actual.valor):
                resultado.agregar(actual.valor)
            actual = actual.siguiente
        return resultado
    
    def diferencia(self, otro_conjunto):
        resultado = Conjunto()
        actual = self.cabeza
        while actual:
            if not otro_conjunto.pertenece(actual.valor):
                resultado.agregar(actual.valor)
            actual = actual.siguiente
        return resultado
    
    def diferencia_simetrica(self,otro_conjunto):
        return self.diferencia(otro_conjunto).unión(otro_conjunto.diferencia(self))
    
    
    def a_lista(self):
        resultado = []
        actual = self.cabeza
        while actual:
            resultado.append(actual.valor)
            actual = actual.siguiente
        return resultado
    
    def __str__(self):
        return "{" + ", ".join(str(x) for x in self.a_lista()) + "}"
    

A= Conjunto(["A","B","C"])
B= Conjunto(["B","C","D"])
C= Conjunto(["C","D","E"])
print("Conjunto A:", A)
print("Conjunto B:", B)
