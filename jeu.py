import pygame 
from joueur import Joueur
from manoir import Manoir 
from ClassePiece import *
# Importation de Porte pour la logique de 'deplacement'
from ClassePorte import Porte 

# --- CONSTANTES D'AFFICHAGE ---
colonnes_jeu = 5
lignes_jeu = 9 

nb_pixels_piece = 80
start_x_grille = 20
start_y_grille = 20

largeur_grille_seule = colonnes_jeu * nb_pixels_piece 
hauteur_grille_seule = lignes_jeu * nb_pixels_piece

largeur_inventaire = 500
espace_inventiare = 50

# affichage complet jeu
affichage_largeur = start_x_grille + largeur_grille_seule + espace_inventiare + largeur_inventaire + start_x_grille
affichage_hauteur = start_y_grille * 2 + hauteur_grille_seule

# Chemin relatif pour la police (plus robuste)
try:
    police_path = os.path.join(os.path.dirname(__file__), 'Police', 'Stay Retro PersonalUseOnly.ttf')
    # Vérification si le fichier existe
    if not os.path.exists(police_path):
        # Si le chemin du Bureau était correct sur votre PC, on l'utilise en fallback
        police_path = 'C:/Users/maxdr/OneDrive/Bureau/Police/Stay Retro PersonalUseOnly.ttf'
        if not os.path.exists(police_path):
            raise FileNotFoundError # Déclenche le except
    police = police_path
except FileNotFoundError:
    print(f"Attention : Police non trouvée. Utilisation de la police par défaut.")
    police = None # Pygame utilisera sa police par défaut
    

