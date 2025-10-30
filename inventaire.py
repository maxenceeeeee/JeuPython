# inventaire.py

class Inventaire:
    """
    Cette classe représente le sac à dos du joueur. Son rôle est de stocker 
    et gérer toutes les ressources numériques (pas, clés, gemmes, etc.) et les objets 
    permanents du jeu, sans s'occuper de l'affichage (qui sera fait par l'interface Pygame).
    """
    def __init__(self):
        #RESSOURCES CONSOMMABLES (Valeurs de départ du projet modifiables)
        # Ces valeurs sont des nombres qui diminuent ou augmentent.
        
        self.pas = 70               # La monnaie principale de la vie du joueur. Perdue à chaque déplacement.
        self.pieces_or = 0          # L'argent pour acheter des objets dans les magasins (pièces jaunes).
        self.gemmes = 2             # L'argent magique pour choisir des pièces coûteuses au tirage.
        self.cles = 0               # Pour ouvrir les portes verrouillées et les coffres.
        self.des = 0                # Permet de retenter un tirage de pièces non satisfaisant.

        #OBJETS PERMANENTS (Capacités spéciales)
        # On utilise un dictionnaire pour savoir rapidement si le joueur possède une capacité.
        # Le nom de l'objet est la clé, la valeur est True/False.
        self.objets_permanents = {
            
            "Pelle": False,            
            "Marteau": False,          
            "Kit de Crochetage": False, 
            "Détecteur de Métaux": False, 
            "Patte de Lapin": False,   
            "Loupe de l'Architecte": False,
            "Pièce Faux-Fonds": False, 
            "Bracelet de Résistance": False,
        }
    
    # LOGIQUE DE VÉRIFICATION ET DÉPENSE
    
    def a_objet_permanent(self, nom_objet: str) -> bool:
        """
        Vérifie si le joueur possède un objet permanent avant de tenter une action
        (Ex: le jeu vérifie si 'Pelle' est True avant de proposer l'action 'Creuser').
        """
        # Le .get(nom_objet, False) permet de ne pas planter si on vérifie un objet qui n'existe pas dans le dictionnaire (il retourne False par défaut ?).
        return self.objets_permanents.get(nom_objet, False)

    def depenser_gemmes(self, cout: int) -> bool:
        """
        Essaie de payer un coût en gemmes. Utilisé pour choisir une pièce.
        S'il peut payer, il soustrait et retourne True. Sinon, il ne change rien et retourne False.
        """
        if self.gemmes >= cout:
            self.gemmes -= cout
            return True
        return False

    def depenser_cles(self, cout: int = 1) -> bool:
        """
        Essaie de dépenser une clé. Utilisé pour les portes et les coffres.
        Idem : vérification avant la soustraction.
        """
        if self.cles >= cout:
            self.cles -= cout
            return True
        return False

    def depenser_des(self, cout: int = 1) -> bool:
        """
        Essaie de dépenser un dé. Utilisé pour relancer le tirage de pièces.
        """
        if self.des >= cout:
            self.des -= cout
            return True
        return False
        
    def depenser_pieces_or(self, cout: int = 1) -> bool:
        """
        Similaire aux autres, pour les achats dans les magasins (pièces jaunes).
        """
        if self.pieces_or >= cout:
            self.pieces_or -= cout
            return True
        return False

    #LOGIQUE DE RAMASSAGE D'OBJET (Point de connexion avec les classes Objet) ---

    def ramasser_objet(self, objet_instance, joueur_instance):
        """
        La nouvelle méthode OOP. Prend une INSTANCE d'objet (ex: Cle())
        et applique son effet.
        """
        if objet_instance.type_objet == "Permanent":
            # Si c'est un objet permanent, on le "coche" dans le dictionnaire
            if objet_instance.nom in self.objets_permanents:
                self.objets_permanents[objet_instance.nom] = True
                print(f"Objet permanent obtenu : {objet_instance.nom}")
            else:
                print(f"Avertissement : Objet permanent '{objet_instance.nom}' non prévu dans l'inventaire.")
            # L'objet appelle sa propre méthode 'utiliser' (qui ne fait rien et retourne False)
            objet_instance.utiliser(joueur_instance)
            
        elif objet_instance.type_objet == "Consommable":
            # Si c'est un consommable, on appelle sa méthode utiliser.
            # La méthode (ex: Cle.utiliser) s'occupe elle-même d'incrémenter les clés, pas, etc., du joueur.
            objet_instance.utiliser(joueur_instance)
            
        else:
            print(f"Erreur: Type d'objet inconnu : {objet_instance.type_objet}")