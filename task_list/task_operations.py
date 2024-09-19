from utils.node import Node
from utils.helpers import is_empty, find_task

def add_task(head, tail, task, priority):
    new_node = Node(task, priority)

    if head:
            new_node.next = head
            head.previous = new_node
            head = new_node

    else:
        head = new_node
        tail = new_node

    return head, tail

def remove_task(head, tail, id):
    is_empty(head)

    # Remove a tarefa do inicio da lista
    if head.id == id:
        head = head.next
        head.previous = None

    # Remove a tarefa do final da lista
    elif tail.id == id:
        tail = tail.previous
        tail.next = None

    else:
        node = find_task(head.next, id)
        '''Quando o ponteiro chegar no nó a ser removido
            O ponteiro "next" do nó anterior passará a apontar para o proximo do nó a ser removido
            E o ponteiro "previous" do proximo nó passará a apontar para o nó anterior do que será removido'''
        
        if node.id == id:
            node.previous.next = node.next
            node.next.previous = node.previous
    
    return head, tail

def modify_task_value(head, tail, old_task_id, new_task):
    is_empty(head)

    # Modificada a tarefa do inicio
    if head.id == old_task_id:
        head.data = new_task

    # Modificada a tarefa do final
    elif tail.id == old_task_id:
        tail.data = new_task
    
    # Procura a tarefa no restante da lista e modifica
    else:
        node = find_task(head.next, old_task_id)
        node.data = new_task

def modify_priority(head, tail, id, priority):
    is_empty(head)
    
    # Modifica a prioridade da tarefa do inicio
    if head.id == id:
        head.priority = priority

    # Modifica a prioridade da tarefa do final
    elif tail.id == id:
        tail.priority = priority

    # Procura a tarefa com a prioridade a ser modificada no restante da lista e modifica
    else:
        node = find_task(head.next, id)
        node.priority = priority
