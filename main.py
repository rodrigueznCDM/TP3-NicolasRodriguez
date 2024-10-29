"""
Nom: Nicolas Rodriguez
Groupe: 406
Description: Combat de monstres
"""

import random

print("TP3 - Combat de Monstres\n")

hp = 40
num_encounters = 0
consecutive_victories = 0
victories = 0
defeats = 0
enemy_strength = 0
past_battle = "aucun"
boss_encountered = False


while hp > 0:
    num_encounters += 1
    battle_num = 0
    exit_room = False
    num_monsters = random.randint(1, 3)
    monsters_left = num_monsters
    difficulty_1 = random.randint(3, 9)
    difficulty_2 = random.randint(3, 9)
    difficulty_3 = random.randint(3, 9)

    while monsters_left != 0:
        battle_num += 1
        if battle_num == 1:
            enemy_strength = difficulty_1
        elif battle_num == 2:
            enemy_strength = difficulty_2
        elif battle_num == 3:
            enemy_strength = difficulty_3

        end_battle = False
        while not end_battle:
            if victories % 3 == 0 and victories != 0:
                print("\nVous êtes téléporté dans l'arène du boss. C'est un monstre d'une difficulté de 11\n")
                boss_encountered = True
                enemy = "le boss"
                enemy_strength = 11
                monsters_left = 1
            else:
                enemy = "cet adversaire"
                if num_monsters == 1:
                    print(f"\nVous tombez face à face avec un adversaire. C'est un monstre d'une difficulté de "
                          f"{enemy_strength}\n")
                elif num_monsters > 1:
                    print(f"\nVous tombez face à face avec l'adversaire #{battle_num} dans la pièce. C'est un monstre "
                          f"d'une difficulté de {enemy_strength}\n")

            battle = input(f"Que voulez-vous faire? :"
                           f"\n1- Combattre {enemy}"
                           f"\n2- Contourner {enemy}"
                           f"\n3- Voir les règles"
                           f"\n4- Quitter la partie\n\n")
            if battle.isdigit():
                battle = int(battle)
                if 4 >= battle >= 1:

                    if battle == 1:
                        dice = random.randint(1, 6) + random.randint(1, 6)
                        print("\nOn lance le dé...\n")
                        print(f"\nStatu de la partie:"
                              f"\n- Monstre rencontré #{num_encounters}"
                              f"\n- Adversaire avec {enemy_strength} de force"
                              f"\n- Vous avez {hp} point(s) de vie"
                              f"\n- Combat #{num_encounters}: {victories} victoires et {defeats} défaites"
                              f"\n- Résultat de la dernière bataille: {past_battle}"
                              f"\n- Résultat de votre lancer: {dice}\n")
                        if dice > enemy_strength:
                            victories += 1
                            consecutive_victories += 1
                            hp += enemy_strength
                            past_battle = "Victoire"
                            print(f"Victoire:"
                                  f"\n- Vous avez {hp} point(s) de vie"
                                  f"\n- Vous avez gagné {consecutive_victories} victoires consécutives\n")
                            end_battle = True
                            if boss_encountered:
                                boss_encountered = False
                        elif dice <= enemy_strength:
                            defeats += 1
                            consecutive_victories = 0
                            hp -= enemy_strength
                            past_battle = "Défaite"
                            print(f"Défaite:"
                                  f"\n- Vous avez {hp} point(s) de vie\n")
                            end_battle = True
                        monsters_left -= 1

                    elif battle == 2:
                        if not boss_encountered:
                            hp -= 1
                            print(f"\nVous perdez 1 point de vie en vous échapant."
                                  f"\nVous avez {hp} point(s) de vie\n")
                            monsters_left -= 1
                            end_battle = True
                        elif boss_encountered:
                            print("\nVous ne pouvez pas contourner le boss\n")

                    elif battle == 3:
                        print("\nPour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la"
                              " force de l’adversaire."
                              "\nSi on a plusieurs adversaires, on se bat avec le premier, puis le deuxième et"
                              " ainsi de suite."
                              "\nDans le cas d'une victoire, le niveau de vie de l’usager est augmenté de la force"
                              " de l’adversaire."
                              "\nUne défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou"
                              " égale à la force de l’adversaire."
                              "\nDans ce cas, le niveau de vie de l’usager est diminué de la force de"
                              " l’adversaire.\n"
                              "\nLa partie se termine lorsque les points de vie de l’usager tombent sous 0.\n"
                              "\nL’usager peut combattre ou éviter les adversaires, dans le cas de l’évitement,"
                              " il y a une pénalité de 1 point de vie.\n")

                    elif battle == 4:
                        exit("\nMerci et au revoir...")

                else:
                    print("\nEntrez un numéro de 1 à 4\n")

            else:
                print("\nEntrez un numéro de 1 à 4\n")

print(f"\nVous êtes mort..."
      f"\n\nVous avez vaincu {victories} monstre(s) en total.")
end_game = True
