import random

## CLASSE DE BASE : OBJET
# on définit les propriétés communes à tous les objets du jeu.

class Objet:
    """
    Classe de base pour tous les objets du jeu (consommables ou permanents).
    """
    def __init__(self, nom: str, description: str, type_objet: str, rarete: int):
        # nom de l'objet quon va afficher à lécran
        self.nom = nom
        # décrit leffet de lobjet
        self.description = description
        # type : soit consommable soit permanent
        self.type_objet = type_objet 
        # rareté : 0 (Très Commun) à 3 (Épique/Légendaire)
        self.rarete = rarete         

    def __str__(self):
        return f"{self.nom} ({self.type_objet}, Rareté: {self.rarete})"

    def utiliser(self, joueur):
        """
        Méthode à implémenter dans les sous-classes. 
        Applique leffet de lobjet sur le joueur (ou le manoir).
        Retourne True si lobjet est consommé, False sinon.
        """
        raise NotImplementedError("La méthode 'utiliser' doit être implémentée par les sous-classes.")


class ObjetConsommable(Objet):
    """
    Classe de base pour tous les objets qui sont retirés de linventaire 
    après utilisation (nourriture, ressources, potions, etc.).
    """
    def __init__(self, nom: str, description: str, rarete: int):
        super().__init__(nom, description, "Consommable", rarete)

    # La méthode utiliser doit être définie dans les sous-classes et on doit retourner True pour indiquer que lobjet est consommé


class Nourriture(ObjetConsommable): 
    """Classe de base pour tous les objets redonnant des pas dans le manoir."""
    def __init__(self, nom: str, pas_rendus: int, rarete: int):
        description = f"Redonne {pas_rendus} pas."
        super().__init__(nom, description, rarete) # On appelle le constructeur de ObjetConsommable
        self.pas_rendus = pas_rendus

    def utiliser(self, joueur):
        """Augmente les pas du joueur et consomme lobjet."""
        joueur.inventaire.pas += self.pas_rendus
        print(f"{self.nom} consommé : +{self.pas_rendus} pas.")
        return True # L'objet est consommé

class Pomme(Nourriture):
    def __init__(self):
        super().__init__("Pomme", 2, 0) 

class Banane(Nourriture):
    def __init__(self):
        super().__init__("Banane", 3, 0)  # 3 pas comme dans le sujet

class Gateau(Nourriture):
    def __init__(self):
        super().__init__("Gâteau", 10, 1)  # 10 pas comme dans le sujet

class Sandwich(Nourriture):
    def __init__(self):
        super().__init__("Sandwich", 15, 1)  # 15 pas comme dans le sujet

class Repas(Nourriture):
    def __init__(self):
        super().__init__("Repas", 25, 2)  # 25 pas comme dans le sujet


class Ressource(ObjetConsommable):
    def __init__(self, nom : str, rarete : int, quantite : int = 1): 
        description = f"{quantite} {nom}(s) ajouté(s) à l'inventaire."
        super().__init__(nom, description, rarete)
        self.quantite = quantite

    def utiliser(self, joueur):
        if self.nom == "Clé":
            joueur.inventaire.cles += self.quantite
        elif self.nom == "Pièce d'Or":
            joueur.inventaire.pieces_or += self.quantite 
        elif self.nom == "Gemme":
            joueur.inventaire.gemmes += self.quantite
        elif self.nom == "Dé":
            joueur.inventaire.des += self.quantite
        else:
            return False
            
        print(f"Ramassé : +{self.quantite} {self.nom}.")
        return True

class Cle(Ressource):
    def __init__(self):
        super().__init__("Clé", 0)  # Commun

class PieceDor(Ressource):
    def __init__(self):
        super().__init__("Pièce d'Or", 0)  # Commun
        
class Gemme(Ressource):
    def __init__(self, quantite : int = 1):
        super().__init__("Gemme", 1, quantite)  # Peu commun
        
class De(Ressource):
    def __init__(self):
        super().__init__("Dé", 1)  # Peu commun

class ObjetPermanent(Objet):
    """Classe de base pour tous les objets permanents."""
    def __init__(self, nom: str, description: str, rarete: int):
        super().__init__(nom, description, "Permanent", rarete)

    def utiliser(self, joueur):
        """
        Les objets permanents NE SONT PAS consommés après utilisation.
        Retourne False pour indiquer qu'ils DOIVENT rester dans l'inventaire.
        """
        print(f"Objet permanent activé : {self.nom}. Effet actif.")
        return False  # L'objet N'EST PAS consommé/retiré de l'inventaire

class Pelle(ObjetPermanent):
    def __init__(self):
        super().__init__("Pelle", "Permet de creuser une fois dans des endroits spécifiques.", 2)

    def utiliser(self, joueur):
        """La pelle est utilisée pour creuser (l'objet reste)."""
        print("Pelle disponible pour creuser.")
        return False  # Reste dans l'inventaire

class Marteau(ObjetPermanent):
    def __init__(self):
        super().__init__("Marteau", "Permet de briser les cadenas des coffres sans dépenser de clé.", 2)

    def utiliser(self, joueur):
        """Le marteau est utilisé pour ouvrir des coffres (l'objet reste)."""
        print("Marteau disponible pour ouvrir les coffres.")
        return False  # Reste dans l'inventaire

class KitDeCrochetage(ObjetPermanent):
    def __init__(self):
        super().__init__("Kit de Crochetage", "Permet d'ouvrir une porte verrouillée de niveau 1 sans dépenser de clé.", 2)

    def utiliser(self, joueur):
        """Le kit est utilisé pour ouvrir des portes niveau 1 (l'objet reste)."""
        print("Kit de crochetage disponible pour ouvrir les portes Niv 1.")
        return False  # Reste dans l'inventaire
        
class DetecteurMetaux(ObjetPermanent):
    def __init__(self):
        super().__init__("Détecteur de Métaux", "Augmente la chance de trouver des clés et des pièces.", 2)

    def utiliser(self, joueur):
        """Active l'effet permanent (l'objet reste)."""
        joueur.inventaire.detecteur_actif = True
        print("Détecteur de métaux activé - effet permanent.")
        return False  # Reste dans l'inventaire

class PatteDeLapin(ObjetPermanent):
    def __init__(self):
        super().__init__("Patte de Lapin", "Augmente la chance de trouver des objets (y compris permanents).", 3)

    def utiliser(self, joueur):
        """Active l'effet permanent (l'objet reste)."""
        joueur.inventaire.patte_lapin_active = True
        print("Patte de lapin activée - effet permanent.")
        return False  # Reste dans l'inventaire


# ITEM FACTORY
# Dictionnaire qui mappe les noms (str) aux classes (class)
OBJET_MAP = {
    # Nourriture
    "Pomme": Pomme,
    "Banane": Banane,
    "Gâteau": Gateau,
    "Sandwich": Sandwich,
    "Repas": Repas,
    
    # Ressources
    "Clé": Cle,
    "Pièce d'Or": PieceDor,
    "Gemme": Gemme,
    "Dé": De,
    
    # Objets Permanents (maintenant à usage unique)
    "Pelle": Pelle,
    "Marteau": Marteau,
    "Kit de Crochetage": KitDeCrochetage,
    "Détecteur de Métaux": DetecteurMetaux,
    "Patte de Lapin": PatteDeLapin,
}