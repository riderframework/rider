import sys
from os import chdir, getcwd, path


def load_project(app_dir=''):
    sys.path.append(path.join(getcwd(), app_dir))
    __import__('__init__')
