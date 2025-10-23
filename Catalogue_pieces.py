"""
Dictionnaire de 15 pièces représentatives du jeu, avec nom, couleur, portes et items.
CORRECTION: Les clés de direction sont en Anglais (up, down, left, right) 
pour correspondre au reste du code (jeu.py, joueur.py).
"""

catalogue_pieces = [
    {
        "nom": "Entrance Hall",
        "couleur": "bleue",
        "portes": {"up": True, "down": False, "left": True, "right": True}, # Corrigé
        "items": ["lettre", "plan", "allowance token"],
        "image" : "Images/entrancehall.webp",
        "cout_gemmes": 0, "rarete": 0 
    },
    {
        "nom": "The Foundation",
        "couleur": "grise",
        "portes": {"up": True, "down": True, "left": False, "right": False}, # Corrigé
        "items": ["pierre ancienne", "blueprint part"],
        "image" : "Images/foundation.webp",
        "cout_gemmes": 0, "rarete": 1
    },
    {
        "nom": "Nook",
        "couleur": "bleue",
        "portes": {"up": False, "down": False, "left": True, "right": True}, # Corrigé
        "items": ["clé", "note noire", "livre"],
        "image" : "Images/nook.webp",
        "cout_gemmes": 0, "rarete": 0
    },
    {
        "nom": "Garage",
        "couleur": "bleue",
        "portes": {"up": False, "down": True, "left": True, "right": False}, # Corrigé
        "items": ["voiture", "clé", "coffre dans le coffre"],
        "image" : "Images/garage.webp",
        "cout_gemmes": 1, "rarete": 1
    },
    {
        "nom": "Music Room",
        "couleur": "bleue",
        "portes": {"up": False, "down": False, "left": True, "right": True}, # Corrigé
        "items": ["partitions", "clé spéciale"],
        "image" : "Images/musicroom.webp",
        "cout_gemmes": 1, "rarete": 1
    },
    {
        "nom": "Locker Room",
        "couleur": "bleue",
        "portes": {"up": False, "down": True, "left": True, "right": False}, # Corrigé
        "items": ["casiers", "clé", "pièces"],
        "image" : "Images/lockerroom.webp",
        "cout_gemmes": 0, "rarete": 0
    },
    {
        "nom": "Den",
        "couleur": "bleue",
        "portes": {"up": True, "down": True, "left": False, "right": False}, # Corrigé
        "items": ["gemme", "coffre verrouillé"],
        "image" : "Images/den.webp",
        "cout_gemmes": 2, "rarete": 2 
    },
    {
        "nom": "Wine Cellar",
        "couleur": "bleue",
        "portes": {"up": False, "down": True, "left": False, "right": True}, # Corrigé
        "items": ["bouteilles", "gemmes"],
        "image" : "Images/winecellar.webp",
        "cout_gemmes": 1, "rarete": 1
    },
    {
        "nom": "Trophy Room",
        "couleur": "dorée", 
        "portes": {"up": False, "down": False, "left": True, "right": True}, # Corrigé
        "items": ["trophées", "gemmes"],
        "image" : "Images/trophyroom.webp",
        "cout_gemmes": 2, "rarete": 2
    },
    {
        "nom": "Ballroom",
        "couleur": "blanche",
        "portes": {"up": True, "down": False, "left": False, "right": True}, # Corrigé
        "items": ["lustre", "partition", "clé de scène"],
        "image" : "Images/ballroom.webp",
        "cout_gemmes": 1, "rarete": 1
    },
    {
        "nom": "Pantry",
        "couleur": "verte", 
        "portes": {"up": False, "down": False, "left": True, "right": True}, # Corrigé
        "items": ["fruit", "pièces"],
        "image" : "Images/pantry.webp",
        "cout_gemmes": 0, "rarete": 0 
    },
    {
        "nom": "Rumpus Room",
        "couleur": "bleue",
        "portes": {"up": True, "down": False, "left": True, "right": False}, # Corrigé
        "items": ["machine Alzara", "pièces"],
        "image" : "Images/rumpusroom.webp",
        "cout_gemmes": 1, "rarete": 1
    },
    {
        "nom": "Observatory",
        "couleur": "violette", 
        "portes": {"up": True, "down": False, "left": True, "right": True}, # Corrigé
        "items": ["télescope", "constellation map"],
        "image" : "Images/observatory.webp",
        "cout_gemmes": 2, "rarete": 2
    },
    {
        "nom": "Library",
        "couleur": "brune",
        "portes": {"up": True, "down": False, "left": True, "right": True}, # Corrigé
        "items": ["livres", "note de recherche"],
        "image" : "Images/library.webp",
        "cout_gemmes": 1, "rarete": 1
    },
    {
        "nom": "Vault",
        "couleur": "dorée",
        "portes": {"up": False, "down": False, "left": True, "right": False}, # Corrigé
        "items": ["coffre-fort", "gemmes", "clés"],
        "image" : "Images/vault.webp",
        "cout_gemmes": 3, "rarete": 3 
    },
    
    {
        "nom": "Antechamber",
        "couleur": "bleue",
        "portes": {"up": False, "down": False, "left": True, "right": False}, # Corrigé
        "items": [],
        "image" : "Images/antechamber.webp",
        "cout_gemmes": 0, "rarete": 0
    }
]