import random
from ClassePiece import Piece
from ClassePorte import Porte
from Catalogue_pieces import catalogue_pieces
from typing import List


class Manoir:
    """
    Gère la grille du manoir 5x9, la pioche de pièces
    et la logique de placement des pièces dans le jeu.
    
    Attributes:
        lignes (int): Nombre de lignes de la grille.
        colonnes (int): Nombre de colonnes de la grille.
        grille (list[list[Piece|None]]): Grille 2D contenant les pièces ou None.
        pioche (list[Piece]): Liste des pièces disponibles à placer.
    """

    def __init__(self, lignes_jeu=9, colonnes_jeu=5):
        """
        Initialise le manoir avec une grille vide et la pioche de pièces.
        Place automatiquement l'Entrance Hall et l'Antechamber aux positions
        définies.

        Args:
            lignes_jeu (int): Nombre de lignes dans la grille.
            colonnes_jeu (int): Nombre de colonnes dans la grille.
        """
        self.lignes = lignes_jeu
        self.colonnes = colonnes_jeu

        # Grille 2D stockant les objets Piece (ou None si vide)
        self.grille = [[None for _ in range(self.colonnes)] for _ in range(self.lignes)]

        # Pioche de pièces (objets Piece, pas dictionnaires)
        self.pioche = self._initialiser_pioche()

        # Placer l'entrée et la pièce finale
        self._placer_piece_depart()
        self._placer_piece_finale()

    def _initialiser_pioche(self) -> List[Piece]:
        """
        Crée la pioche d'objets Piece à partir du catalogue de dictionnaires.
        L'Entrance Hall et l'Antechamber sont exclues de la pioche.
        
        Returns:
            List[Piece]: Liste des objets Piece prêts à être tirés.
        
        """
        pioche = []
        for data_piece in catalogue_pieces:
            if data_piece["nom"] not in ["Entrance Hall", "Antechamber"]:
                # Convertit le dictionnaire en objet Piece
                piece = Piece(**data_piece)
                piece.charger_image("Images.zip")
                pioche.append(piece)
        return pioche

    def _placer_piece_depart(self):
        """
        Trouve l'Entrance Hall, la crée et la place sur la grille à la position (8,2).
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
        Place l'Antechamber à la position (0,2) sur la grille.
        Initialise les portes comme fermées, avec un niveau de verrouillage
        dépendant de la position.        
        """
        pos_ligne, pos_col = 0, 2
        data_finale = next((p for p in catalogue_pieces if p["nom"] == "Antechamber"), None)
        piece_finale = Piece(**data_finale)
        piece_finale.charger_image("Images.zip")
        self.grille[pos_ligne][pos_col] = piece_finale

        for direction, existe in piece_finale.portes.items():
            if existe:
                niveau = Porte.generer_niveau_verrouillage(pos_ligne, self.lignes)
                if pos_ligne == 0:
                    niveau = 2  # Double verrouillage pour la pièce finale
                # Porte FERMÉE par défaut, quelle que soit son niveau
                piece_finale.portes_objets[direction] = Porte(niveau=niveau, ouverte=False)

    def get_piece_at(self, ligne: int, colonne: int) -> Piece | None:
        """
        Récupère la pièce à la position donnée dans la grille.

        Args:
            ligne (int): Numéro de ligne.
            colonne (int): Numéro de colonne.

        Returns:
            Piece | None: L'objet Piece à la position ou None si vide ou hors limites.
        """
        if 0 <= ligne < self.lignes and 0 <= colonne < self.colonnes:
            return self.grille[ligne][colonne]
        return None

    def placer_piece(self, piece: Piece, ligne: int, colonne: int,
                    ligne_entree: int, col_entree: int, direction_mouvement: str):
        """
        Place une pièce sur la grille aux coordonnées données et crée ses portes.

        Args:
            piece (Piece): La pièce à placer.
            ligne (int): Ligne où placer la pièce.
            colonne (int): Colonne où placer la pièce.
            ligne_entree (int): Ligne de la pièce depuis laquelle on arrive.
            col_entree (int): Colonne de la pièce depuis laquelle on arrive.
            direction_mouvement (str): Direction du mouvement ('up', 'down', 'left', 'right').

        Notes:
            - La porte correspondant à l'entrée est ouverte et déverrouillée.
            - Les autres portes sont générées avec un niveau de verrouillage mais fermées par défaut.
        """
        if not (0 <= ligne < self.lignes and 0 <= colonne < self.colonnes):
            return

        self.grille[ligne][colonne] = piece
        if piece in self.pioche:
            self.pioche.remove(piece)

        directions_opposees = {'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left'}
        porte_entree_nom = directions_opposees[direction_mouvement]

        # Créer les portes de la nouvelle pièce
        for direction, existe in piece.portes.items():
            if existe:
                if direction == porte_entree_nom:
                    # Porte d'entrée : OUVERTE et déverrouillée
                    porte = Porte(niveau=0, ouverte=True)
                else:
                    # CORRECTION : Autres portes - générer niveau mais TOUJOURS FERMÉES au départ
                    niveau = Porte.generer_niveau_verrouillage(ligne, self.lignes)
                    porte = Porte(niveau=niveau, ouverte=False)  # ← IMPORTANT : ouverte=False
                piece.portes_objets[direction] = porte

        # Synchroniser la porte de la pièce précédente
        piece_precedente = self.get_piece_at(ligne_entree, col_entree)
        if piece_precedente:
            if direction_mouvement in piece_precedente.portes_objets:
                piece_precedente.portes_objets[direction_mouvement].ouverte = True
            if porte_entree_nom in piece.portes_objets:
                piece.portes_objets[porte_entree_nom].ouverte = True

    def tirer_trois_pieces(self, ligne_actuelle: int, col_actuelle: int,
                           ligne_nouvelle: int, col_nouvelle: int,
                           direction_mouvement: str) -> list[Piece]:
        """
        Tire 3 pièces candidates pour le nouvel emplacement, en respectant la rareté,
        la règle de la pièce gratuite et la continuité des portes.
        
        Args:
            ligne_actuelle (int): Ligne de la pièce actuelle.
            col_actuelle (int): Colonne de la pièce actuelle.
            ligne_nouvelle (int): Ligne de la nouvelle pièce à placer.
            col_nouvelle (int): Colonne de la nouvelle pièce à placer.
            direction_mouvement (str): Direction depuis laquelle on entre dans la nouvelle pièce.

        Returns:
            list[Piece]: Liste de 3 pièces candidates pour le joueur (peut être < 3 si pas assez de pièces compatibles).
        
        """
        directions_opposees = {'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left'}
        porte_requise = directions_opposees[direction_mouvement]

        candidates = []

        # Fonction pour calculer le poids selon la rareté
        def poids_rarete(piece):
            return 1 / (3 ** max(piece.rarete, 0))

        # Filtrer la pioche pour ne garder que les pièces avec la porte requise
        pioche_compatible = [p for p in self.pioche if p.portes.get(porte_requise, False)]

        if not pioche_compatible:
            return []  # Aucune pièce compatible

        # Séparer gratuites et payantes
        pieces_gratuites = [p for p in pioche_compatible if p.cout_gemmes == 0]

        # Choisir au moins une pièce gratuite compatible (si disponible)
        if pieces_gratuites:
            poids_gratuites = [poids_rarete(p) for p in pieces_gratuites]
            choix_gratuit = random.choices(pieces_gratuites, weights=poids_gratuites, k=1)[0]
            candidates.append(choix_gratuit)

        # Remplir avec les autres pièces compatibles jusqu'à 3
        pioche_restante_compatible = [p for p in pioche_compatible if p not in candidates]

        while len(candidates) < 3 and pioche_restante_compatible:
            poids_restants = [poids_rarete(p) for p in pioche_restante_compatible]
            choix = random.choices(pioche_restante_compatible, weights=poids_restants, k=1)[0]
            candidates.append(choix)
            pioche_restante_compatible.remove(choix)

        # Configuration des portes pour chaque candidate
        for p in candidates:
            p.portes_objets[porte_requise] = Porte(niveau=0, ouverte=True)
            for dir, exists in p.portes.items():
                if exists and dir != porte_requise and dir not in p.portes_objets:
                    niveau = Porte.generer_niveau_verrouillage(ligne_nouvelle, self.lignes)
                    p.portes_objets[dir] = Porte(niveau=niveau, ouverte=(niveau == 0))

        random.shuffle(candidates)
        return candidates
