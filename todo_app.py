import sys

def load_tasks():
    tasks = {}
    try:
        with open('tasks.txt', 'r') as file:
            for line in file.readlines():
                parts = line.strip().split(';', 2)
                if len(parts) == 3:
                    task_id, done, description = parts
                    tasks[task_id] = {'done': done == 'True', 'description': description}
    except FileNotFoundError:
        pass
    return tasks

def save_tasks(tasks):
    with open('tasks.txt', 'w') as file:
        for id, info in tasks.items():
            file.write(f"{id};{info['done']};{info['description']}\n")

def add_task(tasks):
    description = input("Descrição da tarefa: ")
    task_id = str(max([int(x) for x in tasks.keys()] + [0]) + 1)
    tasks[task_id] = {'done': False, 'description': description}
    save_tasks(tasks)
    print("Tarefa adicionada.")

def mark_task_done(tasks):
    task_id = input("ID da tarefa a marcar como feita: ")
    if task_id in tasks and not tasks[task_id]['done']:
        tasks[task_id]['done'] = True
        save_tasks(tasks)
        print("Tarefa marcada como feita.")
    else:
        print("Tarefa não encontrada ou já concluída.")

def delete_task(tasks):
    task_id = input("ID da tarefa a remover: ")
    if task_id in tasks:
        del tasks[task_id]
        save_tasks(tasks)
        print("Tarefa removida.")
    else:
        print("Tarefa não encontrada.")

def list_pending_tasks(tasks):
    print("\nTarefas Pendentes:")
    pending_tasks = {id: info for id, info in tasks.items() if not info['done']}
    if not pending_tasks:
        print("Nenhuma tarefa pendente.")
    else:
        for id, info in pending_tasks.items():
            print(f"{id}: {info['description']}")

def main():
    tasks = load_tasks()
    while True:
        print("\n1. Adicionar tarefa")
        print("2. Marcar tarefa como feita")
        print("3. Excluir tarefa")
        print("4. Listar tarefas pendentes")
        print("5. Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            mark_task_done(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            list_pending_tasks(tasks)
        elif choice == "5":
            print("Saindo do programa.")
            sys.exit()
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