# --- CLASSE JEU ---
    
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
        
        self.etat_jeu = "Deplacement" # États: "Deplacement", "Selection pieces", "Fin"
        self.pieces_proposees = []
        self.message_statut = "Utilisez ZQSD pour vous déplacer."

        # Ajout de variables pour mémoriser la transition
        self.nouvelle_piece_coords = None 
        self.direction_mouvement = None

        # Gestion des polices
        self.font_petit = pygame.font.Font(None, 30)
        self.font_moyen = pygame.font.Font(None, 35)
        try:
            self.font_grand = pygame.font.Font(police, 30)
            self.font_titre = pygame.font.Font(police, 45)
        except Exception: # Attrape FileNotFoundError ou erreur pygame si police=None
            print(f"Utilisation de la police par défaut de Pygame.")
            self.font_grand = pygame.font.Font(None, 40) # Fallback
            self.font_titre = pygame.font.Font(None, 50) # Fallback
    
    # --- AFFICHAGE FIN DE PARTIE ---
    def affichage_d_v(self): 
        fenetre_fin = pygame.Surface((affichage_largeur, affichage_hauteur), pygame.SRCALPHA)
        fenetre_fin.fill((0, 0, 0, 220)) 
        self.screen.blit(fenetre_fin, (0, 0))
        
        if self.victoire == True:
            texte = "VICTOIRE : Vous êtes arrivés à l'antichambre :)"
            affichage = self.font_titre.render(texte, True, (0, 255, 0))
        else:
            [span_29](start_span)texte = "DEFAITE : Vous êtes à cours de pas :("[span_29](end_span)
            affichage = self.font_titre.render(texte, True, (255, 0, 0))
            
        espace_texte = affichage.get_rect(center=(affichage_largeur // 2, affichage_hauteur // 2))
        self.screen.blit(affichage, espace_texte)
        
        instruction_surface = self.font_moyen.render("Pour quitter : ENTREE", True, (255, 255, 255))
        instruction_rect = instruction_surface.get_rect(center=(affichage_largeur // 2, affichage_hauteur // 2 + 50))
        self.screen.blit(instruction_surface, instruction_rect)

    # --- AFFICHAGE JEU ---
    def affichage_grille(self):
        self.screen.fill((168,195,188)) # Fond général
        
        # Fond de la grille
        fond_grille_rect = pygame.Rect(start_x_grille, start_y_grille, largeur_grille_seule, hauteur_grille_seule)
        pygame.draw.rect(self.screen, (10, 10, 10), fond_grille_rect) # Fond noir pour les cases vides
        
        for r in range(lignes_jeu): 
            for c in range(colonnes_jeu):
                x = start_x_grille + c * nb_pixels_piece
                y = start_y_grille + r * nb_pixels_piece
                
                piece = self.manoir.get_piece_at(r, c)
                if piece and piece.image:
                    image_redim = pygame.transform.scale(piece.image, (nb_pixels_piece, nb_pixels_piece))
                    self.screen.blit(image_redim, (x, y))
                elif piece: # Si la pièce existe mais l'image a échoué à charger
                     pygame.draw.rect(self.screen, (255,0,0), (x,y, nb_pixels_piece, nb_pixels_piece))
                # else: (On laisse le fond noir)
                
        # Dessiner les bordures de la grille
        bords_jeu = pygame.Rect(start_x_grille - 2, start_y_grille - 2, largeur_grille_seule + 4, hauteur_grille_seule + 4)
        pygame.draw.rect(self.screen, (255, 255, 255), bords_jeu, 2)
        
        
    def affichage_inventaire(self): 
        x = start_x_grille + largeur_grille_seule + espace_inventiare
        y = start_y_grille
        
        inventaire_rect = pygame.Rect(x, y, largeur_inventaire, hauteur_grille_seule)
        pygame.draw.rect(self.screen, (0, 0, 0), inventaire_rect)

        self.screen.blit(self.font_grand.render("Inventaire", True, (255, 255, 255)), (x+15, y+15))

        dicto_inventaire = {
            'PERMANENT': [
                ("Kit de Crochetage", self.joueur.inventaire.a_objet_permanent("Kit de Crochetage")),
                ("Patte de Lapin", self.joueur.inventaire.a_objet_permanent("Patte de Lapin")),
                ("Pelle", self.joueur.inventaire.a_objet_permanent("Pelle")),
                ("Marteau", self.joueur.inventaire.a_objet_permanent("Marteau")),
                ("Détecteur de Métaux", self.joueur.inventaire.a_objet_permanent("Détecteur de Métaux")),],
            'CONSOMMABLE': [
                ("Pas", self.joueur.inventaire.pas),
                ("Pièces d'or", self.joueur.inventaire.pieces_or),
                ("Gemmes", self.joueur.inventaire.gemmes),
                ("Clés", self.joueur.inventaire.cles),
                ("Dés", self.joueur.inventaire.des),]
        }
        
        y_permanent = y + 90
        for n, q in dicto_inventaire['PERMANENT']:
            couleur = (0, 200, 0) if q else (150, 150, 150) # Vert si possédé, gris sinon
            self.screen.blit(self.font_petit.render(n, True, couleur), (x + 20, y_permanent))
            y_permanent += 50

        y_consommable = y + 90
        posx_ob_c = x + (largeur_inventaire // 2) + 40
        for n, q in dicto_inventaire['CONSOMMABLE']:
            couleur = (255, 255, 255)
            if n == "Pas" and q <= 10: couleur = (255, 100, 100) # Rouge si peu de pas
            elif n == "Pas" and q > 70: couleur = (100, 255, 100) # Vert si beaucoup de pas
                
            self.screen.blit(self.font_petit.render(f"{n} : {q}", True, couleur), (posx_ob_c, y_consommable))
            y_consommable += 50
        
        
    def affichage_curseur(self): 
        curseur_c = self.joueur.position_colonne
        curseur_r = self.joueur.position_ligne
        
        x = start_x_grille + curseur_c * nb_pixels_piece
        y = start_y_grille + curseur_r * nb_pixels_piece
        curseur = pygame.Rect(x, y, nb_pixels_piece, nb_pixels_piece)
        pygame.draw.rect(self.screen, (255, 255, 0), curseur, 3) # Epaisseur 3 pour visibilité

    def affichage_message_statut(self):
        """Affiche le message de statut en bas de l'inventaire."""
        x = start_x_grille + largeur_grille_seule + espace_inventiare
        y = start_y_grille + hauteur_grille_seule - 100 # En bas de l'inventaire
        
        # Fond pour le message
        fond_message_rect = pygame.Rect(x, y, largeur_inventaire, 100)
        pygame.draw.rect(self.screen, (30, 30, 30), fond_message_rect) # Gris foncé
        
        # Texte (potentiellement sur plusieurs lignes)
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
            cout_txt = f"Coût : {piece.cout_gemmes} Gemme(s)"
            couleur_cout = (0, 255, 255)
            if piece.cout_gemmes > self.joueur.inventaire.gemmes:
                couleur_cout = (255, 0, 0) # Rouge si pas assez
            elif piece.cout_gemmes == 0:
                 couleur_cout = (0, 255, 0) # Vert si gratuit
                 
            cout_surface = self.font_petit.render(cout_txt, True, couleur_cout)
            cout_rect = cout_surface.get_rect(center=(x_carte + 100, y_carte + 280))
            self.screen.blit(cout_surface, cout_rect)

    # --- LOGIQUE DE JEU ---
    def deplacement(self, direction):
        if self.etat_jeu != "Deplacement":
            self.message_statut = "Veuillez choisir une pièce (Touches 1, 2, 3)"
            return

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
        """Logique appelée quand le joueur appuie sur 1, 2 ou 3."""
        
        if not (0 <= index_choix < len(self.pieces_proposees)):
            return # Touche invalide

        piece_choisie = self.pieces_proposees[index_choix]
        cout = piece_choisie.cout_gemmes

        #Tenter de dépenser les gemmes
        if self.joueur.inventaire.depenser_gemmes(cout):
            # Assez de gemmes
            ligne, col = self.nouvelle_piece_coords
            
            # Placer la pièce dans le manoir
            self.manoir.placer_piece(
                piece_choisie,
                ligne, col,
                self.joueur.position_ligne, self.joueur.position_colonne,
                self.direction_mouvement
            )
            
            # Déplacer le joueur
            if self.joueur.deplacer_vers(ligne, col):
                self.message_statut = f"Vous avez découvert : {piece_choisie.nom}"
                # TODO: Ramasser les items de la pièce
            else:
                self.game_over = True # Ne devrait pas arriver ici, mais sécurité
            
            # Réinitialiser
            self.etat_jeu = "Deplacement"
            self.pieces_proposees = []
            self.nouvelle_piece_coords = None
            self.direction_mouvement = None
            
        else:
            # Pas assez de gemmes
            self.message_statut = f"Pas assez de gemmes ! (Requis: {cout})"

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


    # --- GESTION DES EVENEMENTS ---
    def gestion_evenements(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                self.flag_en_cours = False
            
            if event.type == pygame.KEYDOWN :
                
                # --- État "Fin de partie" ---
                if self.etat_jeu == "Fin":
                    if event.key == pygame.K_RETURN:
                        self.flag_en_cours = False
                
                # --- État "Déplacement" ---
                elif self.etat_jeu == "Deplacement":
                    if event.key == pygame.K_z: # ZQSD
                        self.deplacement('up')
                    elif event.key == pygame.K_q :
                        self.deplacement('left')
                    elif event.key == pygame.K_s :
                        self.deplacement('down')
                    elif event.key == pygame.K_d :
                        self.deplacement('right')
                
                # --- État "Sélection de pièces" ---
                elif self.etat_jeu == "Selection pieces":
                    if event.key == pygame.K_1 or event.key == pygame.K_KP_1: # Touche 1
                        self.selectionner_piece(0)
                    elif event.key == pygame.K_2 or event.key == pygame.K_KP_2: # Touche 2
                        self.selectionner_piece(1)
                    elif event.key == pygame.K_3 or event.key == pygame.K_KP_3: # Touche 3
                        self.selectionner_piece(2)
                    elif event.key == pygame.K_r: # 'R' pour Relancer (Dé)
                        self.utiliser_de()

                
    def verification_fin_jeu(self):
        # On vérifie si on doit passer à l'état "Fin"
        if self.game_over or self.victoire:
            self.etat_jeu = "Fin"
            return

        # Vérification des conditions de défaite
        if self.joueur.inventaire.pas <= 0:
            self.game_over = True
            self.etat_jeu = "Fin"
            
    # --- BOUCLE PRINCIPALE ---
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
                
            else: # "Deplacement" ou "Selection pieces"
                self.affichage_grille()
                self.affichage_inventaire()
                self.affichage_curseur()
                self.affichage_message_statut() # Affichage du message
                
                if self.etat_jeu == "Selection pieces":
                    self.affichage_selection_pieces() # Affichage du choix
                
            
            pygame.display.flip()
            self.clock.tick(60) # 60 FPS
            
        pygame.quit()
