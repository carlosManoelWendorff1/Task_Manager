class TaskManager:
    def __init__(self, tasks, priorities):
        # Armazena as tarefas e suas condições
        self.tasks = tasks
        # Prioridades das tarefas
        self.task_priority = priorities

    def check_conditions(self):
        # Verifica a primeira tarefa com condição True, com base na prioridade
        for task, condition in sorted(self.tasks.items(), key=lambda item: self.task_priority[item[0]]):
            if condition:
                return task
        return None  # Nenhuma tarefa a ser realizada

    def assign_task(self):
        task = self.check_conditions()
        if task:
            print(f"Tarefa atribuída: {task}")
            return task
        else:
            print("Nenhuma tarefa disponível no momento.")
            return None

    def update_conditions(self, task):
        if task in self.tasks:
            self.tasks[task] = False  # Marca a tarefa como concluída
        print(f"task {task} DONE")
