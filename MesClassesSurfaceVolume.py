class CalculateurSurface:

    # Initialisons la classe
    def __init__(self, precision):
        self.precision = precision

    def calculer_aire_rectangle(self, longueur, largeur):
        aire = longueur * largeur
        return round(aire, self.precision)

    def calculer_aire_cercle(self, rayon):
        import math
        aire = math.pi * rayon ** 2
        return round(aire, self.precision)

class CalculateurVolume:

    def __init__(self, precision):
        self.precision = precision

    def calculer_volume_parallelepipede(self, longueur, largeur, hauteur):

        volume = longueur * largeur * hauteur
        return round(volume, self.precision)

    def calculer_volume_sphere(self, rayon):
        volume = (4/3) * math.pi * rayon ** 3
        return round(volume, self.precision)