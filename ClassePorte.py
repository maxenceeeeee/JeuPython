## Classe porte (verrouillage, ouverture, génération)
import random
# On a besoin de la classe Joueur pour le type hint, mais cela crée une dépendance circulaire
# On va utiliser un 'forward reference' (string) ou l'enlever.
from joueur import Joueur 

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
        """
        Tente d'ouvrir la porte. 
        Retourne True si l'ouverture réussit (et dépense les clés si nécessaire).
        Retourne False si l'ouverture échoue.
        """
        if self.ouverte:
            return True # Déjà ouverte
            
        if not self.peut_ouvrir(joueur):
            return False # Ne peut pas ouvrir

        # Si on peut ouvrir, on gère la dépense de clé
        if self.niveau == 1 and not joueur.inventaire.a_objet_permanent("Kit de Crochetage"):
            joueur.inventaire.depenser_cles(1) 
        elif self.niveau == 2:
            joueur.inventaire.depenser_cles(1) 
        
        self.ouverte = True
        return True

    @staticmethod
    def generer_niveau_verrouillage(ligne: int, hauteur_grille: int) -> int:
        """
        Renvoie un niveau (0-2) selon la profondeur dans le manoir.
        La ligne 0 est le haut (Antichambre), la ligne 8 (hauteur_grille - 1) est le bas (Entrée).
        """
        # Ligne de départ (en bas) : toujours niveau 0
        # Note : ligne == 8 (si hauteur == 9)
        if ligne == hauteur_grille - 1:
            return 0    
        
        # Ligne d'arrivée (en haut) : toujours niveau 2
        # Note : ligne == 0
        if ligne == 0:
            return 2
        
        # Entre les deux, la probabilité augmente en montant.
        # Plus 'ligne' est petit (proche de 0), plus c'est difficile.
        
        progression = (hauteur_grille - 1 - ligne) / (hauteur_grille - 2.0) # Va de ~0.14 à 1.0
        
        proba = random.random() # 0.0 à 1.0
        
        if proba < (progression * 0.3): # Probabilité de Niv 2 (augmente vite)
            return 2
        elif proba < (progression * 0.7): # Probabilité de Niv 1
            return 1
        else:
            return 0 # Reste (Niv 0)
