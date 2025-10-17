# Manoir.py
import random
from ClassePiece import Piece
from portes import Porte
from Catalogues_pieces import CATALOGUE_PIECES
from jeu import lignes_jeu, colonnes_jeu # Importe les constantes de la grille

class Manoir:
    """
    Gère la grille du manoir 5x9, la pioche de pièces
    et la logique de placement.
    """
    def __init__(self):
        self.lignes = lignes_jeu
        self.colonnes = colonnes_jeu
        
        # Grille 2D stockant les objets Piece (ou None si vide)
        self.grille = [[None for _ in range(self.colonnes)] for _ in range(self.lignes)]
        
        # Pioche de pièces (objets Piece, pas dictionnaires)
        self.pioche = self._initialiser_pioche()
        
        # Placer l'entrée
        self._placer_piece_depart()

    def _initialiser_pioche(self) -> list[Piece]:
        """
        Crée la pioche d'objets Piece à partir du catalogue de dictionnaires.
        L'Entrance Hall est exclue de la pioche car elle est placée au début.
        """
        pioche = []
        for data_piece in CATALOGUE_PIECES:
            if data_piece["nom"] != "Entrance Hall":
                # Convertit le dictionnaire en objet Piece
                pioche.append(Piece(**data_piece))
        return pioche

    def _placer_piece_depart(self):
        """
        Trouve l'Entrance Hall, la crée et la place sur la grille (8, 2).
        Initialise ses portes comme étant déverrouillées et ouvertes.
        """
        pos_ligne, pos_col = 8, 2 # Position de départ
        
        # Trouve les données de l'Entrance Hall
        data_entree = next((p for p in CATALOGUE_PIECES if p["nom"] == "Entrance Hall"), None)
        
        if data_entree is None:
            raise ValueError("Erreur : 'Entrance Hall' non trouvée dans le catalogue.")

        piece_entree = Piece(**data_entree)
        self.grille[pos_ligne][pos_col] = piece_entree
        
        # Crée les objets Porte pour l'Entrance Hall
        # Les portes de départ sont toujours ouvertes et niveau 0
        for direction, existe in piece_entree.portes_config.items():
            if existe:
                piece_entree.portes_objets[direction] = Porte(niveau=0, ouverte=True)

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
        directions_opposees = {'up': 'bas', 'down': 'haut', 'left': 'droite', 'right': 'left'}
        porte_entree_nom = directions_opposees[direction_mouvement]

        # 4. Créer les objets Porte pour la nouvelle pièce
        for direction, existe in piece.portes_config.items():
            if existe:
                if direction == porte_entree_nom:
                    # La porte par laquelle on entre est ouverte et niveau 0
                    porte = Porte(niveau=0, ouverte=True)
                else:
                    # Les autres portes sont générées aléatoirement
                    niveau = Porte.generer_niveau_verrouillage(ligne, self.lignes) #
                    porte = Porte(niveau=niveau, ouverte=False)
                
                piece.portes_objets[direction] = porte
                
        # 5. Mettre à jour la porte de la pièce d'origine (l'ouvrir)
        piece_precedente = self.get_piece_at(ligne_entree, col_entree)
        if piece_precedente and piece_precedente.get_porte(direction_mouvement):
             piece_precedente.portes_objets[direction_mouvement].ouverte = True


    def tirer_trois_pieces(self, ligne_actuelle: int, col_actuelle: int, ligne_nouvelle: int, col_nouvelle: int, direction_mouvement: str) -> list[Piece]:
        """
        Tire 3 pièces candidates pour le nouvel emplacement.
        """
        # 1. Définir la porte que la nouvelle pièce DOIT avoir
        directions_opposees = {'up': 'bas', 'down': 'haut', 'left': 'droite', 'right': 'left'}
        porte_requise = directions_opposees[direction_mouvement]
        
        # 2. Filtrer la pioche
        #    Doit avoir la porte d'entrée
        #    Doit respecter les conditions de placement (ex: 'côté ouest') 
        #    Doit respecter les portes extérieures (ne pas créer de porte vers le vide)
        
        pioche_filtree = [
            p for p in self.pioche 
            if p.portes_config.get(porte_requise, False) # Vérifie si la porte requise existe
        ]

        if not pioche_filtree:
            return [] # Plus de pièces valides

        # 3. S'assurer qu'au moins une pièce gratuite est proposée 
        pieces_gratuites = [p for p in pioche_filtree if p.cout_gemmes == 0]
        pieces_payantes = [p for p in pioche_filtree if p.cout_gemmes > 0]
        
        candidates = []
        
        # TODO: Implémenter la logique de rareté 
        # Pour l'instant, on prend au hasard
        
        # 3a. Ajouter une pièce gratuite (si possible)
        if pieces_gratuites:
            candidates.append(random.choice(pieces_gratuites))
            
        # 3b. Compléter avec d'autres pièces
        pioche_restante = pieces_payantes + pieces_gratuites
        while len(candidates) < 3 and pioche_restante:
            choix = random.choice(pioche_restante)
            if choix not in candidates:
                candidates.append(choix)
            pioche_restante.remove(choix)
            
        return candidates