# joueur.py
# (cela nécessite que la classe Inventaire soit importée ou définie par nous déja)

from inventaire import Inventaire
from typing import Tuple

"""
Le responsabilité principale de la classe Joueur est de mémoriser la position du joueur sur la grille (position_ligne, position_colonne).
Sa seconde responsabilité est de posséder une instance de la classe Inventaire.
"""

class Joueur:
    """
    Représente le personnage joueur. Gère sa position et délègue la gestion des 
    ressources à l'objet Inventaire.
    
    Attributes:
        inventaire (Inventaire): Inventaire du joueur contenant les objets, clés et ressources.
        position_ligne (int): Ligne actuelle du joueur sur la grille du manoir.
        position_colonne (int): Colonne actuelle du joueur sur la grille du manoir.
    """
    def __init__(self):
        """
        Initialise un joueur avec un inventaire vide et une position de départ 
        au centre de la rangée inférieure du manoir.
        """
        self.inventaire = Inventaire() 
        # Le manoir est une grille de 5x9. On commence à l'entrée (ligne 8, colonne 2).
        # (Si la grille fait 5 lignes, les indices vont de 0 à 4. Si elle fait 9 lignes, de 0 à 8)
        # Supposons 9 lignes (y) et 5 colonnes (x) comme dans le schéma 5x9 du sujet.
        self.position_ligne = 8  # Rangée du bas (0 est le haut, 8 est le bas)
        self.position_colonne = 2 # Colonne centrale
        
        # Tous les attributs de ressources (pas, cles, pelle, etc.) ont été déplacés 
        # vers l'objet self.inventaire.
        
 #### MÉTHODES DE DÉPLACEMENT ET POSITION
    
    def calcul_coordonnees_casead(self, choix: str) -> Tuple[int, int]:
        """
        Calcule les coordonnées de la case adjacente en fonction du choix ('up', 'down', etc.).
        Args:
            choix (str): Direction du déplacement ('up', 'down', 'left', 'right')
        Returns:
            Tuple[int, int]: Les coordonnées (ligne, colonne) de la case adjacente.
        """
        case_ligne, case_colonne = 0, 0
        if choix == 'up':
            case_ligne, case_colonne = -1, 0
        elif choix == 'down': 
            case_ligne, case_colonne = 1, 0
        elif choix == 'left': 
            case_ligne, case_colonne = 0, -1
        elif choix == 'right': 
            case_ligne, case_colonne = 0, 1
        
        # Les coordonnées renvoyées sont les coordonnées absolues de la nouvelle case
        return self.position_ligne + case_ligne, self.position_colonne + case_colonne
    
    def deplacer_vers(self, nouvelle_ligne: int, nouvelle_colonne: int) -> bool:
        """
        Déplace le joueur vers une nouvelle position possible et décrémente les pas.
        
        Args:
            nouvelle_ligne (int): Ligne cible du déplacement.
            nouvelle_colonne (int): Colonne cible du déplacement.

        Returns:
            bool: True si le déplacement a eu lieu avec succès (le joueur avait des pas disponibles),
            False sinon (pas de pas restants).
            
        Note:
            La gestion des pas est délégué à l'inventaire.
        """
        # Vérifie si le joueur a des pas avant de se déplacer
        if self.inventaire.pas <= 0:
            return False
        
        # Décrémente les pas directement sur l'inventaire
        self.inventaire.pas -= 1 # 1 pas perdu à chaque déplacement 
        # Met à jour la position
        self.position_ligne = nouvelle_ligne
        self.position_colonne = nouvelle_colonne
        return True
        
 #### INTERACTION AVEC L'INVENTAIRE
    
    def ouverture_porte(self, niveau: int) -> bool: 
        """
        Vérifie si le joueur peut ouvrir la porte en fonction du niveau de verrouillage.
        
        Args:
            niveau (int): Niveau de verrouillage de la porte.
                - 0 : Porte ouverte.
                - 1 : Peut être ouverte avec un Kit de Crochetage ou une Clé.
                - 2 : Nécessite une Clé uniquement.

        Returns:
            bool: True si le joueur peut ouvrir la porte, False sinon.
            
        Note:
            La vérification utilise l'inventaire pour clés et Kit de Crochetage.
        """
        if niveau == 0:
            return True # Porte déverrouillée
        
        elif niveau == 1: 
            # Niveau 1: Utilisation du Kit de crochetage (Permanent) ou d'une clé (Consommable) 
            if self.inventaire.a_objet_permanent("Kit de Crochetage"):
                return True # Ouverture sans clé grâce au Kit 
            # On vérifie si on a une clé. La dépense sera gérée dans Jeu.deplacement si True.
            elif self.inventaire.cles > 0:
                return True # Ouverture en dépensant une clé
            else:
                return False
        
        elif niveau == 2:
            # Niveau 2: Coûte une clé, le Kit de crochetage ne fonctionne pas
            # On vérifie si on a une clé. La dépense sera gérée dans Jeu.deplacement si True.
            if self.inventaire.cles > 0:
                return True # Ouverture en dépensant une clé 
            else:
                return False
        
        return False # Échec de l'ouverture
    
    def verifie_ouverture_coffre(self) -> bool:
        """
        Vérifie si le joueur peut ouvrir un coffre (Marteau ou Clé).
        
        Returns:
            bool: True si le joueur possède un objet permettant d’ouvrir le coffre, False sinon.
        
        Note:
            La vérification est déléguée à l'inventaire pour les objets permanents et les clefs.
        """
        # Peut être ouvert avec le marteau (Permanent) 
        if self.inventaire.a_objet_permanent("Marteau"):
            return True
        # Peut être ouvert avec une clé (Consommable)
        if self.inventaire.cles > 0: 
            # On ne la dépense pas ici, juste on vérifie la possession, la dépense aura lieu si le joueur confirme l'action
            return True
        return False

    def verifie_pelle(self) -> bool:
        """
        Vérifie si le joueur possède la pelle pour creuser.
        
        Returns:
            bool: True si le joueur possède la Pelle, False sinon.
            
        Note:
            La vérification est déléguée à l'inventaire pour l'objet permanent 'Pelle'
        """
        return self.inventaire.a_objet_permanent("Pelle")