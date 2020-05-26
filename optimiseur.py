def optimiser(code: str) -> None:
    """Optimise le code directement dans le fichier"""
    # TODO: Optimiser le code directement dans le fichier
    # TODO: 1 espace tous les 5 + ou -
    # TODO: Retour à la ligne quand ouverture et fermeture de boucle \ Garder les possibles commentaires sur la ligne
    # TODO: Retour à la ligne après un . ou une ,
    pass


def executer():
    pass
    # TODO: pouvoir choisir ce qu'on veut optimiser


if __name__ == '__main__':
    from sys import argv
    from menu import lire

    optimiser(lire(argv[1] if len(argv) > 1 else 'main.bf'))
