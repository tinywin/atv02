import sys

def load_tasks():
    try:
        with open('tasks.txt', 'r') as file:
            tasks = [line.strip().split(';', 2) for line in file.readlines()]
        return {task[0]: {'done': task[1] == 'True', 'description': task[2]} for task in tasks}
    except FileNotFoundError:
        return {}

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

def main():
    tasks = load_tasks()
    while True:
        print("\n1. Adicionar tarefa")
        print("5. Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "5":
            print("Saindo do programa.")
            sys.exit()
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()

