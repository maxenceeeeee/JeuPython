# manoir.py
import random
from ClassePiece import Piece
from ClassePorte import Porte
from Catalogue_pieces import catalogue_pieces

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
        
        # Placer l'entrée et la pièce finale
        self._placer_piece_depart()
        self._placer_piece_finale()

    def _initialiser_pioche(self) -> list[Piece]:
        """
        Crée la pioche d'objets Piece à partir du catalogue de dictionnaires.
        L'Entrance Hall et l'Antichambre sont exclues de la pioche.
        """
        pioche = []
        for data_piece in catalogue_pieces:
            if data_piece["nom"] not in ["Entrance Hall", "Antechamber"]:
                # Convertit le dictionnaire en objet Piece
                pioche.append(Piece(**data_piece))
                pioche[-1].charger_image("Images.zip") 
        return pioche

    def _placer_piece_depart(self):
        """
        Trouve l'Entrance Hall, la crée et la place sur la grille (8, 2).
        Initialise ses portes comme étant déverrouillées et ouvertes.
        """
        pos_ligne, pos_col = 8, 2
        data_entree = next((p for p in catalogue_pieces if p["nom"] == "Entrance Hall"), None)
        piece_entree = Piece(**data_entree)
        piece_entree.charger_image("Images.zip")
        self.grille[pos_ligne][pos_col] = piece_entree
        
        # Création des portes pour l'entrée
        for direction, existe in piece_entree.portes.items():
            if existe:
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
        Met à jour la porte de la pièce précédente et synchronise les portes opposées.
        """
        if not (0 <= ligne < self.lignes and 0 <= colonne < self.colonnes):
            return # Placement hors grille
            
        # Placer la pièce
        self.grille[ligne][colonne] = piece
        
        # Retirer de la pioche si nécessaire
        if piece in self.pioche:
            self.pioche.remove(piece)
        
        # Déterminer la porte d'entrée (opposée au mouvement)
        directions_opposees = {'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left'}
        porte_entree_nom = directions_opposees[direction_mouvement]

        # Créer les portes de la nouvelle pièce
        for direction, existe in piece.portes.items():
            if existe:
                if direction == porte_entree_nom:
                    porte = Porte(niveau=0, ouverte=True)
                else:
                    niveau = Porte.generer_niveau_verrouillage(ligne, self.lignes)
                    porte = Porte(niveau=niveau, ouverte=False)
                piece.portes_objets[direction] = porte

        # Synchroniser la porte de la pièce précédente
        piece_precedente = self.get_piece_at(ligne_entree, col_entree)
        if piece_precedente:
            if direction_mouvement in piece_precedente.portes_objets:
                piece_precedente.portes_objets[direction_mouvement].ouverte = True
            # S'assurer que la porte d'entrée de la nouvelle pièce est bien ouverte
            if porte_entree_nom in piece.portes_objets:
                piece.portes_objets[porte_entree_nom].ouverte = True

    def tirer_trois_pieces(self, ligne_actuelle: int, col_actuelle: int, ligne_nouvelle: int, col_nouvelle: int, direction_mouvement: str) -> list[Piece]:
        """
        Tire 3 pièces candidates pour le nouvel emplacement, en respectant la rareté,
        la règle de la pièce gratuite et la continuité des portes.
        """
        directions_opposees = {'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left'}        
        porte_requise = directions_opposees[direction_mouvement]

        # Filtrer pioche pour ne garder que pièces avec la porte d'entrée
        pioche_filtree = [
            p for p in self.pioche 
            if p.portes.get(porte_requise, False)
        ]
        if not pioche_filtree:
            return []

        # Séparer gratuites et payantes
        pieces_gratuites = [p for p in pioche_filtree if p.cout_gemmes == 0]
        pieces_payantes = [p for p in pioche_filtree if p.cout_gemmes > 0]
        
        candidates = []

        # Fonction pour calculer le poids selon la rareté
        def get_poids(piece):
            return 1 / (3 ** max(piece.rarete, 0))

        # Choisir au moins une pièce gratuite
        if pieces_gratuites:
            poids_gratuites = [get_poids(p) for p in pieces_gratuites]
            choix_gratuit = random.choices(pieces_gratuites, weights=poids_gratuites, k=1)[0]
            candidates.append(choix_gratuit)

        # Compléter jusqu'à 3 pièces
        pioche_restante = [p for p in pioche_filtree if p not in candidates]
        while len(candidates) < 3 and pioche_restante:
            poids_restants = [get_poids(p) for p in pioche_restante]
            choix = random.choices(pioche_restante, weights=poids_restants, k=1)[0]
            candidates.append(choix)
            pioche_restante.remove(choix)

        # S'assurer que chaque candidate a au moins une autre porte ouverte que l'entrée
        for p in candidates:
            for dir, exists in p.portes.items():
                if exists and dir != porte_requise and dir not in p.portes_objets:
                    p.portes_objets[dir] = Porte(
                        niveau=Porte.generer_niveau_verrouillage(ligne_nouvelle, self.lignes),
                        ouverte=False
                    )

        random.shuffle(candidates)
        return candidates
