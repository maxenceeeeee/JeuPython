import pygame 
from joueur import Joueur
from manoir import Manoir 
from inventaire import * 
from ClassePiece import *
from ClasseObjet import *
import zipfile
import os
from ClassePorte import Porte 
from ClasseObjet import OBJET_MAP


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

# affichage complet jeu
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
        "Pièce d'Or": "coin.png", # Pièces d'or -> Pièce d'Or
        "Gemme": "gem.png", # Gemmes -> Gemme
        "Clé": "key.png", # Clés -> Clé
        "Dé": "dice.png", # Dés -> Dé
    }
    for nom, fichier in correspondances.items():
        chemin_image = os.path.join(dossier_images, fichier)
        try:
            # Laisser le try/except est essentiel pour ne pas crasher si un fichier est manquant.
            img = pygame.image.load(chemin_image).convert_alpha()
            images[nom] = pygame.transform.scale(img, (40, 40))
        except:
            images[nom] = None
    return images



class Jeu :
    
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
        
        self.etat_jeu = "Deplacement" # États: "Deplacement", "Selection pieces", "Magasin", "Fin"
        self.pieces_proposees = []
        self.message_statut = "Utilisez ZQSD pour vous déplacer."
        self.images_objets = charger_images_objets()

        # Ajout de variables pour mémoriser la transition
        self.nouvelle_piece_coords = None 
        self.direction_mouvement = None
        
        # Variables pour le Magasin
        self.magasin_items = [] # Les objets en vente (ex: {"item": "Clé", "prix": 10})

        # Gestion des polices
        self.font_petit = pygame.font.Font(None, 30)
        self.font_moyen = pygame.font.Font(None, 35)
        self.font_grand = pygame.font.Font(None, 60)
        self.font_titre = pygame.font.Font(None, 45)
    
    # AFFICHAGE FIN DE PARTIE
    def affichage_d_v(self): 
        fenetre_fin = pygame.Surface((affichage_largeur, affichage_hauteur), pygame.SRCALPHA)
        fenetre_fin.fill((0, 0, 0, 220)) 
        self.screen.blit(fenetre_fin, (0, 0))
        
        if self.victoire == True:
            texte = "VICTOIRE : Vous êtes arrivés à l'antichambre :)"
            affichage = self.font_titre.render(texte, True, (0, 255, 0))
        elif self.joueur.inventaire.pas <= 0:
            texte = "DEFAITE : Vous êtes à cours de pas :("
            affichage = self.font_titre.render(texte, True, (255, 0, 0))
        elif self.game_over: 
            texte = "DEFAITE : La partie est terminée :("
            affichage = self.font_titre.render(texte, True, (255, 0, 0))
            
        espace_texte = affichage.get_rect(center=(affichage_largeur // 2, affichage_hauteur // 2))
        self.screen.blit(affichage, espace_texte)
        
        instruction_surface = self.font_moyen.render("Pour quitter : ENTREE", True, (255, 255, 255))
        instruction_rect = instruction_surface.get_rect(center=(affichage_largeur // 2, affichage_hauteur // 2 + 50))
        self.screen.blit(instruction_surface, instruction_rect)

    #AFFICHAGE JEU
    def affichage_grille(self):
        self.screen.fill((168,195,188)) # Fond général
        
        # Fond de la grille
        fond_grille_rect = pygame.Rect(start_x_grille, start_y_grille, largeur_grille_seule, hauteur_grille_seule)
        pygame.draw.rect(self.screen, (10, 10, 10), fond_grille_rect) # Fond noir pour les cases vides
        
        for r in range(lignes_jeu): 
            for c in range(colonnes_jeu):
                x = start_x_grille + c * nb_pixels_piece
                y = start_y_grille + r * nb_pixels_piece
                rect = pygame.Rect(x, y, nb_pixels_piece, nb_pixels_piece)
                piece = self.manoir.get_piece_at(r, c)
                if piece and piece.image:
                    image_redim = pygame.transform.scale(piece.image, (nb_pixels_piece, nb_pixels_piece))
                    self.screen.blit(image_redim, (x, y))
                elif piece: # Si la pièce existe mais l'image a échoué à charger
                     pygame.draw.rect(self.screen, (255,0,0), (x,y, nb_pixels_piece, nb_pixels_piece))
                pygame.draw.rect(self.screen, (45, 45, 45), rect, 1)
        # Dessiner les bordures de la grille
        bords_jeu = pygame.Rect(start_x_grille - 2, start_y_grille - 2, largeur_grille_seule + 4, hauteur_grille_seule + 4)
        pygame.draw.rect(self.screen, (255, 255, 255), bords_jeu, 2)
    
    
    def affichage_inventaire(self): 
        x = start_x_grille + largeur_grille_seule + espace_inventaire
        y = start_y_grille
        
        inventaire_rect = pygame.Rect(x, y, largeur_inventaire, hauteur_grille_seule)
        pygame.draw.rect(self.screen, (255, 255, 255), inventaire_rect)

        self.screen.blit(self.font_grand.render("Inventaire", True, (45,45,45)), (x+15, y+15))

        dicto_inventaire = {
            'PERMANENT': [
                ("Kit de Crochetage", self.joueur.inventaire.a_objet_permanent("Kit de Crochetage")),
                ("Patte de Lapin", self.joueur.inventaire.a_objet_permanent("Patte de Lapin")),
                ("Pelle", self.joueur.inventaire.a_objet_permanent("Pelle")),
                ("Marteau", self.joueur.inventaire.a_objet_permanent("Marteau")),
                ("Détecteur de Métaux", self.joueur.inventaire.a_objet_permanent("Détecteur de Métaux")),],
            'CONSOMMABLE': [
                ("Pas", self.joueur.inventaire.pas),
                ("Pièce d'Or", self.joueur.inventaire.pieces_or), 
                ("Gemme", self.joueur.inventaire.gemmes), 
                ("Clé", self.joueur.inventaire.cles), 
                ("Dé", self.joueur.inventaire.des),] 
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
                y_permanent += 5
        x_col_droite = x + largeur_colonne
        y_consommable = y_depart_colonnes
        largeur_icone = 40
        marge_icone_texte = 10 
        marge_droite_col = 15
        for n, q in dicto_inventaire['CONSOMMABLE']:
            img = self.images_objets.get(n)
            couleur_texte = (45,45,45)
            if n == "Pas" and q <= 10: couleur_texte = (255, 100, 100) # Rouge si Pas faibles
            elif n == "Pas" and q > 70: couleur_texte = (100, 255, 100) # Vert si Pas élevés
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
        pygame.draw.rect(self.screen, (255, 255, 0), curseur, 3) # Epaisseur 3 pour visibilité

    def affichage_message_statut(self):
        """Affiche le message de statut en bas de l'inventaire. Taille augmentée."""
        x = start_x_grille + largeur_grille_seule + espace_inventaire
        
        # Hauteur du bloc de message augmentée
        hauteur_message = 150 
        y = start_y_grille + hauteur_grille_seule - hauteur_message # Positionne le bloc au bas de l'inventaire
        
        # Fond pour le message
        fond_message_rect = pygame.Rect(x, y, largeur_inventaire, hauteur_message)
        pygame.draw.rect(self.screen, (30, 30, 30), fond_message_rect) # Gris foncé
        
        # Texte (potentiellement sur plusieurs lignes)
        mots = self.message_statut.split(' ')
        lignes_texte = []
        ligne_actuelle = ""
        
        for mot in mots:
            test_ligne = f"{ligne_actuelle} {mot}".strip()
            # On vérifie si la ligne testée dépasse la largeur du bloc
            if self.font_petit.size(test_ligne)[0] < largeur_inventaire - 20:
                ligne_actuelle = test_ligne
            else:
                lignes_texte.append(ligne_actuelle)
                ligne_actuelle = mot
        lignes_texte.append(ligne_actuelle)

        # Affichage des lignes
        y_texte = y + 15
        for ligne in lignes_texte:
            texte_surface = self.font_petit.render(ligne, True, (255, 255, 255))
            self.screen.blit(texte_surface, (x + 10, y_texte))
            y_texte += 30

    def affichage_selection_pieces(self):
        """Affiche l'écran de sélection des 3 pièces."""
        # 1. Fond semi-transparent
        overlay = pygame.Surface((affichage_largeur, affichage_hauteur), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 200))
        self.screen.blit(overlay, (0, 0))

        # 2. Titre
        titre_surface = self.font_titre.render("CHOISISSEZ UNE PIECE", True, (255, 255, 255))
        titre_rect = titre_surface.get_rect(center=(affichage_largeur // 2, 100))
        self.screen.blit(titre_surface, titre_rect)

        # 3. Affichage des 3 pièces
        nb_choix = len(self.pieces_proposees)
        largeur_totale_cartes = nb_choix * 200 + (nb_choix - 1) * 50
        start_x = (affichage_largeur - largeur_totale_cartes) // 2
        y_carte = affichage_hauteur // 2 - 100

        for i, piece in enumerate(self.pieces_proposees):
            x_carte = start_x + i * (200 + 50)
            carte_rect = pygame.Rect(x_carte, y_carte, 200, 300)
            
            # Couleur de fond basée sur la couleur de la pièce
            couleurs = {"bleue": (0,0,100), "dorée": (100,80,0), "verte": (0,80,0), "violette": (80,0,80), "grise": (50,50,50), "blanche": (100,100,100), "brune": (70,30,0)}
            couleur_fond = couleurs.get(piece.couleur, (30,30,30))
            pygame.draw.rect(self.screen, couleur_fond, carte_rect)
            pygame.draw.rect(self.screen, (255,255,255), carte_rect, 2)

            # Touche (1, 2, 3)
            touche_surface = self.font_grand.render(f"Touche {i+1}", True, (255, 255, 0))
            touche_rect = touche_surface.get_rect(center=(x_carte + 100, y_carte + 30))
            self.screen.blit(touche_surface, touche_rect)

            # Nom
            nom_surface = self.font_moyen.render(piece.nom, True, (255, 255, 255))
            nom_rect = nom_surface.get_rect(center=(x_carte + 100, y_carte + 80))
            self.screen.blit(nom_surface, nom_rect)

            # Image
            if piece.image:
                img_scaled = pygame.transform.scale(piece.image, (160, 160))
                self.screen.blit(img_scaled, (x_carte + 20, y_carte + 110))

            # Coût Gemmes
            if piece.cout_gemmes == 0:
                cout_txt = "Gratuit"
                couleur_cout = (0, 255, 0)
            else:
                cout_txt = f"Coût : {piece.cout_gemmes} Gemme(s)"
                couleur_cout = (0, 255, 255)
                if piece.cout_gemmes > self.joueur.inventaire.gemmes:
                    couleur_cout = (255, 0, 0) # Rouge si pas assez
                    
            cout_surface = self.font_petit.render(cout_txt, True, couleur_cout)
            cout_rect = cout_surface.get_rect(center=(x_carte + 100, y_carte + 280))
            self.screen.blit(cout_surface, cout_rect)
            
    # AFFICHAGE MAGASIN
    def affichage_magasin(self):
        """Affiche l'écran de la boutique."""
        # 1. Fond semi-transparent
        overlay = pygame.Surface((affichage_largeur, affichage_hauteur), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 200))
        self.screen.blit(overlay, (0, 0))

        # 2. Titre
        titre_surface = self.font_titre.render("BOUTIQUE", True, (255, 215, 0)) # Doré
        titre_rect = titre_surface.get_rect(center=(affichage_largeur // 2, 100))
        self.screen.blit(titre_surface, titre_rect)
        
        # Info
        info_surface = self.font_moyen.render("Appuyez sur 'Q' pour quitter", True, (255, 255, 255))
        info_rect = info_surface.get_rect(center=(affichage_largeur // 2, 150))
        self.screen.blit(info_surface, info_rect)

        # 3. Affichage des objets en vente
        nb_choix = len(self.magasin_items)
        largeur_totale_cartes = nb_choix * 200 + (nb_choix - 1) * 50
        start_x = (affichage_largeur - largeur_totale_cartes) // 2
        y_carte = affichage_hauteur // 2 - 100

        for i, item_data in enumerate(self.magasin_items):
            item_nom = item_data["item"]
            item_prix = item_data["prix"]
            
            x_carte = start_x + i * (200 + 50)
            carte_rect = pygame.Rect(x_carte, y_carte, 200, 300)
            
            pygame.draw.rect(self.screen, (50, 50, 50), carte_rect) # Fond gris
            pygame.draw.rect(self.screen, (255, 215, 0), carte_rect, 2) # Bordure dorée

            # Touche (1, 2, 3)
            touche_surface = self.font_grand.render(f"Touche {i+1}", True, (255, 255, 0))
            touche_rect = touche_surface.get_rect(center=(x_carte + 100, y_carte + 40))
            self.screen.blit(touche_surface, touche_rect)

            # Nom de l'objet
            nom_surface = self.font_moyen.render(item_nom, True, (255, 255, 255))
            nom_rect = nom_surface.get_rect(center=(x_carte + 100, y_carte + 100))
            self.screen.blit(nom_surface, nom_rect)
            
            # Image de l'objet
            img = self.images_objets.get(item_nom)
            if img:
                 img_scaled = pygame.transform.scale(img, (80, 80))
                 img_rect = img_scaled.get_rect(center=(x_carte + 100, y_carte + 170))
                 self.screen.blit(img_scaled, img_rect)

            # Prix
            cout_txt = f"Prix : {item_prix} Or"
            couleur_cout = (0, 255, 255) # Cyan
            if item_prix > self.joueur.inventaire.pieces_or:
                couleur_cout = (255, 0, 0) # Rouge si pas assez
                 
            cout_surface = self.font_petit.render(cout_txt, True, couleur_cout)
            cout_rect = cout_surface.get_rect(center=(x_carte + 100, y_carte + 250))
            self.screen.blit(cout_surface, cout_rect)

    # LOGIQUE DE JEU
    
    def _instancier_objet(self, nom_item: str):
        """Crée une instance d'objet à partir de son nom, via le MAP."""
        classe_objet = OBJET_MAP.get(nom_item)
        if classe_objet:
            return classe_objet() # Crée une instance, ex: Cle()
        else:
            print(f"Avertissement: Objet '{nom_item}' non trouvé dans OBJET_MAP.")
            return None

    def _generer_et_ramasser_butin(self, piece: Piece):
        """
        Génère le butin de la pièce (selon la couleur et la table de loot)
        et l'ajoute à l'inventaire du joueur.
        """
        objets_trouves = [] # Noms (str) des objets trouvés
        
        # 1. Récupérer la définition du loot depuis le catalogue
        loot_data = piece.loot
        if not loot_data:
            self.message_statut += " | Aucun objet ici."
            return

        # 2. Traiter le loot garanti
        for nom_item in loot_data.get("garanti", []):
            objets_trouves.append(nom_item)
            
        # 3. Traiter le loot aléatoire
        for nom_item, proba in loot_data.get("aleatoire", []):
            if random.random() < proba: # random() donne un float entre 0.0 et 1.0
                objets_trouves.append(nom_item)
                
        # 4. Traiter le loot basé sur la COULEUR 
        if piece.couleur == "verte": # Jardins
            if random.random() < 0.2: # 20% chance de gemme en plus
                objets_trouves.append("Gemme")
        
        elif piece.couleur == "violette": # Chambres
             if random.random() < 0.3: # 30% chance de pomme en plus (gain de pas)
                objets_trouves.append("Pomme")
        
        # 5. Si aucun objet n'a été trouvé
        if not objets_trouves:
            self.message_statut += " | Aucun objet ici."
            return

        # 6. Instancier et ramasser les objets
        message_loot = " | Vous trouvez : "
        items_str_list = []
        
        for nom_item in objets_trouves:
            objet_instance = self._instancier_objet(nom_item)
            if objet_instance:
                # La méthode ramasser_objet gère l'ajout (permanent ou consommable)
                self.joueur.inventaire.ramasser_objet(objet_instance, self.joueur)
                items_str_list.append(nom_item)
        
        self.message_statut += message_loot + ", ".join(items_str_list)

    def _entrer_magasin(self, piece: Piece):
        """Prépare et passe le jeu en état Magasin."""
        if piece.magasin:
            self.magasin_items = piece.magasin
            self.etat_jeu = "Magasin"
            self.message_statut = "Boutique ! (1, 2, 3) pour acheter. (Q) pour quitter."
        else:
            print(f"Avertissement: Pièce dorée '{piece.nom}' n'a pas de 'magasin' défini.")

    def _acheter_objet(self, index_choix: int):
        """Logique d'achat d'un objet dans la boutique."""
        if not (0 <= index_choix < len(self.magasin_items)):
            return # Touche invalide

        item_data = self.magasin_items[index_choix]
        nom_item = item_data["item"]
        prix = item_data["prix"]
        
        # 1. Vérifier si le joueur a assez d'or
        if self.joueur.inventaire.depenser_pieces_or(prix):
            # 2. Si oui, instancier l'objet
            objet_instance = self._instancier_objet(nom_item)
            if objet_instance:
                # 3. Ramasser l'objet
                self.joueur.inventaire.ramasser_objet(objet_instance, self.joueur)
                self.message_statut = f"Achat réussi : {nom_item} pour {prix} Or."
                
                # Optionnel : Retirer l'objet du magasin (stock limité)
                # self.magasin_items.pop(index_choix) 
            else:
                # Rembourser si l'objet n'existe pas (bogue ?)
                self.joueur.inventaire.pieces_or += prix
                self.message_statut = f"Erreur: Objet {nom_item} inconnu."
        else:
            # 4. Pas assez d'argent
            self.message_statut = f"Pas assez d'Or ! (Requis: {prix})"


    def deplacement(self, direction):
        if self.etat_jeu not in ["Deplacement", "Magasin"]: # On peut pas bouger si on choisit une pièce
            self.message_statut = "Veuillez choisir une pièce (Touches 1, 2, 3)"
            return
        # Si on est dans un magasin et on bouge, on quitte le magasin
        if self.etat_jeu == "Magasin":
            self.etat_jeu = "Deplacement"
            self.message_statut = "Vous quittez la boutique."

        nouvelle_ligne, nouvelle_colonne = self.joueur.calcul_coordonnees_casead(direction)

        if not (0 <= nouvelle_ligne < lignes_jeu and 0 <= nouvelle_colonne < colonnes_jeu):
            self.message_statut = "C'est un mur extérieur."
            return 

        piece_actuelle = self.manoir.get_piece_at(self.joueur.position_ligne, self.joueur.position_colonne)
        
     
        # Vérification si une porte (objet) existe dans cette direction
        porte_obj = piece_actuelle.portes_objets.get(direction)

        if porte_obj is None:
            self.message_statut = "Il n'y a pas de porte dans cette direction."
            return
        # LOGIQUE D'OUVERTURE ET DE DÉPLACEMENT 
        # On tente d'ouvrir la porte (gère la dépense de clé)
        if porte_obj.ouvrir(self.joueur):
            
            # L'ouverture a réussi (ou était déjà ouverte)
            destination_piece = self.manoir.get_piece_at(nouvelle_ligne, nouvelle_colonne)

            if destination_piece:
                # La pièce existe, on s'y déplace
                if self.joueur.deplacer_vers(nouvelle_ligne, nouvelle_colonne):
                    self.message_statut = f"Vous entrez dans {destination_piece.nom}"
                    # Vérifier si c'est l'antichambre (victoire)
                    if destination_piece.nom in ["Antechamber", "Antichambre"]:
                        self.victoire = True
                    # GESTION BOUTIQUE SI ON RE-ENTRE
                    elif destination_piece.couleur == "dorée":
                        self._entrer_magasin(destination_piece)
                else:
                    # Plus de pas
                    self.game_over = True
            else:
                #La pièce n'existe pas, on lance le tirage
                self.pieces_proposees = self.manoir.tirer_trois_pieces(
                    self.joueur.position_ligne,
                    self.joueur.position_colonne,
                    nouvelle_ligne,
                    nouvelle_colonne,
                    direction
                )

                if not self.pieces_proposees:
                    self.message_statut = "Perdu ! Plus de pièces valides dans la pioche."
                    self.game_over = True
                    return

                # Mémoriser la destination pour 'selectionner_piece'
                self.nouvelle_piece_coords = (nouvelle_ligne, nouvelle_colonne)
                self.direction_mouvement = direction
                
                self.etat_jeu = "Selection pieces"
                self.message_statut = "Choisissez une pièce (1, 2, 3). Dépensez un Dé (Touche R) pour relancer."
        else:
            # L'ouverture a échoué (porte verrouillée, pas de clé/kit)
            if porte_obj.niveau == 1:
                 self.message_statut = "Porte verrouillée (Niv 1). Clé ou Kit nécessaire."
            elif porte_obj.niveau == 2:
                self.message_statut = "Porte verrouillée (Niv 2). Clé nécessaire."


    def selectionner_piece(self, index_choix: int):
        """Logique appelée quand le joueur appuie sur 1, 2 ou 3.
        Place la pièce choisie, déplace le joueur et gère le ramassage des items.
        """
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

    def utiliser_de(self):
        """Relance le tirage des pièces si le joueur a un dé."""
        if self.joueur.inventaire.depenser_des(1): 
             # On ré-appelle la logique de tirage
             ligne, col = self.nouvelle_piece_coords
             self.pieces_proposees = self.manoir.tirer_trois_pieces(
                 self.joueur.position_ligne,
                 self.joueur.position_colonne,
                 ligne, col,
                 self.direction_mouvement
             )
             self.message_statut = "Tirage relancé ! (1, 2, 3 ou R)"
        else:
            self.message_statut = "Vous n'avez pas de Dés !"


    def gestion_evenements(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                self.flag_en_cours = False
            
            if event.type == pygame.KEYDOWN :
                
                if self.etat_jeu == "Fin":
                    if event.key == pygame.K_RETURN:
                        self.flag_en_cours = False
                
                elif self.etat_jeu == "Deplacement":
                    if event.key == pygame.K_z:
                        self.deplacement('up')
                    elif event.key == pygame.K_a:
                        self.deplacement('left')
                    elif event.key == pygame.K_s :
                        self.deplacement('down')
                    elif event.key == pygame.K_d :
                        self.deplacement('right')
                
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
                    elif event.key == pygame.K_q:
                        self.etat_jeu = "Deplacement"
                        self.message_statut = "Vous quittez la boutique."

                
    def verification_fin_jeu(self):
        # On vérifie si on doit passer à l'état "Fin"
        if self.game_over or self.victoire:
            self.etat_jeu = "Fin"
            return

        # Vérification des conditions de défaite
        if self.joueur.inventaire.pas <= 0:
            self.game_over = True
            self.etat_jeu = "Fin"
            
    # BOUCLE PRINCIPALE
    def en_cours_gestion(self):
        while self.flag_en_cours == True:
            # 1. Gérer les inputs
            self.gestion_evenements()
            
            # 2. Mettre à jour l'état du jeu
            self.verification_fin_jeu()
            
            # 3. Affichage
            if self.etat_jeu == "Fin":
                # On affiche l'écran de fin par-dessus le reste
                self.affichage_grille()
                self.affichage_inventaire()
                self.affichage_curseur()
                self.affichage_d_v()
                
            else: # "Deplacement", "Selection pieces", ou "Magasin"
                self.affichage_grille()
                self.affichage_inventaire()
                self.affichage_curseur()
                self.affichage_message_statut() # Affichage du message
                
                if self.etat_jeu == "Selection pieces":
                    self.affichage_selection_pieces() # Affichage du choix
                
                elif self.etat_jeu == "Magasin":
                    self.affichage_magasin() # Affichage de la boutique
            
            
            pygame.display.flip()
            self.clock.tick(60) # 60 FPS
            
        pygame.quit()