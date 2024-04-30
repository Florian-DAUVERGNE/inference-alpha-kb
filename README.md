# Projet : Système d'inférence de propositions logiques

Ce projet est un système d'inférence de propositions logiques basé sur la syntaxe de logique sémantique. Il permet aux utilisateurs de saisir des formules logiques en utilisant des symboles logiques, puis de déterminer si il existe une inférence entre les formules.

## Installation

1. Assurez-vous d'avoir Python 3 installé sur votre système.

2. Clonez ce dépôt

    ```
    git clone git@github.com:Florian-DAUVERGNE/inference-alpha-kb.git
    ```

 ou téléchargez les fichiers source.

![alt text]( https://bpb-us-e1.wpmucdn.com/sites.northwestern.edu/dist/b/3044/files/2021/05/github.png)


3. (Optionnel) Si vous préférez travailler dans un environnement virtuel, vous pouvez le créer en utilisant les étapes suivantes :
    ```
    python -m venv venv
    source venv/bin/activate  # Pour Linux/macOS
    .\venv\Scripts\activate   # Pour Windows
    ```

4. Installez les dépendances nécessaires en exécutant la commande suivante :
    ```
    pip install -r requirements.txt
    ```

## Utilisation

1. Exécutez le script principal en utilisant Python :
  ```
  python Inference.py #Python
  python3 Inference.py #Python3
  ```
2. Taper le nombre de formule dans votre base de connaissances(KB).

3. Entrez vos formules pour KB

4. Entrez votre formule pour alpha


## Exemple de Formule

```
Exemple KB |= α: KB1 = A | B, KB2 = ~C | A, alpha = A | B | C
Exemple KB /|= α: KB1 = A | B, KB2 = ~C | A, alpha = A & C
```

## Structure du Projet

- `AnalyseurSyntaxique.py` : Code du projet `verificateur-syntaxique`. Utilisé pour la saisie des formules de KB et alpha
- `Grammaire.py` : Contient le lexer et le parser PLY pour analyser les formules logiques.
-`Inference.py` : Le script principal qui gère l'interaction avec l'utilisateur et le système d'inférence de propositions.

## Bibliothèque
ply : https://github.com/dabeaz/ply

terminaltables : https://pypi.org/project/terminaltables/

## Ressources
Logic and Reasoning R&N 7-9 : https://www.cs.cmu.edu/afs/cs/academic/class/15381-s07/www/slides/022707reasoning.pdf

Équivalence logique : https://fr.wikipedia.org/wiki/%C3%89quivalence_logique

Implication (logique) : https://fr.wikipedia.org/wiki/Implication_(logique)

## Lien vers l'ancien repertoire GitHub
https://github.com/Florian-DAUVERGNE/evaluateur_de_propositions
