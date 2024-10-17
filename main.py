"""
Nom: Nicolas Rodriguez
Groupe: 406
Description: Combat de monstres
"""

import random

print("TP3 - Combat de Monstres\n")

hp = 40
num_encounters = 0
past_battle = "aucun"
consecutive_victories = 0
victories = 0
defeats = 0
skip_exploit_possible = False
boss_encountered = False
end_game = False
num_monsters = 1
enemy = None
enemy_strength = 0
difficulty_1 = None
difficulty_2 = None
difficulty_3 = None


def monster_generate():
    global num_monsters
    global boss_encountered
    global difficulty_1
    global difficulty_2
    global difficulty_3

    if not boss_encountered:
        num_monsters = random.randint(1, 3)

        difficulty_1 = random.randint(3, 9)
        difficulty_2 = random.randint(3, 9)
        difficulty_3 = random.randint(3, 9)

        if num_monsters == 1:
            print(f"\nVous tombez face à face avec un adversaire. C'est un monstre d'une difficulté de "
                  f"{difficulty_1}\n")

        elif num_monsters == 2:
            print(f"\nVous tombez face à face avec deux adversaires. Ces monstres ont une difficulté de "
                  f"{difficulty_1} et {difficulty_2}\n")

        elif num_monsters == 3:
            print(f"\nVous tombez face à face avec trois adversaires. Ces monstres ont une difficulté de "
                  f"{difficulty_1}, {difficulty_2} et {difficulty_3}\n")

    elif boss_encountered:
        print("\nVous tombez face à face avec le boss. C'est un monstre d'une difficulté de 11\n")


def battle_sequence():
    global hp
    global victories
    global defeats
    global past_battle
    global consecutive_victories
    global boss_encountered
    global exit_room
    global monsters_left
    global enemy

    # on s'assure que le boss n'apparait qu'une fois par 3 victoires
    if victories / 3 is int and not boss_encountered:
        boss_encountered = True
        enemy = "le boss"
        exit_room = True

    else:
        enemy = "cet adversaire"

    if num_monsters > 1:
        print(f"\nVous allez vous battre avec l'adversaire #{battle_num}. C'est un monstre d'une difficulté de "
              f"{enemy_strength}\n")

    # message d'erreur personnalisé
    battle = int(input(f"Que voulez-vous faire? :"
                       f"\n1- Combattre {enemy}"
                       f"\n2- Contourner {enemy}"
                       f"\n3- Quitter la partie\n\n"))

    if battle == 1:
        dice = random.randint(1, 6) + random.randint(1, 6)

        print(f"\nStatu de la partie:"
              f"\n- Monstre rencontré #{num_encounters}"
              f"\n- Adversaire avec {enemy_strength} de force"
              f"\n- Vous avez {hp} point(s) de vie"
              f"\n- Combat #{num_encounters}: {victories} victoires et {defeats} défaites"
              f"\n- Résultat de la dernière bataille: {past_battle}"
              f"\n- Résultat de votre lancer: {dice}\n")

        print("\nOn lance le dé")

        if dice > enemy_strength:
            victories += 1
            consecutive_victories += 1
            hp += enemy_strength
            past_battle = "Victoire"
            print(f"Victoire:"
                  f"\n- Vous avez {hp} point(s) de vie"
                  f"\n- Vous avez gagné {consecutive_victories} victoires consécutives\n")

            if boss_encountered:
                boss_encountered = False

        elif dice <= enemy_strength:
            defeats += 1
            consecutive_victories = 0
            hp -= enemy_strength
            past_battle = "Défaite"
            print(f"Défaite:"
                  f"\n- Vous avez {hp} point(s) de vie\n")

        monsters_left -= 1

    elif battle == 2:

        if not boss_encountered:
            hp -= 1
            print(f"\nVous perdez 1 point de vie en vous échapant."
                  f"\nVous avez {hp} point(s) de vie\n")
            exit_room = True

        elif boss_encountered:
            print("\nVous ne pouvez pas contourner le boss\n")
            boss_encountered = False

    else:
        exit("\nMerci et au revoir...")


while not end_game:
    while hp > 0:
        num_encounters += 1
        battle_num = 0
        monster_generate()

        if not boss_encountered:
            exit_room = False
            monsters_left = num_monsters

            while not exit_room and monsters_left != 0:
                for i in range(num_monsters):
                    battle_num += 1

                    if battle_num == 1:
                        enemy_strength = difficulty_1

                    elif battle_num == 2:
                        enemy_strength = difficulty_2

                    elif battle_num == 3:
                        enemy_strength = difficulty_3

                    battle_sequence()

                exit_room = True

        elif boss_encountered:
            num_monsters = 1
            enemy_strength = 11
            battle_sequence()

        view_rules = input("\nVoulez-vous voir les règles du jeu? (o/n'importe quelle clé)\n\n")

        if view_rules == "o":
            print("\nPour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de"
                  " l’adversaire."
                  "\nSi on a plusieurs adversaires, on se bat avec le premier, puis le deuxième et ainsi de suite."
                  "\nDans le cas d'une victoire, le niveau de vie de l’usager est augmenté de la force de"
                  " l’adversaire."
                  "\nUne défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la"
                  " force de l’adversaire."
                  "\nDans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.\n"
                  "\nLa partie se termine lorsque les points de vie de l’usager tombent sous 0.\n"
                  "\nL’usager peut combattre ou éviter les adversaires, dans le cas de l’évitement,"
                  " il y a une pénalité d'un point de vie.\n")

    print(f"\nVous êtes mort..."
          f"\n\nVous avez vaincu {victories} monstre(s) en total.")
    end_game = True
