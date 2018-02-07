from WallE.API.RobotAPI import VisionAPI, ArmAPI
from WallE import Interface

class HalVisionAPI(VisionAPI):

    def __init__(self, init_info):
        super(HalVisionAPI, self).__init__(init_info)
        print('initializing hal vision ...')

    def setup(self):
        print('setting up hal vision...')

    def start(self):
        print('starting hal vision ...')

    def shutdown(self):
        print('shutting down hal vision ...')

    def get_img(self):
        print('getting img ...')

class HalArmAPI(ArmAPI):

    def __init__(self, init_info):
        super(HalArmAPI, self).__init__(init_info)
        print('initializing hal arm ...')

    def setup(self):
        print('setting up hal arm...')

    def start(self):
        print('starting hal arm ...')

    def shutdown(self):
        print('shutting down hal arm ...')

    def move_to(self):
        print('moving arm ...')

class HalAPI(HalArmAPI, HalVisionAPI):

    def __init__(self, init_info):
        super(HalAPI, self).__init__(init_info)
        print('initializing hal ...')

    def start(self):
        super(HalAPI, self).start()

robot = Interface.Robot(api_mode='module', api_info={'module_impl': HalAPI})

robot.get_img()
