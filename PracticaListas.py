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
              
            
