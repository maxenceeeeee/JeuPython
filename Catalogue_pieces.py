
"""
Dictionnaire d'un qunizaine de pièces représentatives du jeu.
On ignore les effets et les couleurs des pièces, on se concentre sur ses items.

"""
catalogue_pieces = [
    {
        "nom": "Entrance Hall",
        "couleur": "bleue",
        "portes": {"haut": True, "bas": False, "gauche": True, "droite": True},
        "items": ["lettre", "plan", "allowance token"]
    },
    {
        "nom": "The Foundation",
        "couleur": "grise",
        "portes": {"haut": True, "bas": True, "gauche": False, "droite": False},
        "items": ["pierre ancienne", "blueprint part"]
    },
    {
        "nom": "Nook",
        "couleur": "bleue",
        "portes": {"haut": False, "bas": False, "gauche": True, "droite": True},
        "items": ["clé", "note noire", "livre"]
    },
    {
        "nom": "Garage",
        "couleur": "bleue",
        "portes": {"haut": False, "bas": True, "gauche": True, "droite": False},
        "items": ["voiture", "clé", "coffre dans le coffre"]
    },
    {
        "nom": "Music Room",
        "couleur": "bleue",
        "portes": {"haut": False, "bas": False, "gauche": True, "droite": True},
        "items": ["partitions", "clé spéciale"]
    },
    {
        "nom": "Locker Room",
        "couleur": "bleue",
        "portes": {"haut": False, "bas": True, "gauche": True, "droite": False},
        "items": ["casiers", "clé", "pièces"]
    },
    {
        "nom": "Den",
        "couleur": "bleue",
        "portes": {"haut": True, "bas": True, "gauche": False, "droite": False},
        "items": ["gemme", "coffre verrouillé"]
    },
    {
        "nom": "Wine Cellar",
        "couleur": "bleue",
        "portes": {"haut": False, "bas": True, "gauche": False, "droite": True},
        "items": ["bouteilles", "gemmes"]
    },
    {
        "nom": "Trophy Room",
        "couleur": "dorée",
        "portes": {"haut": False, "bas": False, "gauche": True, "droite": True},
        "items": ["trophées", "gemmes"]
    },
    {
        "nom": "Ballroom",
        "couleur": "blanche",
        "portes": {"haut": True, "bas": False, "gauche": False, "droite": True},
        "items": ["lustre", "partition", "clé de scène"]
    },
    {
        "nom": "Pantry",
        "couleur": "verte",
        "portes": {"haut": False, "bas": False, "gauche": True, "droite": True},
        "items": ["fruit", "pièces"]
    },
    {
        "nom": "Rumpus Room",
        "couleur": "bleue",
        "portes": {"haut": True, "bas": False, "gauche": True, "droite": False},
        "items": ["machine Alzara", "pièces"]
    },
    {
        "nom": "Observatory",
        "couleur": "violette",
        "portes": {"haut": True, "bas": False, "gauche": True, "droite": True},
        "items": ["télescope", "constellation map"]
    },
    {
        "nom": "Library",
        "couleur": "brune",
        "portes": {"haut": True, "bas": False, "gauche": True, "droite": True},
        "items": ["livres", "note de recherche"]
    },
    {
        "nom": "Vault",
        "couleur": "dorée",
        "portes": {"haut": False, "bas": False, "gauche": True, "droite": False},
        "items": ["coffre-fort", "gemmes", "clés"]
    }
]

