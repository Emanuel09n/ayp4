#class nodo
class Nodo:
    def __init__(self, valor):
        self.valor= valor
        self.siguiente= None

    def es_vacio(self):
        return self.valor is None


#class pila
class Pila:
    def __init__(self):
        self.tope= None
        self.tamaño= 0
    
    def push(self, valor):
        nuevo_nodo= Nodo(valor)
        nuevo_nodo.siguiente= self.tope
        self.tope= nuevo_nodo
        self.tamaño += 1
    
    def pop(self):
        if self.tamaño == 0:
            raise IndexError("La pila está vacía")
        valor= self.tope.valor
        self.tope= self.tope.siguiente
        self.tamaño -= 1
        return valor
    
    def peek(self):
        if self.tamaño == 0:
            raise IndexError("La pila está vacía")
        return self.tope.valor
    


#convertir imfija a postfija
def infija_a_postfija(expresion):

    elif token in precedencia:
        # Es un operador
        while (
            not pila.esta_vacia()
            and pila.peek() != '('
            and pila.peek() in precedencia
            and precedencia[pila.peek()] >= precedencia[token]
        ):
            salida.append(pila.pop())

        pila.push(token)
        print(f"    '{token}' (operador) -> pila")

    print(f"    Salida: {salida}")
    print(f"    Pila: {pila}")

    #vaciar la pila
    print("\nVaciando la pila...")
    while not pila.esta_vacia():
        salida.append(pila.pop())
        print(f"    Salida: {salida}")
        print(f"    Pila: {pila}")

    # HACER:una funcion que diga si una funcion es correcta o incorrecta por ejemplo{[}]
    