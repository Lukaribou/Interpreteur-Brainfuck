def afficher_menu() -> None:
    """Affiche le menu et attend un choix"""

    menu = {
        'Quitter': __import__('sys').exit,
        'Interpreter': __import__('interpreteur').executer,
        'Optimiser':  __import__('optimiseur').executer
    }

    print('\n** Menu **\n')
    for k, v in enumerate(menu):
        print(f'{k}: {v}')
    print('')  # afficher une ligne vide entre la liste et la question
    choix = demander('Choisissez l\'action que vous souhaitez faire sur votre fichier: ',
                     lambda rep: True if str.isnumeric(rep) and 0 <= int(rep) < len(menu) else False)
    print('')  # afficher une ligne vide en dessous de la question

    for index, v in enumerate(menu):  # (v = 'Quitter'...)
        if index == int(choix):
            menu[v]()  # execute la fonction associée


def demander(question, verif=(lambda rep: True if str.lower(rep) in ['n', 'y'] else False)) -> str:
    """Pose la question jusqu'à ce que la verif renvoie True

    La verif de base attendant un y ou un n"""
    while True:
        rep = input(question)
        if verif(rep):  # si la verif est bonne on retourne la valeur
            return rep


def formatter_nom_fichier(nom: str) -> str:
    """Gère le nom du fichier"""
    if (not nom.endswith('.bf')) and (not nom.endswith('.txt')):
        if '.' in nom:
            print(f"L'extension '.{nom.split('.', 1)[1]}' m'est inconnue.")
            exit(1)
        else:
            nom += '.bf'
    return nom


def lire(nom: str) -> str:
    """Lis le fichier et renvoie son contenu sous la forme d'une seule string"""
    nom = formatter_nom_fichier(nom)
    try:
        with open(nom, 'r') as fichier:
            print(f'Lecture de \"{nom}\"...')
            return ''.join(fichier.readlines())
    except FileNotFoundError:
        print(f'Le fichier \'{nom}\' est introuvable.')
        exit(404)


if __name__ == '__main__':
    from sys import argv
    from constants import DEFAULT_PATH, DEFAULT_FOLDER

    cible = DEFAULT_FOLDER + argv[1] if len(argv) > 1 else DEFAULT_PATH
    afficher_menu()
