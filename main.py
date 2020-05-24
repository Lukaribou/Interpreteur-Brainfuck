tableau_val = [0]
parcours, pointeur = 0, 0


def lire(file_name: str):
    with open(file_name, 'r') as fichier:
        return "".join(fichier.readlines())


def nettoyer(code: str) -> str:
    return ''.join(filter(lambda x: x in ['.', ',', '[', ']', '<', '>', '+', '-'], code))


def executer(code):
    global pointeur, parcours
    boucle = trouver_boucle(code)

    while parcours < len(code):
        signe = code[parcours]
        if signe == "+":
            tableau_val[pointeur] += 1 if tableau_val[pointeur] < 255 else -255  # 255 += -255 = -255
        elif signe == '-':
            tableau_val[pointeur] -= 1 if tableau_val[pointeur] > 0 else -255  # 0 -= -255 = 255
        elif signe == ">":
            if pointeur + 1 == len(tableau_val):
                tableau_val.append(0)
            pointeur += 1
        elif signe == "<" and not pointeur == 0:
            pointeur -= 1
        elif signe == ".":
            print(chr(tableau_val[pointeur]), end="")
        elif signe == ",":
            try:
                tableau_val[pointeur] = int(input("Entrée byte: "))
            except ValueError:
                print("Une erreur est survenue. L'entrée attendue est un nombre entre 0 et 255 !")
        elif signe == "[" and tableau_val[pointeur] == 0:
            parcours = boucle["fin"]
        elif signe == "]" and tableau_val[pointeur] != 0:
            parcours = boucle["debut"]

        parcours += 1


def trouver_boucle(code):
    boucle = {}
    for index, signe in enumerate(code):
        if signe == "[":
            boucle["debut"] = index
        if signe == "]":
            boucle["fin"] = index
    return boucle


if __name__ == '__main__':
    import sys
    executer(nettoyer(lire(sys.argv[1] if len(sys.argv) > 1 else 'test.bf')))

