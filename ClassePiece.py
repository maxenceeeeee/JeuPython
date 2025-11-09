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

    Attributs :
    # ... (Vos attributs existants)
        cadenas_casse (bool) : Indique si le cadenas du coffre a été brisé (False = verrouillé). NOUVEAU
        a_coffre (bool) : Indique si la pièce contient un coffre. NOUVEAU
    """

    def __init__(self, nom, couleur, portes, loot, image, cout_gemmes=0, rarete=0, endroits_creuser=0, a_coffre=False):
        """
        Initialise une pièce du manoir.

        Args:
        # ... (Vos Args existants)
            a_coffre (bool, optional) : Indique si la pièce contient un coffre verrouillé. Defaults to False.
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
        
        self.endroits_creuser = endroits_creuser
        self.endroit_creuse = False
        
        # GESTION DU CADENAS (COFFRE)
        self.a_coffre = a_coffre
        self.cadenas_casse = not a_coffre 

    def afficher_infos(self):
        # ... (méthode inchangée)
        print(f"Pièce : {self.nom}")
        print(f"Couleur : {self.couleur.capitalize()}")
        print(f"Loot : {self.loot}")
        print(f"Coût : {self.cout_gemmes} gemmes, Rareté : {self.rarete}")
        print(f"Endroits à creuser : {self.endroits_creuser} (creusé: {self.endroit_creuse})")
        
        if self.a_coffre: 
            etat_cadenas = "Ouvert" if self.cadenas_casse else "Verrouillé"
            print(f"Coffre : Présent ({etat_cadenas})")
            
        print("Portes :")
        for direction, porte in self.portes.items():
            if porte:
                print(f"  - {direction} (niveau {porte.niveau})")
        print()

    def niveau_porte(self, direction: str) -> int:
        # ... (méthode inchangée)
        porte = self.portes_objets.get(direction)
        if porte is not None:
            return porte.niveau
        else:
            return -1

    def peut_creuser(self) -> bool:
        # ... (méthode inchangée)
        return self.endroits_creuser > 0 and not self.endroit_creuse

    def creuser(self, patte_lapin_active: bool) -> dict:
        if not self.peut_creuser():
            return {'success': False, 'message': "Aucun endroit où creuser ici ou déjà creusé."}
        self.endroit_creuse = True
            
        chance_base = 0.6
        if patte_lapin_active:
            chance_base = min(1.0, chance_base + 0.2) 
        if random.random() < chance_base:
            loot_possibles = [
                ("Pièce d'Or", 0.3),
                ("Clé", 0.25), 
                ("Gemme", 0.2),
                ("Pomme", 0.1),
                ("Banane", 0.08),
                ("Gâteau", 0.05),
                ("Dé", 0.02)
            ]
                
            objet_trouve = None
            r = random.random()
            cumul = 0
            for objet, proba in loot_possibles:
                cumul += proba
                if r <= cumul:
                    objet_trouve = objet
                    break
                
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
                'objet': None,
                'message': "Vous creusez mais ne trouvez rien..."
            }

    def tenter_casser_cadenas(self) -> dict:
        """
        Tente de briser le cadenas si un coffre est présent et verrouillé.
        """
        if not self.a_coffre:
            return {'success': False, 'message': f"Il n'y a pas de cadenas ou de coffre à briser dans {self.nom}."}
            
        if self.cadenas_casse:
            return {'success': False, 'message': "Le coffre dans cette pièce est déjà ouvert."}
            
        self.cadenas_casse = True
                
        loot_trouve = []
        
        if self.loot.get("coffre_loot"):
            for nom_item, quantite in self.loot["coffre_loot"].items():
                loot_trouve.extend([nom_item] * quantite)
        else:
            loot_trouve.append("Clé")
            
        return {
            'success': True,
            'loot_trouve': loot_trouve,
            'message': f"Le Marteau a brisé le cadenas du coffre!"
        }
    
    def charger_image(self, zip_path="Images.zip"):
        # ... (méthodes de gestion d'image inchangées)
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