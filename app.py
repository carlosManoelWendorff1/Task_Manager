from Agent.Agent import Agent
from TaskManager.TaskManager import TaskManager


def load_tasks_from_file(file_path):
    tasks = {}
    priorities = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            condition, priority = value.split(',')
            tasks[key] = True if condition == 'True' else False
            priorities[key] = int(priority)
    return tasks, priorities

# Carrega as tarefas e prioridades do arquivo
tasks, priorities = load_tasks_from_file('tarefas.txt')

# Inicializa o TaskManager com as tarefas e suas respectivas prioridades
task_manager = TaskManager(tasks, priorities)

# Agentes genéricos
agents = [
    Agent('Agente 1', 'wash_dishes'),
    Agent('Agente 2', 'sweep_floor'),
    Agent('Agente 3', 'water_plants'),
    Agent('Agente 4', 'take_out_trash'),
    Agent('Agente 5', 'clean_windows')
]

# Simulação de execução das tarefas
while True:
    
    task = task_manager.assign_task()
    if task is None:
        break  # Sai do loop se não houver mais tarefas

    # Procura um agente que seja capaz de realizar a tarefa
    for agent in agents:
        if task == agent.task:
            agent.perform_task()
            task_manager.update_conditions(task)  # Atualiza o estado após a tarefa
            break  # Após encontrar o agente, sai do loop e atribui a próxima tarefa