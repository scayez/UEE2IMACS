def calculer_aire_rectangle_mod2(longueur, largeur):
    """Cette fonction calcule l'aire d'un rectangle avec des valeurs numériques de longueur et largeur."""
    aire = longueur * largeur
    return aire

if __name__ == '__main__':
    # Exemple d'utilisation en tant que programme principal
    longueur = 5
    largeur = 9
    mon_aire = calculer_aire_rectangle_mod2(longueur, largeur)
    print(f"L'aire du rectangle de longueur {longueur} et largeur {largeur} est : {mon_aire}")