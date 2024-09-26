"""
Nom: Nicolas Rodriguez
Groupe: 406
Description: Combat de monstres
"""

import random

print("TP3 - Combat de Monstres\n")
hp = 20
num_ennemies = 0
battle_result = "aucun"
consecutive_victories = 0
victories = 0
defeats = 0


def monster_generate():
    monster = random.randint(1, 5)
    return monster


while hp > 0:
    difficulty = monster_generate()
    print(f"Vous tombez face à face avec un adversaire d'une difficulté de {difficulty}.")
    num_ennemies += 1
    battle = int(input("Que voulez-vous faire? :\n1- Combattre cet adversaire\n2- Contourner cet adversaire et aller ouvrir une autre porte\n3- Afficher les règles du jeu\n4- Quitter la partie"))

    try:
        if battle == 1:
            dice = random.randint(1, 6)
            print(f"Statu de la partie:"
                  f"-Advesaire #{num_ennemies}"
                  f"-Adversaire avec {difficulty} de force"
                  f"-Vous avez {hp} de vie"
                  f"-Combat #{num_ennemies} avec {victories} victoires et {defeats} défaites"
                  f"\nVotre lancer: {dice}"
                  f"\nRésultat de la dernière bataille: {battle_result}")

            if dice > difficulty:
                victories += 1
                battle_result = "Victoire"

            elif dice <= difficulty:
                defeats += 1
                hp -= difficulty
                battle_result = "Défaite"

            print(f"Statu de la partie:"
                  f"-Advesaire #{num_ennemies}"
                  f"-Adversaire avec {difficulty} de force"
                  f"-Vous avez {hp} de vie"
                  f"-Combat #{num_ennemies} avec {victories} victoires et {defeats} défaites"
                  f"\nVotre lancer: {dice}"
                  f"\nRésultat de le bataille: {battle_result}")

        elif battle == 2:
            hp -= 1
            print("\nVous perdez 1 point de vie en vous échapant du monstre.\n")

        elif battle == 3:
            print(f"\nPour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire."
                  f"Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire."
                  f"Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire."
                  f"Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.\n"
                  f"La partie se termine lorsque les points de vie de l’usager tombent sous 0.\n"
                  f"L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.\n")

        elif battle == 4:
            exit("Merci et au revoir...")

    except ValueError:
        print("\nEntrez un numéro.")
