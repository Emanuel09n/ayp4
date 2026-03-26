from collections import deque

class Jugador:
    def __init__(self, jugador_id, nivel):
        self.jugador_id = jugador_id
        self.nivel = nivel

    def __str__(self):
        return f"ID: {self.jugador_id}, Nivel: {self.nivel}"


class Matchmaking:
    def __init__(self):
        self.cola = deque()

    def agregar_jugador(self, jugador_id, nivel):
        nuevo_jugador = Jugador(jugador_id, nivel)

        for i, jugador_esperando in enumerate(self.cola):
            if abs(jugador_esperando.nivel - nuevo_jugador.nivel) <= 150:
                pareja = self.cola[i]
                del self.cola[i]
                print(f"\nEmparejados: {nuevo_jugador} <--> {pareja}\n")
                return

        self.cola.append(nuevo_jugador)
        print(f"\nNo se encontró pareja para {nuevo_jugador}. Queda en cola.\n")

    def mostrar_cola(self):
        if not self.cola:
            print("\nLa cola está vacía.\n")
        else:
            print("\nJugadores en cola:")
            for jugador in self.cola:
                print(jugador)
            print()


sistema = Matchmaking()

while True:
    print("1. Agregar jugador")
    print("2. Mostrar cola")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        jugador_id = input("Ingrese ID del jugador: ")
        nivel = int(input("Ingrese nivel del jugador: "))
        sistema.agregar_jugador(jugador_id, nivel)

    elif opcion == "2":
        sistema.mostrar_cola()

    elif opcion == "3":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción no válida.\n")