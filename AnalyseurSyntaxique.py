from Grammaire import lexer, parser
from terminaltables import AsciiTable


def afficher_aide():
    """
    Affiche un message d'aide avec la liste des symboles valides pour les formules de logique de proposition.
    """

    # Définition du tableau des correspondances connecteur / symbole
    tableau_de_correspondace = AsciiTable([
        ["Connecteur", "Symbole"],
        # Connecteur correspondant au symbole de négation
        ["Négation (¬)",    "~"],
        # Connecteur correspondant au symbole de conjonction
        ["Conjonction (∧)", "&"],
        # Connecteur correspondant au symbole de disjonction
        ["Disjonction (∨)", "|"],
        # Connecteur correspondant au symbole d'implication
        ["Implication (→)", ">>"],
        # Connecteur correspondant au symbole d'équivalence
        ["Équivalence (↔)", "="]
    ]).table

    # Affichage de la table de correspondance
    print("Tableau de correspondance")
    print(tableau_de_correspondace)

        # Affichage du message d'aide
    print("\n-----Taper votre formule-----")
    print("Exemple KB |= α: KB1 = A | B, KB2 = ~C | A, alpha = A | B | C\n")
    print("Exemple KB /|= α: KB1 = A | B, KB2 = ~C | A, alpha = A & C\n")


def convertir_mots_en_symboles(expression):
    """
    Convertit les mots-clés en symboles logiques.
    """
    # Dictionnaire des mots-clés en symboles
    mots_en_symboles = {
        "~": "¬",
        "&": "∧",
        "|": "∨",
        ">>": "→",
        "=": "↔"
    }
    # Expression non convertie
    expression_convertie = expression

    # Convertir tous les mots en symboles
    for mots, symboles in mots_en_symboles.items():
        expression_convertie = expression_convertie.replace(mots, symboles)

    # Retourner l'expression convertie
    return expression_convertie


def convertir_saisie():
    """
    Demande a l'utilisateur de rentrer une formule et la convertit.
    """

    # Saisie de la formule
    saisie = input('Votre formule : ')

    # Si la saisie est vide, retour à la saisie
    if not saisie:
        return False

    # Afficher l'aide si l'utilisateur tape "help"
    if saisie == 'help':
        afficher_aide()

    # Convertir la syntaxe de la formule saisie
    return convertir_mots_en_symboles(saisie)


def analyser_formule(formule):
    """
    Analyse la formule et vérifie si elle est correcte.
    """

    # Executer le parseur
    try:
        # Si le parseur renvoie un résultat la formule est correcte
        if (parser.parse(formule, lexer=lexer)):
            return True
    except:
        # Si le parseur ne renvoie pas de résultat la formule est incorrecte
        return False


if __name__ == "__main__":

    # Afficher l'aide au démarrage
    afficher_aide()

    while True:
        # Demander a l'utilisateur de rentrer une formule
        formule = convertir_saisie()

        # Afficher si la formule est correcte
        if analyser_formule(formule):
            print("Formule correcte : {}".format(formule))
        else:
            print("Formule incorrecte : {}".format(formule))
