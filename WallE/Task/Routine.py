from abc import ABC, abstractmethod
from .util import *

class Routine(ABC):

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def run(self):
        pass

class SimpleRoutine(Routine):

    def __init__(self):
        self.tasks = []

    def add(self, robot, mode, task_meta):
        module_name = task_meta['module_name']
        class_name = task_meta['class_name']
        task = None
        if mode == 'local':
            task = load_local_task_module(robot, module_name, class_name)
        if mode == 'remote':
            url = task_meta['url']
            task = load_remote_task_module(robot, module_name, class_name, url)
        self.tasks.append(task)

    def run(self):
        for task in self.tasks:
            task.setup()
            task.run()
        print('All tasks done')
