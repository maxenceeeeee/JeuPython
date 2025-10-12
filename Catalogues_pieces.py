## catalogues de pieces avec les définitions
CATALOGUE_PIECES  = [
    {
        "nom": "The Foundation",
        "couleur": "bleue",
        "portes": {"haut": False, "bas": False, "gauche": True, "droite": True},
        "cout_gemmes": 0,
        "objets": ["levier d'ascenseur", "planches", "pierres", "emplacements de fouille"],
        "effet": "Point d'accès au sous-sol via un ascenseur activable",
        "rarete": 1,
        "condition_placement": "zones intérieures",
        "image_path": "assets/rooms/the_foundation.png",
        "secrets": [
            "Permet l'accès initial au sous-sol",
            "Ascenseur bloqué au départ, nécessite levier",
            "Contient 2-5 emplacements de fouille",
            "Après activation, l'ascenseur mène au sous-sol"
        ]
    },
    {
        "nom": "Entrance Hall",
        "couleur": "bleue",
        "portes": {"haut": True, "bas": False, "gauche": True, "droite": True},
        "cout_gemmes": 0,
        "objets": ["lettre", "plan", "allowance token", "coffres verrouillés"],
        "effet": "Point de départ du joueur, contient table centrale et objets interactifs",
        "rarete": 0,
        "condition_placement": "centre du rang 1",
        "image_path": "assets/rooms/entrance_hall.png",
        "secrets": [
            "Vase de droite : Microchip B si brisé avec Sledgehammer",
            "Blessing of the Monk : drafter l’Outer Room version",
            "Twin Constellation : deux coffres verrouillés apparaissent"
        ]
    },
    {
        "nom": "Spare Room",
        "couleur": "bleue",
        "portes": {"haut": True, "bas": False, "gauche": True, "droite": True},
        "cout_gemmes": 1,
        "objets": ["lit", "armoire", "coffre verrouillé"],
        "effet": "Salle supplémentaire pouvant stocker des objets",
        "rarete": 0,
        "condition_placement": "adjacent à Hall",
        "image_path": "assets/rooms/spare_room.png",
        "secrets": ["Coffre secret derrière l’armoire"]
    },
    {
        "nom": "Rotunda",
        "couleur": "bleue",
        "portes": {"haut": True, "bas": True, "gauche": True, "droite": True},
        "cout_gemmes": 2,
        "objets": ["statue", "plantes décoratives"],
        "effet": "Salle centrale circulaire pour navigation et esthétique",
        "rarete": 1,
        "condition_placement": "centre du manoir",
        "image_path": "assets/rooms/rotunda.png",
        "secrets": []
    },
    {
        "nom": "Parlor",
        "couleur": "bleue",
        "portes": {"haut": True, "bas": False, "gauche": True, "droite": True},
        "cout_gemmes": 1,
        "objets": ["canapés", "cheminée", "table basse"],
        "effet": "Salle de détente offrant bonus de moral",
        "rarete": 0,
        "condition_placement": "près de Hall ou Rotunda",
        "image_path": "assets/rooms/parlor.png",
        "secrets": []
    },
    {
        "nom": "Billiard Room",
        "couleur": "bleue",
        "portes": {"haut": True, "bas": True, "gauche": True, "droite": False},
        "cout_gemmes": 2,
        "objets": ["table de billard", "queues", "boules"],
        "effet": "Divertissement, augmente moral et interaction sociale",
        "rarete": 1,
        "condition_placement": "adjacent à Parlor",
        "image_path": "assets/rooms/billiard_room.png",
        "secrets": ["Tiroir secret sous la table de billard"]
    },
    {
        "nom": "Gallery",
        "couleur": "bleue",
        "portes": {"haut": True, "bas": False, "gauche": True, "droite": True},
        "cout_gemmes": 1,
        "objets": ["tableaux", "sculptures", "coffres"],
        "effet": "Salle d’exposition, peut contenir objets rares",
        "rarete": 1,
        "condition_placement": "adjacent à Rotunda",
        "image_path": "assets/rooms/gallery.png",
        "secrets": ["Coffre caché derrière tableau"]
    },
    {
        "nom": "Room 8",
        "couleur": "bleue",
        "portes": {"haut": False, "bas": True, "gauche": True, "droite": True},
        "cout_gemmes": 1,
        "objets": ["lit", "armoire", "coffre"],
        "effet": "Chambre secondaire pouvant stocker objets et gemmes",
        "rarete": 0,
        "condition_placement": "étage supérieur",
        "image_path": "assets/rooms/room_8.png",
        "secrets": []
    },
    {
        "nom": "Closet",
        "couleur": "bleue",
        "portes": {"haut": False, "bas": True, "gauche": False, "droite": True},
        "cout_gemmes": 0,
        "objets": ["vêtements", "coffre"],
        "effet": "Petit espace de rangement",
        "rarete": 0,
        "condition_placement": "adjacent à chambre",
        "image_path": "assets/rooms/closet.png",
        "secrets": ["Coffre caché derrière vêtements"]
    },
    {
        "nom": "Walk-in Closet",
        "couleur": "bleue",
        "portes": {"haut": False, "bas": True, "gauche": True, "droite": False},
        "cout_gemmes": 1,
        "objets": ["vêtements", "chaussures", "coffre"],
        "effet": "Grand espace de rangement",
        "rarete": 1,
        "condition_placement": "proche des chambres principales",
        "image_path": "assets/rooms/walk_in_closet.png",
        "secrets": []
    },
    {
        "nom": "Attic",
        "couleur": "bleue",
        "portes": {"haut": False, "bas": True, "gauche": False, "droite": True},
        "cout_gemmes": 2,
        "objets": ["caisses", "objets anciens", "coffres"],
        "effet": "Stockage secondaire, objets rares possibles",
        "rarete": 1,
        "condition_placement": "au sommet du manoir",
        "image_path": "assets/rooms/attic.png",
        "secrets": ["Objets rares cachés sous les caisses"]
    },
    {
        "nom": "Storeroom",
        "couleur": "bleue",
        "portes": {"haut": True, "bas": False, "gauche": True, "droite": True},
        "cout_gemmes": 1,
        "objets": ["caisses", "sacs", "coffres verrouillés"],
        "effet": "Salle de stockage principale",
        "rarete": 1,
        "condition_placement": "adjacent aux cuisines ou hall",
        "image_path": "assets/rooms/storeroom.png",
        "secrets": ["Coffre rare derrière les caisses"]
    },
    {
        "nom": "Nook",
        "couleur": "bleue",
        "portes": {"haut": False, "bas": False, "gauche": True, "droite": True},
        "cout_gemmes": 0,
        "objets": ["clé", "flyer"],
        "effet": "contient une clé sur la table principale",
        "rarete": 0,  # common / Blueprint
        "condition_placement": "",
        "image_path": "assets/rooms/nook.png",
        "secrets": []
    },
    {
        "nom": "Garage",
        "couleur": "bleue",
        "portes": {"haut": False, "bas": True, "gauche": True, "droite": False},
        "cout_gemmes": None,
        "objets": ["3 clés murales", "voiture", "coffre dans le coffre de la voiture"],
        "effet": "Dead End, accès via le carport si l’électricité est activée",
        "rarete": 1,  # unusual
        "condition_placement": "côté ouest",
        "image_path": "assets/rooms/garage.png",
        "secrets": [
            "Trunk contient un upgrade disk",
            "Peut être drafté uniquement à l’ouest du manoir"
        ]
    },
    {
        "nom": "Music Room",
        "couleur": "bleue",
        "portes": {"haut": False, "bas": False, "gauche": True, "droite": True},
        "cout_gemmes": None,
        "objets": ["clé spéciale", "clé normale", "feuilles de musique (4)"],
        "effet": "contient des partitions musicales et des clés",
        "rarete": 0,
        "condition_placement": "",
        "image_path": "assets/rooms/music_room.png",
        "secrets": []
    },
    {
        "nom": "Locker Room",
        "couleur": "bleue",
        "portes": {"haut": False, "bas": True, "gauche": True, "droite": False},
        "cout_gemmes": None,
        "objets": ["casier (certains ouvrables)", "pièces, gemmes ou objets", "clé dans certains casiers"],
        "effet": "répartit des clés dans la maison (Spread Keys)",
        "rarete": 1,  # Rare
        "condition_placement": "nécessite que Pool ait été drafté",
        "image_path": "assets/rooms/locker_room.png",
        "secrets": []
    },
    {
        "nom": "Den",
        "couleur": "bleue",
        "portes": {"haut": True, "bas": True, "gauche": False, "droite": False},
        "cout_gemmes": 0,
        "objets": ["gemme", "coffre verrouillé (parfois)"],
        "effet": "contient toujours une gemme, peut générer un coffre verrouillé",
        "rarete": 0,
        "condition_placement": "",
        "image_path": "assets/rooms/den.png",
        "secrets": []
    },
    {
        "nom": "Wine Cellar",
        "couleur": "bleue",
        "portes": {"haut": False, "bas": True, "gauche": False, "droite": True},
        "cout_gemmes": 0,
        "objets": ["3 gemmes"],
        "effet": "Dead End room, contient 3 gemmes, peut générer un dig spot",
        "rarete": 0,
        "condition_placement": "",
        "image_path": "assets/rooms/wine_cellar.png",
        "secrets": []
    },
    {
        "nom": "Trophy Room",
        "couleur": "bleue",
        "portes": {"haut": False, "bas": False, "gauche": True, "droite": True},
        "cout_gemmes": None,
        "objets": ["8 gemmes", "trophées exposés"],
        "effet": "musée de trophées, contient 8 gemmes",
        "rarete": 0,
        "condition_placement": "",
        "image_path": "assets/rooms/trophy_room.png",
        "secrets": []
    },
    {
        "nom": "Ballroom",
        "couleur": "bleue",
        "portes": {"haut": True, "bas": False, "gauche": False, "droite": True},
        "cout_gemmes": None,
        "objets": ["partition musicale", "autres objets"],
        "effet": "Quand on entre, le nombre de gemmes est fixé à 2",
        "rarete": 1,  # unusual
        "condition_placement": "",
        "image_path": "assets/rooms/ballroom.png",
        "secrets": []
    },
    {
        "nom": "Pantry",
        "couleur": "bleue",
        "portes": {"haut": False, "bas": False, "gauche": True, "droite": True},
        "cout_gemmes": 0,
        "objets": ["fruit aléatoire", "4 pièces"],
        "effet": "",
        "rarete": 0,
        "condition_placement": "",
        "image_path": "assets/rooms/pantry.png",
        "secrets": []
    },
    {
        "nom": "Rumpus Room",
        "couleur": "bleue",
        "portes": {"haut": True, "bas": False, "gauche": True, "droite": False},
        "cout_gemmes": None,
        "objets": ["8 pièces", "Alzara (machine de divination)"],
        "effet": "Permet de payer 1 pièce pour voir une coupe d’indices (Alzara)",
        "rarete": 0,
        "condition_placement": "",
        "image_path": "assets/rooms/rumpus_room.png",
        "secrets": []
    },
    {
        "nom": "??",  # pour la pièce 024 selon le listing
        "couleur": "bleue",
        "portes": {"haut": False, "bas": False, "gauche": False, "droite": False},
        "cout_gemmes": None,
        "objets": [],
        "effet": "",
        "rarete": 0,
        "condition_placement": "",
        "image_path": "",
        "secrets": []
    },
    {
        "nom": "Nook",
        "couleur": "bleue",
        "portes": {"haut": None, "bas": None, "gauche": None, "droite": None},
        "cout_gemmes": 0,
        "objets": ["clé", "flyer"],
        "effet": "Contient une clé sur la table principale",
        "rarete": 0,
        "condition_placement": None,
        "image_path": "assets/rooms/nook.png",
        "secrets": []
    },

    # 014
    {
        "nom": "Garage",
        "couleur": "bleue",
        "portes": {"haut": None, "bas": None, "gauche": None, "droite": None},
        "cout_gemmes": None,
        "objets": ["voiture", "trunk (coffre de voiture)"],
        "effet": "Dead End ; parfois contient un coffre dans la voiture",
        "rarete": 1,
        "condition_placement": "côté extérieur (ouest) possible",
        "image_path": "assets/rooms/garage.png",
        "secrets": ["Coffre dans le trunk peut contenir un upgrade disk"]
    },

    # 015
    {
        "nom": "Music Room",
        "couleur": "bleue",
        "portes": {"haut": None, "bas": None, "gauche": None, "droite": None},
        "cout_gemmes": None,
        "objets": ["partitions (feuilles de musique)", "clés (parfois)"],
        "effet": "Contient partitions musicales et potentiellement des clés",
        "rarete": 0,
        "condition_placement": None,
        "image_path": "assets/rooms/music_room.png",
        "secrets": []
    },

    # 016
    {
        "nom": "Locker Room",
        "couleur": "bleue",
        "portes": {"haut": None, "bas": None, "gauche": None, "droite": None},
        "cout_gemmes": None,
        "objets": ["casiers (certains ouvrables)", "pièces/gemmes/objets dans certains cas"],
        "effet": "Peut répartir des clés/objets (Spread Keys)",
        "rarete": 1,
        "condition_placement": None,
        "image_path": "assets/rooms/locker_room.png",
        "secrets": []
    },

    # 017
    {
        "nom": "Den",
        "couleur": "bleue",
        "portes": {"haut": None, "bas": None, "gauche": None, "droite": None},
        "cout_gemmes": 0,
        "objets": ["gemme", "coffre verrouillé (parfois)"],
        "effet": "Contient toujours une gemme, parfois un coffre verrouillé",
        "rarete": 0,
        "condition_placement": None,
        "image_path": "assets/rooms/den.png",
        "secrets": []
    },

    # 018
    {
        "nom": "Wine Cellar",
        "couleur": "bleue",
        "portes": {"haut": None, "bas": None, "gauche": None, "droite": None},
        "cout_gemmes": 0,
        "objets": ["3 gemmes", "possibilité de dig spot"],
        "effet": "Dead End ; contient 3 gemmes et peut générer un dig spot",
        "rarete": 0,
        "condition_placement": None,
        "image_path": "assets/rooms/wine_cellar.png",
        "secrets": []
    },

    # 019
    {
        "nom": "Trophy Room",
        "couleur": "bleue",
        "portes": {"haut": None, "bas": None, "gauche": None, "droite": None},
        "cout_gemmes": None,
        "objets": ["trophées", "8 gemmes"],
        "effet": "Salle d’exposition de trophées ; contient 8 gemmes",
        "rarete": 0,
        "condition_placement": None,
        "image_path": "assets/rooms/trophy_room.png",
        "secrets": []
    },

    # 020
    {
        "nom": "Ballroom",
        "couleur": "bleue",
        "portes": {"haut": None, "bas": None, "gauche": None, "droite": None},
        "cout_gemmes": None,
        "objets": ["partitions musicales", "objets divers"],
        "effet": "À l'entrée le nombre de gemmes peut être fixé (ex. 2) selon scenario",
        "rarete": 1,
        "condition_placement": None,
        "image_path": "assets/rooms/ballroom.png",
        "secrets": []
    },

    # 021
    {
        "nom": "Pantry",
        "couleur": "bleue",
        "portes": {"haut": None, "bas": None, "gauche": None, "droite": None},
        "cout_gemmes": 0,
        "objets": ["fruit aléatoire", "4 pièces (parfois)"],
        "effet": "",
        "rarete": 0,
        "condition_placement": None,
        "image_path": "assets/rooms/pantry.png",
        "secrets": []
    },

    # 022
    {
        "nom": "Rumpus Room",
        "couleur": "bleue",
        "portes": {"haut": None, "bas": None, "gauche": None, "droite": None},
        "cout_gemmes": None,
        "objets": ["8 pièces", "Alzara (machine de divination)"],
        "effet": "Permet de payer pour obtenir des indices via Alzara",
        "rarete": 0,
        "condition_placement": None,
        "image_path": "assets/rooms/rumpus_room.png",
        "secrets": []
    },

    # 023
    {
        "nom": "Vault",
        "couleur": "bleue",
        "portes": {"haut": None, "bas": None, "gauche": None, "droite": None},
        "cout_gemmes": None,
        "objets": ["coffres/gemmes (très riche)"],
        "effet": "Salle très lucrative en gemmes/objets",
        "rarete": 1,
        "condition_placement": None,
        "image_path": "assets/rooms/vault.png",
        "secrets": []
    },

    # 024
    {
        "nom": "Office",
        "couleur": "bleue",
        "portes": {"haut": None, "bas": None, "gauche": None, "droite": None},
        "cout_gemmes": None,
        "objets": ["bureau", "documents", "objets de bureau"],
        "effet": "",
        "rarete": 0,
        "condition_placement": None,
        "image_path": "assets/rooms/office.png",
        "secrets": []
    },

    # 025
    {
        "nom": "Drawing Room",
        "couleur": "bleue",
        "portes": {"haut": None, "bas": None, "gauche": None, "droite": None},
        "cout_gemmes": None,
        "objets": [],
        "effet": None,
        "rarete": None,
        "condition_placement": None,
        "image_path": "assets/rooms/drawing_room.png",
        "secrets": []
    },

    # 026
    {
        "nom": "Study",
        "couleur": "bleue",
        "portes": {"haut": None, "bas": None, "gauche": None, "droite": None},
        "cout_gemmes": None,
        "objets": [],
        "effet": None,
        "rarete": None,
        "condition_placement": None,
        "image_path": "assets/rooms/study.png",
        "secrets": []
    },

    # 027
    {
        "nom": "Library",
        "couleur": "bleue",
        "portes": {"haut": None, "bas": None, "gauche": None, "droite": None},
        "cout_gemmes": None,
        "objets": ["livres", "indices écrits"],
        "effet": "Pièce d’information ; peut garantir certains drafts (selon upgrade)",
        "rarete": None,
        "condition_placement": None,
        "image_path": "assets/rooms/library.png",
        "secrets": []
    },

    # 028
    {
        "nom": "Chamber of Mirrors",
        "couleur": "bleue",
        "portes": {"haut": None, "bas": None, "gauche": None, "droite": None},
        "cout_gemmes": None,
        "objets": ["miroirs", "objets réfléchis"],
        "effet": None,
        "rarete": None,
        "condition_placement": None,
        "image_path": "assets/rooms/chamber_of_mirrors.png",
        "secrets": []
    },

    # 029
    {
        "nom": "The Pool",
        "couleur": "bleue",
        "portes": {"haut": None, "bas": None, "gauche": None, "droite": None},
        "cout_gemmes": None,
        "objets": ["eau", "pompe (selon état)"],
        "effet": None,
        "rarete": None,
        "condition_placement": None,
        "image_path": "assets/rooms/the_pool.png",
        "secrets": []
    },

    # 030
    {
        "nom": "Drafting Studio",
        "couleur": "bleue",
        "portes": {"haut": None, "bas": None, "gauche": None, "droite": None},
        "cout_gemmes": None,
        "objets": ["plans", "blueprints"],
        "effet": "Influence sur le pool de draft (atelier de plans)",
        "rarete": None,
        "condition_placement": None,
        "image_path": "assets/rooms/drafting_studio.png",
        "secrets": []
    },

    # 031
    {
        "nom": "Utility Closet",
        "couleur": "bleue",
        "portes": {"haut": None, "bas": None, "gauche": None, "droite": None},
        "cout_gemmes": None,
        "objets": ["outils", "pièces"],
        "effet": "Petit local utilitaire",
        "rarete": None,
        "condition_placement": None,
        "image_path": "assets/rooms/utility_closet.png",
        "secrets": []
    },

    # 032
    {
        "nom": "Boiler Room",
        "couleur": "bleue",
        "portes": {"haut": None, "bas": None, "gauche

