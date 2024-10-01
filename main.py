"""
Nom: Nicolas Rodriguez
Groupe: 406
Description: Combat de monstres
"""

import random

print("TP3 - Combat de Monstres\n")
hp = 20
num_encounters = 0
past_battle = "aucun"
consecutive_victories = 0
victories = 0
defeats = 0
rules_seen = False


def monster_generate():
    global rules_seen
    monster = random.randint(1, 5)

    if not rules_seen:
        return monster

    elif rules_seen:
        rules_seen = False
        return previous_monster


while hp > 0:
    num_encounters += 1
    difficulty = monster_generate()
    previous_monster = difficulty
    print(f"\nVous tombez face à face avec un adversaire d'une difficulté de {difficulty}\n")
    battle = int(input(f"Que voulez-vous faire? :"
                       f"\n1- Combattre cet adversaire"
                       f"\n2- Contourner cet adversaire et aller ouvrir une autre porte"
                       f"\n3- Afficher les règles du jeu"
                       f"\n4- Quitter la partie\n\n"))

    try:
        if battle == 1:
            dice = random.randint(1, 6)
            print(f"\nStatu de la partie:"
                  f"\n- Advesaire #{num_encounters}"
                  f"\n- Adversaire avec {difficulty} de force"
                  f"\n- Vous avez {hp} point(s) de vie"
                  f"\n- Combat #{num_encounters}: {victories} victoires et {defeats} défaites"
                  f"\n- Résultat de la dernière bataille: {past_battle}"
                  f"\n- Résultat de votre lancer: {dice}\n")

            if dice > difficulty:
                victories += 1
                consecutive_victories += 1
                past_battle = "Victoire"
                print(f"Victoire:"
                      f"\n- Vous avez {hp} point(s) de vie"
                      f"\n- Vous avez gagné {consecutive_victories} victoires consécutives\n")

            elif dice <= difficulty:
                defeats += 1
                consecutive_victories = 0
                hp -= difficulty
                past_battle = "Défaite"
                print(f"Défaite:"
                      f"\n- Vous avez {hp} point(s) de vie\n")

        elif battle == 2:
            hp -= 1
            print(f"\nVous perdez 1 point de vie en vous échapant du monstre."
                  f"\nVous avez {hp} point(s) de vie\n")

        elif battle == 3:
            rules_seen = True
            print(f"\nPour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de"
                  f" l’adversaire."
                  f"\nDans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire."
                  f"\nUne défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force"
                  f" de l’adversaire."
                  f"\nDans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.\n"
                  f"\nLa partie se termine lorsque les points de vie de l’usager tombent sous 0.\n"
                  f"\nL’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une"
                  f" pénalité de 1 point de vie.\n")

        elif battle == 4:
            exit("\nMerci et au revoir...")

    except ValueError:
        print("\nEntrez un numéro.\n")

print(f"\nVous êtes mort."
      f"\nVous avez vaincu {victories} monstre(s) en total.")
