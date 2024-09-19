from utils.helpers import is_empty

# Formata "True" e "False" para "Sim" e "Não" respectivamente
def _priority_format(value):
    value = str(value)

    if value == 'True':
        value = 'Sim'
    else:
        value = 'Não'
    return value

# Adiciona todas as tarefas em uma lista de tuplas
def _all_tasks(head):
    is_empty(head)
    pointer = head
    lst = []

    while pointer:
        priority = _priority_format(pointer.priority)
        lst.append((pointer.id, pointer.data, priority, pointer.status))

        pointer = pointer.next

    return lst

# Exibe a lista
def _print_list(list):

    for task in list:
        print(f'ID: {task[0]} Tarefa: {task[1]:^50} Prioridade: {task[2]:^5} Status: {task[3]}')

'''Lista todas as tarefas por id em ordem crescente
    Quando "reverse_list=True", lista em ordem decrescente'''
def listing_format_by_id(head, reverse_list):
    list = _all_tasks(head)
    list = sorted(list)

    if reverse_list:
        list = reversed(list)

    _print_list(list)

'''Lista todas as tarefas por prioridade
    Por padrão tarefas com prioridade ficarão no topo
    Quando "reverse_list=True", as tarefas sem prioridade irão para o topo'''
def listing_format_by_priority(head, reverse_list):
    list = _all_tasks(head)
    list = sorted(list, key=lambda x: x[2], reverse=True)

    if reverse_list:
        list = reversed(list)

    _print_list(list)

'''Lista todas as tarefas pelo status
    Por padrão as tarefas com status de não concluído ficarão no topo
    Quando "reverse_list=True", tarefas com status de concluído irão para o topo'''
def listing_format_by_status(head, reverse_list):
    list = _all_tasks(head)
    list = sorted(list, key=lambda x: x[3])

    if reverse_list:
        list = reversed(list)

    _print_list(list)
