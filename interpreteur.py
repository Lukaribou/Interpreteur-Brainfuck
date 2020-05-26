def nettoyer(code: str) -> str:
    """Enlève tous les caractères ne faisant pas partie de ceux du BrainFuck"""
    print('Nettoyage du code...')
    return ''.join(filter(lambda x: x in ['.', ',', '[', ']', '<', '>', '+', '-'], code))


def interpreter(code: str) -> None:
    """Interprête le code qui lui est donné"""
    print('Interpretation...\n')
    parcours, pointeur, tableau_val = 0, 0, [0]

    temp, boucles = [], {}
    for index, signe in enumerate(code):
        if signe == '[':
            temp.append(index)
        elif signe == ']':
            x = temp.pop()
            boucles[x] = index
            boucles[index] = x
    del temp

    while parcours < len(code):
        signe = code[parcours]
        if signe == '+':
            tableau_val[pointeur] += 1 if tableau_val[pointeur] < 255 else -255  # 255 += -255 = 0
        elif signe == '-':
            tableau_val[pointeur] -= 1 if tableau_val[pointeur] > 0 else -255  # 0 -= -255 = +255
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
        elif signe == '[' and tableau_val[pointeur] == 0:
            parcours = boucles[parcours]
        elif signe == ']' and tableau_val[pointeur] != 0:
            parcours = boucles[parcours]

        parcours += 1

        # TODO: Détecter et gérer les boucles infinies


if __name__ == '__main':
    from sys import argv
    from menu import lire

    interpreter(nettoyer(lire(argv[1] if len(argv) > 1 else 'main.bf')))
