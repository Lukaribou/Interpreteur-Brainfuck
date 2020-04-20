tableau_val = [0]
code = ''


def lire():
    with open('./bf.txt', 'r') as fichier:
        global code
        code = ''.join(fichier.readlines())
        code = ''.join(filter(lambda x: x in ['.', ',', '[', ']', '<', '>', '+', '-'], code))


def executer():
    pointeur, parcours, boucle_cptr = 0, 0, 0
    boucles = trouver_boucle()

    while parcours < len(code):
        signe = code[parcours]
        if signe == '+':
            tableau_val[pointeur] += 1 if tableau_val[pointeur] < 255 else 0
        elif signe == '-':
            if tableau_val[pointeur] > 0:
                tableau_val[pointeur] -= 1
        elif signe == '>':
            if pointeur + 1 == len(tableau_val):
                tableau_val.append(0)
            pointeur += 1
        elif signe == '<':
            if not pointeur - 1 == -1:
                pointeur -= 1
        elif signe == '.':
            print(chr(tableau_val[pointeur]), end='')
        elif signe == ',':
            try:
                tableau_val[pointeur] = int(input('Entree byte: '))
            except ValueError:
                print('Une erreur est survenue. L\'entree attendue est un nombre entre 0 et 255 !')
        elif signe == '[':
            boucle_cptr += 1
        elif signe == ']':
            if tableau_val[pointeur] != 0:
                parcours = boucles[boucle_cptr - 1]['debut']
            else:
                boucle_cptr -= 1

        parcours += 1


def trouver_boucle():
    boucle, temp, cpt = [], [], 0
    for index, signe in enumerate(code):
        print(cpt)
        if signe == '[':
            temp.append(index)
            cpt += 1
        elif signe == ']':
            debut = temp.pop()
            boucle[cpt - 1] = {'debut': debut, 'fin': index}
    print(boucle)
    return boucle


lire()
executer()
