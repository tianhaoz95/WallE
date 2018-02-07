from WallE.API.RobotAPI import VisionAPI, ArmAPI
from WallE import Interface
from WallE.API.Manage.Task import SimpleTask

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

class LocateObjects(SimpleTask):

    def __init__(self, robot):
        super().__init__(robot)

    def setup(self):
        super().setup()
        print('starting camera ...')
        print('downloading pre train model ...')

    def run(self):
        self.robot.get_img()
        print('passing img through YOLO ...')
        print('passing img through MASK layer ...')
        return None

    def report(self):
        print('reporting detail status ...')

class GrabObject(SimpleTask):
    def __init__(self, robot):
        super().__init__(robot)
        self.add_dep('locator', LocateObjects)

    def setup(self):
        super().setup()
        print('starting arm ...')

    def run(self):
        loc = self.deps['locator'].run()
        if loc:
            self.robot.move_to(loc)
            dest = 'some location'
            self.robot.move_to(dest)
        else:
            print('no object found')
        print('done')

    def report(self):
        print('reporting detail status ...')

robot = Interface.Robot(api_mode='module', api_info={'module_impl': HalAPI})
robot.add_task(GrabObject)
robot.run_task()
