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
skip_exploit_possible = False
boss_encountered = False
end_game = False


def monster_generate():
    global skip_exploit_possible
    global boss_encountered
    # les monstres normaux seronts toujours plus faibles que le boss
    normal_monster = random.randint(1, 4)
    boss_monster = 5

    # empècher un "exploit" qui permet de contourner sans perdre de point de vie
    if not skip_exploit_possible:

        if boss_encountered:
            return boss_monster

        elif not boss_encountered:
            return normal_monster

    elif skip_exploit_possible:
        skip_exploit_possible = False

        if boss_encountered:
            return boss_monster

        elif not boss_encountered:
            return previous_monster


while not end_game:

    while hp > 0:
        num_encounters += 1
        difficulty = 0

        # on s'assure que le boss n'apparait qu'une fois
        if victories == 3 and not boss_encountered:
            boss_encountered = True
            enemy = "le boss"
            difficulty = monster_generate()
            print(f"\nVous tombez face à face avec le boss. C'est un monstre d'une difficulté de {difficulty}\n")

        else:
            enemy = "cet adversaire"
            difficulty = monster_generate()
            print(f"\nVous tombez face à face avec un adversaire d'une difficulté de {difficulty}\n")
            previous_monster = difficulty

        # message d'erreur personnalisé
        try:
            battle = int(input(f"Que voulez-vous faire? :"
                               f"\n1- Combattre {enemy}"
                               f"\n2- Contourner {enemy} et aller ouvrir une autre porte"
                               f"\n3- Afficher les règles du jeu"
                               f"\n4- Quitter la partie\n\n"))
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

                # s'assurer que le joueur se bat contre le boss
                if not boss_encountered:
                    hp -= 1
                    print(f"\nVous perdez 1 point de vie en vous échapant du monstre."
                          f"\nVous avez {hp} point(s) de vie\n")

                elif boss_encountered:
                    # pour que le joueur rencontre le boss encore
                    boss_encountered = False
                    print("\nVous ne pouvez pas contourner le boss\n")

            elif battle == 3:
                skip_exploit_possible = True
                print("\nPour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de"
                      " l’adversaire."
                      "\nDans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire."
                      "\nUne défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la"
                      " force de l’adversaire."
                      "\nDans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.\n"
                      "\nLa partie se termine lorsque les points de vie de l’usager tombent sous 0.\n"
                      "\nL’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a"
                      " une pénalité d'un point de vie.\n")

            elif battle == 4:
                exit("\nMerci et au revoir...")

        except ValueError:
            print("\nEntrez un numéro.\n")
            skip_exploit_possible = True

    print(f"\nVous êtes mort."
          f"\nVous avez vaincu {victories} monstre(s) en total.")
