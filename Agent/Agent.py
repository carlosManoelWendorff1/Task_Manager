
from TaskManager.TaskManager import TaskManager

class Agent:
    def __init__(self, name, task):
        self.name = name
        self.task = task

    def perform_task(self):
        print(f"{self.name} está realizando a tarefa: {self.task}")
