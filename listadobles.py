class NodoDoble:
    def __init__(self,dato):
        self.siguiente=None
        self.anterior=None





class ListaDbole:
    """lista doblemente ligada"""

    def __init__(self):
        self.cabeza=None
        self.cola=None

    def esta_vacia(self):
        """verifica si la lista esta avcia """
        return self.cabeza is None
    
    def insertar_inicio(self,dato):
        """insertar un eemento al inicio """
        nuevo_NodoDoble(dato)
 
        if self.esta_vacia():
            #lista vacia,cabeza apuunta a cola
            self.cabeza=nuevo
            self.cola=nuevo
        else:
            #conectar nuevo con la cabeza actual
            nuevo.siguiente=self.cabeza
            self.cabeza.anterior=nuevo
            self.cabeza=nuevo

    def insertar_final(self,dato):
        """insertar un elemento al final de la lista"""
        nuevo=NodoDoble(dato)

        if self.esta_vacia():
            self.cabeza=None
            self.cola=nuevo
        else:
            nuevo.anterior=self.cola
            self.cola=nuevo


    def eliminar_inicio(self):
        """elimina el primer elemento de la lista"""
        if self.esta_vacia():
           return None
        dato=self.cabeza.dato

        if self.cabeza==self.cola
        #solo un elemento
        self.cabeza=None
        self.cola=None
        else: 
        self.cabeza=self.cabeza.siguiente
        self.cabeza.anterior=None

    def recorrer_Adelante(self):
        """imprime la lista de inicio a fin"""
        if self.esta_vacia():
            print("lista vacia")
            return
        print("inicio->fin",end=" ")
        actual=self.cabeza
        elementos= []
        while actual:
            elementos.append(str(actual.dato))
            actual=actual.siguiente
        print("<->".join(elementos)) 

    def recorrer_atras(self):
        """imprime la lista de fin a inicio"""
        if self.esta_vacia():
            print("lista vacia")
            return
        


    def buscar(self,dato):
        actual=self.cabeza
        while actual:
            if actual.dato==dato:
                return True
            actual=actual.siguiente
        return False
    
    def __len__(self):
        """retorna la cantidad de elementos"""
        contador=0
        actual=self.cabeza
        while actual:
            contador+=1
            actual=actual.siguiente
        return contador
    

     

