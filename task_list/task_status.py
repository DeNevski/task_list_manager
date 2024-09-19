from utils.helpers import is_empty, find_task

# Altera o status de uma tarefa para "✔" (concluído)
def task_completed(head, tail, id):
    is_empty(head)

    if head.id == id:
        head.status = '✔'

    elif tail.id == id:
        tail.status = '✔'
        
    else:
        node = find_task(head.next, id)
        node.status = '✔'

# Altera o status de uma tarefa para "x" (não concluído)
def task_incompleted(head, tail, id):
    is_empty(head)

    if head.id == id:
        head.status = 'x'

    elif tail.id == id:
        tail.status = 'x'

    else:
        node = find_task(head.next, id)
        node.status = 'x'
