class Joueur:
    
    def __init__(self):
        self.pas = 70
        self.pieces_or = 0
        self.gemmes = 2
        self.cles = 0
        self.des = 0
        self.pelle = False
        self.marteau = False
        self.kitcrochetage = False
        self.detecteur_metal = False
        self.patte_lapin = False
        self.position_ligne = 8
        self.position_colonne = 2
        
        
        
    def calcul_coordonnees_casead(self, choix):
        case_ligne, case_colonne = 0, 0
        if choix == 'up':
            case_ligne, case_colonne = -1, 0
        elif choix == 'down': 
            case_ligne, case_colonne = 1, 0
        elif choix == 'left': 
            case_ligne, case_colonne = 0, -1
        elif choix == 'right': 
            case_ligne, case_colonne = 0, 1
        return self.position_ligne + case_ligne, self.position_colonne + case_colonne
    
    
    def deplacer_vers(self, posx, posy):
        if self.pas <= 0:
            return False
        else :
            self.perdre_pas(1)
            self.position_ligne = posx
            self.position_colonne = posy
            return True
        
        
    def ouverture_porte(self, niveau):    
        if niveau == 1: 
            if self.cles > 0:
                self.utiliser_cle()
                return True 
            if self.kitcrochetage:
                return True       
        elif niveau == 2:
            if self.cles > 0:
                self.utiliser_cle()
                return True
        elif niveau == 0:
            return True  
        else :
            return False

    def pas_en_moins(self, pas):
        if self.pas == 0 :
            return 0
        else :
            self.pas = self.pas - pas

    def pas_en_plus(self, pas):
        self.pas = self.pas + pas

    def pieces_or_en_plus(self, nb_pieces_or):
        self.pieces_or = self.pieces_or + nb_pieces_or

    def pieces_or_en_moins(self, prix):
        if self.pieces_or < prix:
            return False
        else:
            self.pieces_or = self.pieces_or - prix
            return True

    def gemmes_en_plus(self, nb_gemmes):
        self.gemmes = self.gemmes + nb_gemmes

    def depenser_gemmes(self, prix):
        
        if self.gemmes < prix:
            return False
        else :
            self.gemmes = self.gemmes - prix
            return True
        
        
    def cles_enplus(self, nb):
        self.cles = self.cles + nb

    def cle_enmoins(self):
        if self.cles > 0:
            self.cles =  self.cles - 1
            return True
        else : 
            return False
        
    def des_enplus(self, nb):
        self.des = self.des + nb

    def de_enmoins(self):
        if self.des <= 0 :
            return False
        else :
            self.des -= 1
            return True

    def récuperer_obj_perma(self, objet):
        if objet == 'marteau': 
            self.marteau = True
        if objet == 'pelle': 
            self.pelle = True
        if objet == 'kitcrochetage': 
            self.kitcrochetage = True
        if objet == 'detecteur_metal': 
            self.detecteur_metal = True
        if objet == 'patte_lapin': 
            self.patte_lapin = True

    def verifie_ouverture_coffre(self):
        if self.marteau == True or self.cles > 0 :
            return True
        else :
            return False

    def verifie_pelle(self):
        if self.pelle == True :
            return True
        else :
            return False
    