# inventaire.py

class Inventaire:
    """
    Cette classe représente le sac à dos du joueur. Son rôle est de stocker 
    et gérer toutes les ressources numériques (pas, clés, gemmes, etc.) et les objets 
    permanents du jeu, sans s'occuper de l'affichage (qui sera fait par l'interface Pygame).
    """
    def __init__(self):
        # --- 1. RESSOURCES CONSOMMABLES (Valeurs de départ du projet) ---
        # Ces valeurs sont des nombres qui diminuent ou augmentent.
        
        self.pas = 70               # La monnaie principale de la vie du joueur. Perdue à chaque déplacement.
        self.pieces_or = 0          # L'argent pour acheter des objets dans les magasins (pièces jaunes).
        self.gemmes = 2             # L'argent magique pour choisir des pièces coûteuses au tirage.
        self.cles = 0               # Pour ouvrir les portes verrouillées et les coffres.
        self.des = 0                # Permet de retenter un tirage de pièces non satisfaisant.

        # --- 2. OBJETS PERMANENTS (Capacités spéciales) ---
        # On utilise un dictionnaire pour savoir rapidement si le joueur possède une capacité.
        # Le nom de l'objet est la clé, la valeur est True/False.
        self.objets_permanents = {
            # Du sujet :
            "Pelle": False,            
            "Marteau": False,          
            "Kit de Crochetage": False, 
            "Détecteur de Métaux": False, 
            "Patte de Lapin": False,   
            "Loupe de l'Architecte": False, 
            "Pièce Faux-Fonds": False,
            "Bracelet de Résistance": False,
        }
    
    # --- 3. LOGIQUE DE VÉRIFICATION ET DÉPENSE ---
    
    def a_objet_permanent(self, nom_objet: str) -> bool:
        """
        Vérifie si le joueur possède un objet permanent avant de tenter une action
        (Ex: le jeu vérifie si 'Pelle' est True avant de proposer l'action 'Creuser').
        """
        # Le .get(nom_objet, False) permet de ne pas planter si on vérifie un objet 
        # qui n'existe pas dans le dictionnaire (il retourne False par défaut).
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
        
    # def depenser_pieces_or(self, cout: int = 1) -> bool:
    #     """
    #     Similaire aux autres, pour les achats dans les magasins (pièces jaunes).
    #     """
    #     if self.pieces_or >= cout:
    #         self.pieces_or -= cout
    #         return True
    #     return False

    # --- 4. LOGIQUE DE RAMASSAGE D'OBJET (Point de connexion avec les classes Objet) ---

    def ramasser_nom_objet(self, nom_item: str):
        if nom_item in self.objets_permanents:
            self.objets_permanents[nom_item] = True
            print(f"Objet permanent obtenu : {nom_item}")
            return True

        if nom_item == "Pas":
            self.pas += 10
        elif nom_item == "Pièces d'or":
            self.pieces_or += 1
        elif nom_item == "Gemmes":
            self.gemmes += 1
        elif nom_item == "Clés":
            self.cles += 1
        elif nom_item == "Dés":
            self.des += 1
        else:
            print(f"Objet inconnu : {nom_item}")
            return False

        print(f"Objet consommable ramassé : {nom_item}")
        return True
