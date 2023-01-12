"""
1 - Définir la grille - ✅
1.5 - Affichage de l'interface - ✅
2 - Vérification de la grille - ⏳
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

display_grille(grille)


def check_grille(grille:list) -> str or bool:
    """
    Fonction qui va vérifier si la grille est remplie.
    :param grille: La liste contenant la grille.
    :return: Une vérification de si la liste est complétée par les joueurs et empêchant les joueurs de jouer l'un sur l'autre.
    """

    for lines in grille:
        if lines[0] == lines[1] == lines[2] and lines[0] != None:
            return True
        for i in range(3):
            if grille[0][i] == grille[1][i] == grille[2][i] and grille[0][i] != None:
                return True
            for diagonal in grille:
                if lines[0] == i[0] == lines[1] == i[1] == lines[2] == i[2] and (lines[0] and i[0]) != None:
                    return True

    return False






