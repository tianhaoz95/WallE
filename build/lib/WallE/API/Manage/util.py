import urllib.request as urllib2
import zipfile
import os
from importlib import import_module

def check_dir(path):
    if not os.path.isdir(path):
        print('path not exist, creating ', path, ' ... ')
        os.makedirs(path)
    else:
        print(path, ' exist')

def check_init(path):
    if not os.path.exists('__init__.py'):
        print('Creating init file ...')
        f = open(path + '/__init__.py', 'w')
        f.close()
    else:
        print('Init file exist, continue')

def task_exist(module_name):
    dir_list = module_name.split('.')
    foldername = dir_list[0]
    task_list = os.listdir('tasks')
    if foldername in set(task_list):
        return True
    else:
        return False

def load_local_task_module(robot, module_name, class_name):
    check_dir('tasks')
    check_dir('tmp')
    check_init('tasks')
    task_module = import_module('tasks.' + module_name)
    task_class = getattr(task_module, class_name)
    task = task_class(robot)
    return task

def load_remote_task_module(robot, module_name, class_name, url):
    check_dir('tasks')
    check_dir('tmp')
    check_init('tasks')
    if not task_exist(module_name):
        print(module_name, ' not exist, starting download ...')
        package = urllib2.urlopen(url)
        with open('tmp/task_package.zip','wb') as output:
            output.write(package.read())
        zip_ref = zipfile.ZipFile('tmp/task_package.zip', 'r')
        zip_ref.extractall('tasks')
        zip_ref.close()
        os.remove('tmp/task_package.zip')
    else:
        print(module_name, ' already exist locally')
    task = load_local_task_module(robot, module_name, class_name)
    return task
