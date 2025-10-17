import pygame 
from joueur import Joueur
from Manoir import Manoir 

colonnes_jeu = 5
lignes_jeu = 9 

nb_pixels_piece = 70
start_x_grille = 50
start_y_grille = 50

largeur_grille_seule = colonnes_jeu * nb_pixels_piece 
hauteur_grille_seule = lignes_jeu * nb_pixels_piece

largeur_inventaire = 450
espace_inventiare = 100

# affichage complet jeu
affichage_largeur = start_x_grille + largeur_grille_seule + espace_inventiare + largeur_inventaire + start_x_grille
affichage_hauteur = start_y_grille * 2 + hauteur_grille_seule

police = 'C:/Users/maxdr/OneDrive/Bureau/Police/Stay Retro PersonalUseOnly.ttf'
    
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
        
        self.etat_jeu = "Deplacement" # États possibles: "Deplacement", "Selection pieces"
        self.pieces_proposees = []
        self.message_statut = "Utilisez ZQSD pour vous déplacer."

        self.font_petit = pygame.font.Font(None, 30)
        # Gestion de l'erreur si la police n'est pas trouvée
        try:
            self.font_grand = pygame.font.Font(police, 30)
        except FileNotFoundError:
            print(f"Attention : Police non trouvée à l'adresse {police}. Utilisation de la police par défaut.")
            self.font_grand = pygame.font.Font(None, 40)
    
    def affichage_d_v(self): 
        fenetre_fin = pygame.Surface((affichage_largeur, affichage_hauteur), pygame.SRCALPHA)
        fenetre_fin.fill((0, 0, 0, 220)) 
        self.screen.blit(fenetre_fin, (0, 0))
        
        if self.victoire == True:
            texte = "VICTOIRE : Vous êtes arrivés à l'antichambre :)"
            affichage = self.font_grand.render(texte, True, (0, 255, 0))
        else:
            texte = "DEFAITE : Vous êtes à cours de pas :("
            affichage = self.font_grand.render(texte, True, (255, 0, 0))
            
        espace_texte = affichage.get_rect(center=(affichage_largeur // 2, affichage_hauteur // 2))
        self.screen.blit(affichage, espace_texte)
        
        instruction_surface = self.font_petit.render("Pour quitter : ENTREE", True, (255, 255, 255))
        instruction_rect = instruction_surface.get_rect(center=(affichage_largeur // 2, affichage_hauteur // 2 + 50))
        self.screen.blit(instruction_surface, instruction_rect)


    def affichage_grille(self):
        self.screen.fill((168,195,188))
        
        for r in range(lignes_jeu): 
            for c in range(colonnes_jeu):
                x = start_x_grille + c * nb_pixels_piece
                y = start_y_grille + r * nb_pixels_piece
                rect = pygame.Rect(x, y, nb_pixels_piece, nb_pixels_piece)
                
                #Dessiner la pièce si elle existe ---
                piece = self.manoir.get_piece_at(r, c)
                if piece:
                    # TODO: Charger et afficher piece.image_path
                    pygame.draw.rect(self.screen, (50, 50, 150), rect) # Couleur temporaire
                else:
                    pygame.draw.rect(self.screen, (0, 0, 0), rect) 
                
        bords_jeu = pygame.Rect(start_x_grille - 2, start_y_grille - 2, largeur_grille_seule + 4, hauteur_grille_seule + 4)
        pygame.draw.rect(self.screen, (255, 255, 255), bords_jeu, 2)
        
        
    def affichage_inventaire(self): 
        x = start_x_grille + largeur_grille_seule + espace_inventiare
        y = start_y_grille
        
        inventaire_rect = pygame.Rect(x, y, largeur_inventaire, hauteur_grille_seule)
        pygame.draw.rect(self.screen, (30, 30, 60), inventaire_rect)

        self.screen.blit(self.font_grand.render("Inventaire", True, (255, 255, 255)), (x+5, y+15))

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
            if q :
                self.screen.blit(self.font_petit.render(n, True, (0, 128, 0)), (x + 10, y_permanent))
                y_permanent += 50
            else :
                self.screen.blit(self.font_petit.render(n, True, (255, 255, 255)), (x + 10, y_permanent))
                y_permanent += 50

        y_consommable = y + 90
        posx_ob_c = x + (largeur_inventaire // 2) + 60
        for n, q in dicto_inventaire['CONSOMMABLE']:
            self.screen.blit(self.font_petit.render(f"{n} : {q}", True, (255, 255, 255)), (posx_ob_c, y_consommable))
            y_consommable += 50
        
        
    def affichage_curseur(self): 
        curseur_c = self.joueur.position_colonne
        curseur_r = self.joueur.position_ligne
        
        x = start_x_grille + curseur_c * nb_pixels_piece
        y = start_y_grille + curseur_r * nb_pixels_piece
        curseur = pygame.Rect(x, y, nb_pixels_piece, nb_pixels_piece)
        pygame.draw.rect(self.screen, (255, 255, 0), curseur, 2)

    def deplacement(self, direction):
        
        # On ne peut pas se déplacer si on doit choisir une pièce
        if self.etat_jeu == "Selection pieces":
            self.message_statut = "Veuillez choisir une pièce (Touches 1, 2, 3)"
            return

        nouvelle_ligne, nouvelle_colonne = self.joueur.calcul_coordonnees_casead(direction)
        
        if not (0 <= nouvelle_ligne < lignes_jeu and 0 <= nouvelle_colonne < colonnes_jeu):
            self.message_statut = "C'est un mur extérieur."
            return 
            
        destination_piece = self.manoir.get_piece_at(nouvelle_ligne, nouvelle_colonne)
        piece_actuelle = self.manoir.get_piece_at(self.joueur.position_ligne, self.joueur.position_colonne)
        
        lock_level = piece_actuelle.get_door_lock_level(direction) 
        
        if lock_level == -1:
            self.message_statut = "Il n'y a pas de porte dans cette direction."
            return

        if destination_piece is not None:
            # La pièce existe, on vérifie juste si la porte est ouverte (lock_level 0)
            if lock_level != 0:
                self.message_statut = "La porte est refermée ?" # Cas étrange
                return
                
            if self.joueur.deplacer_vers(nouvelle_ligne, nouvelle_colonne):
                self.message_statut = f"Vous entrez dans {destination_piece.nom}"
            else:
                self.game_over = True # Plus de pas
            return
        
        if self.joueur.ouverture_porte(lock_level) == True:
            self.pieces_proposees = self.manoir.tirer_trois_pieces(
                self.joueur.position_ligne, self.joueur.position_colonne, 
                nouvelle_ligne, nouvelle_colonne, direction
            )
            
            if not self.pieces_proposees:
                 self.message_statut = "Perdu ! Plus de pièces disponibles dans la pioche."
                 self.game_over = True
                 return

            self.etat_jeu = "Selection pieces"
            self.message_statut = "Choississez une piece (1, 2, 3)"
            
            # TODO: Il manque la logique pour gérer la sélection (dans self.quitter)
            # et appeler self.manoir.placer_piece(...)
            
        else:
            # Échec de l'ouverture
            if lock_level == 1 and self.joueur.inventaire.a_objet_permanent("Kit de Crochetage"):
                 self.message_statut = "Porte verrouillée (Niv 1) et vous n'avez plus de clé."
            elif lock_level == 2:
                 self.message_statut = "Porte verrouillée (Niv 2) : une clé est nécessaire."
            else:
                 self.message_statut = "Porte verrouillée (Niv 1) : Clé ou Kit nécessaire."
                 
                 
    def quitter(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                self.flag_en_cours = False
            if event.type == pygame.KEYDOWN :
                
                if (self.game_over == True and event.key == pygame.K_RETURN):
                    self.flag_en_cours = False
                    
                if not self.game_over and self.etat_jeu == "Deplacement":
                    if event.key == pygame.K_z :
                        self.deplacement('up')
                    if event.key == pygame.K_q :
                        self.deplacement('left')
                    if event.key == pygame.K_s :
                        self.deplacement('down')
                    if event.key == pygame.K_d :
                        self.deplacement('right')
                
                # TODO: Gérer l'état "Selection pieces"
                # if not self.game_over and self.etat_jeu == "Selection pieces":
                #    if event.key == pygame.K_1:
                #        choix = self.pieces_proposees[0]
                #        ... (logique de placement)
                
                
    def verification_fin_jeu(self):
        if (self.joueur.inventaire.pas <= 0 or self.victoire == True): 
            self.game_over = True
            
    def en_cours_gestion(self):
        while self.flag_en_cours == True:
            self.quitter()
            self.verification_fin_jeu()
            
            if not self.game_over:
                self.affichage_grille()
                self.affichage_inventaire()
                self.affichage_curseur()
                
                # TODO: Afficher les pièces proposées si etat_jeu == "Selection pieces"
                # TODO: Afficher self.message_statut
                
            else :
                self.affichage_d_v()
            
            pygame.display.flip()
            self.clock.tick(100)
            
        pygame.quit()
