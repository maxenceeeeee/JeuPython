## Classe porte (verrouillage, ouverture, génération)
import random
# On a besoin de la classe Joueur pour le type hint, mais cela crée une dépendance circulaire
# On va utiliser un 'forward reference' (string) ou l'enlever.
from joueur import Joueur 
from inventaire import *

class Porte:
    """ Une porte entre deux pièces du manoir."""
    def __init__(self, niveau=0, ouverte=False):
        self.niveau = niveau  # 0 = dévérouillée, 1 = vérouillée, ou 2
        self.ouverte = ouverte

    def peut_ouvrir(self, joueur) -> bool: # 'joueur' doit avoir inventaire.cles et inventaire.a_objet_permanent
        """Vérifie si le joueur a les ressources pour ouvrir."""
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
        if self.ouverte == True:
            return True
        if not self.peut_ouvrir(joueur):
            return False
        
        if self.niveau == 2:
            if not joueur.inventaire.depenser_cles(1):
                return False
        if self.niveau == 1:
            if not joueur.inventaire.a_objet_permanent("Kit de Crochetage"):
                if not joueur.inventaire.depenser_cles(1):
                    return False    
        self.ouverte = True
        return True

    @staticmethod
    def generer_niveau_verrouillage(ligne: int, hauteur_grille: int) -> int:
        if ligne == hauteur_grille - 1:
            return 0    
        if ligne == 0:
            return 2
        
        progression = (hauteur_grille - 1 - ligne) / (hauteur_grille - 2.0) 
        
        proba = random.random()
        
        if proba < (progression * 0.3): 
            return 2
        elif proba < (progression * 0.7):
            return 1
        else:
            return 0