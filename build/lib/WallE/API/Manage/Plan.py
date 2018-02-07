from abc import ABC, abstractmethod
from .util import *

class Plan(ABC):

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def run(self):
        pass

class Schedule(Plan):

    def __init__(self, robot):
        self.tasks = []
        self.robot = robot

    def add(self, mode, task_meta):
        module_name = task_meta['module_name']
        class_name = task_meta['class_name']
        task = None
        if mode == 'local':
            task = load_local_task_module(self.robot, module_name, class_name)
        if mode == 'remote':
            url = task_meta['url']
            task = load_remote_task_module(self.robot, module_name, class_name, url)
        self.tasks.append(task)

    def run(self, get_task=None):
        for task in self.tasks:
            task.setup()
            task.run()
        print('All tasks done')

class Interactive(Plan):

    def __init__(self, robot):
        self.tasks = []
        self.robot = robot

    def add(self, mode, task_meta):
        module_name = task_meta['module_name']
        class_name = task_meta['class_name']
        task = None
        if mode == 'local':
            task = load_local_task_module(self.robot, module_name, class_name)
        if mode == 'remote':
            url = task_meta['url']
            task = load_remote_task_module(self.robot, module_name, class_name, url)
        self.tasks.append(task)

    def run(self, get_task):
        while True:
            if self.tasks:
                current_task = self.tasks[0]
                del tasks[0]
                current_task.setup()
                current_task.run()
            else:
                task_info = get_task()
                if not task_info:
                    break
                else:
                    self.add(task_info['mode'], task_info['task_meta'])
        print('terminating ...')
