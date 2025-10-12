
## CLASSE DE BASE : PIECE

class Piece:
    """
    Une classe générale pour une pièce du manoir avec les attributs communs à toutes les pièces.
    """

    def __init__(self, nom, couleur, portes=None, cout_gemmes=0, objets=None, effet="",
                 rarete=0, condition_placement="", image_path="", secrets=None, upgrades=None):
        """
        Initialise une pièce du manoir.

        Args:
            nom (str): Nom de la pièce.
            couleur (str): Couleur thématique de la pièce.
            portes (dict): Dictionnaire indiquant la présence de portes (haut, bas, gauche, droite).
            cout_gemmes (int): Coût en gemmes pour drafter la pièce.
            objets (list): Liste d'objets présents dans la pièce.
            effet (str): Effet principal de la pièce.
            rarete (int): Rareté de la pièce (0 = commune, 1 = rare, etc.).
            condition_placement (str): Condition ou restriction de placement.
            image_path (str): Chemin vers l'image représentant la pièce.
            secrets (list): Liste des secrets ou interactions spéciales de la pièce.
            upgrades (list): Liste des améliorations possibles pour la pièce.
        """
        self.nom = nom
        self.couleur = couleur
        self.portes = portes if portes else {"haut": False, "bas": False, "gauche": False, "droite": False}
        self.cout_gemmes = cout_gemmes
        self.objets = objets if objets else []
        self.effet = effet
        self.rarete = rarete
        self.condition_placement = condition_placement
        self.image_path = image_path
        self.secrets = secrets if secrets else []
        self.upgrades = upgrades if upgrades else []

    