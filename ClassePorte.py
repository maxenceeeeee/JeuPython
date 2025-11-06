import random
# from joueur import * # from inventaire import *


class Porte:
    """ 
    Représente une porte entre deux pièces du manoir.
    
    Une porte peut être :
        - déverrouillée (niveau 0)
        - verrouillée (niveau 1)
        - verrouillée à double tour (niveau 2)
    
    Chaque porte peut être ouverte ou fermée, et son ouverture dépend
    des ressources du joueur.
    """

    def __init__(self, niveau=0, ouverte=False):
        self.niveau = niveau  # 0 = déverrouillée, 1 = verrouillée, 2 = verrouillée à double tour
        self.ouverte = ouverte

    def peut_ouvrir(self, joueur) -> bool:
        """Vérifie si le joueur a les ressources pour ouvrir la porte."""
        if self.niveau == 0:
            return True

        if self.niveau == 1:
            # Kit de crochetage ou clé
            return joueur.inventaire.a_objet_permanent("Kit de Crochetage") or joueur.inventaire.cles > 0

        if self.niveau == 2:
            # Clé uniquement
            return joueur.inventaire.cles > 0

        return False

    def ouvrir(self, joueur) -> bool:
        """
        [MODIFIÉ] Tente d'ouvrir la porte. Retourne True si déjà ouverte ou si Niv 0.
        Si la porte est verrouillée (Niv 1 ou 2), retourne True si peut_ouvrir est True.
        """
        # Si la porte est déjà ouverte, rien à faire
        if self.ouverte:
            return True

        # Niveau 0 : ouverture immédiate
        if self.niveau == 0:
            self.ouverte = True
            return True

        # Niveaux 1 et 2 : on ne dépense rien, on vérifie si le joueur est *prêt* à payer
        if self.niveau > 0:
            return self.peut_ouvrir(joueur)
            
        return False  # Ne devrait jamais arriver

    @staticmethod
    def generer_niveau_verrouillage(ligne: int, hauteur_grille: int) -> int:
        """
        Génère aléatoirement le niveau de verrouillage d'une porte en fonction
        de la progression du joueur dans le manoir.

        Args:
            ligne (int): Numéro de la ligne actuelle (0 = plus loin, hauteur-1 = entrée).
            hauteur_grille (int): Nombre total de lignes dans la grille du manoir.

        Returns:
            int: Niveau de verrouillage généré (0, 1 ou 2).
        """
        if ligne == hauteur_grille - 1:
            return 0
        if ligne == 0:
            return 2

        # Progression (entre 0 et 1) : plus on monte, plus les portes sont verrouillées
        progression = (hauteur_grille - 1 - ligne) / (hauteur_grille - 2.0)
        proba = random.random()

        # Ajustement de la probabilité selon la progression
        # ANCIENNES PROBABILITÉS: 0.4 pour Niv 2, 0.8 pour Niv 1 (si progression = 1)
        # NOUVELLES PROBABILITÉS (Plus agressives):
        
        if proba < (progression * 0.5):  # Augmenté de 0.4 -> 0.5 (Plus de Niv 2)
            return 2
        elif proba < (progression * 0.85):  # Augmenté de 0.8 -> 0.85 (Plus de Niv 1, moins de Niv 0)
            return 1
        else:
            return 0
