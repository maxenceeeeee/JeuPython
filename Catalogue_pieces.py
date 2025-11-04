"""
Dictionnaire de 15 pièces représentatives du jeu, avec nom, couleur, portes et loot.
Le "loot" est un dictionnaire qui peut contenir :
- "garanti": liste d'objets (str) toujours donnés.
- "aleatoire": liste de (objet_str, proba_de_0_a_1)
- "magasin": liste de {"item": str, "prix": int}
- "endroits_creuser": int (0 ou 1) - nombre d'endroits où creuser
"""

catalogue_pieces = [
    {
        "nom": "Entrance Hall",
        "couleur": "bleue",
        "portes": {"up": True, "down": False, "left": True, "right": True},
        "loot": {
            "garanti": ["Pièce d'Or", "Pièce d'Or", "Clé"],  # Clé ajoutée en garanti
            "aleatoire": [("Clé", 0.5), ("Pomme", 0.3)]  # Probabilités augmentées
        },
        "endroits_creuser": 0,
        "image": "Images/entrancehall.webp",
        "cout_gemmes": 0,
        "rarete": 0
    },
    {
        "nom": "The Foundation",
        "couleur": "grise",
        "portes": {"up": True, "down": True, "left": True, "right": True},
        "loot": {
            "garanti": ["Pièce d'Or", "Pièce d'Or"],  # Deux pièces garanties
            "aleatoire": [("Pièce d'Or", 0.7), ("Clé", 0.4), ("Pelle", 0.2)]  # Pelle ajoutée à 20%
        },
        "endroits_creuser": 0,
        "image": "Images/foundation.webp",
        "cout_gemmes": 0,
        "rarete": 1
    },
    {
        "nom": "Nook",
        "couleur": "bleue",
        "portes": {"up": False, "down": True, "left": True, "right": False},
        "loot": {
            "garanti": ["Clé", "Clé"],  # Deux clés garanties
            "aleatoire": [("Clé", 0.7), ("Pièce d'Or", 1.0), ("Pomme", 0.5), ("Kit de Crochetage", 0.15)]  # Kit à 15%
        },
        "endroits_creuser": 0,
        "image": "Images/nook.webp",
        "cout_gemmes": 0,
        "rarete": 0
    },
    {
        "nom": "Garage",
        "couleur": "bleue",
        "portes": {"up": False, "down": True, "left": False, "right": False},
        "loot": {
            "garanti": ["Clé", "Clé", "Marteau"],  # Marteau garanti
            "aleatoire": [("Clé", 0.4), ("Pièce d'Or", 0.3)]  # Probabilités augmentées
        },
        "endroits_creuser": 0,
        "image": "Images/garage.webp",
        "cout_gemmes": 1,
        "rarete": 1
    },
    {
        "nom": "Music Room",
        "couleur": "bleue",
        "portes": {"up": False, "down": True, "left": True, "right": False},
        "loot": {
            "garanti": ["Dé", "Dé"],  # Deux dés garantis
            "aleatoire": [("Pièce d'Or", 0.9), ("Dé", 0.4), ("Gemme", 0.2)]  # Probabilités augmentées
        },
        "endroits_creuser": 0,
        "image": "Images/musicroom.webp",
        "cout_gemmes": 1,
        "rarete": 1
    },
    {
        "nom": "Locker Room",
        "couleur": "bleue",
        "portes": {"up": True, "down": True, "left": False, "right": False},
        "loot": {
            "garanti": ["Pièce d'Or", "Clé", "Pelle"],  # Pelle garanti
            "aleatoire": [("Clé", 0.3), ("Kit de Crochetage", 0.25)]  # Kit à 25%
        },
        "endroits_creuser": 0,
        "image": "Images/lockerroom.webp",
        "cout_gemmes": 0,
        "rarete": 0
    },
    {
        "nom": "Den",
        "couleur": "bleue",
        "portes": {"up": False, "down": True, "left": True, "right": True},
        "loot": {
            "garanti": ["Gemme", "Gemme"],  # Deux gemmes garanties
            "aleatoire": [("Clé", 0.7), ("Patte de Lapin", 0.4), ("Détecteur de Métaux", 0.3)]  # Probabilités augmentées
        },
        "endroits_creuser": 0,
        "image": "Images/den.webp",
        "cout_gemmes": 2,
        "rarete": 2
    },
    {
        "nom": "Wine Cellar",
        "couleur": "bleue",
        "portes": {"up": False, "down": True, "left": False, "right": False},
        "loot": {
            "garanti": ["Gemme", "Gemme", "Banane"],  # Banane garantie
            "aleatoire": [("Gemme", 0.3), ("Banane", 0.5), ("Repas", 0.2)]  # Probabilités augmentées
        },
        "endroits_creuser": 0,
        "image": "Images/winecellar.webp",
        "cout_gemmes": 1,
        "rarete": 1
    },
    {
        "nom": "Trophy Room",
        "couleur": "dorée",
        "portes": {"up": False, "down": True, "left": True, "right": False},
        "loot": {
            "garanti": ["Gemme", "Gemme", "Gemme"],  # Trois gemmes garanties
            "aleatoire": [("Pièce d'Or", 0.6)],
            "magasin": [
                {"item": "Clé", "prix": 3},        # Prix réduits
                {"item": "Dé", "prix": 5},
                {"item": "Pomme", "prix": 1},
                {"item": "Kit de Crochetage", "prix": 15}  # Kit ajouté au magasin
            ]
        },
        "endroits_creuser": 0,
        "image": "Images/trophyroom.webp",
        "cout_gemmes": 2,
        "rarete": 2
    },
    {
        "nom": "Ballroom",
        "couleur": "blanche",
        "portes": {"up": True, "down": True, "left": False, "right": False},
        "loot": {
            "garanti": ["Gemme", "Gâteau"],  # Gâteau garanti
            "aleatoire": [("Pièce d'Or", 0.5), ("Gâteau", 0.3), ("Sandwich", 0.2)]  # Probabilités augmentées
        },
        "endroits_creuser": 0,
        "image": "Images/ballroom.webp",
        "cout_gemmes": 1,
        "rarete": 1
    },
    {
        "nom": "Pantry",
        "couleur": "verte",
        "portes": {"up": False, "down": False, "left": True, "right": True},
        "loot": {
            "garanti": ["Pièce d'Or", "Pièce d'Or", "Pièce d'Or", "Pièce d'Or", "Détecteur de Métaux"],  # Détecteur garanti
            "aleatoire": [("Banane", 0.5), ("Pomme", 0.7), ("Repas", 0.3)]  # Probabilités augmentées
        },
        "endroits_creuser": 1,
        "image": "Images/pantry.webp",
        "cout_gemmes": 0,
        "rarete": 0
    },
    {
        "nom": "Rumpus Room",
        "couleur": "bleue",
        "portes": {"up": True, "down": True, "left": False, "right": False},
        "loot": {
            "garanti": ["Pièce d'Or", "Pièce d'Or", "Pièce d'Or", "Pièce d'Or", "Dé"],  # Dé garanti
            "aleatoire": [("Pièce d'Or", 0.7), ("Dé", 0.4), ("Gemme", 0.3)]  # Probabilités augmentées
        },
        "endroits_creuser": 0,
        "image": "Images/rumpusroom.webp",
        "cout_gemmes": 1,
        "rarete": 1
    },
    {
        "nom": "Observatory",
        "couleur": "violette",
        "portes": {"up": False, "down": True, "left": True, "right": False},
        "loot": {
            "garanti": ["Kit de Crochetage"],  # Kit garanti
            "aleatoire": [("Gâteau", 0.3), ("Gemme", 0.4), ("Patte de Lapin", 0.35)]  # Probabilités augmentées
        },
        "endroits_creuser": 0,
        "image": "Images/observatory.webp",
        "cout_gemmes": 2,
        "rarete": 2
    },
    {
        "nom": "Library",
        "couleur": "brune",
        "portes": {"up": False, "down": True, "left": True, "right": False},
        "loot": {
            "garanti": ["Pièce d'Or", "Pièce d'Or"],  # Deux pièces garanties
            "aleatoire": [("Pièce d'Or", 0.3), ("Dé", 0.4), ("Sceau de Sécurité", 0.25)]  # Probabilités augmentées
        },
        "endroits_creuser": 0,
        "image": "Images/library.webp",
        "cout_gemmes": 1,
        "rarete": 1
    },
    {
        "nom": "Vault",
        "couleur": "dorée",
        "portes": {"up": False, "down": True, "left": False, "right": False},
        "loot": {
            "garanti": ["Pièce d'Or"] * 15,  # Plus de pièces
            "aleatoire": [("Gemme", 0.5)],
            "magasin": [
                {"item": "Pelle", "prix": 10},           # Prix fortement réduits
                {"item": "Marteau", "prix": 12},
                {"item": "Kit de Crochetage", "prix": 15},
                {"item": "Détecteur de Métaux", "prix": 20},
                {"item": "Patte de Lapin", "prix": 25}
            ]
        },
        "endroits_creuser": 0,
        "image": "Images/vault.webp",
        "cout_gemmes": 3,
        "rarete": 3
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
        "rarete": 0
    }
]