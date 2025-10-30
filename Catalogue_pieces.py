"""
Dictionnaire de 15 pièces représentatives du jeu, avec nom, couleur, portes et loot.
Le "loot" est un dictionnaire qui peut contenir :
- "garanti": liste d'objets (str) toujours donnés.
- "aleatoire": liste de (objet_str, proba_de_0_a_1)
- "magasin": liste de {"item": str, "prix": int}
"""

catalogue_pieces = [
    {
        "nom": "Entrance Hall",
        "couleur": "bleue",
        "portes": {"up": True, "down": False, "left": True, "right": True},
        "loot": {
            "garanti": [], # Pas de loot dans l'entrée
            "aleatoire": []
        },
        "image" : "Images/entrancehall.webp",
        "cout_gemmes": 0, "rarete": 0 
    },
    {
        "nom": "The Foundation",
        "couleur": "grise",
        "portes": {"up": False, "down": True, "left": True, "right": True},
        "loot": {
            "garanti": ["Pièce d'Or"],
            "aleatoire": [("Pièce d'Or", 0.5)] # 50% chance d'une 2e pièce
        },
        "image" : "Images/foundation.webp",
        "cout_gemmes": 0, "rarete": 1
    },
    {
        "nom": "Nook",
        "couleur": "bleue",
        "portes": {"up": False, "down": True, "left": True, "right": False},
        "loot": {
            "garanti": [],
            "aleatoire": [("Clé", 0.5), ("Pièce d'Or", 1.0)] # 50% Clé, 100% Pièce
        },
        "image" : "Images/nook.webp",
        "cout_gemmes": 0, "rarete": 0
    },
    {
        "nom": "Garage",
        "couleur": "bleue",
        "portes": {"up": False, "down": True, "left": False, "right": False},
        "loot": { "garanti": [], "aleatoire": [("Clé", 0.2)] },
        "image" : "Images/garage.webp",
        "cout_gemmes": 1, "rarete": 1
    },
    {
        "nom": "Music Room",
        "couleur": "bleue",
        "portes": {"up": False, "down": True, "left": True, "right": False},
        "loot": { "garanti": [], "aleatoire": [("Pièce d'Or", 0.8)] },
        "image" : "Images/musicroom.webp",
        "cout_gemmes": 1, "rarete": 1
    },
    {
        "nom": "Locker Room",
        "couleur": "bleue",
        "portes": {"up": True, "down": True, "left": False, "right": False},
        "loot": { "garanti": ["Pièce d'Or"], "aleatoire": [("Clé", 0.1)] },
        "image" : "Images/lockerroom.webp",
        "cout_gemmes": 0, "rarete": 0
    },
    {
        "nom": "Den",
        "couleur": "bleue",
        "portes": {"up": False, "down": True, "left": True, "right": True},
        "loot": { "garanti": ["Gemme"], "aleatoire": [("Clé", 0.5)] }, # Garanti une gemme
        "image" : "Images/den.webp",
        "cout_gemmes": 2, "rarete": 2 
    },
    {
        "nom": "Wine Cellar",
        "couleur": "bleue",
        "portes": {"up": False, "down": True, "left": False, "right": False},
        "loot": { "garanti": [], "aleatoire": [("Gemme", 0.1)] },
        "image" : "Images/winecellar.webp",
        "cout_gemmes": 1, "rarete": 1
    },
    {
        "nom": "Trophy Room",
        "couleur": "dorée", # C'est une boutique 
        "portes": {"up": False, "down": True, "left": True, "right": False},
        "loot": {
            "garanti": ["Pièce d'Or", "Pièce d'Or"], # On trouve 2 pièces en entrant
            "aleatoire": [],
            "magasin": [
                {"item": "Clé", "prix": 5},
                {"item": "Dé", "prix": 8},
                {"item": "Pomme", "prix": 1}
            ]
        },
        "image" : "Images/trophyroom.webp",
        "cout_gemmes": 2, "rarete": 2
    },
    {
        "nom": "Ballroom",
        "couleur": "blanche",
        "portes": {"up": True, "down": True, "left": False, "right": False},
        "loot": { "garanti": [], "aleatoire": [("Pièce d'Or", 0.3)] },
        "image" : "Images/ballroom.webp",
        "cout_gemmes": 1, "rarete": 1
    },
    {
        "nom": "Pantry",
        "couleur": "verte", # Pièce verte
        "portes": {"up": False, "down": False, "left": True, "right": True},
        "loot": { 
            "garanti": ["Pomme"], # Garanti une pomme
            "aleatoire": [("Banane", 0.3)] # Chance d'une banane
        },
        "image" : "Images/pantry.webp",
        "cout_gemmes": 0, "rarete": 0 
    },
    {
        "nom": "Rumpus Room",
        "couleur": "bleue",
        "portes": {"up": True, "down": True, "left": False, "right": False},
        "loot": { "garanti": [], "aleatoire": [("Pièce d'Or", 0.5)] },
        "image" : "Images/rumpusroom.webp",
        "cout_gemmes": 1, "rarete": 1
    },
    {
        "nom": "Observatory",
        "couleur": "violette", # Pièce violette
        "portes": {"up": False, "down": True, "left": True, "right": False},
        "loot": { 
            "garanti": [], 
            "aleatoire": [("Gâteau", 0.1)] # Chance de Gâteau (redonne des pas)
        },
        "image" : "Images/observatory.webp",
        "cout_gemmes": 2, "rarete": 2
    },
    {
        "nom": "Library",
        "couleur": "brune",
        "portes": {"up": False, "down": True, "left": True, "right": False},
        "loot": { "garanti": [], "aleatoire": [("Pièce d'Or", 0.1)] },
        "image" : "Images/library.webp",
        "cout_gemmes": 1, "rarete": 1
    },
    {
        "nom": "Vault",
        "couleur": "dorée", # C'est une boutique 
        "portes": {"up": False, "down": True, "left": False, "right": False},
        "loot": {
            "garanti": ["Gemme"], # Garanti une gemme en entrant
            "aleatoire": [],
            "magasin": [
                {"item": "Pelle", "prix": 30},
                {"item": "Kit de Crochetage", "prix": 50},
                {"item": "Patte de Lapin", "prix": 75}
            ]
        },
        "image" : "Images/vault.webp",
        "cout_gemmes": 3, "rarete": 3 
    },
    
    {
        "nom": "Antechamber",
        "couleur": "bleue",
        "portes": {"up": False, "down": True, "left": True, "right": True},
        "loot": { "garanti": [], "aleatoire": [] },
        "image" : "Images/antechamber.webp",
        "cout_gemmes": 0, "rarete": 0
    }
]