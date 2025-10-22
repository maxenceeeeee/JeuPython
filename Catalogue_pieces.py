"""
Dictionnaire de 15 pièces représentatives du jeu, avec nom, couleur, portes et items.

"""

catalogue_pieces = [
    {
        "nom": "Entrance Hall",
        "couleur": "bleue",
        "portes": {"haut": True, "bas": False, "gauche": True, "droite": True},
        "items": ["lettre", "plan", "allowance token"],
        "image" : "Images/entrancehall.webp",
        "cout_gemmes": 0, "rarete": 0 
    },
    {
        "nom": "The Foundation",
        "couleur": "grise",
        "portes": {"haut": True, "bas": True, "gauche": False, "droite": False},
        "items": ["pierre ancienne", "blueprint part"],
        "image" : "Images/foundation.webp",
        "cout_gemmes": 0, "rarete": 1
    },
    {
        "nom": "Nook",
        "couleur": "bleue",
        "portes": {"haut": False, "bas": False, "gauche": True, "droite": True},
        "items": ["clé", "note noire", "livre"],
        "image" : "Images/nook.webp",
        "cout_gemmes": 0, "rarete": 0
    },
    {
        "nom": "Garage",
        "couleur": "bleue",
        "portes": {"haut": False, "bas": True, "gauche": True, "droite": False},
        "items": ["voiture", "clé", "coffre dans le coffre"],
        "image" : "Images/garage.webp",
        "cout_gemmes": 1, "rarete": 1
    },
    {
        "nom": "Music Room",
        "couleur": "bleue",
        "portes": {"haut": False, "bas": False, "gauche": True, "droite": True},
        "items": ["partitions", "clé spéciale"],
        "image" : "Images/musicroom.webp",
        "cout_gemmes": 1, "rarete": 1
    },
    {
        "nom": "Locker Room",
        "couleur": "bleue",
        "portes": {"haut": False, "bas": True, "gauche": True, "droite": False},
        "items": ["casiers", "clé", "pièces"],
        "image" : "Images/lockerroom.webp",
        "cout_gemmes": 0, "rarete": 0
    },
    {
        "nom": "Den",
        "couleur": "bleue",
        "portes": {"haut": True, "bas": True, "gauche": False, "droite": False},
        "items": ["gemme", "coffre verrouillé"],
        "image" : "Images/den.webp",
        "cout_gemmes": 2, "rarete": 2 # Contient une gemme, donc plus rare/chère
    },
    {
        "nom": "Wine Cellar",
        "couleur": "bleue",
        "portes": {"haut": False, "bas": True, "gauche": False, "droite": True},
        "items": ["bouteilles", "gemmes"],
        "image" : "Images/winecellar.webp",
        "cout_gemmes": 1, "rarete": 1
    },
    {
        "nom": "Trophy Room",
        "couleur": "dorée", # Jaune (Magasin)
        "portes": {"haut": False, "bas": False, "gauche": True, "droite": True},
        "items": ["trophées", "gemmes"],
        "image" : "Images/trophyroom.webp",
        "cout_gemmes": 2, "rarete": 2
    },
    {
        "nom": "Ballroom",
        "couleur": "blanche",
        "portes": {"haut": True, "bas": False, "gauche": False, "droite": True},
        "items": ["lustre", "partition", "clé de scène"],
        "image" : "Images/ballroom.webp",
        "cout_gemmes": 1, "rarete": 1
    },
    {
        "nom": "Pantry",
        "couleur": "verte", # Verte 
        "portes": {"haut": False, "bas": False, "gauche": True, "droite": True},
        "items": ["fruit", "pièces"],
        "image" : "Images/pantry.webp",
        "cout_gemmes": 0, "rarete": 0 # Contient de la nourriture 
    },
    {
        "nom": "Rumpus Room",
        "couleur": "bleue",
        "portes": {"haut": True, "bas": False, "gauche": True, "droite": False},
        "items": ["machine Alzara", "pièces"],
        "image" : "Images/rumpusroom.webp",
        "cout_gemmes": 1, "rarete": 1
    },
    {
        "nom": "Observatory",
        "couleur": "violette", # Violette (Chambre)
        "portes": {"haut": True, "bas": False, "gauche": True, "droite": True},
        "items": ["télescope", "constellation map"],
        "image" : "Images/observatory.webp",
        "cout_gemmes": 2, "rarete": 2
    },
    {
        "nom": "Library",
        "couleur": "brune",
        "portes": {"haut": True, "bas": False, "gauche": True, "droite": True},
        "items": ["livres", "note de recherche"],
        "image" : "Images/library.webp",
        "cout_gemmes": 1, "rarete": 1
    },
    {
        "nom": "Vault", # Exemple du PDF
        "couleur": "dorée", # Jaune (Magasin))
        "portes": {"haut": False, "bas": False, "gauche": True, "droite": False},
        "items": ["coffre-fort", "gemmes", "clés"],
        "image" : "Images/vault.webp",
        "cout_gemmes": 3, "rarete": 3 
    },
    
    {
        "nom": "Antechamber",
        "couleur": "bleue",
        "portes": {"haut": False, "bas": False, "gauche": True, "droite": False},
        "items": [],
        "image" : "Images/antechamber.webp",
        "cout_gemmes": 0, "rarete": 0
    }
]
