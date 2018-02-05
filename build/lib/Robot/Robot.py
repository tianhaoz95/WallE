from .util import get_impl

reserved_attr = set(['clean_cache'])

class Robot:
    __instance = None

    def __init__(self, mode=None, info=None):
        """ Create robot instance """
        if Robot.__instance is None:
            robot_impl = get_impl(mode, info)
            Robot.__instance = robot_impl()
        self.__dict__['_Robot__instance'] = Robot.__instance

    def __getattr__(self, attr):
        """ Delegate access to actual robot implementation """
        if attr in reserved_attr:
            return getattr(self, attr)
        else:
            return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        """ Delegate access to actual robot implementation """
        return setattr(self.__instance, attr, value)

    def clean_cache(self):
        print('cleaning cache ...')
