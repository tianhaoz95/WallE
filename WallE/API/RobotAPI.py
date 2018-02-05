from abc import ABC, abstractmethod

class RobotAPI(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def shutdown(self):
        pass
