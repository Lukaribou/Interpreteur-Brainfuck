fichier = ''


def optimiser(code: str) -> None:
    """Optimise le code en utilisant toutes les fonctions"""
    print('Optimisation...')
    sauvegarder(finitions(retour_ligne(espacer(code))))


def espacer(code: str) -> str:
    """Place des espaces à certains endroits pour rendre le code plus lisible"""
    from re import compile
    temp = compile(r'(-----|\+\+\+\+\+)').split(code)
    for i, v in enumerate(temp):
        if v == '' or v == ' ':  # enlever les vides
            del temp[i]
    return ' '.join(temp)


def retour_ligne(code: str) -> str:
    """Place des retours à la ligne pour rendre plus lisible"""
    c = list(code)  # split tous les caractères
    for i, char in enumerate(c):
        if char in ['.', ',', '[', ']']:
            if char in ['[', ']']:
                c[i] = f'\n{char}\n'
            else:
                c[i] = f'{char}\n'
    return ''.join(c)


def finitions(code: str) -> str:
    return '\n'.join([x.strip() for x in code.splitlines()])  # strip les lignes


def sauvegarder(code: str) -> None:
    try:
        with open(fichier, 'w') as fic:
            fic.write(code)
            print('Votre fichier a bien ete optimise !')
    except FileNotFoundError:
        print(f'Le fichier {fichier} est introuvable')


def executer() -> None:
    from menu import lire, formatter_nom_fichier
    from interpreteur import nettoyer
    global fichier
    fichier = formatter_nom_fichier(input('Quel fichier voulez-vous optimiser ? '))
    optimiser(nettoyer(lire(fichier)))
    # TODO: pouvoir choisir ce qu'on veut optimiser
    # TODO: ne pas supprimer les commentaires


if __name__ == '__main__':
    from sys import argv
    from menu import lire

    optimiser(lire(argv[1] if len(argv) > 1 else 'main.bf'))
