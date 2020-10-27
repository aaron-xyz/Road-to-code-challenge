# determina el ganador de 2 jugadores para el juego piedra, papel o tijera
def rockPaperScissors(player1, player2):
    # situaciones a favor del jugador 1
    if (player1 == "piedra" and player2 == "papel") or (player1 == "papel" and player2 == "tijeras") or (player1 == "tijeras" and player2 == "piedra"):
        return "Jugador 2"
    # situaciones a favor del jugador 2
    elif (player1 == "papel" and player2 == "piedra") or (player1 == "tijeras" and player2 == "papel") or (player1 == "piedra" and player2 == "tijeras"):
        return "Jugador 1"
    # situaciones de empate
    elif player1 == player2:
        return "Empate"
    # Ocurrio algun error
    else:
        return "Ingresa un valor valido. [piedra/papel/tijera]"

if __name__ == '__main__':
    player1 = input("Elige: piedra, papel o tijera [Jugador 1]: ")
    player2 = input("Elige: piedra, papel o tijera [Jugador 2]: ")
    result = rockPaperScissors(player1, player2)
    print(f"El resultado es para: {result}")