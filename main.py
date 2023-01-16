"""
1 - Définir la grille - ✅
1.5 - Affichage de l'interface - ✅
2 - Vérification de la grille - ✅
3 - Joueur qui joue - ⏳
4 - Autre Joueur qui joue - ⏳
5 - Vérifier que les joueurs ne jouent pas sur l'autre - ⏳
6 - Si un des joueurs fait une ligne de 3 le jeu s'arrête et le joueur en question gagne - ⏳
7 - Si aucun des joueurs n'aligne 3 objets alors la partie se termine sur un match nul - ⏳
"""

# Définition de la grille

grille = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

player = "X"

# Mise en place des lignes de ma grille
def display_grille(grille:list) -> str:
    """
    Fonction qui prend une liste et qui va devoir décomposer cette liste pour en faire une grille.
    :param grille: La liste contenant la grille.
    :return: La grille qui apparaît dans la console.
    """
    for lines in grille:
        print("-".join(lines))


def check_grille(grille:list) -> str or bool:
    """
    Fonction qui va vérifier si la grille est remplie.
    :param grille: La liste contenant la grille.
    :return: Une vérification de si la liste est complétée par les joueurs et empêchant les joueurs de jouer l'un sur l'autre.
    """

    for lines in grille[0][2]:
        if lines[0] == player and lines[1] == player and lines[2] == player:
            return True
    for column in range(3):
        if grille[0][column] == player and grille[1][column] == player and grille[2][column] == player:
            return True
    if grille[0][0] == player and grille[1][1] == player and grille[2][2] == player:
        return True
    if grille[0][2] == player and grille[1][1] == player and grille[2][0] == player:
        return True
    return False



def play_game():
    current_player = 'X'
    while True:
        display_grille(grille)
        lines = int(input(f"{current_player} Veuillez choisir une ligne entre (0 1 2): "))
        column = int(input(f"{current_player} Veuillez choisir une colonne entre (0 1 2): "))
        if grille[lines][column] != ' ':
            print("La case est déjà prise.")
            continue
        grille[lines][column] = current_player
        if check_grille(grille, current_player):
            display_grille(grille)
            print(f"{current_player} gagne !")
            break
        current_player = 'X' if current_player == 'O' else 'O'

play_game()