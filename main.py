"""
1 - Définir la grille
1.5 - Affichage de l'interface
2 - Joueur qui joue
3 - Autre Joueur qui joue
4 - Vérifier que les joueurs ne jouent pas sur l'autre
5 - Si un des joueurs fait une ligne de 3 le jeu s'arrête et le joueur gagne
6 - Si jamais aucun des joueurs n'aligne 3 objets alors la partie se termine sur un match nul
"""

# Définissons en premier les limites de la grille

grille = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"],
]

def display_grille(grille:list) -> str:
    """
    Fonction qui prend une liste et qui va devoir décomposer cette liste pour en faire une grille.
    :param grille: La liste contenant la grille.
    :return: La grille qui apparaît dans la console.
    """
    for i in grille:
       result = print(i)
    return result

print(display_grille(grille))