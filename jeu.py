import pygame 
from joueur import Joueur
from manoir import Manoir 
from inventaire import * 
from ClassePiece import *
from ClasseObjet import *
import os
from ClasseObjet import OBJET_MAP
import random

# CONSTANTES D'AFFICHAGE
colonnes_jeu = 5
lignes_jeu = 9 

nb_pixels_piece = 80
start_x_grille = 20
start_y_grille = 20

largeur_grille_seule = colonnes_jeu * nb_pixels_piece 
hauteur_grille_seule = lignes_jeu * nb_pixels_piece

largeur_inventaire = 500
espace_inventaire = 50

affichage_largeur = start_x_grille + largeur_grille_seule + espace_inventaire + largeur_inventaire + start_x_grille
affichage_hauteur = start_y_grille * 2 + hauteur_grille_seule

def charger_images_objets():
    dossier_images = os.path.join(os.path.dirname(__file__), "Images_objets")
    
    images = {}
    correspondances = {
        "Pelle": "spade.png",
        "Kit de Crochetage": "lockpick.png",
        "Patte de Lapin": "rabbit.png",
        "Détecteur de Métaux": "metal-detector.png",
        "Marteau": "hammer.png",
        "Pas": "footstep.png",
        "Pièce d'Or": "coin.png",
        "Gemme": "gem.png",
        "Clé": "key.png",
        "Dé": "dice.png",
        "Pomme": "apple.png",
        "Banane": "banana.png",
        "Gâteau": "cake.png",
        "Sandwich": "sandwich.png",
        "Repas": "meal.png",
    }
    
    for nom, fichier in correspondances.items():
        chemin_image = os.path.join(dossier_images, fichier)
        try:
            if os.path.exists(chemin_image):
                img = pygame.image.load(chemin_image).convert_alpha()
                images[nom] = pygame.transform.scale(img, (40, 40))
            else:
                images[nom] = None
                print(f"Image manquante: {chemin_image}")
        except Exception as e:
            print(f"Erreur chargement image {chemin_image}: {e}")
            images[nom] = None
    
    return images

