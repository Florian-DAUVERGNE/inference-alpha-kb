import itertools
import re
from AnalyseurSyntaxique import (
    convertir_mots_en_symboles,
    analyser_formule,
    afficher_aide,
)
from terminaltables import AsciiTable


def convertir_formule(formule):
    """
    Convertir l'implication (>>) en formule avec des opérateurs logiques
    Source : https://fr.wikipedia.org/wiki/Implication_(logique)#Sous_forme_implicative
    """
    formule_sans_implication = re.sub(
        r"(\([^()]*\)|[A-Za-z])\s*>>\s*(\([^()]*\)|[A-Za-z])", r"(~\1 | \2)", formule
    )

    """ 
    Convertir l'équivalence (=) en formule avec des opérateurs logiques 
    Source : https://fr.wikipedia.org/wiki/%C3%89quivalence_logique#Calcul_propositionnel
    """
    formule_sans_equivalence = re.sub(
        r"(\([^()]*\)|[A-Za-z])\s*=\s*(\([^()]*\)|[A-Za-z])",
        r"((\1 & \2) | (~\1 & ~\2))",
        formule_sans_implication,
    )
    return formule_sans_equivalence


def evaluer_expression(expression, variables, valeurs_variables):
    """
    Évalue une expression booléenne avec des variables et des valeurs données.
    """
    # Remplace chaque variable par sa valeur correspondante dans l'expression
    for variable, valeur in zip(variables, valeurs_variables):
        expression = expression.replace(variable, str(valeur))

    # Remplace les opérateurs logiques par leurs équivalents Python
    expression = (
        expression.replace("&", " and ").replace("|", " or ").replace("~", " not ")
    )

    # Évalue l'expression avec la fonction eval()
    resultat = eval(expression)

    # Retourne le résultat de l'évaluation
    return int(resultat)


def generer_table_de_verite(expression):
    """
    Génère une table de vérité pour une expression booléenne donnée.
    """
    # Sauvegarde de l'expression originale pour affichage
    expression_originelle = expression

    # Si l'expression contient des opérateurs logiques spéciaux, les convertir
    if ">>" in expression or "=" in expression:
        expression = convertir_formule(expression)

    # Trouver les variables dans l'expression
    variables = sorted(set(re.findall(r"[A-Za-z]", expression)))
    num_variables = len(variables)

    # Générer toutes les combinaisons de valeurs de vérité pour les variables
    combinations_variables = list(itertools.product([0, 1], repeat=num_variables))

    # Créer la table de vérité
    table_de_verite = []
    for valeur_variable in combinations_variables:
        # Convertir les valeurs de vérité en liste et évaluer l'expression pour chaque combinaison
        valeurs_verite = list(valeur_variable)
        valeurs_verite.append(
            evaluer_expression(expression, variables, valeur_variable)
        )
        table_de_verite.append(valeurs_verite)

    # Titres des colonnes de la table (variables + expression)
    titre_des_colonnes = variables[:]
    titre_des_colonnes.append(expression_originelle)

    # Afficher la table de vérité avec AsciiTable
    print(AsciiTable([titre_des_colonnes] + table_de_verite).table)

    return table_de_verite


def generer_tables_de_verite_commune(tables_de_verite, expression):
    """
    Combine plusieurs tables de vérité en une seule en utilisant une expression commune.
    """
    # Trouver le nombre maximal de lignes parmi les tables de vérité
    nbr_lignes = max(len(table) for table in tables_de_verite)

    # Trouver les variables dans l'expression
    variables = sorted(set(re.findall(r"[A-Za-z]", expression)))

    # Initialiser une liste pour les tables de vérité combinées
    tables_combinees = []

    # Pour chaque ligne dans la table de vérité
    for i in range(nbr_lignes):
        # Sélectionner la valeur de vérité de la i-ème ligne pour chaque table
        valeurs_combinees = [table[i % len(table)] for table in tables_de_verite]

        # Ajouter les valeurs de vérité combinées à la table de vérité combinée
        tables_combinees.append(valeurs_combinees)

    return tables_combinees


import re


