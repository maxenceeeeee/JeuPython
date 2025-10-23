## CLASSE DE BASE : PIECE

from ClassePorte import *
import pygame
import os
from zipfile import ZipFile
from io import BytesIO
from Catalogue_pieces import catalogue_pieces

class Piece:
    """Représente une pièce du manoir, avec sa couleur, ses items et ses portes."""

    def __init__(self, nom, couleur, portes, items, image, cout_gemmes=0, rarete=0):
        """
        Initialise une pièce du manoir.

        Args:
            nom (str): Nom de la pièce.
            couleur (str): Couleur principale de la pièce (ex: 'bleue', 'dorée', etc.).
            portes (dict): Dictionnaire indiquant les directions et si une porte est présente (True/False).
            items (list): Liste des objets présents dans la pièce.
            image (str): Nom du fichier image.
            cout_gemmes (int): Coût en gemmes pour choisir cette pièce. 
            rarete (int): Rareté de la pièce (0-3).
        """
        self.nom = nom
        self.couleur = couleur
        self.portes_objets = {} # C'est manoir.py qui va remplir ça
        self.items = items or []
        self.image_nom = image 
        self.image = None  
        self.cout_gemmes = cout_gemmes
        self.rarete = rarete
        
        #
        # On stocke le dictionnaire de configuration des portes (ex: {'haut': True, ...})
        # On NE CRÉE PAS d'objets Porte() ici.
        self.portes = portes
        

    def afficher_infos(self):
        """Affiche les informations principales de la pièce."""
        print(f"Pièce : {self.nom}")
        print(f"Couleur : {self.couleur.capitalize()}")
        print(f"Items : {', '.join(self.items) if self.items else 'Aucun'}")
        print(f"Coût : {self.cout_gemmes} gemmes, Rareté : {self.rarete}")
        print("Portes :")
        for direction, porte in self.portes.items():
            if porte:
                print(f"  - {direction} (niveau {porte.niveau_verrou})")
        print()

    def niveau_porte(self, direction: str) -> int:
        #On utilise portes_objets qui contient les instances de Porte
        porte = self.portes_objets.get(direction)
        if porte is not None:
            #L'attribut s'appelle 'niveau' dans ClassePorte.py
            return porte.niveau
        else:
            return -1
        
    def charger_image(self, zip_path="Images.zip"):
        if self.image is not None:
            return
        
        # Assumons que Images.zip est au même niveau que le script
        script_dir = os.path.dirname(__file__)
        zip_path_complet = os.path.join(script_dir, zip_path)
        
        if not os.path.exists(zip_path_complet):
            print(f"Erreur : {zip_path_complet} non trouvé.")
            # Créer une image de remplacement
            self.image = pygame.Surface((80, 80))
            self.image.fill((128, 0, 128)) # Une couleur flashy (violet) pour voir l'erreur
            font = pygame.font.Font(None, 20)
            text = font.render("IMG ZIP?", True, (255, 255, 255))
            text_rect = text.get_rect(center=(40, 40))
            self.image.blit(text, text_rect)
            return

        try:
            with ZipFile(zip_path_complet, "r") as archive:
                try:
                    with archive.open(self.image_nom) as file:
                        file_bytes = BytesIO(file.read())
                        file_bytes.seek(0) 
                        self.image = pygame.image.load(file_bytes).convert_alpha()
                except KeyError:
                    print(f"Image {self.image_nom} non trouvée dans {zip_path}.")
                    # Créer une image de remplacement
                    self.image = pygame.Surface((80, 80))
                    self.image.fill((200, 200, 0)) # Jaune pour image non trouvée
                    font = pygame.font.Font(None, 15)
                    text_lines = self.image_nom.split('/')
                    y = 25
                    for line in text_lines:
                        text = font.render(line, True, (0, 0, 0))
                        text_rect = text.get_rect(center=(40, y))
                        self.image.blit(text, text_rect)
                        y += 15
                        
        except FileNotFoundError:
             print(f"Fichier ZIP {zip_path_complet} non trouvé.")
             # Idem, image de remplacement
             self.image = pygame.Surface((80, 80))
             self.image.fill((128, 0, 128))
             font = pygame.font.Font(None, 20)
             text = font.render("NO ZIP", True, (255, 255, 255))
             text_rect = text.get_rect(center=(40, 40))
             self.image.blit(text, text_rect)
