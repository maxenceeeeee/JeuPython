
=======

## CLASSE DE BASE : PIECE

# piece.py
from .porte import Porte

class Piece:
    """Représente une pièce du manoir, avec sa couleur, ses items et ses portes."""

 # piece.py
from .porte import Porte

class Piece:
    """Représente une pièce du manoir, avec sa couleur, ses items et ses portes."""

    def __init__(self, nom, couleur, portes, items):
        """
        Initialise une pièce du manoir.

        Args:
            nom (str): Nom de la pièce.
            couleur (str): Couleur principale de la pièce (ex: 'bleue', 'dorée', etc.).
            portes (dict): Dictionnaire indiquant les directions et si une porte est présente (True/False).
            items (list): Liste des objets présents dans la pièce.
        """
        self.nom = nom
        self.couleur = couleur
        self.items = items or []
        # Création d'un dictionnaire de portes (porte ouverte -> instance de Porte, sinon None)
        self.portes = {
            direction: Porte() if ouverte else None
            for direction, ouverte in portes.items()
        }

    def afficher_infos(self):
        """Affiche les informations principales de la pièce."""
        print(f"Pièce : {self.nom}")
        print(f"Couleur : {self.couleur.capitalize()}")
        print(f"Items : {', '.join(self.items) if self.items else 'Aucun'}")
        print("Portes :")
        for direction, porte in self.portes.items():
            if porte:
                print(f"  - {direction} (niveau {porte.niveau_verrou})")
        print()
