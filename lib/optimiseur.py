class Optimiseur:
    def __init__(self, fichier=None) -> None:
        from menu import formatter_nom_fichier
        self._fichier = formatter_nom_fichier(fichier if fichier else input('Quel fichier voulez-vous optimiser ? '))
        self._content = {
            'code': '',
            'commentaires': ''
        }

    def executer(self) -> None:
        """Optimise le code en utilisant toutes les fonctions"""
        from menu import lire
        self.separer(lire(self._fichier))

        print('Optimisation...')
        self.espacer()
        self.retour_ligne()
        self.finitions()
        self.sauvegarder()

    def espacer(self) -> None:
        """Place des espaces à certains endroits pour rendre le code plus lisible"""
        from re import compile
        temp = compile(r'(-----|\+\+\+\+\+)').split(self._content['code'])
        for i, v in enumerate(temp):
            if v == '' or v == ' ':  # enlever les vides
                del temp[i]
        self._content['code'] = ' '.join(temp)

    def retour_ligne(self) -> None:
        """Place des retours à la ligne pour rendre plus lisible"""
        c = list(self._content['code'])  # split tous les caractères
        for i, char in enumerate(c):
            if char in ['.', ',', '[', ']']:
                if char in ['[', ']']:
                    c[i] = f'\n{char}\n'
                else:
                    c[i] = f'{char}\n'
        self._content['code'] = ''.join(c)

    def finitions(self) -> None:
        self._content['code'] = '\n'.join([x.strip() for x in self._content['code'].splitlines()])  # strip les lignes

    def sauvegarder(self) -> None:
        try:
            with open(self._fichier, 'w') as fic:
                self._content['commentaires'] = ''.join(self._content['commentaires'])
                code = ''
                if self._content['commentaires'] != '':
                    if self._content['commentaires'].find('## Commentaires') == -1:  # index si il trouve, -1 sinon
                        code = self._content['code'] + \
                               "\n\n## Commentaires (Anciennes lignes) ##\n" + self._content['commentaires']
                    else:
                        code = self._content['code'] + "\n\n" + self._content['commentaires']
                fic.write(code)
                print('Votre fichier a bien ete optimise !')
        except FileNotFoundError:
            print(f'Le fichier {self._fichier} est introuvable')

    def separer(self, contenant: str) -> None:
        print("Separation du code et des commentaires...")
        for cpt, ligne in enumerate(contenant.splitlines()):
            if ligne.strip().startswith('##'):
                self._content['commentaires'] = "\n".join(contenant.splitlines()[cpt:])
                break
            for index, c in enumerate(ligne):
                if c in ['.', ',', '[', ']', '<', '>', '+', '-']:
                    self._content['code'] += c
                elif c == "#":
                    self._content['commentaires'] += f'Ligne {cpt + 1}:{ligne[index + 1:]}\n'
                    break
                else:
                    continue

    # TODO: mettre les opérations effectuées dans un logs.txt


if __name__ == '__main__':
    from sys import argv
    from constants import DEFAULT_PATH, DEFAULT_FOLDER

    Optimiseur(DEFAULT_FOLDER + argv[1] if len(argv) > 1 else DEFAULT_PATH).executer()
