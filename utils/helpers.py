# Verifica se a lista de tarefas está vazia
def is_empty(head):
    if not head:
        raise ValueError('The list is empty!')

# Percorre toda a lista em busca de uma tarefa. Se encontrar retorna ela, se não retorna um erro
def find_task(head, id):
    pointer = head

    while pointer:
        if pointer.id == id:
            return pointer
        
        pointer = pointer.next
        
    raise IndexError('ID not found!')
