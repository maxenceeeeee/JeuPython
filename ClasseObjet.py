import random

## CLASSE DE BASE : OBJET
# on définit les propriétés communes à tous les objets du jeu.

class Objet:
    """
    Classe de base pour tous les objets du jeu (consommables ou permanents).
    """
    def __init__(self, nom: str, description: str, type_objet: str, rarete: int):
        # nom de l'objet qu'on va afficher à l'écran
        self.nom = nom
        # décrit l'effet de l'objet
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
        Applique l'effet de l'objet sur le joueur (ou le manoir).
        Retourne True si l'objet est consommé, False sinon.
        """
        raise NotImplementedError("La méthode 'utiliser' doit être implémentée par les sous-classes.")


class ObjetConsommable(Objet):
    """
    Classe de base pour tous les objets qui sont retirés de l'inventaire 
    après utilisation (nourriture, ressources, potions, etc.).
    """
    def __init__(self, nom: str, description: str, rarete: int):
        super().__init__(nom, description, "Consommable", rarete)

    # La méthode utiliser doit être définie dans les sous-classes et on doit retourner True pour indiquer que l'objet est consommé


class Nourriture(ObjetConsommable): 
    """Classe de base pour tous les objets redonnant des pas dans le manoir."""
    def __init__(self, nom: str, pas_rendus: int, rarete: int):
        description = f"Redonne {pas_rendus} pas."
        super().__init__(nom, description, rarete) # On appelle le constructeur de ObjetConsommable
        self.pas_rendus = pas_rendus

    def utiliser(self, joueur):
        """Augmente les pas du joueur et consomme l'objet."""
        joueur.inventaire.pas += self.pas_rendus
        print(f"{self.nom} consommé : +{self.pas_rendus} pas.")
        return True 

class Pomme(Nourriture):
    def __init__(self):
        super().__init__("Pomme", 2, 0) 

class Banane(Nourriture):
    def __init__(self):
        super().__init__("Banane", 5, 1)

class Gateau(Nourriture):
    def __init__(self):
        super().__init__("Gâteau", 12, 2)

class Ressource(ObjetConsommable):
    """Classe de base pour les ressources (Clé, Gemme, Pièce d'Or, Dé)."""
    def __init__(self, nom: str, rarete: int):
        description = f"Ajoute 1 {nom} à l'inventaire."
        super().__init__(nom, description, rarete)

    def utiliser(self, joueur):
        """Ajoute la ressource correspondante à l'inventaire et consomme l'objet."""
        attribut_inventaire = self.nom.lower().replace(' ', '_').replace('é', 'e') + 's' 
        
        if hasattr(joueur.inventaire, attribut_inventaire):
            setattr(joueur.inventaire, attribut_inventaire, getattr(joueur.inventaire, attribut_inventaire) + 1)
            print(f"Ramassé : +1 {self.nom}.")
            return True
        else:
            print(f"Erreur: L'inventaire ne supporte pas la ressource {self.nom}.")
            return False

class Cle(Ressource):
    def __init__(self):
        super().__init__("Clé", 1)

class PieceDor(Ressource):
    def __init__(self):
        super().__init__("Pièce d'Or", 0)
        
class Gemme(Ressource):
    def __init__(self):
        super().__init__("Gemme", 2)
        
class De(Ressource):
    def __init__(self):
        super().__init__("Dé", 1)


class SceauSecurite(ObjetConsommable):
    def __init__(self):
        description = "Permet de 'figer' une des trois pièces tirées au sort, même si un Dé est ensuite utilisé."
        super().__init__("Sceau de Sécurité", description, 2)

    def utiliser(self, joueur):
        """Déclenche la logique de 'figer' une pièce pendant le tirage."""
        # La logique réelle d'application se fera dans la classe Jeu
        print(f"Utilisation du {self.nom}. Le prochain tirage de pièces sera 'scellé' après le premier choix.")
        return True # L'objet est consommé

class PotionTeleportation(ObjetConsommable):
    def __init__(self):
        description = "Permet de se déplacer immédiatement vers n'importe quelle pièce déjà découverte sans dépenser de pas."
        super().__init__("Potion de Téléportation", description, 3)

    def utiliser(self, joueur):
        """Déclenche la logique de sélection de pièce sur la grille."""
        # La logique de sélection de la destination doit être gérée par la classe "Jeu"
        print(f"Utilisation de la {self.nom}. Veuillez choisir une pièce de destination sur la grille.")
        return True # L'objet est consommé


class ObjetPermanent(Objet):
    """Classe de base pour tous les objets permanents."""
    def __init__(self, nom: str, description: str, rarete: int):
        # type_objet est ici "permanent"
        super().__init__(nom, description, "Permanent", rarete)

    def utiliser(self, joueur):
        """Les objets permanents ne sont pas 'consommés' après avoir été ramassés."""
        print(f"Objet permanent ramassé : {self.nom}. Son effet est actif.")
        return False # L'objet n'est PAS consommé/retiré de l'inventaire après usage

class Pelle(ObjetPermanent):
    def __init__(self):
        super().__init__("Pelle", "Permet de creuser dans des endroits spécifiques.", 2)

class KitDeCrochetage(ObjetPermanent):
    def __init__(self):
        super().__init__("Kit de Crochetage", "Ouvre les portes verrouillées de niveau 1 sans dépenser de clé.", 3)
        
class PatteDeLapin(ObjetPermanent):
    def __init__(self):
        super().__init__("Patte de Lapin", "Augmente la chance de trouver des objets (y compris permanents) dans le manoir.", 3)

class LoupeArchitecte(ObjetPermanent):
    def __init__(self):
        super().__init__("Loupe de l'Architecte", "Révèle le niveau de verrouillage des portes non ouvertes adjacentes à la pièce actuelle.", 2)
        
class PieceFauxFonds(ObjetPermanent):
    def __init__(self):
        super().__init__("Pièce Faux-Fonds", "Chance (10%) de ne pas dépenser une Pièce d'Or lors de l'achat dans un magasin.", 1)