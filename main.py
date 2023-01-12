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
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"],
]

player_cross = "X"
player_tac = "O"

# Mise en place des lignes de ma grille
def display_grille(grille:list) -> str:
    """
    Fonction qui prend une liste et qui va devoir décomposer cette liste pour en faire une grille.
    :param grille: La liste contenant la grille.
    :return: La grille qui apparaît dans la console.
    """
    for space in grille:
        print(" ".join(space))


def check_grille(grille:list) -> str or bool:
    """
    Fonction qui va vérifier si la grille est remplie.
    :param grille: La liste contenant la grille.
    :return: Une vérification de si la liste est complétée par les joueurs et empêchant les joueurs de jouer l'un sur l'autre.
    """

    for lines in grille[0][2]:
        if lines[0] == lines[1] == lines[2] and lines[0] != None:
            return True
        for i in range(3):
            if grille[0][i] == grille[1][i] == grille[2][i] and grille[0][i] != None:
                return True
            for diagonal in lines and i:
                if diagonal[lines[0][i[0]]] == diagonal[lines[1][i[1]]] == diagonal[lines[2][i[2]]] and diagonal[lines[0][i[0]]] != None:
                    return True
            for diagonal_reverse in lines and i:
                if diagonal_reverse[lines[0][i[2]]] == diagonal_reverse[lines[1][i[1]]] == diagonal_reverse[lines[2][i[0]]] and diagonal_reverse[lines[0][i[2]]] != None:
                    return True

    return False


while True:
    display_grille(grille)
    ask_players_line = int(input("Dans quelle ligne souhaitez-vous jouer ? [1] - [2] - [3] :"))
    ask_players_column = int(input("Dans quelle colonne souhaitez-vous jouer ? [1] - [2] - [3] :"))

    for lines in grille:
        if ask_players_line ==
    break