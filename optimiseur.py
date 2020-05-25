def optimiser(code: str) -> None:
    pass


if __name__ == '__main__':
    from sys import argv
    from menu import lire, cibler

    optimiser(lire(argv[1] if len(argv) > 1 else 'main.bf'))
