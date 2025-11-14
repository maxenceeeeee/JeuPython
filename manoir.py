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
                piece_template = Piece(**data_piece)
                
                # Détermine combien de copies ajouter à la pioche
                if piece_template.rarete == 0:
                    copies = 4 
                elif piece_template.rarete == 1:
                    copies = 3 
                elif piece_template.rarete == 2:
                    copies = 2
                elif piece_template.rarete == 3:
                    copies = 1
                else:
                    copies = 1
                
                for _ in range(copies):
                    # Cloner l'objet Piece pour s'assurer qu'ils sont indépendants
                    piece = Piece(**data_piece)
                    try:
                        piece.charger_image("Images.zip") 
                    except NameError:
                        pass 
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
        try:
            piece_entree.charger_image("Images.zip")
        except NameError:
            pass
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
        try:
            piece_finale.charger_image("Images.zip")
        except NameError:
            pass
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
            - La pièce n'est plus retirée de la pioche, permettant les réutilisations.
        """
        if not (0 <= ligne < self.lignes and 0 <= colonne < self.colonnes):
            return

        self.grille[ligne][colonne] = piece
        # La pièce n'est plus retirée de self.pioche, elle est seulement placée dans la grille.

        directions_opposees = {'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left'}
        porte_entree_nom = directions_opposees[direction_mouvement]

        # Créer les portes de la nouvelle pièce
        for direction, existe in piece.portes.items():
            if existe:
                if direction == porte_entree_nom:
                    # Porte d'entrée : OUVERTE et déverrouillée
                    porte = Porte(niveau=0, ouverte=True)
                else:
                    # Autres portes - générer niveau mais TOUJOURS FERMÉES au départ
                    niveau = Porte.generer_niveau_verrouillage(ligne, self.lignes)
                    porte = Porte(niveau=niveau, ouverte=False)
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
        
        Notes: Les pièces tirées sont des copies, permettant leur réutilisation dans le pool de pioche.
        
        Returns:
            list[Piece]: Liste de 3 pièces candidates pour le joueur.
        """
        directions_opposees = {'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left'}
        porte_requise = directions_opposees[direction_mouvement]

        pioche_compatible = [p for p in self.pioche if p.portes.get(porte_requise, False)]

        if not pioche_compatible:
            return []  # Aucune pièce compatible

        # Fonction pour calculer le poids selon la rareté
        def poids_rarete(piece):
            # Favorise les pièces de rareté inférieure (plus communes)
            return 1 / (0.2** max(piece.rarete, 0)) 
        
        poids = [poids_rarete(p) for p in pioche_compatible]

        # 2. Tirer 3 pièces (avec remplacement car la liste est complète et autorise les doublons)
        candidates_references = random.choices(pioche_compatible, weights=poids, k=3)
        
        # 3. Créer des COPIES INDÉPENDANTES des pièces tirées pour la sélection
        candidates = []
        for piece_ref in candidates_references:
            # Retrouver les données d'origine (nécessaire pour garantir l'indépendance totale de l'objet)
            data = next((p for p in catalogue_pieces if p["nom"] == piece_ref.nom), None)
            if data:
                new_piece = Piece(**data)
                try:
                    new_piece.charger_image("Images.zip")
                except NameError:
                    pass
                candidates.append(new_piece)
        
        if not candidates:
            # Ne devrait pas arriver si pioche_compatible n'est pas vide, mais par sécurité
            return []
        
        # 4. S'assurer qu'au moins une pièce est gratuite (règle du jeu, si possible)
        pieces_gratuites_candidates = [p for p in candidates if p.cout_gemmes == 0]
        pioche_originale_gratuites = [p for p in pioche_compatible if p.cout_gemmes == 0]
        
        if not pieces_gratuites_candidates and pioche_originale_gratuites:
            # Remplacer la pièce payante la plus chère par une gratuite
            # Tirer une nouvelle instance de pièce gratuite compatible
            piece_gratuite_data = random.choice(pioche_originale_gratuites)
            piece_remplacement = Piece(**next(p for p in catalogue_pieces if p["nom"] == piece_gratuite_data.nom))
            try:
                piece_remplacement.charger_image("Images.zip")
            except NameError:
                pass
            
            # Remplacer la pièce la plus chère
            index_remplacement = max(range(len(candidates)), key=lambda i: candidates[i].cout_gemmes)
            candidates[index_remplacement] = piece_remplacement
            
        for p in candidates:
            p.portes_objets[porte_requise] = Porte(niveau=0, ouverte=True)
            for dir, exists in p.portes.items():
                if exists and dir != porte_requise and dir not in p.portes_objets:
                    niveau = Porte.generer_niveau_verrouillage(ligne_nouvelle, self.lignes)
                    p.portes_objets[dir] = Porte(niveau=niveau, ouverte=False)

        random.shuffle(candidates)
        return candidates