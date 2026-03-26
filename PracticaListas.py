class Nodo:
    def __init__(self,documento,nombre):
        self.documento=documento
        self.nombre=nombre
        self.siguiente=None

class Lista:
    def __init__(self,):
        self.cabeza = None  
        self.cola= None  

    def AgregarALInicio(self,nombre,documento):
        nodo=Nodo(documento,nombre)

        if self.cabeza==None:
            self.cabeza=nodo
            self.cola = nodo
        else:
            self.cola.siguiente=nodo
            self.cola=nodo

    def contar(self,nodo=None):
        if nodo is none:
            nodo=self.cabeza
        if nodo.siguiente is none:
            return 0
        return sumar(nodo.siguiente)+nodo.dato  
    
    #saber si un dato esta o no en la lista recursivo
    def buscar(self,nodo=none,dato,primea_llamada=true): 
        if primea_llamada:
            nodo=self.cabeza
        if nodo is none:
            return False
        if nodo.dato==dato:
            return True
        return buscar(nodo.siguiente,dato,false)
              
            
