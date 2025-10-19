## CLASSE DE BASE : PIECE

from ClassePorte import *
import pygame
import os
from zipfile import ZipFile
from io import BytesIO
from Catalogue_pieces import catalogue_pieces

class Piece:
    """Représente une pièce du manoir, avec sa couleur, ses items et ses portes."""

    def __init__(self, nom, couleur, portes, items, image):
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
        self.portes_objets = {}
        self.items = items or []
        self.image_nom = image 
        self.image = None  
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

    def niveau_porte(self, direction: str) -> int:
        porte = self.portes_objets.get(direction)
        if porte is not None:
            return porte.niveau
        else:
            return -1
        
    def charger_image(self, zip_path="Images.zip"):
        if self.image is not None:
            return
        with ZipFile(zip_path, "r") as archive:
            try:
                with archive.open(self.image_nom) as file:
                    file_bytes = BytesIO(file.read())
                    # Correction pour Pygame : se repositionner au début du flux
                    file_bytes.seek(0) 
                    self.image = pygame.image.load(file_bytes).convert_alpha()
            except KeyError:
                print(f"Image {self.image_nom} non trouvée dans le zip.")