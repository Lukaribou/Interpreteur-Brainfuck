def optimiser(code: str) -> None:
    """Optimise le code directement dans le fichier"""
    pass


if __name__ == '__main__':
    from sys import argv
    from menu import lire

    optimiser(lire(argv[1] if len(argv) > 1 else 'main.bf'))
