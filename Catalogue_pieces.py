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
        "items": ["Lettre", "Plan", "Allowance token"],
        "image" : "Images/entrancehall.webp",
        "cout_gemmes": 0, "rarete": 0 
    },
    {
        "nom": "The Foundation",
        "couleur": "grise",
        "portes": {"up": True, "down": True, "left": False, "right": False}, # Corrigé
        "items": ["Pierre ancienne", "Blueprint part"],
        "image" : "Images/foundation.webp",
        "cout_gemmes": 0, "rarete": 1
    },
    {
        "nom": "Nook",
        "couleur": "bleue",
        "portes": {"up": False, "down": False, "left": True, "right": True}, # Corrigé
        "items": ["Clé", "Note noire", "Livre"],
        "image" : "Images/nook.webp",
        "cout_gemmes": 0, "rarete": 0
    },
    {
        "nom": "Garage",
        "couleur": "bleue",
        "portes": {"up": False, "down": True, "left": True, "right": False}, # Corrigé
        "items": ["Voiture", "Clé", "Coffre dans le coffre"],
        "image" : "Images/garage.webp",
        "cout_gemmes": 1, "rarete": 1
    },
    {
        "nom": "Music Room",
        "couleur": "bleue",
        "portes": {"up": False, "down": False, "left": True, "right": True}, # Corrigé
        "items": ["Partitions", "Clé spéciale"],
        "image" : "Images/musicroom.webp",
        "cout_gemmes": 1, "rarete": 1
    },
    {
        "nom": "Locker Room",
        "couleur": "bleue",
        "portes": {"up": False, "down": True, "left": True, "right": False}, # Corrigé
        "items": ["Casiers", "Clé", "Pièces"],
        "image" : "Images/lockerroom.webp",
        "cout_gemmes": 0, "rarete": 0
    },
    {
        "nom": "Den",
        "couleur": "bleue",
        "portes": {"up": True, "down": True, "left": False, "right": False}, # Corrigé
        "items": ["Gemme", "Coffre verrouillé"],
        "image" : "Images/den.webp",
        "cout_gemmes": 2, "rarete": 2 
    },
    {
        "nom": "Wine Cellar",
        "couleur": "bleue",
        "portes": {"up": False, "down": True, "left": False, "right": True}, # Corrigé
        "items": ["Bouteilles", "Gemmes"],
        "image" : "Images/winecellar.webp",
        "cout_gemmes": 1, "rarete": 1
    },
    {
        "nom": "Trophy Room",
        "couleur": "dorée", 
        "portes": {"up": False, "down": False, "left": True, "right": True}, # Corrigé
        "items": ["Trophées", "Gemmes"],
        "image" : "Images/trophyroom.webp",
        "cout_gemmes": 2, "rarete": 2
    },
    {
        "nom": "Ballroom",
        "couleur": "blanche",
        "portes": {"up": True, "down": False, "left": False, "right": True}, # Corrigé
        "items": ["Lustre", "Partition", "Clé de scène"],
        "image" : "Images/ballroom.webp",
        "cout_gemmes": 1, "rarete": 1
    },
    {
        "nom": "Pantry",
        "couleur": "verte", 
        "portes": {"up": False, "down": False, "left": True, "right": True}, # Corrigé
        "items": ["Fruit", "Pièces"],
        "image" : "Images/pantry.webp",
        "cout_gemmes": 0, "rarete": 0 
    },
    {
        "nom": "Rumpus Room",
        "couleur": "bleue",
        "portes": {"up": True, "down": False, "left": True, "right": False}, # Corrigé
        "items": ["Machine Alzara", "Pièces"],
        "image" : "Images/rumpusroom.webp",
        "cout_gemmes": 1, "rarete": 1
    },
    {
        "nom": "Observatory",
        "couleur": "violette", 
        "portes": {"up": True, "down": False, "left": True, "right": True}, # Corrigé
        "items": ["Télescope", "Constellation map"],
        "image" : "Images/observatory.webp",
        "cout_gemmes": 2, "rarete": 2
    },
    {
        "nom": "Library",
        "couleur": "brune",
        "portes": {"up": True, "down": False, "left": True, "right": True}, # Corrigé
        "items": ["Livres", "Note de recherche"],
        "image" : "Images/library.webp",
        "cout_gemmes": 1, "rarete": 1
    },
    {
        "nom": "Vault",
        "couleur": "dorée",
        "portes": {"up": False, "down": False, "left": True, "right": False}, # Corrigé
        "items": ["Coffre-fort", "Gemmes", "Clés"],
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