class Jeu:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Blue Prince Game")
        self.screen = pygame.display.set_mode((affichage_largeur, affichage_hauteur))
        self.clock = pygame.time.Clock()
        
        self.joueur = Joueur() 
        self.manoir = Manoir() 
        
        self.flag_en_cours = True
        self.game_over = False
        self.victoire = False
        
        self.etat_jeu = "Deplacement"
        self.pieces_proposees = []
        self.message_statut = "Utilisez ZQSD pour vous déplacer. C pour creuser si disponible."
        self.images_objets = charger_images_objets()

        self.nouvelle_piece_coords = None 
        self.direction_mouvement = None
        
        self.magasin_items = []

        self.creusage_disponible = False

        self.font_petit = pygame.font.Font(None, 30)
        self.font_moyen = pygame.font.Font(None, 35)
        self.font_grand = pygame.font.Font(None, 60)
        self.font_titre = pygame.font.Font(None, 45)

    def affichage_d_v(self): 
        fenetre_fin = pygame.Surface((affichage_largeur, affichage_hauteur), pygame.SRCALPHA)
        fenetre_fin.fill((0, 0, 0, 220)) 
        self.screen.blit(fenetre_fin, (0, 0))
        
        if self.victoire == True:
            texte = "VICTOIRE : Vous êtes arrivés à l'antichambre :)"
            couleur = (0, 255, 0)
        elif self.joueur.inventaire.pas <= 0:
            texte = "DEFAITE : Vous êtes à cours de pas :("
            couleur = (255, 0, 0)
        elif self.game_over: 
            texte = "DEFAITE : La partie est terminée :("
            couleur = (255, 0, 0)
            
        affichage = self.font_titre.render(texte, True, couleur)
        espace_texte = affichage.get_rect(center=(affichage_largeur // 2, affichage_hauteur // 2))
        self.screen.blit(affichage, espace_texte)
        
        instruction_surface = self.font_moyen.render("Pour quitter : ENTREE", True, (255, 255, 255))
        instruction_rect = instruction_surface.get_rect(center=(affichage_largeur // 2, affichage_hauteur // 2 + 50))
        self.screen.blit(instruction_surface, instruction_rect)

    def affichage_grille(self):
        self.screen.fill((168, 195, 188))
        
        fond_grille_rect = pygame.Rect(start_x_grille, start_y_grille, largeur_grille_seule, hauteur_grille_seule)
        pygame.draw.rect(self.screen, (10, 10, 10), fond_grille_rect)
        
        for r in range(lignes_jeu): 
            for c in range(colonnes_jeu):
                x = start_x_grille + c * nb_pixels_piece
                y = start_y_grille + r * nb_pixels_piece
                rect = pygame.Rect(x, y, nb_pixels_piece, nb_pixels_piece)
                piece = self.manoir.get_piece_at(r, c)
                if piece and piece.image:
                    image_redim = pygame.transform.scale(piece.image, (nb_pixels_piece, nb_pixels_piece))
                    self.screen.blit(image_redim, (x, y))
                elif piece:
                    pygame.draw.rect(self.screen, (255, 0, 0), (x, y, nb_pixels_piece, nb_pixels_piece))
                pygame.draw.rect(self.screen, (45, 45, 45), rect, 1)
        
        bords_jeu = pygame.Rect(start_x_grille - 2, start_y_grille - 2, largeur_grille_seule + 4, hauteur_grille_seule + 4)
        pygame.draw.rect(self.screen, (255, 255, 255), bords_jeu, 2)

    def affichage_inventaire(self): 
        x = start_x_grille + largeur_grille_seule + espace_inventaire
        y = start_y_grille
        
        inventaire_rect = pygame.Rect(x, y, largeur_inventaire, hauteur_grille_seule)
        pygame.draw.rect(self.screen, (255, 255, 255), inventaire_rect)

        self.screen.blit(self.font_grand.render("Inventaire", True, (45, 45, 45)), (x + 15, y + 15))

        dicto_inventaire = {
            'PERMANENT': [
                ("Kit de Crochetage", self.joueur.inventaire.a_objet_permanent("Kit de Crochetage")),
                ("Patte de Lapin", self.joueur.inventaire.a_objet_permanent("Patte de Lapin")),
                ("Pelle", self.joueur.inventaire.a_objet_permanent("Pelle")),
                ("Marteau", self.joueur.inventaire.a_objet_permanent("Marteau")),
                ("Détecteur de Métaux", self.joueur.inventaire.a_objet_permanent("Détecteur de Métaux")),
            ],
            'CONSOMMABLE': [
                ("Pas", self.joueur.inventaire.pas),
                ("Pièce d'Or", self.joueur.inventaire.pieces_or), 
                ("Gemme", self.joueur.inventaire.gemmes), 
                ("Clé", self.joueur.inventaire.cles), 
                ("Dé", self.joueur.inventaire.des),
            ] 
        }
        
        y_depart_colonnes = y + 100 
        largeur_colonne = largeur_inventaire // 2 
        
        x_col_gauche = x
        y_permanent = y_depart_colonnes
        marge_gauche = 20
        decalage_texte_x = 50 

        for n, q in dicto_inventaire['PERMANENT']:
            if q: 
                img = self.images_objets.get(n)
                if img:
                    self.screen.blit(img, (x_col_gauche + marge_gauche, y_permanent))
                couleur = (0, 200, 0) 
                self.screen.blit(self.font_petit.render(n, True, couleur), (x_col_gauche + decalage_texte_x + marge_gauche, y_permanent + 10))
                y_permanent += 50
            else:
                couleur = (150, 150, 150) 
                self.screen.blit(self.font_petit.render(n, True, couleur), (x_col_gauche + decalage_texte_x + marge_gauche, y_permanent + 10))
                y_permanent += 50

        x_col_droite = x + largeur_colonne
        y_consommable = y_depart_colonnes
        largeur_icone = 40
        marge_icone_texte = 10 
        
        for n, q in dicto_inventaire['CONSOMMABLE']:
            img = self.images_objets.get(n)
            couleur_texte = (45, 45, 45)
            if n == "Pas" and q <= 10:
                couleur_texte = (255, 100, 100)
            elif n == "Pas" and q > 70: 
                couleur_texte = (100, 255, 100)
            texte_quantite = self.font_petit.render(f"x{q}", True, couleur_texte)
            largeur_texte = texte_quantite.get_width()
            largeur_bloc = largeur_icone + marge_icone_texte + largeur_texte
            x_depart_bloc = x_col_droite + (largeur_colonne - largeur_bloc) // 2 
            if img:
                posx_img = x_depart_bloc
                self.screen.blit(img, (posx_img, y_consommable))
            
            posx_texte = x_depart_bloc + largeur_icone + marge_icone_texte
            self.screen.blit(texte_quantite, (posx_texte, y_consommable + 10))
            
            y_consommable += 50

    def affichage_curseur(self): 
        curseur_c = self.joueur.position_colonne
        curseur_r = self.joueur.position_ligne
        
        x = start_x_grille + curseur_c * nb_pixels_piece
        y = start_y_grille + curseur_r * nb_pixels_piece
        curseur = pygame.Rect(x, y, nb_pixels_piece, nb_pixels_piece)
        pygame.draw.rect(self.screen, (255, 255, 0), curseur, 3)

    def affichage_message_statut(self):
        x = start_x_grille + largeur_grille_seule + espace_inventaire
        hauteur_message = 150 
        y = start_y_grille + hauteur_grille_seule - hauteur_message
        
        fond_message_rect = pygame.Rect(x, y, largeur_inventaire, hauteur_message)
        pygame.draw.rect(self.screen, (30, 30, 30), fond_message_rect)
        
        mots = self.message_statut.split(' ')
        lignes_texte = []
        ligne_actuelle = ""
        
        for mot in mots:
            test_ligne = f"{ligne_actuelle} {mot}".strip()
            if self.font_petit.size(test_ligne)[0] < largeur_inventaire - 20:
                ligne_actuelle = test_ligne
            else:
                lignes_texte.append(ligne_actuelle)
                ligne_actuelle = mot
        lignes_texte.append(ligne_actuelle)

        y_texte = y + 15
        for ligne in lignes_texte:
            texte_surface = self.font_petit.render(ligne, True, (255, 255, 255))
            self.screen.blit(texte_surface, (x + 10, y_texte))
            y_texte += 30

        if self.creusage_disponible and self.etat_jeu == "Deplacement":
            indication_creuser = self.font_petit.render("Appuyez sur C pour creuser", True, (255, 255, 0))
            self.screen.blit(indication_creuser, (x + 10, y_texte))

    def affichage_selection_pieces(self):
        overlay = pygame.Surface((affichage_largeur, affichage_hauteur), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 200))
        self.screen.blit(overlay, (0, 0))

        titre_surface = self.font_titre.render("CHOISISSEZ UNE PIECE", True, (255, 255, 255))
        titre_rect = titre_surface.get_rect(center=(affichage_largeur // 2, 100))
        self.screen.blit(titre_surface, titre_rect)

        nb_choix = len(self.pieces_proposees)
        largeur_totale_cartes = nb_choix * 200 + (nb_choix - 1) * 50
        start_x = (affichage_largeur - largeur_totale_cartes) // 2
        y_carte = affichage_hauteur // 2 - 100

        for i, piece in enumerate(self.pieces_proposees):
            x_carte = start_x + i * (200 + 50)
            carte_rect = pygame.Rect(x_carte, y_carte, 200, 300)
            
            couleurs = {"bleue": (0, 0, 100), "dorée": (100, 80, 0), "verte": (0, 80, 0), "violette": (80, 0, 80), "grise": (50, 50, 50), "blanche": (100, 100, 100), "brune": (70, 30, 0)}
            couleur_fond = couleurs.get(piece.couleur, (30, 30, 30))
            pygame.draw.rect(self.screen, couleur_fond, carte_rect)
            pygame.draw.rect(self.screen, (255, 255, 255), carte_rect, 2)

            touche_surface = self.font_grand.render(f"Touche {i+1}", True, (255, 255, 0))
            touche_rect = touche_surface.get_rect(center=(x_carte + 100, y_carte + 30))
            self.screen.blit(touche_surface, touche_rect)

            nom_surface = self.font_moyen.render(piece.nom, True, (255, 255, 255))
            nom_rect = nom_surface.get_rect(center=(x_carte + 100, y_carte + 80))
            self.screen.blit(nom_surface, nom_rect)

            if piece.image:
                img_scaled = pygame.transform.scale(piece.image, (160, 160))
                self.screen.blit(img_scaled, (x_carte + 20, y_carte + 110))

            if piece.cout_gemmes == 0:
                cout_txt = "Gratuit"
                couleur_cout = (0, 255, 0)
            else:
                cout_txt = f"Coût : {piece.cout_gemmes} Gemme(s)"
                couleur_cout = (0, 255, 255)
                if piece.cout_gemmes > self.joueur.inventaire.gemmes:
                    couleur_cout = (255, 0, 0)
                    
            cout_surface = self.font_petit.render(cout_txt, True, couleur_cout)
            cout_rect = cout_surface.get_rect(center=(x_carte + 100, y_carte + 280))
            self.screen.blit(cout_surface, cout_rect)

    def affichage_magasin(self):
        overlay = pygame.Surface((affichage_largeur, affichage_hauteur), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 200))
        self.screen.blit(overlay, (0, 0))

        titre_surface = self.font_titre.render("BOUTIQUE", True, (255, 215, 0))
        titre_rect = titre_surface.get_rect(center=(affichage_largeur // 2, 100))
        self.screen.blit(titre_surface, titre_rect)
        
        info_surface = self.font_moyen.render("Appuyez sur 'A' pour quitter", True, (255, 255, 255))
        info_rect = info_surface.get_rect(center=(affichage_largeur // 2, 150))
        self.screen.blit(info_surface, info_rect)

        nb_choix = len(self.magasin_items)
        largeur_totale_cartes = nb_choix * 200 + (nb_choix - 1) * 50
        start_x = (affichage_largeur - largeur_totale_cartes) // 2
        y_carte = affichage_hauteur // 2 - 100

        for i, item_data in enumerate(self.magasin_items):
            item_nom = item_data["item"]
            item_prix = item_data["prix"]
            
            x_carte = start_x + i * (200 + 50)
            carte_rect = pygame.Rect(x_carte, y_carte, 200, 300)
            
            pygame.draw.rect(self.screen, (50, 50, 50), carte_rect)
            pygame.draw.rect(self.screen, (255, 215, 0), carte_rect, 2)

            touche_surface = self.font_grand.render(f"Touche {i+1}", True, (255, 255, 0))
            touche_rect = touche_surface.get_rect(center=(x_carte + 100, y_carte + 40))
            self.screen.blit(touche_surface, touche_rect)

            nom_surface = self.font_moyen.render(item_nom, True, (255, 255, 255))
            nom_rect = nom_surface.get_rect(center=(x_carte + 100, y_carte + 100))
            self.screen.blit(nom_surface, nom_rect)
            
            img = self.images_objets.get(item_nom)
            if img:
                img_scaled = pygame.transform.scale(img, (80, 80))
                img_rect = img_scaled.get_rect(center=(x_carte + 100, y_carte + 170))
                self.screen.blit(img_scaled, img_rect)

            cout_txt = f"Prix : {item_prix} Or"
            couleur_cout = (0, 255, 255)
            if item_prix > self.joueur.inventaire.pieces_or:
                couleur_cout = (255, 0, 0)
                    
            cout_surface = self.font_petit.render(cout_txt, True, couleur_cout)
            cout_rect = cout_surface.get_rect(center=(x_carte + 100, y_carte + 250))
            self.screen.blit(cout_surface, cout_rect)

    def _instancier_objet(self, nom_item: str):
        classe_objet = OBJET_MAP.get(nom_item)
        if classe_objet:
            return classe_objet()

    
    def _generer_et_ramasser_butin(self, piece: Piece):
        objets_trouvés = []
        
        detecteur_actif = self.joueur.inventaire.detecteur_actif
        patte_lapin_active = self.joueur.inventaire.patte_lapin_active

        loot_data = piece.loot
        if not loot_data:
            self.message_statut += " | Aucun objet ici."
            return

        for nom_item in loot_data.get("garanti", []):
            objets_trouvés.append(nom_item)
            
        for nom_item, proba_base in loot_data.get("aleatoire", []):
            proba_modifiee = proba_base
            
            if nom_item in ["Clé", "Pièce d'Or"] and detecteur_actif:
                proba_modifiee = min(1.0, proba_modifiee + 0.25)
            
            if patte_lapin_active:
                proba_modifiee = min(1.0, proba_modifiee + 0.15) 

            if random.random() < proba_modifiee:
                objets_trouvés.append(nom_item)
                
        if piece.couleur == "verte":
            proba_gemme = 0.2
            if patte_lapin_active: proba_gemme = min(1.0, proba_gemme + 0.15)
            if random.random() < proba_gemme:
                objets_trouvés.append("Gemme")
        
        elif piece.couleur == "violette":
            proba_pomme = 0.3
            if patte_lapin_active: proba_pomme = min(1.0, proba_pomme + 0.15)
            if random.random() < proba_pomme:
                objets_trouvés.append("Pomme")

        if not objets_trouvés:
            self.message_statut += " | Aucun objet trouvé ici."
            return

        message_loot = " | Vous trouvez : "
        items_str_list = []
        
        for nom_item in objets_trouvés:
            objet_instance = self._instancier_objet(nom_item)
            if objet_instance:
                self.joueur.inventaire.ramasser_objet(objet_instance, self.joueur)
                items_str_list.append(nom_item)
        
        self.message_statut += message_loot + ", ".join(items_str_list)
        
    def _entrer_magasin(self, piece: Piece):
        if piece.magasin:
            self.magasin_items = piece.magasin
            self.etat_jeu = "Magasin"
            self.message_statut = "Boutique ! Touche (1, 2, 3) pour acheter. (A) pour quitter."

    def _acheter_objet(self, index_choix: int):
        if not (0 <= index_choix < len(self.magasin_items)):
            return

        item_data = self.magasin_items[index_choix]
        nom_item = item_data["item"]
        prix = item_data["prix"]
        
        if self.joueur.inventaire.depenser_pieces_or(prix):
            objet_instance = self._instancier_objet(nom_item)
            if objet_instance:
                self.joueur.inventaire.ramasser_objet(objet_instance, self.joueur)
                self.message_statut = f"Achat réussi : {nom_item} pour {prix} Or."
            else:
                self.joueur.inventaire.pieces_or += prix
                self.message_statut = f"Erreur: Objet {nom_item} inconnu."
        else:
            self.message_statut = f"Pas assez d'Or ! (Requis: {prix})"

    def _mettre_a_jour_creusage_disponible(self):
        piece_actuelle = self.manoir.get_piece_at(
            self.joueur.position_ligne, 
            self.joueur.position_colonne
        )
        
        if piece_actuelle is None:
            self.creusage_disponible = False
            return
            
        self.creusage_disponible = (
            piece_actuelle.peut_creuser() and 
            self.joueur.verifie_pelle()
        )

    def creuser_dans_piece_actuelle(self):
        
        if not self.joueur.verifie_pelle():
            self.message_statut = "Vous avez besoin d'une pelle pour creuser !"
            return
            
        piece_actuelle = self.manoir.get_piece_at(
            self.joueur.position_ligne, 
            self.joueur.position_colonne
        )
        
        if piece_actuelle:
            patte_lapin_active = self.joueur.inventaire.patte_lapin_active
            resultat = piece_actuelle.creuser(patte_lapin_active)
            
            if resultat['success']:
                objet_instance = self._instancier_objet(resultat['objet'])
                if objet_instance:
                    self.joueur.inventaire.ramasser_objet(objet_instance, self.joueur)
                self.message_statut = resultat['message']
            else:
                self.message_statut = resultat['message']
            
            self._mettre_a_jour_creusage_disponible()
        else:
            self.message_statut = "Aucun endroit où creuser ici."

    def deplacement(self, direction):
        if self.etat_jeu not in ["Deplacement", "Magasin"]: 
            self.message_statut = "Veuillez choisir une pièce (Touches 1, 2, 3)"
            return
        if self.etat_jeu == "Magasin":
            self.etat_jeu = "Deplacement"
            self.message_statut = "Vous quittez la boutique."

        nouvelle_ligne, nouvelle_colonne = self.joueur.calcul_coordonnees_casead(direction)

        if not (0 <= nouvelle_ligne < lignes_jeu and 0 <= nouvelle_colonne < colonnes_jeu):
            self.message_statut = "C'est un mur extérieur."
            return 

        piece_actuelle = self.manoir.get_piece_at(self.joueur.position_ligne, self.joueur.position_colonne)
        
        porte_obj = piece_actuelle.portes_objets.get(direction)

        if porte_obj is None:
            self.message_statut = "Il n'y a pas de porte dans cette direction."
            return
        
        if porte_obj.ouvrir(self.joueur):
            destination_piece = self.manoir.get_piece_at(nouvelle_ligne, nouvelle_colonne)

            if destination_piece:
                if self.joueur.deplacer_vers(nouvelle_ligne, nouvelle_colonne):
                    self.message_statut = f"Vous entrez dans {destination_piece.nom}"
                    
                    self._mettre_a_jour_creusage_disponible()
                    
                    if destination_piece.nom in ["Antechamber", "Antichambre"]:
                        self.victoire = True
                    elif destination_piece.couleur == "dorée":
                        self._entrer_magasin(destination_piece)
                else:
                    self.game_over = True
            else:
                self.pieces_proposees = self.manoir.tirer_trois_pieces(
                    self.joueur.position_ligne,
                    self.joueur.position_colonne,
                    nouvelle_ligne,
                    nouvelle_colonne,
                    direction
                )

                if not self.pieces_proposees:
                    self.message_statut = "DEFAITE : La pioche ne contient plus de pièces valides."
                    self.game_over = True
                    return

                # Défaite par manque de gemmes/dés après tirage (SUPPRIMÉ)
                # peut_payer = any(p.cout_gemmes <= self.joueur.inventaire.gemmes for p in self.pieces_proposees)
                # a_de = self.joueur.inventaire.des > 0
                
                # if not peut_payer and not a_de:
                #     self.message_statut = "DEFAITE : Aucune pièce abordable et pas de Dé pour relancer. Jeu terminé."
                #     self.game_over = True
                #     return
                
                self.nouvelle_piece_coords = (nouvelle_ligne, nouvelle_colonne)
                self.direction_mouvement = direction
                
                self.etat_jeu = "Selection pieces"
                self.message_statut = "Choisissez une pièce (1, 2, 3). Dépensez un Dé (Touche R) pour relancer."
        else:
            if porte_obj.niveau == 1:
                self.message_statut = "Porte verrouillée (Niv 1). Clé ou Kit nécessaire."
            elif porte_obj.niveau == 2:
                self.message_statut = "Porte verrouillée (Niv 2). Clé nécessaire."

    def selectionner_piece(self, index_choix: int):
        if not (0 <= index_choix < len(self.pieces_proposees)):
            return 

        piece_choisie = self.pieces_proposees[index_choix]
        cout = piece_choisie.cout_gemmes

        if self.joueur.inventaire.depenser_gemmes(piece_choisie.cout_gemmes):
            ligne, col = self.nouvelle_piece_coords
            self.manoir.placer_piece(
                piece_choisie, ligne, col,
                self.joueur.position_ligne, self.joueur.position_colonne,
                self.direction_mouvement
            )

            if self.joueur.deplacer_vers(ligne, col):
                self.message_statut = f"Vous avez découvert : {piece_choisie.nom}"
                
                self._generer_et_ramasser_butin(piece_choisie)
                self._mettre_a_jour_creusage_disponible()
                
                if piece_choisie.couleur == "dorée":
                    self._entrer_magasin(piece_choisie)

            else:
                self.game_over = True

            self.etat_jeu = "Deplacement"
            self.pieces_proposees = []
            self.nouvelle_piece_coords = None
            self.direction_mouvement = None
        else:
            self.message_statut = f"Pas assez de gemmes ! (Requis : {piece_choisie.cout_gemmes})"

    def utiliser_de(self,):
        if self.joueur.inventaire.depenser_des(1): 
            ligne, col = self.nouvelle_piece_coords
            self.pieces_proposees = self.manoir.tirer_trois_pieces(
                self.joueur.position_ligne,
                self.joueur.position_colonne,
                ligne, col,
                self.direction_mouvement
            )
            
            self.message_statut = "Tirage relancé ! (1, 2, 3 ou R)"
            
            if not self.pieces_proposees:
                self.message_statut = "DEFAITE : La relance n'a trouvé aucune pièce valide. Jeu terminé."
                self.game_over = True
                return
        else:
            self.message_statut = "Vous n'avez pas de Dés !"

    def gestion_evenements(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.flag_en_cours = False
            
            if event.type == pygame.KEYDOWN:
                
                if self.etat_jeu == "Fin":
                    if event.key == pygame.K_RETURN:
                        self.flag_en_cours = False
                
                elif self.etat_jeu == "Deplacement":
                    if event.key == pygame.K_z:
                        self.deplacement('up')
                    elif event.key == pygame.K_q:
                        self.deplacement('left')
                    elif event.key == pygame.K_s:
                        self.deplacement('down')
                    elif event.key == pygame.K_d:
                        self.deplacement('right')
                    elif event.key == pygame.K_c and self.creusage_disponible:
                        self.creuser_dans_piece_actuelle()
                    elif event.key == pygame.K_p: 
                        self.utiliser_objet_permanent("Pelle")
                    elif event.key == pygame.K_k: 
                        self.utiliser_objet_permanent("Kit de Crochetage")
                    elif event.key == pygame.K_m: 
                        self.utiliser_objet_permanent("Marteau")
                    elif event.key == pygame.K_l: 
                        self.utiliser_objet_permanent("Patte de Lapin")
                    elif event.key == pygame.K_t: 
                        self.utiliser_objet_permanent("Détecteur de Métaux")
                
                elif self.etat_jeu == "Selection pieces":
                    if event.key == pygame.K_1 or event.key == pygame.K_KP_1:
                        self.selectionner_piece(0)
                    elif event.key == pygame.K_2 or event.key == pygame.K_KP_2:
                        self.selectionner_piece(1)
                    elif event.key == pygame.K_3 or event.key == pygame.K_KP_3:
                        self.selectionner_piece(2)
                    elif event.key == pygame.K_r:
                        self.utiliser_de()
                        
                elif self.etat_jeu == "Magasin":
                    if event.key == pygame.K_1 or event.key == pygame.K_KP_1:
                        self._acheter_objet(0)
                    elif event.key == pygame.K_2 or event.key == pygame.K_KP_2:
                        self._acheter_objet(1)
                    elif event.key == pygame.K_3 or event.key == pygame.K_KP_3:
                        self._acheter_objet(2)
                    elif event.key == pygame.K_a:
                        self.etat_jeu = "Deplacement"
                        self.message_statut = "Vous quittez la boutique."
    
    def utiliser_objet_permanent(self, nom_objet: str):
        if not self.joueur.inventaire.a_objet_permanent(nom_objet):
            self.message_statut = f"Vous n'avez pas de {nom_objet} !"
            return False
        
        objet_instance = self._instancier_objet(nom_objet)
        if objet_instance:
            objet_instance.utiliser(self.joueur) 
            
            self.message_statut = f"{nom_objet} utilisé. Il reste dans l'inventaire."
            
            self._mettre_a_jour_creusage_disponible()
            return True
        else:
            self.message_statut = f"Erreur: Impossible d'utiliser {nom_objet}"
            return False
    
    def verification_fin_jeu(self):
        if self.game_over or self.victoire:
            self.etat_jeu = "Fin"
            return

        if self.joueur.inventaire.pas <= 0:
            self.game_over = True
            self.etat_jeu = "Fin"
            
    def en_cours_gestion(self):
        while self.flag_en_cours == True:
            
            self.gestion_evenements()
            
            self.verification_fin_jeu()
            
            if self.etat_jeu == "Fin":
                self.affichage_grille()
                self.affichage_inventaire()
                self.affichage_curseur()
                self.affichage_d_v()
            else:
                self.affichage_grille()
                self.affichage_inventaire()
                self.affichage_curseur()
                self.affichage_message_statut()
                
                if self.etat_jeu == "Selection pieces":
                    self.affichage_selection_pieces()
                elif self.etat_jeu == "Magasin":
                    self.affichage_magasin()
            
            pygame.display.flip()
            self.clock.tick(60)
            
        pygame.quit()