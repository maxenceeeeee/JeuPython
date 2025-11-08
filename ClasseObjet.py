import random

## CLASSE DE BASE : OBJET
# on définit les propriétés communes à tous les objets du jeu.

class Objet:
    """
    Classe de base pour tous les objets du jeu (consommables ou permanents).
    
    Attributes:
        nom (str): Nom de l'objet affiché à l'écran.
        description (str): texte décrivant l'effet de l'objet
        type_objet (str) : type de l'objet (consommable ou permanent)
        rarete (int) : indique la rareté de l'objet de 0 (très commun) à 3 (épique/légendaire) 
    """
    def __init__(self, nom: str, description: str, type_objet: str, rarete: int):
        self.nom = nom
        self.description = description
        self.type_objet = type_objet 
        self.rarete = rarete         

    def __str__(self):
        """Retourne une réprésentation lisible de l'objet """
        return f"{self.nom} ({self.type_objet}, Rareté: {self.rarete})"

    def utiliser(self, joueur):
        """
        Méthode à implémenter dans les sous-classes. 
        Applique l'effet de l'objet sur le joueur (ou le manoir).
        
        Args:
            joueur: Instance du joueur sur laquelle appliquer l'effet
        
        Returns:
            bool: True si l'objet est consommé après usage, False sinon.
        """
        raise NotImplementedError("La méthode 'utiliser' doit être implémentée par les sous-classes.")


class ObjetConsommable(Objet):
    """
    Classe de base pour tous les objets qui sont retirés de l'inventaire 
    après utilisation (nourriture, ressources, potions, etc.).
    """
    def __init__(self, nom: str, description: str, rarete: int):
        super().__init__(nom, description, "Consommable", rarete)

    # La méthode utiliser doit être définie dans les sous-classes et on doit retourner True pour indiquer que lobjet est consommé


class Nourriture(ObjetConsommable): 
    """
    Classe de base pour tous les objets redonnant des pas dans le manoir.
    
    Attributes:
        pas_rendus (int): Nombre de pas restitués au joueur lors de la consommation.
    
    """
    def __init__(self, nom: str, pas_rendus: int, rarete: int):
        description = f"Redonne {pas_rendus} pas."
        super().__init__(nom, description, rarete) # On appelle le constructeur de ObjetConsommable
        self.pas_rendus = pas_rendus

    def utiliser(self, joueur):
        """ Augmente les pas du joueur et consomme l'objet. """
        joueur.inventaire.pas += self.pas_rendus
        print(f"{self.nom} consommé : +{self.pas_rendus} pas.")
        return True # L'objet est consommé

class Pomme(Nourriture):
    """Objet commun redonnant 2 pas """
    def __init__(self):
        super().__init__("Pomme", 2, 0) 

class Banane(Nourriture):
    """Objet commun redonnant 3 pas """
    def __init__(self):
        super().__init__("Banane", 3, 0)  

class Gateau(Nourriture):
    """Objet peu commun redonnat 10 pas."""
    def __init__(self):
        super().__init__("Gâteau", 10, 1)  
class Sandwich(Nourriture):
    """Objet peu commmun redonnant 15 pas."""
    def __init__(self):
        super().__init__("Sandwich", 15, 1)  
class Repas(Nourriture):
    """Objet rare redonnant 25 pas. """
    def __init__(self):
        super().__init__("Repas", 25, 2)

class Ressource(ObjetConsommable):
    """ 
    Classe générique pour les ressources consommables ajoutées à l'inventaire.
    Attributes:
        quantite (int): Nombre d'unités de ressources ramassées.
    """
    def __init__(self, nom : str, rarete : int, quantite : int = 1): 
        description = f"{quantite} {nom}(s) ajouté(s) à l'inventaire."
        super().__init__(nom, description, rarete)
        self.quantite = quantite

    def utiliser(self, joueur):
        """
        Ajoute la ressource correspondante à l'inventaire du joueur.
        Args:
            joueur: le joueur qui ramasse la ressource.
        Returns:
            bool: True si la ressource est ajouté avec succès.
        """
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
    """Objet commun permettant d'ouvrir des coffres ou portes verrouillées."""
    def __init__(self):
        super().__init__("Clé", 0)

class PieceDor(Ressource):
    """Objet commun représentant la monnaie du jeu."""
    def __init__(self):
        super().__init__("Pièce d'Or", 0)
        
class Gemme(Ressource):
    """Objet peu commun utilisé comme monnaie spéciale."""
    def __init__(self, quantite : int = 1):
        super().__init__("Gemme", 1, quantite)  
        
class De(Ressource):
    """Objet peu commun permettant d'activer certains effets aléatoires."""
    def __init__(self):
        super().__init__("Dé", 1)

class ObjetPermanent(Objet):
    """Classe de base pour tous les objets permanents."""
    def __init__(self, nom: str, description: str, rarete: int):
        super().__init__(nom, description, "Permanent", rarete)

    def utiliser(self, joueur):
        """
        Active l'effet de l'objet sans le retirer de l'inventaire.
        Args:
            joueur: Le joueur qui active l'objet.
        Returns:
            bool: False car l'objet reste dans l'inventaire.
        """
        print(f"Objet permanent activé : {self.nom}. Effet actif.")
        return False

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