# Projet POO - Blue Prince (M1 IPS)

Implémentation du jeu "Blue Prince" en Python et Pygame dans le cadre de l'UE de Programmation Orientée Objet (Responsable : Louis ANNABI).

### Membres du Groupe
* Jeanne LAKITS
* Maxence DEMANGE--ROCHE
* Alen GREBENC

---

## 🚀 Installation et Lancement

Ce projet nécessite Python 3.10+ et les dépendances listées dans `requirements.txt`.

### 1. Installation
1.  Clonez ce dépôt Git (ou téléchargez les fichier ZIP).
    ```bash
    git clone https://github.com/maxenceeeeee/JeuPython.git
    cd JeuPython
    ```


3.  Installez les dépendances requises :
    ```bash
    pip install -r requirements.txt
    ```

### 2. Lancement
Pour démarrer le jeu, exécutez `main.py` :
```bash
python main.py
```

## 🎮 Comment Jouer

### Objectif
L'objectif est de traverser le manoir en partant de la pièce "Entrance Hall" (située en bas au centre de la grille) pour atteindre la pièce "Antichambre" (située en haut au centre).

La partie est gagnée si vous atteignez l'Antichambre. La partie est perdue si votre compteur de Pas (👣) tombe à 0.

### Commandes
##### ZQSD : Se déplacer dans le manoir (Haut, Gauche, Bas, Droit). Le déplacement d'une pièce à l'autre coûte 1 Pas.

### Découverte de Pièces
Lorsque vous ouvrez une porte vers une case vide (noire), le jeu se met en pause et vous propose 3 nouvelles pièces au choix.

##### Touches 1, 2, 3 : Choisir la pièce que vous souhaitez placer.

Certaines pièces coûtent des Gemmes (💎) pour être choisies. Ce coût est indiqué sur la carte de sélection.

##### Touche R : Dépenser un Dé (🎲) pour relancer le tirage des 3 pièces.


Portes Verrouillées
Les portes peuvent être verrouillées (Niveau 1 ou 2).

Ouvrir une porte verrouillée consomme 1 Clé (🔑).

Si vous possédez le Kit de Crochetage, vous pouvez ouvrir les portes de Niveau 1 sans dépenser de clé. Le kit ne fonctionne pas sur le Niveau 2.
