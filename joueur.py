# joueur.py
# (cela nécessite que la classe Inventaire soit importée ou définie par nous déja)

from inventaire import Inventaire

class Joueur:
    """
    Représente le personnage joueur. Gère sa position et délègue la gestion des 
    ressources à l'objet Inventaire.
    """
    def __init__(self):
       # Le joueur possède son inventaire
        self.inventaire = Inventaire() 
        # Le manoir est une grille de 5x9. On commence à l'entrée (ligne 8, colonne 2).
        # (Si la grille fait 5 lignes, les indices vont de 0 à 4. Si elle fait 9 lignes, de 0 à 8)
        # Supposons 9 lignes (y) et 5 colonnes (x) comme dans le schéma 5x9 du sujet.
        self.position_ligne = 8  # Rangée du bas (0 est le haut, 8 est le bas)
        self.position_colonne = 2 # Colonne centrale
        
        # Tous les attributs de ressources (pas, cles, pelle, etc.) ont été déplacés 
        # vers l'objet self.inventaire.
        
    # MÉTHODES DE DÉPLACEMENT ET POSITION
    
    def calcul_coordonnees_casead(self, choix: str) -> tuple[int, int]:
        """Calcule les coordonnées de la case adjacente en fonction du choix ('up', 'down', etc.)."""
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
        Déplace le joueur et décrémente les pas.
        DÉLÉGATION: Utilise les pas stockés dans l'inventaire.
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
        
    # INTERACTION AVEC L'INVENTAIRE
    
    def ouverture_porte(self, niveau: int) -> bool: 
        """
        Vérifie si le joueur peut ouvrir la porte en fonction du niveau de verrouillage.
        DÉLÉGATION: Utilise les clés et le Kit de Crochetage de l'inventaire.
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
        DÉLÉGATION: Vérifie les objets permanents et les clés dans l'inventaire.
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
        DÉLÉGATION: Vérifie l'objet permanent 'Pelle'.
        """
        return self.inventaire.a_objet_permanent("Pelle")