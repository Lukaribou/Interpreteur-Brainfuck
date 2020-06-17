fichier = ''
content = {}


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
            print(content['commentaires'])
            content['commentaires'] = ''.join(content['commentaires'])
            if content['commentaires'] != '':
                x = content['commentaires'].find('## Commentaires')  # index si il trouve, -1 sinon
                if x == -1:
                    code = code + "\n\n## Commentaires (Anciennes lignes) ##\n" + content['commentaires']
                else:
                    code = code + "\n\n" + content['commentaires']
            fic.write(code)
            print('Votre fichier a bien ete optimise !')
    except FileNotFoundError:
        print(f'Le fichier {fichier} est introuvable')


def separer(contenant: str) -> dict:
    d = {'code': '', 'commentaires': ''}
    print("Separation du code et des commentaires...")
    for cpt, ligne in enumerate(contenant.splitlines()):
        if ligne.strip().startswith('##'):
            d['commentaires'] = "\n".join(contenant.splitlines()[cpt:])
            break
        for index, c in enumerate(ligne):
            if c in ['.', ',', '[', ']', '<', '>', '+', '-']:
                d['code'] += c
            elif c == "#":
                d['commentaires'] += f'Ligne {cpt + 1}:{ligne[index + 1:]}\n'
                break
            else:
                continue
    return d
    

def executer(fl=None) -> None:
    from menu import lire, formatter_nom_fichier
    global fichier, content
    fichier = formatter_nom_fichier(fl if fl else input('Quel fichier voulez-vous optimiser ? '))
    content = separer(lire(fichier))
    optimiser(content['code'])

    # TODO: pouvoir choisir ce qu'on veut optimiser
    # TODO: ne pas supprimer les commentaires
    # TODO: mettre les opérations effectuées dans un logs.txt


if __name__ == '__main__':
    from sys import argv
    from constants import DEFAULT_PATH, DEFAULT_FOLDER

    executer(DEFAULT_FOLDER + argv[1] if len(argv) > 1 else DEFAULT_PATH)
