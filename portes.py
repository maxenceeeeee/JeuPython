
## Classe porte (verrouillage, ouverture, génération)
import random

class Porte:
    """ Une porte entre deux pièces du manoir."""
    def __init__(self, niveau=0, ouverte=False):
        self.niveau = niveau  # 0 = dévérouillée, 1 = vérouillée, ou 2
        self.ouverte = ouverte

    def peut_ouvrir(self, joueur):
        if self.niveau == 0:
            return True
        if self.niveau == 1:
            return joueur.cles > 0 or joueur.kit_crochetage
        if self.niveau == 2:
            return joueur.cles > 0
        return False

    def ouvrir(self, joueur):
        if not self.peut_ouvrir(joueur):
            return False
        if self.niveau == 1 and not joueur.kit_crochetage:
            joueur.cles -= 1
        elif self.niveau == 2:
            joueur.cles -= 1
        self.ouverte = True
        return True

    def generer_niveau_verrouillage(ligne, hauteur):
        """Renvoie un niveau (0-2) selon la profondeur dans le manoir."""
        if ligne == 0:
            return 0    #Toujours ouverte en bas
        if ligne == hauteur - 1:
            return 2
        
        #entre les deux, probabilité augmente progressivement
        proba = random.random()
        if proba < ligne / hauteur:
            return 1
        elif proba < ligne / hauteur + 0.2:
            return 2
        return 0
