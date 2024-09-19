from task_list.task_operations import add_task, remove_task, modify_task_value, modify_priority
from task_list.task_status import task_completed, task_incompleted
from task_list.task_listing import listing_format_by_id, listing_format_by_priority, listing_format_by_status

class TaskList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Adiciona uma tarefa na lista
    def append(self, task, priority=False):
        add = add_task(self.head, self.tail, task, priority)
        self.head, self.tail = add
            
    # Remove uma tarefa da lista
    def remove(self, id):
        remove = remove_task(self.head, self.tail, id)
        self.head, self.tail = remove
        
    # Modifica uma tarefa da lista
    def modify_task(self, old_task_id, new_task):
        modify_task_value(self.head, self.tail, old_task_id, new_task)

    # Altera a prioridade de alguma tarefa
    def priority(self, id, priority):
        modify_priority(self.head, self.tail, id, priority)

    # Marca uma tarefa como concluída
    def completed(self, id):
        task_completed(self.head, self.tail, id)

    # Marca uma tarefa como não concluída
    def incompleted(self, id):
        task_incompleted(self.head, self.tail, id)
                
    # Lista as tarefas por id
    def listing_by_id(self, reverse_list=False):
        listing_format_by_id(self.head, reverse_list)
    
    # Lista as tarefas por prioridade
    def listing_by_priority(self, reverse_list=False):
        listing_format_by_priority(self.head, reverse_list)

    # Lista as tarefas pelo status
    def listing_by_status(self, reverse_list=False):
        listing_format_by_status(self.head, reverse_list)
