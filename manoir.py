# Manoir.py
import random
from ClassePiece import Piece
from ClassePorte import Porte
from Catalogue_pieces import catalogue_pieces
# L'import "from jeu import *" peut causer des problèmes de dépendance circulaire
# Il vaut mieux l'éviter si possible, mais on le laisse pour l'instant car pas d'autres solution.
#from jeu import * 
class Manoir:
    """
    Gère la grille du manoir 5x9, la pioche de pièces
    et la logique de placement.
    """
    def __init__(self, lignes_jeu=9, colonnes_jeu=5):
        self.lignes = lignes_jeu
        self.colonnes = colonnes_jeu
        
        # Grille 2D stockant les objets Piece (ou None si vide)
        self.grille = [[None for _ in range(self.colonnes)] for _ in range(self.lignes)]
        
        # Pioche de pièces (objets Piece, pas dictionnaires)
        self.pioche = self._initialiser_pioche()
        
        # Placer l'entrée
        self._placer_piece_depart()
        self._placer_piece_finale()

    def _initialiser_pioche(self) -> list[Piece]:
        """
        Crée la pioche d'objets Piece à partir du catalogue de dictionnaires.
        L'Entrance Hall et l'Antichambre sont exclues de la pioche.
        """
        pioche = []
        for data_piece in catalogue_pieces:
            if data_piece["nom"] != "Entrance Hall" and data_piece["nom"] != "Antechamber":
                # Convertit le dictionnaire en objet Piece
                pioche.append(Piece(**data_piece))
                # Chargement de l'image dès l'initialisation
                pioche[-1].charger_image("Images.zip") 
        return pioche

    def _placer_piece_depart(self):
        """
        Trouve l'Entrance Hall, la crée et la place sur la grille (8, 2).
        Initialise ses portes comme étant déverrouillées et ouvertes.
        """
        pos_ligne, pos_col = 8, 2 # Position de départ
        
        data_entree = next((p for p in catalogue_pieces if p["nom"] == "Entrance Hall"), None)
        piece_entree = Piece(**data_entree)
        piece_entree.charger_image("Images.zip")
        self.grille[pos_ligne][pos_col] = piece_entree
        
        # Crée les objets Porte pour l'Entrance Hall
        
        for direction, existe in piece_entree.portes.items():
            if existe:
                 # Les portes de départ sont toujours ouvertes et niveau 0
                piece_entree.portes_objets[direction] = Porte(niveau=0, ouverte=True)
       

    def _placer_piece_finale(self):
        """
        Trouve l'Antichambre, la crée et la place sur la grille (0, 2).
        """
        pos_ligne, pos_col = 0, 2 
        data_finale = next((p for p in catalogue_pieces if p["nom"] == "Antechamber"), None)
        piece_finale = Piece(**data_finale)
        piece_finale.charger_image("Images.zip")
        self.grille[pos_ligne][pos_col] = piece_finale
        
        # Création des portes pour la pièce finale
        for direction, existe in piece_finale.portes.items():
            if existe:
                #Niveau de verrouillage généré selon la profondeur
                niveau = Porte.generer_niveau_verrouillage(pos_ligne, self.lignes)
                
                
                if pos_ligne == 0:
                    niveau = 2
                
                piece_finale.portes_objets[direction] = Porte(niveau=niveau, ouverte=False)
                
                
    def get_piece_at(self, ligne: int, colonne: int) -> Piece | None:
        """
        Récupère l'objet Piece aux coordonnées données.
        """
        if 0 <= ligne < self.lignes and 0 <= colonne < self.colonnes:
            return self.grille[ligne][colonne]
        return None

    def placer_piece(self, piece: Piece, ligne: int, colonne: int, ligne_entree: int, col_entree: int, direction_mouvement: str):
        """
        Place une pièce choisie sur la grille et crée ses portes.
        Met aussi à jour la porte de la pièce précédente.
        """
        if not (0 <= ligne < self.lignes and 0 <= colonne < self.colonnes):
            return # Placement hors grille
            
        # 1. Placer la pièce
        self.grille[ligne][colonne] = piece
        
        # 2. Retirer de la pioche (si elle y est)
        if piece in self.pioche:
            self.pioche.remove(piece)
            
        # 3. Définir la direction d'où l'on vient (pour la nouvelle pièce)
        
        directions_opposees = {'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left'}
        
        porte_entree_nom = directions_opposees[direction_mouvement] # ex: 'up' -> 'down'

        # 4. Créer les objets Porte pour la nouvelle pièce
        for direction, existe in piece.portes.items():
            if existe:
                # On vérifie si la porte actuelle (ex: 'down') est la porte d'entrée
                if direction == porte_entree_nom:
                    # La porte par laquelle on entre est ouverte et niveau 0
                    porte = Porte(niveau=0, ouverte=True)
                else:
                    # Les autres portes sont générées aléatoirement
                    niveau = Porte.generer_niveau_verrouillage(ligne, self.lignes) 
                    porte = Porte(niveau=niveau, ouverte=False)
                
                piece.portes_objets[direction] = porte
                
        # 5. Mettre à jour la porte de la pièce d'origine (l'ouvrir)
        piece_precedente = self.get_piece_at(ligne_entree, col_entree)
        if piece_precedente and direction_mouvement in piece_precedente.portes_objets:
             piece_precedente.portes_objets[direction_mouvement].ouverte = True


    def tirer_trois_pieces(self, ligne_actuelle: int, col_actuelle: int, ligne_nouvelle: int, col_nouvelle: int, direction_mouvement: str) -> list[Piece]:
        """
        Tire 3 pièces candidates pour le nouvel emplacement, en respectant la rareté
        et la règle de la pièce gratuite.
        """
        
        # 1.Définir la porte que la nouvelle pièce DOIT avoir
        directions_opposees = {'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left'}        
        porte_requise = directions_opposees[direction_mouvement]
        
        # 2. Filtrer la pioche
        pioche_filtree = [
            p for p in self.pioche 
            if p.portes.get(porte_requise, False) # Vérifie si la porte requise existe
        ]

        if not pioche_filtree:
            return [] # Plus de pièces valides

        # 3. Séparer gratuites et payantes pour la règle
        pieces_gratuites = [p for p in pioche_filtree if p.cout_gemmes == 0]
        pieces_payantes = [p for p in pioche_filtree if p.cout_gemmes > 0]
        
        candidates = []
        
        # 4. Gérer la rareté
        def get_poids(piece):
            # Ajout d'une protection pour éviter la division par zéro si rareté est négative (peu probable)
            # Et gestion de 3**0 = 1
            if piece.rarete < 0: return 1.0
            return 1 / (3**piece.rarete)

        # 5. S'assurer qu'au moins une pièce gratuite est proposée
        if pieces_gratuites:
            poids_gratuites = [get_poids(p) for p in pieces_gratuites]
            if not any(p > 0 for p in poids_gratuites): # Au cas où tous les poids sont 0
                choix_gratuit = random.choice(pieces_gratuites)
            else:
                choix_gratuit = random.choices(pieces_gratuites, weights=poids_gratuites, k=1)[0]
            candidates.append(choix_gratuit)

        # 6. Compléter avec d'autres pièces (gratuites ou payantes)
        pioche_restante = [p for p in pioche_filtree if p not in candidates] # Évite les doublons
        
        while len(candidates) < 3 and pioche_restante:
            poids_restants = [get_poids(p) for p in pioche_restante]
            
            if not any(p > 0 for p in poids_restants):
                if not pioche_restante: break # Sécurité
                choix = random.choice(pioche_restante)
            else:
                choix = random.choices(pioche_restante, weights=poids_restants, k=1)[0]
            
            candidates.append(choix)
            pioche_restante.remove(choix) # Assure l'unicité
            
        random.shuffle(candidates) # Mélange l'ordre d'affichage
        return candidates