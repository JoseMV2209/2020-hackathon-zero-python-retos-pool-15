from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):

    resultPlaer = player.lower()
    resultAI = ai.lower()
    result = ""

    if (resultPlaer == "papel" and resultAI == "piedra") or (resultPlaer == "piedra" and resultAI == "tijeras") or (resultPlaer == "tijeras" and resultAI == "papel"):
        result = "Ganaste!"
    elif (resultPlaer == "tijeras" and resultAI == "piedra") or (resultPlaer == "papel" and resultAI == "tijeras") or (resultPlaer == "piedra" and resultAI == "papel"):
        result = "Perdiste!"
    else:
        result = "Empate!"

    return result

# Entry Point
def Game():

    # player = input("Introduce piedra, papel o tijera: ")
    # ai = options[randint(0,2)]
    
    winner = quienGana(player, ai)

    print(winner)
