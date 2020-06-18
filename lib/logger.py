class Logger:
    def __init__(self, file) -> None:
        self._file = file

    def log(self, ligne, code='_') -> None:
        with open(self._file, 'a') as f:
            f.write(f'Ligne [{ligne}]: {self.obtenir_code_affiliation()[code]}.')

    @staticmethod
    def obtenir_code_affiliation() -> dict[str, str]:
        return {
            's': 'Ajout d\'un espace',
            'e': 'Une erreur est survenue',
            'n': 'Ajout d\'une nouvelle ligne',
            '_': 'Opération non répertoriée'
        }
