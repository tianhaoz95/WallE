from abc import ABC, abstractmethod

class SimpleTask(ABC):

    def __init__(self, robot):
        self.robot = robot
        self.deps = {}

    def add_dep(self, name, dep):
        self.deps[name] = dep(self.robot)

    def setup_deps(self):
        for dep in self.deps:
            print('setup ', dep, ' ... ')
            self.deps[dep].setup()
        print('done setup dependencies')

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def report(self):
        pass
