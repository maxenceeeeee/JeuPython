"""
Dictionnaire de 20 pièces représentatives du jeu, avec nom, couleur, portes et loot.
CATALOGUE FINAL AVEC AUGMENTATION DES GEMMES ET CLÉS.
"""
catalogue_pieces = [
    {
        "nom": "Entrance Hall",
        "couleur": "bleue",
        "portes": {"up": True, "down": False, "left": True, "right": True},
        "loot": {
            "garanti": ["Pièce d'Or", "Pièce d'Or", "Clé"], 
            "aleatoire": [("Clé", 0.6), ("Pomme", 0.3)]
        },
        "endroits_creuser": 0,
        "image": "Images/entrancehall.webp",
        "cout_gemmes": 0,
        "rarete": 0,
        "a_coffre": False, 
    },
    {
        "nom": "The Foundation",
        "couleur": "bleue",
        "portes": {"up": False, "down": True, "left": True, "right": True},
        "loot": {
            "garanti": ["Pièce d'Or", "Pièce d'Or", "Gemme"], 
            "aleatoire": [("Pièce d'Or", 0.7), ("Clé", 0.5), ("Pelle", 0.2)]
        },
        "endroits_creuser": 1,
        "image": "Images/foundation.webp",
        "cout_gemmes": 0,
        "rarete": 1,
        "a_coffre": False,
    },
    {
        "nom": "Nook",
        "couleur": "bleue",
        "portes": {"up": False, "down": True, "left": True, "right": False},
        "loot": {
            "garanti": ["Clé", "Clé"], 
            "aleatoire": [("Clé", 0.8), ("Pièce d'Or", 1.0), ("Pomme", 0.5), ("Kit de Crochetage", 0.05)] 
        },
        "endroits_creuser": 0,
        "image": "Images/nook.webp",
        "cout_gemmes": 0,
        "rarete": 0,
        "a_coffre": False,
    },
    {
        "nom": "Garage",
        "couleur": "bleue",
        "portes": {"up": False, "down": True, "left": False, "right": False},
        "loot": {
            "garanti": ["Clé", "Clé", "Marteau"], 
            "aleatoire": [("Clé", 0.4), ("Pièce d'Or", 0.3)] 
        },
        "endroits_creuser": 0,
        "image": "Images/garage.webp",
        "cout_gemmes": 1,
        "rarete": 1,
        "a_coffre": False,
    },
    {
        "nom": "Music Room",
        "couleur": "bleue",
        "portes": {"up": False, "down": True, "left": True, "right": False},
        "loot": {
            "garanti": ["Dé", "Dé"], 
            "aleatoire": [("Pièce d'Or", 0.9), ("Dé", 0.4), ("Gemme", 0.3)]
        },
        "endroits_creuser": 0,
        "image": "Images/musicroom.webp",
        "cout_gemmes": 1,
        "rarete": 1,
        "a_coffre": False,
    },
    {
        "nom": "Locker Room",
        "couleur": "bleue",
        "portes": {"up": True, "down": True, "left": False, "right": False},
        "loot": {
            "garanti": ["Pièce d'Or", "Clé", "Pelle"], 
            "aleatoire": [("Clé", 0.3), ("Kit de Crochetage", 0.10)]
        },
        "endroits_creuser": 0,
        "image": "Images/lockerroom.webp",
        "cout_gemmes": 0,
        "rarete": 0,
        "a_coffre": False,
    },
    {
        "nom": "Den",
        "couleur": "bleue",
        "portes": {"up": False, "down": True, "left": True, "right": True},
        "loot": {
            "garanti": ["Gemme", "Gemme", "Gemme"], 
            "aleatoire": [("Clé", 0.7), ("Patte de Lapin", 0.4), ("Détecteur de Métaux", 0.3)],
            "coffre_loot": {"Gemme": 2, "Dé": 1},
        },
        "endroits_creuser": 0,
        "image": "Images/den.webp",
        "cout_gemmes": 2,
        "rarete": 2,
        "a_coffre": True, # COFFRE ACTIVÉ
    },
    {
        "nom": "Wine Cellar",
        "couleur": "bleue",
        "portes": {"up": False, "down": True, "left": False, "right": False},
        "loot": {
            "garanti": ["Gemme", "Gemme", "Gemme", "Banane"], 
            "aleatoire": [("Gemme", 0.4), ("Banane", 0.5), ("Repas", 0.2)] 
        },
        "endroits_creuser": 0,
        "image": "Images/winecellar.webp",
        "cout_gemmes": 1,
        "rarete": 1,
        "a_coffre": False,
    },
    {
        "nom": "Trophy Room",
        "couleur": "dorée",
        "portes": {"up": False, "down": True, "left": True, "right": False},
        "loot": {
            "garanti": ["Gemme"] * 4, 
            "aleatoire": [("Pièce d'Or", 0.6)],
            "magasin": [
                {"item": "Clé", "prix": 3}, 
                {"item": "Dé", "prix": 5},
                {"item": "Pomme", "prix": 1},
                {"item": "Kit de Crochetage", "prix": 15} 
            ]
        },
        "endroits_creuser": 0,
        "image": "Images/trophyroom.webp",
        "cout_gemmes": 2,
        "rarete": 2,
        "a_coffre": False,
    },
    {
        "nom": "Ballroom",
        "couleur": "bleue",
        "portes": {"up": True, "down": True, "left": False, "right": False},
        "loot": {
            "garanti": ["Gemme", "Gemme", "Gâteau"], 
            "aleatoire": [("Pièce d'Or", 0.5), ("Gâteau", 0.3), ("Sandwich", 0.2)] 
        },
        "endroits_creuser": 0,
        "image": "Images/ballroom.webp",
        "cout_gemmes": 1,
        "rarete": 1,
        "a_coffre": False,
    },
    {
        "nom": "Pantry",
        "couleur": "bleue",
        "portes": {"up": False, "down": True, "left": True, "right": False},
        "loot": {
            "garanti": ["Pièce d'Or", "Pièce d'Or", "Pièce d'Or", "Pièce d'Or", "Détecteur de Métaux"], 
            "aleatoire": [("Banane", 0.5), ("Pomme", 0.7), ("Repas", 0.3)],
            "coffre_loot": {"Pièce d'Or": 10, "Pomme": 2},
        },
        "endroits_creuser": 1,
        "image": "Images/pantry.webp",
        "cout_gemmes": 0,
        "rarete": 0,
        "a_coffre": True, # COFFRE ACTIVÉ
    },
    {
        "nom": "Rumpus Room",
        "couleur": "bleue",
        "portes": {"up": True, "down": True, "left": False, "right": False},
        "loot": {
            "garanti": ["Pièce d'Or", "Pièce d'Or", "Pièce d'Or", "Pièce d'Or", "Dé"], 
            "aleatoire": [("Pièce d'Or", 0.7), ("Dé", 0.4), ("Gemme", 0.3)],
            "coffre_loot": {"Dé": 2, "Pièce d'Or": 5},
        },
        "endroits_creuser": 0,
        "image": "Images/rumpusroom.webp",
        "cout_gemmes": 1,
        "rarete": 1,
        "a_coffre": True, # COFFRE ACTIVÉ
    },
    {
        "nom": "Observatory",
        "couleur": "bleue",
        "portes": {"up": False, "down": True, "left": True, "right": False},
        "loot": {
            "garanti": ["Kit de Crochetage", "Gemme"], 
            "aleatoire": [("Gâteau", 0.3), ("Gemme", 0.4), ("Patte de Lapin", 0.35)] 
        },
        "endroits_creuser": 0,
        "image": "Images/observatory.webp",
        "cout_gemmes": 2,
        "rarete": 2,
        "a_coffre": False,
    },
    {
        "nom": "Library",
        "couleur": "brune",
        "portes": {"up": False, "down": True, "left": True, "right": False},
        "loot": {
            "garanti": ["Pièce d'Or", "Pièce d'Or"], 
            "aleatoire": [("Pièce d'Or", 0.3), ("Dé", 0.4), ("Patte de Lapin", 0.25), ("Gemme", 0.2)] 
        },
        "endroits_creuser": 0,
        "image": "Images/library.webp",
        "cout_gemmes": 1,
        "rarete": 1,
        "a_coffre": False,
    },
    {
        "nom": "Vault",
        "couleur": "bleue",
        "portes": {"up": False, "down": True, "left": False, "right": False},
        "loot": {
            "garanti": ["Pièce d'Or"] * 15, 
            "aleatoire": [("Gemme", 0.6)],
            "coffre_loot": {"Pièce d'Or": 10, "Gemme": 3},
            "magasin": [
                {"item": "Pelle", "prix": 10}, 
                {"item": "Marteau", "prix": 12},
                {"item": "Kit de Crochetage", "prix": 15},
                {"item": "Détecteur de Métaux", "prix": 20},
                {"item": "Patte de Lapin", "prix": 25}
            ]
        },
        "endroits_creuser": 0,
        "image": "Images/vault.webp",
        "cout_gemmes": 3,
        "rarete": 3,
        "a_coffre": True, # COFFRE ACTIVÉ
    },
    {
        "nom": "Antechamber",
        "couleur": "bleue",
        "portes": {"up": False, "down": True, "left": True, "right": True},
        "loot": {
            "garanti": [], 
            "aleatoire": [] 
        },
        "endroits_creuser": 0,
        "image": "Images/antechamber.webp",
        "cout_gemmes": 0,
        "rarete": 0,
        "a_coffre": False,
    },
    
    {
        "nom": "Great Hall",
        "couleur": "orange",
        "portes": {"up": True, "down": True, "left": True, "right": True},
        "loot": {
            "garanti": ["Pièce d'Or", "Gemme"], 
            "aleatoire": [("Gemme", 0.3), ("Clé", 0.6)]
        },
        "image" : "Images/greathall.png",
        "cout_gemmes": 1,
        "rarete": 1,
        "a_coffre": False,
    },
    {
        "nom": "Gallery",
        "couleur": "bleue",
        "portes": {"up": True, "down": True, "left": False, "right": False},
        "loot": {
            "garanti": ["Pièce d'Or", "Pièce d'Or", "Gemme"],
            "aleatoire": [("Pièce d'Or", 0.5), ("Clé", 0.4)]
        },
        "image" : "Images/gallery.png",
        "cout_gemmes": 1,
        "rarete": 1,
        "a_coffre": False,
    },
    {
        "nom": "Hallway",
        "couleur": "orange",
        "portes": {"up": False, "down": True, "left": True, "right": True}, 
        "loot": {
            "garanti": ["Gemme", "Gemme", "Gemme"],
            "aleatoire": [("Potion", 0.2), ("Clé", 0.05)]
        },
        "endroits_creuser": 0,
        "image" : "Images/hallway.png",
        "cout_gemmes": 2,
        "rarete": 2,
        "a_coffre": False,
    },
    {
        "nom": "Archives",
        "couleur": "rouge",
        "portes": {"up": True, "down": True, "left": True, "right": True},
        "loot": {
            "garanti": ["Gemme"],
            "aleatoire": [("Clé", 0.5), ("Gemme", 0.5)],
            "coffre_loot": {"Clé": 2, "Dé": 1}, 
            "magasin": [
                {"item": "Gemme", "prix": 5},
                {"item": "Gâteau", "prix": 8}
            ]
        },
        "endroits_creuser": 0,
        "image" : "Images/archives.png",
        "cout_gemmes": 2,
        "rarete": 2,
        "a_coffre": True, # COFFRE ACTIVÉ
    },
    {"nom": "Workshop",
        "couleur": "bleue",
        "portes": {"up": True, "down": True, "left": False, "right": False},
        "loot": {
            "garanti": ["Marteau", "Clé"], 
            "aleatoire": [("Pièce d'Or", 0.6), ("Pelle", 0.4), ("Kit de Crochetage", 0.2)],
            "coffre_loot": {"Pièce d'Or": 5, "Clé": 1},
        },
        "endroits_creuser": 1,
        "image": "Images/workshop.png",
        "cout_gemmes": 0,
        "rarete": 1,
        "a_coffre": False,
    },
    {
        "nom": "Foyer",
        "couleur": "brune",
        "portes": {"up": True, "down": True, "left": False, "right": False},
        "loot": {
            "garanti": ["Pièce d'Or", "Gemme"], 
            "aleatoire": [("Gemme", 0.4), ("Clé", 0.3), ("Dé", 0.2)]
        },
        "image": "Images/foyer.png",
        "cout_gemmes": 2,
        "rarete": 2,
        "a_coffre": False,
    },
    {
        "nom": "Veranda",
        "couleur": "verte",
        "portes": {"up": True, "down": True, "left": False, "right": False},
        "loot": {
            "garanti": ["Gemme", "Pomme"], 
            "aleatoire": [("Banane", 0.4), ("Clé", 0.2), ("Repas", 0.3)]
        },
        "endroits_creuser": 1,
        "image": "Images/veranda.png",
        "cout_gemmes": 2,
        "rarete": 2,
        "a_coffre": False,
    },
    {
        "nom": "Showroom",
        "couleur": "dorée",
        "portes": {"up": True, "down": True, "left": False, "right": False},
        "loot": {
            "garanti": ["Pièce d'Or", "Pièce d'Or", "Gemme", "Gemme"], 
            "aleatoire": [("Dé", 0.3), ("Clé", 0.5)],
            "magasin": [
                {"item": "Détecteur de Métaux", "prix": 18},
                {"item": "Patte de Lapin", "prix": 25},
                {"item": "Gâteau", "prix": 10}
            ]
        },
        "endroits_creuser": 0,
        "image": "Images/showroom.png",
        "cout_gemmes": 2,
        "rarete": 3,
        "a_coffre": False,
    }
]