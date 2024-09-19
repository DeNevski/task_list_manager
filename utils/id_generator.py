# Gera um número inteiro único e sequencial a cada vez que é chamado
class IDGenerator:
    def __init__(self):
        self._id = 0

    def next_id(self):
        self._id += 1
        return self._id