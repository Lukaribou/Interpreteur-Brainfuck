

def lire(file_name: str) -> str:
    with open(file_name, 'r') as fichier:
        print(f'Lecture de \"{file_name}\"...')
        return ''.join(fichier.readlines())


def nettoyer(code: str) -> str:
    print('Nettoyage du code...')
    return ''.join(filter(lambda x: x in ['.', ',', '[', ']', '<', '>', '+', '-'], code))


def executer(code: str) -> None:
    print('Interpretation...\n')
    parcours, pointeur, tableau_val, boucle_cptr = 0, 0, [0], 0
    boucles = trouver_boucle(code)

    while parcours < len(code):
        signe = code[parcours]
        if signe == '+':
            tableau_val[pointeur] += 1 if tableau_val[pointeur] < 255 else -255  # 255 += -255 = -255
        elif signe == '-':
            tableau_val[pointeur] -= 1 if tableau_val[pointeur] > 0 else -255  # 0 -= -255 = 255
        elif signe == '>':
            if pointeur + 1 == len(tableau_val):
                tableau_val.append(0)
            pointeur += 1
        elif signe == '<' and not pointeur == 0:
            pointeur -= 1
        elif signe == '.':
            print(chr(tableau_val[pointeur]), end='')
        elif signe == ',':
            try:
                tableau_val[pointeur] = int(input('Entrée byte: '))
            except ValueError:
                print('Une erreur est survenue. L\'entrée attendue est un nombre entre 0 et 255 !')
                break
        elif signe == '[':
            if tableau_val[pointeur] == 0:
                parcours = boucles[boucle_cptr]['fin']
                boucle_cptr -= 1
            else:
                boucle_cptr += 1
        elif signe == ']' and tableau_val[pointeur] != 0:
            parcours = boucles[boucle_cptr - 1]['debut']

        parcours += 1


def trouver_boucle(code: str):
    boucles, cptr = [], 0
    for index, signe in enumerate(code):
        if signe == '[':
            boucles.append({
                'debut': index,
                'fin': None
            })
            cptr += 1
        if signe == ']':
            cptr -= 1
            boucles[cptr]['fin'] = index
    print(boucles)
    return boucles


if __name__ == '__main__':
    import sys
    executer(nettoyer(lire(sys.argv[1] if len(sys.argv) > 1 else 'test.bf')))

