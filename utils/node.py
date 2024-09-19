from utils.id_generator import IDGenerator

# Instância o gerador de IDs
id_generator = IDGenerator()

# Permite a criação de nós e a vínculação de uns aos outros
class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.status = 'x'
        self.previous = None
        self.next = None
        self.id = id_generator.next_id()
