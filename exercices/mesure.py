def vitesse(distance, temps):
    """
    Calcule la vitesse d'un objet en utilisant la formule v = distance / temps.

    Arguments:
        distance (float): La distance parcourue par l'objet en mètres.
        temps (float): Le temps écoulé pour parcourir la distance en secondes.

    Returns:
        float: La vitesse de l'objet en mètres par seconde.
    """
    v = distance / temps
    return v

def energie_cinetique(masse, vitesse):
    """
    Calcule l'énergie cinétique d'un objet en utilisant la formule E = (1/2) * masse * vitesse^2.

    Args:
        masse (float): La masse de l'objet en kilogrammes.
        vitesse (float): La vitesse de l'objet en mètres par seconde.

    Returns:
        float: L'énergie cinétique de l'objet en joules.
    """
    ec = (1/2) * masse * vitesse**2
    return ec