def demontrer_theoreme(
    table_de_verite_KB, table_de_verite_alpha, expressions_KB, expressions_alpha
):
    """
    Démontre si l'expression alpha est conséquence logique de l'ensemble de clauses KB.
    """
    # Combinaison des tables de vérité de KB et alpha en utilisant l'expression alpha
    table_de_verite_alpha = generer_tables_de_verite_commune(
        [table_de_verite_KB, table_de_verite_alpha], expressions_alpha
    )

    # Trouver les variables de KB et alpha
    variables_KB = sorted(set(re.findall(r"[A-Za-z]", expressions_KB)))
    variables_alpha = sorted(set(re.findall(r"[A-Za-z]", expressions_alpha)))

    # Fusionner les variables de KB et alpha sans doublons
    variables_KB = list(set(variables_KB + variables_alpha))

    # Initialisation de la table de vérité combinée
    table_de_verite_combinee = []

    # Pour chaque ligne dans la table de vérité de KB
    for lignes in table_de_verite_KB:
        # Sélectionner les valeurs de vérité correspondantes pour les variables alpha
        valeurs_alpha = [
            lignes[variables_KB.index(variables_alpha[i])]
            for i in range(len(variables_alpha))
        ]
        # Ajouter les valeurs de vérité de KB et alpha à la table de vérité combinée
        table_de_verite_combinee.append(valeurs_alpha + [lignes[-1]])

    # Trier les tables de vérité combinées selon les valeurs de vérité des variables alpha
    table_de_verite_combinee = sorted(table_de_verite_combinee, key=lambda x: x[:-1])
    table_de_verite_alpha = sorted(table_de_verite_alpha, key=lambda x: x[:-1])

    # Comparer les tables de vérité combinées et alpha pour vérifier la conséquence logique
    for kb, alpha in zip(table_de_verite_combinee, table_de_verite_alpha):
        if kb[-1] == 1 and alpha[-1] == 0:
            print("KB /|= α")  # KB n'implique pas alpha
            return
    print("KB |= α")  # KB implique alpha


def gestion_saisie(i, composant):
    """
    Gère la saisie de formules logiques pour Alpha et les composants de KB.
    """
    # Si le composant est "alpha"
    if composant == "alpha":
        # Demande à l'utilisateur d'entrer la formule de Alpha
        saisie = input(f"Entrez la formule de Alpha : ")
        # Vérifie si aucune saisie n'a été effectuée
        if not saisie:
            return False
        # Retourne la saisie
        return saisie

    # Pour les composants de KB
    # Demande à l'utilisateur d'entrer la formule i de KB
    saisie = input(f"Entrez la formule {i} de KB : ")
    # Vérifie si aucune saisie n'a été effectuée
    if not saisie:
        return False
    # Retourne la saisie
    return saisie


def verifier_formule(formule):
    """
    Vérifie si une formule logique est correcte en utilisant l'analyseur de formules.
    """
    # Convertit les mots en symboles et analyse la formule
    if analyser_formule(convertir_mots_en_symboles(formule)):
        # Si la formule est correcte, affiche un message
        print("Formule correcte : {}".format(formule))
    else:
        # Si la formule est incorrecte, affiche un message et quitte le programme
        print("Formule incorrecte : {}".format(formule))
        quit()


# Affiche l'aide
afficher_aide()

# Initialisation du compteur de formules

nb_formules = 0

while nb_formules <= 0:
    try:
        nb_formules = int(input("Entrer le nombre de formules pour KB: "))
        if nb_formules <= 0:
            print("Veuillez entrer un nombre supérieur à 0")
    except ValueError:
        print("Veuillez entrer un nombre")



i = 1
# Saisie de la première formule pour KB
formule = gestion_saisie(i, "kb")

# Vérifie si aucune saisie n'a été effectuée
if formule == False:
    print("Fin de programme")
    quit()

# Initialisation de la chaîne de caractères pour KB
kb = f"({formule})"

# Saisie des formules suivantes pour KB
while i < int(nb_formules):
    i += 1
    formule = gestion_saisie(i, "kb")
    # Vérifie si une saisie a été effectuée
    if formule != False:
        kb += f" & ({formule})"

# Vérifie si la formule KB est correcte
verifier_formule(kb)

# Saisie de la formule Alpha
formule = gestion_saisie(1, "alpha")

# Vérifie si aucune saisie n'a été effectuée
if formule == False:
    print("Fin de programme")
    quit()

# Construction de la chaîne de caractères pour Alpha
alpha = f"({formule})"

# Vérifie si la formule Alpha est correcte
verifier_formule(alpha)

# Génération de la table de vérité pour KB et Alpha
kb_truth_table = generer_table_de_verite(kb)
alpha_truth_table = generer_table_de_verite(alpha)

# Démonstration du théorème
demontrer_theoreme(kb_truth_table, alpha_truth_table, kb, alpha)

