datos=[5,3,8,1,2,9,4]

import heapq

heapq.heapify(datos)
print("Heap:", datos)

heapq.heappush(datos, 0)
print("Heap después de agregar 0:", datos)

minimo= heapq.heappop(datos)
print("Elemento mínimo extraído:", minimo)
print("Heap después de extraer el mínimo:", datos)

datos2=[(2, 'A'), (1, 'B'), (3, 'C'), (2, 'B')]
heapq.heapify(datos2)
print("Heap de tuplas:", datos2)

#programa para un hispital
#cada paciente tiene una prioridad de 1 a 3,1 es la mas importante
#las perosnas del hospital deben saber quien es el siguiente paciente a atende
# indicar su nombre y prioridad y que pasa si hay dos con la misma prioridad

class Paciente:
    def __init__(self, nombre, prioridad):
        self.nombre= nombre
        self.prioridad= prioridad
    
    def __lt__(self, otro):
        return self.prioridad < otro.prioridad
class Hospital:
    def __init__(self):
        self.pacientes= []
    
    def agregar_paciente(self, paciente):
        heapq.heappush(self.pacientes, paciente)
    
    def siguiente_paciente(self):
        if not self.pacientes:
            return None
        return heapq.heappop(self.pacientes)
hospital= Hospital()
#debo agrgar yo los nombres y prioridades de los pacientes para probar el programa
hospital.agregar_paciente(Paciente("Juan", 2))
hospital.agregar_paciente(Paciente("Maria", 1)) 
hospital.agregar_paciente(Paciente("Pedro", 3))
hospital.agregar_paciente(Paciente("Juan", 1))
siguiente= hospital.siguiente_paciente()
print(f"Siguiente paciente a atender: {siguiente.nombre} con prioridad {siguiente.prioridad}")
siguiente= hospital.siguiente_paciente()
print(f"Siguiente paciente a atender: {siguiente.nombre} con prioridad {siguiente.prioridad}")

print("----------------------------------------------------------------")


#un programa que me permita programar tareas y me diga
#cual es la siguiente tarea a realizar segun calendario
#yo ingreso la cantidad de tareas la descripcion y la fecha
from datetime import datetime
class Tarea:
    def __init__(self, descripcion, fecha):
        self.descripcion= descripcion
        self.fecha= datetime.strptime(fecha, "%Y-%m-%d")
    
    def __lt__(self, otro):
        return self.fecha < otro.fecha
class Calendario:
    def __init__(self):
        self.tareas= []
    
    def agregar_tarea(self, tarea):
        heapq.heappush(self.tareas, tarea)
    
    def siguiente_tarea(self):
        if not self.tareas:
            return None
        return heapq.heappop(self.tareas)
calendario= Calendario()
#hazlo con input para que el usuario ingrese la cantidad de tareas, descripcion y fecha
cantidad_tareas= int(input("Ingrese la cantidad de tareas: "))
for _ in range(cantidad_tareas):
    descripcion= input("Ingrese la descripción de la tarea: ")
    fecha= input("Ingrese la fecha de la tarea (YYYY-MM-DD): ")
    calendario.agregar_tarea(Tarea(descripcion, fecha))
siguiente= calendario.siguiente_tarea()
print(f"Siguiente tarea a realizar: {siguiente.descripcion} con fecha {siguiente.fecha.strftime('%Y-%m-%d')}")


