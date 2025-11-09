class Inventaire:
    """
    Cette classe représente le sac à dos du joueur. Son rôle est de stocker 
    et gérer toutes les ressources numériques (pas, clés, gemmes, etc.) et les objets 
    permanents du jeu, sans s'occuper de l'affichage (qui sera fait par l'interface Pygame).
    """
    
    def __init__(self):
        """Initialise l'inventaire du joueur avec les valeurs de départ. """
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
        
        Args:
            nom_objet (str): Nom de l'objet permanent à vérifier (ex: "Pelle", "Marteau").
        Returns:
            bool: True si l'objet est possédé, False sinon.
        """
        return self.objets_permanents.get(nom_objet, False)

    def depenser_gemmes(self, cout: int) -> bool:
        """ 
        Déduit des gemmes de l'inventaire si le joueur en possède suffisamment.
        
        Args:
            cout (int): Nombre de gemmes à dépenser.
        Returns:
            bool: True si la dépense a réussi, False si le joueur n'a pas assez.
        """
        if self.gemmes >= cout:
            self.gemmes -= cout
            return True
        return False

    def depenser_cles(self, cout: int = 1) -> bool:
        """
        Déduit des clés de l'inventaire si le joueur en possède suffisamment.
        
        Args:
            cout (int, optional): Nombre de clés à dépenser. Par défaut 1.
        Returns:
            bool: True si la dépense a réussi, False sinon.
        """
        if self.cles >= cout:
            self.cles -= cout
            return True
        return False

    def depenser_des(self, cout: int = 1) -> bool:
        """ 
        Déduit des dés de l'inventaire si le joueur en possède suffisamment.
       
        Args:
            cout (int, optional): Nombre de dés à dépenser. Par défaut 1.
        Returns:
            bool: True si la dépense a réussi, False sinon.       
        """
        
        if self.des >= cout:
            self.des -= cout
            return True
        return False
        
    def depenser_pieces_or(self, cout: int = 1) -> bool:
       """ 
       Déduit des pièces d'or de l'inventaire si le joueur en possède suffisamment.
      
       Args:
           cout (int, optional): Nombre de pièces d'or à dépenser. Par défaut 1.
        Returns:
            bool: True si la dépense a réussi, False sinon.
       """
       if self.pieces_or >= cout:
           self.pieces_or -= cout
           return True
       return False

    # LOGIQUE DE RAMASSAGE D'OBJET

    def ramasser_objet(self, objet_instance, joueur_instance):
        """
        Ramasse un objet et applique son effet.
        
        Args:
            objet_instance: Instance de l'objet à ramasser (doit avoir les attributs
                            `type_objet`, `nom`, et la méthode `utiliser`).
            joueur_instance: Instance du joueur recevant l'objet.
        """
        if objet_instance.type_objet == "Permanent":
            if objet_instance.nom in self.objets_permanents and not self.objets_permanents[objet_instance.nom]:
                self.objets_permanents[objet_instance.nom] = True
                objet_instance.utiliser(joueur_instance) #Appel polymorphique
                print(f"Objet permanent obtenu et activé : {objet_instance.nom}")
            elif objet_instance.nom in self.objets_permanents and self.objets_permanents[objet_instance.nom]:
                 print(f"Objet permanent ignoré (déjà possédé) : {objet_instance.nom}")
            else:
                print(f"Avertissement : Objet permanent '{objet_instance.nom}' non prévu dans l'inventaire.")
            
        elif objet_instance.type_objet == "Consommable":
            objet_instance.utiliser(joueur_instance) #Appel polymorphique
            
        else:
            print(f"Erreur: Type d'objet inconnu : {objet_instance.type_objet}")