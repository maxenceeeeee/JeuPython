class Inventaire:
    """
    Cette classe représente le sac à dos du joueur. Son rôle est de stocker 
    et gérer toutes les ressources numériques (pas, clés, gemmes, etc.) et les objets 
    permanents du jeu, sans s'occuper de l'affichage (qui sera fait par l'interface Pygame).
    """
    def __init__(self):
        # RESSOURCES CONSOMMABLES
        self.pas = 70               
        self.pieces_or = 0          
        self.gemmes = 2             
        self.cles = 0               
        self.des = 0                

        # OBJETS PERMANENTS POSSÉDÉS
        self.objets_permanents = {
            "Pelle": False,           
            "Marteau": False,         
            "Kit de Crochetage": False, 
            "Détecteur de Métaux": False, 
            "Patte de Lapin": False,   
        }
        # BONUS PERMANENTS ACTIFS
        self.detecteur_actif = False
        self.patte_lapin_active = False
    
    # LOGIQUE DE VÉRIFICATION ET DÉPENSE
    
    def a_objet_permanent(self, nom_objet: str) -> bool:
        """
        Vérifie si le joueur possède un objet permanent avant de tenter une action
        (Ex: le jeu vérifie si 'Pelle' est True avant de proposer l'action 'Creuser').
        """
        return self.objets_permanents.get(nom_objet, False)

    def depenser_gemmes(self, cout: int) -> bool:
        if self.gemmes >= cout:
            self.gemmes -= cout
            return True
        return False

    def depenser_cles(self, cout: int = 1) -> bool:
        if self.cles >= cout:
            self.cles -= cout
            return True
        return False

    def depenser_des(self, cout: int = 1) -> bool:
        if self.des >= cout:
            self.des -= cout
            return True
        return False
        
    def depenser_pieces_or(self, cout: int = 1) -> bool:
        if self.pieces_or >= cout:
            self.pieces_or -= cout
            return True
        return False

    # LOGIQUE DE RAMASSAGE D'OBJET (Point de connexion avec les classes Objet) ---

    def ramasser_objet(self, objet_instance, joueur_instance):
        """
        La nouvelle méthode OOP. Prend une INSTANCE d'objet (ex: Cle())
        et applique son effet.
        """
        if objet_instance.type_objet == "Permanent":
            if objet_instance.nom in self.objets_permanents and not self.objets_permanents[objet_instance.nom]:
                self.objets_permanents[objet_instance.nom] = True
                # Activation de l'effet permanent (set detecteur_actif/patte_lapin_active)
                objet_instance.utiliser(joueur_instance) 
                print(f"Objet permanent obtenu et activé : {objet_instance.nom}")
            elif objet_instance.nom in self.objets_permanents and self.objets_permanents[objet_instance.nom]:
                 print(f"Objet permanent ignoré (déjà possédé) : {objet_instance.nom}")
            else:
                print(f"Avertissement : Objet permanent '{objet_instance.nom}' non prévu dans l'inventaire.")
            
        elif objet_instance.type_objet == "Consommable":
            # Si c'est un consommable, on appelle sa méthode utiliser immédiatement
            objet_instance.utiliser(joueur_instance)
            
        else:
            print(f"Erreur: Type d'objet inconnu : {objet_instance.type_objet}")