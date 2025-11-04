from ClassePorte import *
import pygame
import os
from zipfile import ZipFile
from io import BytesIO
from Catalogue_pieces import catalogue_pieces
import random

class Piece:
    """
    Représente une pièce du manoir.
    
    Chaque pièce a : 
        - un nom,
        - une couleur,
        - des portes (qui seront des instances de Porte),
        - un loot (objets garanis, aléatoires, ou boutique)
        - une image pour l'affichage,
        - un coût en gemmes pour la selectionner,
        - un niveau de rareté.
    """

    def __init__(self, nom, couleur, portes, loot, image, cout_gemmes=0, rarete=0, endroits_creuser=0):
        """
        Initialise une pièce du manoir.

        Args:
            nom (str): Nom de la pièce.
            couleur (str): Couleur principale de la pièce (ex: 'bleue', 'dorée', etc.).
            portes (dict): Dictionnaire indiquant les directions et si une porte est présente (True/False).
            loot (dict): Dictionnaire de butin (garanti, aleatoire) et boutique.
            image (str): Nom du fichier image.
            cout_gemmes (int): Coût en gemmes pour choisir cette pièce. 
            rarete (int): Rareté de la pièce (0-3).
        """
        self.nom = nom
        self.couleur = couleur
        self.portes_objets = {}
        self.loot = loot or {}  
        self.image_nom = image 
        self.image = None  
        self.cout_gemmes = cout_gemmes
        self.rarete = rarete
        self.portes = portes
        self.magasin = self.loot.get("magasin", None)
        
        # Gestion des endroits à creuser
        self.endroits_creuser = endroits_creuser
        self.endroit_creuse = False

    def afficher_infos(self):
        """Affiche les informations principales de la pièce."""
        print(f"Pièce : {self.nom}")
        print(f"Couleur : {self.couleur.capitalize()}")
        print(f"Loot : {self.loot}")
        print(f"Coût : {self.cout_gemmes} gemmes, Rareté : {self.rarete}")
        print(f"Endroits à creuser : {self.endroits_creuser} (creusé: {self.endroit_creuse})")
        print("Portes :")
        for direction, porte in self.portes.items():
            if porte:
                print(f"  - {direction} (niveau {porte.niveau})")
        print()

    def niveau_porte(self, direction: str) -> int:
        porte = self.portes_objets.get(direction)
        if porte is not None:
            return porte.niveau
        else:
            return -1

    def peut_creuser(self) -> bool:
        """Vérifie si on peut creuser dans cette pièce."""
        return self.endroits_creuser > 0 and not self.endroit_creuse

    def creuser(self, patte_lapin_active: bool) -> dict:
            """
            Tente de creuser dans la pièce. Retourne un dictionnaire avec:
            - 'success': True si creusage réussi et objet trouvé, False si échec
            - 'objet': nom de l'objet trouvé (si success=True)
            - 'message': message à afficher
            """
            if not self.peut_creuser():
                return {'success': False, 'message': "Aucun endroit où creuser ici ou déjà creusé."}
            
            # Marquer comme creusé
            self.endroit_creuse = True
            
            chance_base = 0.6
            if patte_lapin_active:
                chance_base = min(1.0, chance_base + 0.2) # Augmente la chance de succès de 20% max 100%

            # Déterminer si on trouve quelque chose
            if random.random() < chance_base:
                # Table de loot pour le creusage
                loot_possibles = [
                    ("Pièce d'Or", 0.3),
                    ("Clé", 0.25), 
                    ("Gemme", 0.2),
                    ("Pomme", 0.1),
                    ("Banane", 0.08),
                    ("Gâteau", 0.05),
                    ("Dé", 0.02)
                ]
                
                # Tirer un objet au sort selon les probabilités
                objet_trouve = None
                r = random.random()
                cumul = 0
                for objet, proba in loot_possibles:
                    cumul += proba
                    if r <= cumul:
                        objet_trouve = objet
                        break
                
                # S'assurer de toujours trouver quelque chose si succès
                if objet_trouve is None:
                    objet_trouve = "Pièce d'Or" 

                return {
                    'success': True, 
                    'objet': objet_trouve,
                    'message': f"Vous creusez et trouvez : {objet_trouve} !"
                }
            else:
                return {
                    'success': False,
                    'message': "Vous creusez mais ne trouvez rien..."
                }
        
    def charger_image(self, zip_path="Images.zip"):
        """
        Charger l'image de la pièce depuis un fichier ZIP contenant toutes les images.
        """
        if self.image is not None:
            return
        
        script_dir = os.path.dirname(__file__)
        zip_path_complet = os.path.join(script_dir, zip_path)
        
        if not os.path.exists(zip_path_complet):
            print(f"Erreur : {zip_path_complet} non trouvé.")
            self._creer_image_par_defaut()
            return

        try:
            with ZipFile(zip_path_complet, "r") as archive:
                # Vérifier si l'image existe dans le ZIP
                if self.image_nom in archive.namelist():
                    with archive.open(self.image_nom) as file:
                        file_bytes = BytesIO(file.read())
                        file_bytes.seek(0) 
                        self.image = pygame.image.load(file_bytes).convert_alpha()
                else:
                    print(f"Image {self.image_nom} non trouvée dans {zip_path_complet}")
                    self._creer_image_par_defaut()
        except Exception as e:
            print(f"Erreur chargement image {self.image_nom}: {e}")
            self._creer_image_par_defaut()

    def _creer_image_par_defaut(self):
        """Crée une image par défaut avec la couleur de la pièce."""
        self.image = pygame.Surface((80, 80))
        couleurs = {
            "bleue": (0, 0, 255),
            "dorée": (255, 215, 0),
            "verte": (0, 255, 0),
            "violette": (128, 0, 128),
            "grise": (128, 128, 128),
            "blanche": (255, 255, 255),
            "brune": (139, 69, 19)
        }
        couleur = couleurs.get(self.couleur, (128, 128, 128))
        self.image.fill(couleur)
        font = pygame.font.Font(None, 15)
        mots = self.nom.split()
        for i, mot in enumerate(mots):
            text = font.render(mot, True, (0, 0, 0))
            text_rect = text.get_rect(center=(40, 30 + i*15))
            self.image.blit(text, text_rect)