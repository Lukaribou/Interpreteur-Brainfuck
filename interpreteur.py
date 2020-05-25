def nettoyer(code: str) -> str:
    print('Nettoyage du code...')
    return ''.join(filter(lambda x: x in ['.', ',', '[', ']', '<', '>', '+', '-'], code))


def executer(code: str) -> None:
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
        elif signe == '[' and tableau_val[pointeur] == 0:
            parcours = boucles[parcours]
        elif signe == ']' and tableau_val[pointeur] != 0:
            parcours = boucles[parcours]

        parcours += 1


if __name__ == '__main':
    import sys
    from main import lire
    executer(nettoyer(lire(sys.argv[1] if len(sys.argv) > 1 else 'main.bf')))