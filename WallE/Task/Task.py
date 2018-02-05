from abc import ABC, abstractmethod

class SimpleTask(ABC):

    def __init__(self, robot):
        self.robot = robot

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def run(self):
        pass
