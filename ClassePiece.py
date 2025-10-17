## CLASSE DE BASE : PIECE
from portes import Porte 

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
            portes (dict): Dictionnaire (DU CATALOGUE) indiquant la présence de portes (haut, bas, gauche, droite).
            ...
        """
        self.nom = nom
        self.couleur = couleur
        # Stocke la configuration de base (quelles portes EXISTENT)
        self.portes_config = portes if portes else {"haut": False, "bas": False, "gauche": False, "droite": False}
        self.cout_gemmes = cout_gemmes
        self.objets = objets if objets else []
        self.effet = effet
        self.rarete = rarete
        self.condition_placement = condition_placement
        self.image_path = image_path
        self.secrets = secrets if secrets else []
        self.upgrades = upgrades if upgrades else []
        
        
        # Ce dictionnaire stockera les VRAIS objets Porte (avec niveau, état ouverte/fermée)
        # Il sera rempli par le Manoir lors du placement de la pièce.
        self.portes_objets = {
            "haut": None,
            "bas": None,
            "gauche": None,
            "droite": None
        }

    def get_porte(self, direction: str) -> Porte | None:
        """
        Récupère l'objet Porte dans une direction donnée.
        """
        return self.portes_objets.get(direction)

    def get_door_lock_level(self, direction: str) -> int:
        """
        Récupère le niveau de verrouillage (0, 1, 2) d'une porte dans une direction.
        Requis par jeu.py
        """
        porte = self.get_porte(direction)
        if porte:
            # Si la porte est déjà ouverte, elle n'a plus de niveau de verrouillage
            if porte.ouverte:
                return 0
            return porte.niveau
        
        # S'il n'y a pas d'objet Porte, c'est un mur (ou une porte inexistante)
        return -1 # On retourne -1 pour signifier "pas de porte"
