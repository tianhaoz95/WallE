from abc import ABC, abstractmethod
from .util import *

class BasicAPI(ABC):

    def __init__(self, init_info):
        interface_type = 'interactive'
        if init_info and 'interface_type' in init_info:
            interface_type = init_info['interface_type']
        plan_module = get_plan(interface_type)
        self.plan = plan_module(self)

    def add_task(self, mode, task_meta):
        self.checklist.add(mode, task_meta)

    def run(self, get_task=None):
        self.checklist.run(get_task)

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def shutdown(self):
        pass

class VisionAPI(BasicAPI):

    @abstractmethod
    def get_img(self):
        pass

class MobileBaseAPI(BasicAPI):

    @abstractmethod
    def move(self):
        pass

class ArmAPI(BasicAPI):

    @abstractmethod
    def move_to(self):
        pass
