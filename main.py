

def lire(file_name: str) -> str:
    with open(file_name, 'r') as fichier:
        print(f'Lecture de \"{file_name}\"...')
        return ''.join(fichier.readlines())


if __name__ == '__main__':
    from interpreteur import *

    executer(nettoyer(lire(sys.argv[1] if len(sys.argv) > 1 else 'main.bf')))
