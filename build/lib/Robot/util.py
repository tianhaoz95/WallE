import os
from importlib import import_module

def check_dir(path):
    if not os.path.isdir(path):
        print('path not exist, creating ', path, ' ... ')
        os.makedirs(path)
    print(path, ' exist')

def check_init(path):
    if not os.path.exists('__init__.py'):
        print('Creating init file ...')
        f = open(path + '/__init__.py', 'w')
        f.close()
    else:
        print('Init file exist, continue')

def get_impl(mode, info):
    if mode == 'local':
        return get_local_impl(info['module_name'], info['class_name'])
    return None

def get_local_impl(module_name, class_name):
    check_dir('robotlib')
    check_dir('tmp')
    check_init('robotlib')
    robot_module = import_module('robotlib.' + module_name)
    robot_impl = getattr(robot_module, class_name)
    return robot_impl

def get_remote_impl(module_name, class_name, url):
    check_dir('robotlib')
    check_dir('tmp')
    check_init('robotlib')
    package = urllib2.urlopen(url)
    with open('tmp/robotAPI.zip','wb') as output:
        output.write(package.read())
    zip_ref = zipfile.ZipFile('tmp/robotAPI.zip', 'r')
    zip_ref.extractall('robotlib')
    robot_impl = get_local_impl(module_name, class_name)
    return robot_impl
