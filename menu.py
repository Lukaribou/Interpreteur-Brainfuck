def afficher_menu() -> None:
    """Affiche le menu et attend un choix"""

    print('\n** Menu **\n')
    menu = ['Interpreter', 'Optimiser']
    for k, v in enumerate(menu):
        print(f'{k}: {v}')
    print('')  # afficher une ligne vide entre la liste et la question

    choix = demander('Choisissez l\'action que vous souhaitez faire sur votre fichier: ',
                     lambda rep: True if str.isnumeric(rep) and 0 <= int(rep) < len(menu) else False)
    # str.isnumeric() -> https://www.geeksforgeeks.org/python-string-isnumeric-application/
    print('')  # afficher une ligne vide en dessous de la question

    # TODO: Rediriger vers le bon fichier en fonction du choix


def demander(question, verif=(lambda rep: True if str.lower(rep) in ['n', 'y'] else False)) -> str:
    """Pose la question jusqu'à ce que la verif renvoie True

    La verif de base attendant un y ou un n"""
    while True:
        rep = input(question)
        if verif(rep):  # si la verif est bonne on retourne la valeur
            return rep


def lire(file_name: str) -> str:
    """Lis le fichier et renvoie son contenu sous la forme d'une seule string"""
    with open(file_name, 'r') as fichier:
        print(f'Lecture de \"{file_name}\"...')
        return ''.join(fichier.readlines())


if __name__ == '__main__':
    import sys

    cible = sys.argv[1] if len(sys.argv) > 1 else 'main.bf'
    afficher_menu()
