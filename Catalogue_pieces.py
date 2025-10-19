
"""
Dictionnaire de 15 pièces représentatives du jeu, avec nom, couleur, portes et items.
"""

catalogue_pieces = [
    {
        "nom": "Entrance Hall",
        "couleur": "bleue",
        "portes": {"haut": True, "bas": False, "gauche": True, "droite": True},
        "items": ["lettre", "plan", "allowance token"],
        "image" : "Images/entrancehall.webp"
    },
    {
        "nom": "The Foundation",
        "couleur": "grise",
        "portes": {"haut": True, "bas": True, "gauche": False, "droite": False},
        "items": ["pierre ancienne", "blueprint part"],
        "image" : "Images/foundation.webp"
    },
    {
        "nom": "Nook",
        "couleur": "bleue",
        "portes": {"haut": False, "bas": False, "gauche": True, "droite": True},
        "items": ["clé", "note noire", "livre"],
        "image" : "Images/nook.webp"
    },
    {
        "nom": "Garage",
        "couleur": "bleue",
        "portes": {"haut": False, "bas": True, "gauche": True, "droite": False},
        "items": ["voiture", "clé", "coffre dans le coffre"],
        "image" : "Images/garage.webp"
    },
    {
        "nom": "Music Room",
        "couleur": "bleue",
        "portes": {"haut": False, "bas": False, "gauche": True, "droite": True},
        "items": ["partitions", "clé spéciale"],
        "image" : "Images/musicroom.webp"
    },
    {
        "nom": "Locker Room",
        "couleur": "bleue",
        "portes": {"haut": False, "bas": True, "gauche": True, "droite": False},
        "items": ["casiers", "clé", "pièces"],
        "image" : "Images/lockerroom.webp"
    },
    {
        "nom": "Den",
        "couleur": "bleue",
        "portes": {"haut": True, "bas": True, "gauche": False, "droite": False},
        "items": ["gemme", "coffre verrouillé"],
        "image" : "Images/den.webp"
    },
    {
        "nom": "Wine Cellar",
        "couleur": "bleue",
        "portes": {"haut": False, "bas": True, "gauche": False, "droite": True},
        "items": ["bouteilles", "gemmes"],
        "image" : "Images/winecellar.webp"
    },
    {
        "nom": "Trophy Room",
        "couleur": "dorée",
        "portes": {"haut": False, "bas": False, "gauche": True, "droite": True},
        "items": ["trophées", "gemmes"],
        "image" : "Images/trophyroom.webp"
    },
    {
        "nom": "Ballroom",
        "couleur": "blanche",
        "portes": {"haut": True, "bas": False, "gauche": False, "droite": True},
        "items": ["lustre", "partition", "clé de scène"],
        "image" : "Images/ballroom.webp"
    },
    {
        "nom": "Pantry",
        "couleur": "verte",
        "portes": {"haut": False, "bas": False, "gauche": True, "droite": True},
        "items": ["fruit", "pièces"],
        "image" : "Images/pantry.webp"
    },
    {
        "nom": "Rumpus Room",
        "couleur": "bleue",
        "portes": {"haut": True, "bas": False, "gauche": True, "droite": False},
        "items": ["machine Alzara", "pièces"],
        "image" : "Images/rumpusroom.webp"
    },
    {
        "nom": "Observatory",
        "couleur": "violette",
        "portes": {"haut": True, "bas": False, "gauche": True, "droite": True},
        "items": ["télescope", "constellation map"],
        "image" : "Images/observatory.webp"
    },
    {
        "nom": "Library",
        "couleur": "brune",
        "portes": {"haut": True, "bas": False, "gauche": True, "droite": True},
        "items": ["livres", "note de recherche"],
        "image" : "Images/library.webp"
    },
    {
        "nom": "Vault",
        "couleur": "dorée",
        "portes": {"haut": False, "bas": False, "gauche": True, "droite": False},
        "items": ["coffre-fort", "gemmes", "clés"],
        "image" : "Images/vault.webp"
    },
    
    {
        "nom": "Antechamber",
        "couleur": "bleue",
        "portes": {"haut": False, "bas": False, "gauche": True, "droite": False},
        "items": [],
        "image" : "Images/antechamber.webp"
    }
]
