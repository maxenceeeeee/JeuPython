import random
# On a besoin de la classe Joueur pour le type hint, mais cela crée une dépendance circulaire
# On va utiliser un 'forward reference' (string) ou l'enlever.
from joueur import * 
from inventaire import *

class Porte:
    """ 
    Représente une porte entre deux pièces du manoir.
    
    Une porte peut être :
        - dévérrouillée (niveau 0)
        - verouillée (niveau 1)
        - verrouillée à double tour (niveau 2)
        
    Chaque porte peut être ouverte ou fermée, et son ouverture dépend des ressources du joueut
    """
    def __init__(self, niveau=0, ouverte=False):
        self.niveau = niveau  # 0 = dévérouillée, 1 = vérouillée, ou 2 = vérouillée à double tour
        self.ouverte = ouverte

    def peut_ouvrir(self, joueur) -> bool: # 'joueur' doit avoir inventaire.cles et inventaire.a_objet_permanent
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
        """Tente d'ouvrir la porte avec les ressources nécessaires du joueur."""
        
        #Si la porte est déjà ouvrte, rien à faire
        if self.ouverte == True:
            return True
        
        #Si le joueur ne peut pas ouvrir (manque de clés ou d'outil)
        if not self.peut_ouvrir(joueur):
            return False
        
        #Cas 1 : porte à double tour = clé obligatoire.
        if self.niveau == 2:
            if joueur.inventaire.depenser_cles(1):
                self.ouverte = True
                return True
            return False
        
        #Cas 2 : porte verrouillée (niveau 1)
        if self.niveau == 1:
            if joueur.inventaire.a_objet_permanent("Kit de Crochetage"):
                self.ouverte = True
                return True
            else:
                if joueur.inventaire.depenser_cles(1):
                    self.ouverte = True
                    return True
                return False
        
        #Cas 3 : porte déverouillée (niveau 0)
        self.ouverte = True
        return True

    @staticmethod
    def generer_niveau_verrouillage(ligne: int, hauteur_grille: int) -> int:
        """
        Génère aléatoirement le niveau de verrouillage d'une porte en fonction
        de la progression du joueur dans le manoir.

        Le manoir est organisé en lignes (rangées verticales) :
            - Les portes de la première ligne (entrée) sont toujours niveau 0.
            - Les portes de la dernière ligne (antichambre) sont toujours niveau 2.
            - Entre les deux, la probabilité de rencontrer une porte verrouillée
              augmente avec la progression dans le manoir.
              
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
        if proba < (progression * 0.3): 
            return 2
        elif proba < (progression * 0.7):
            return 1
        else:
            return 0