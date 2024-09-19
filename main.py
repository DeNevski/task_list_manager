from task_list.task_main import TaskList

def main():
    teste = TaskList()
    teste.append('Limpar o carro', True)
    teste.append('Fazer o almoço')
    teste.append('Ir ao supermercado', True)
    teste.append('Levar o cachorro para passear')
    teste.append('Estudar', True)

    teste.priority(1, False)
    teste.priority(5, False)
    teste.priority(4, True)

    teste.modify_task(1, 'Limpar o carro e a moto')
    teste.modify_task(5, 'Estudar estruturas de dados')
    teste.modify_task(2, 'Fazer o almoço e montar a marmita')

    teste.remove(1)
    teste.remove(5)
    #teste.remove(3)

    teste.completed(2)
    teste.completed(4)
    teste.incompleted(2)

    teste.listing_by_id()
    #teste.listing_by_id(True)

    #teste.listing_by_priority()
    #teste.listing_by_priority(True)

    #teste.listing_by_status()
    #teste.listing_by_status(True)

if __name__ == '__main__':
    main()