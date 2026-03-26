class Jugador:
    def __init__(self, jugador_id, nivel):
        self.jugador_id = jugador_id
        self.nivel = nivel

    def __str__(self):
        return f"ID: {self.jugador_id}, Nivel: {self.nivel}"


class Matchmaking:
    def __init__(self):
        self.cola = []   # lista para guardar jugadores en orden de llegada

    def agregar_jugador(self, jugador_id, nivel):
        nuevo_jugador = Jugador(jugador_id, nivel)

        # Buscar al primer jugador válido en la cola
        for i in range(len(self.cola)):
            jugador_esperando = self.cola[i]

            if abs(jugador_esperando.nivel - nuevo_jugador.nivel) <= 150:
                # pop(i) elimina y devuelve al jugador encontrado
                pareja = self.cola.pop(i)
                print(f"\nEmparejados: {nuevo_jugador} <--> {pareja}\n")
                return

        # Si no encuentra pareja, se queda en cola
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


# ----------------------------
# Ejemplo de uso
# ----------------------------
mm = Matchmaking()

mm.agregar_jugador(1, 1200)
mm.agregar_jugador(2, 1600)
mm.agregar_jugador(3, 1300)   # se empareja con el 1
mm.agregar_jugador(4, 1700)   # se empareja con el 2
mm.agregar_jugador(5, 2500)

mm.mostrar_cola()